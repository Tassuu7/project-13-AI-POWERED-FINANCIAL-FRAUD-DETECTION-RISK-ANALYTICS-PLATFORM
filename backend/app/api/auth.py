"""Local authentication and role session management."""

from fastapi import APIRouter
from backend.app.models.schemas import LoginRequest, UserSession, UserRole

router = APIRouter(prefix="/auth", tags=["Authentication"])

ROLE_PERMISSIONS = {
    UserRole.ANALYST: [
        "dataset:upload", "dataset:generate", "preprocessing:run",
        "models:train", "predictions:run", "reports:generate"
    ],
    UserRole.REVIEWER: [
        "suspicious:view", "suspicious:review", "suspicious:notes",
        "reports:generate", "exports:download"
    ],
    UserRole.ADMIN: [
        "all:access", "settings:modify", "history:view", "models:delete"
    ]
}


@router.post("/login", response_model=UserSession)
def login(req: LoginRequest):
    """Local demo authentication supporting Analyst, Reviewer, and Admin roles."""
    perms = ROLE_PERMISSIONS.get(req.role, ["read"])
    return UserSession(
        username=req.username or f"demo_{req.role.value.lower()}",
        role=req.role,
        authenticated=True,
        permissions=perms
    )


@router.get("/session", response_model=UserSession)
def get_session():
    """Retrieve default active session."""
    return UserSession(
        username="lead_analyst",
        role=UserRole.ANALYST,
        authenticated=True,
        permissions=ROLE_PERMISSIONS[UserRole.ANALYST]
    )
