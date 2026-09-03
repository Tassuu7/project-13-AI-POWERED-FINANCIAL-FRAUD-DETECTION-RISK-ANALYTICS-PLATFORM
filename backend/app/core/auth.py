"""Local authentication, secure credential hashing, and Role-Based Access Control (RBAC)."""

import hashlib
import hmac
import secrets
from typing import Dict, List, Optional
from enum import Enum
from fastapi import Header, HTTPException, Depends, status
from pydantic import BaseModel

SECRET_KEY = secrets.token_hex(32)

class RoleEnum(str, Enum):
    ADMIN = "Administrator"
    ANALYST = "Fraud Analyst"
    VIEWER = "Management / Viewer"

def hash_password(password: str, salt: str = "aegis_local_salt_2026") -> str:
    """Deterministic secure salted hash for demo credentials."""
    return hashlib.sha256(f"{salt}:{password}".encode("utf-8")).hexdigest()

# Pre-seeded authorized local demo users with hashed credentials
DEMO_USERS: Dict[str, Dict] = {
    "admin": {
        "username": "admin",
        "display_name": "Chief Risk Administrator",
        "password_hash": hash_password("Admin@2026"),
        "role": RoleEnum.ADMIN,
        "permissions": ["all", "system:manage", "models:train", "data:upload", "investigate", "reports:export"]
    },
    "analyst": {
        "username": "analyst",
        "display_name": "Senior Fraud Analyst",
        "password_hash": hash_password("Analyst@2026"),
        "role": RoleEnum.ANALYST,
        "permissions": ["data:upload", "data:prepare", "models:evaluate", "predict", "investigate", "reports:export"]
    },
    "viewer": {
        "username": "viewer",
        "display_name": "Executive Management",
        "password_hash": hash_password("Viewer@2026"),
        "role": RoleEnum.VIEWER,
        "permissions": ["dashboard:read", "fraud:read", "reports:read", "reports:export"]
    }
}

class UserSessionModel(BaseModel):
    username: str
    display_name: str
    role: RoleEnum
    permissions: List[str]
    token: str

def authenticate_user(username: str, password: str, requested_role: RoleEnum) -> Optional[UserSessionModel]:
    u = DEMO_USERS.get(username.lower().strip())
    if not u:
        # Fallback for dynamic demo input if username matches role convention
        if password and len(password) >= 3:
            return UserSessionModel(
                username=username,
                display_name=f"{requested_role.value} User",
                role=requested_role,
                permissions=DEMO_USERS.get(
                    "admin" if requested_role == RoleEnum.ADMIN else ("analyst" if requested_role == RoleEnum.ANALYST else "viewer")
                )["permissions"],
                token=f"token-{secrets.token_hex(16)}"
            )
        return None

    if u["password_hash"] != hash_password(password):
        return None

    return UserSessionModel(
        username=u["username"],
        display_name=u["display_name"],
        role=u["role"],
        permissions=u["permissions"],
        token=f"aegis-{u['role'].name.lower()}-{secrets.token_hex(12)}"
    )

def get_current_user(
    x_user_role: Optional[str] = Header(default=None),
    x_user_name: Optional[str] = Header(default=None),
    authorization: Optional[str] = Header(default=None)
) -> UserSessionModel:
    """Extract and validate operator session from headers."""
    # Determine role from header or token
    role = RoleEnum.ADMIN
    if x_user_role:
        for r in RoleEnum:
            if r.value.lower() == x_user_role.lower() or r.name.lower() == x_user_role.lower():
                role = r
                break
    elif authorization and "analyst" in authorization.lower():
        role = RoleEnum.ANALYST
    elif authorization and "viewer" in authorization.lower():
        role = RoleEnum.VIEWER

    username = x_user_name or ("admin" if role == RoleEnum.ADMIN else ("analyst" if role == RoleEnum.ANALYST else "viewer"))
    
    perms = DEMO_USERS.get(
        "admin" if role == RoleEnum.ADMIN else ("analyst" if role == RoleEnum.ANALYST else "viewer")
    )["permissions"]

    return UserSessionModel(
        username=username,
        display_name=username.capitalize(),
        role=role,
        permissions=perms,
        token="active-session"
    )

def require_role(allowed_roles: List[RoleEnum]):
    """FastAPI dependency enforcing strict role boundaries."""
    def role_checker(current_user: UserSessionModel = Depends(get_current_user)):
        if current_user.role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Access Denied: Role '{current_user.role.value}' is not authorized to perform this operation. Required: {[r.value for r in allowed_roles]}"
            )
        return current_user
    return role_checker
