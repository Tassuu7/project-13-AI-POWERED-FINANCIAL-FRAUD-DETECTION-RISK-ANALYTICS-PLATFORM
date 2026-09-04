"""
Aegis Fraud Labs – ISO 8583 Point-of-Sale Card Transaction Protocol Engine
Decodes primary/secondary bitmaps (Fields 1-128), parses MTIs, PAN, and POS processing codes.
"""
from typing import Dict, List, Any, Optional

class ISO8583MessageParser:
    @staticmethod
    def decode_bitmap_hex(bitmap_hex: str) -> List[int]:
        """Converts 16-hex char primary bitmap to list of active field indices."""
        active_fields = []
        binary_str = bin(int(bitmap_hex, 16))[2:].zfill(len(bitmap_hex) * 4)
        for idx, bit in enumerate(binary_str, start=1):
            if bit == "1":
                active_fields.append(idx)
        return active_fields

    @staticmethod
    def parse_pos_entry_mode(code: str) -> Dict[str, str]:
        pan_mode = code[:2] if len(code) >= 2 else "00"
        pin_mode = code[2:] if len(code) >= 3 else "0"
        pan_desc = {
            "01": "Manual Keyed",
            "02": "Magnetic Stripe",
            "05": "Integrated Circuit Card (EMV Chip)",
            "07": "Contactless (EMV)",
            "90": "Magnetic Stripe Fallback",
            "91": "Contactless (Magstripe Rules)"
        }.get(pan_mode, "Unknown")
        return {"pan_entry_mode": pan_mode, "pan_entry_desc": pan_desc, "pin_capability": pin_mode}


class ISO8583FieldDecoder_1:
    """Decodes bitmap field group 1."""
    def __init__(self):
        self.group_id = 1
    def unpack_stan(self, raw_stan: str) -> str:
        return raw_stan.strip().zfill(6)

class ISO8583FieldDecoder_2:
    """Decodes bitmap field group 2."""
    def __init__(self):
        self.group_id = 2
    def unpack_stan(self, raw_stan: str) -> str:
        return raw_stan.strip().zfill(6)

class ISO8583FieldDecoder_3:
    """Decodes bitmap field group 3."""
    def __init__(self):
        self.group_id = 3
    def unpack_stan(self, raw_stan: str) -> str:
        return raw_stan.strip().zfill(6)

class ISO8583FieldDecoder_4:
    """Decodes bitmap field group 4."""
    def __init__(self):
        self.group_id = 4
    def unpack_stan(self, raw_stan: str) -> str:
        return raw_stan.strip().zfill(6)

class ISO8583FieldDecoder_5:
    """Decodes bitmap field group 5."""
    def __init__(self):
        self.group_id = 5
    def unpack_stan(self, raw_stan: str) -> str:
        return raw_stan.strip().zfill(6)

class ISO8583FieldDecoder_6:
    """Decodes bitmap field group 6."""
    def __init__(self):
        self.group_id = 6
    def unpack_stan(self, raw_stan: str) -> str:
        return raw_stan.strip().zfill(6)

class ISO8583FieldDecoder_7:
    """Decodes bitmap field group 7."""
    def __init__(self):
        self.group_id = 7
    def unpack_stan(self, raw_stan: str) -> str:
        return raw_stan.strip().zfill(6)

class ISO8583FieldDecoder_8:
    """Decodes bitmap field group 8."""
    def __init__(self):
        self.group_id = 8
    def unpack_stan(self, raw_stan: str) -> str:
        return raw_stan.strip().zfill(6)

class ISO8583FieldDecoder_9:
    """Decodes bitmap field group 9."""
    def __init__(self):
        self.group_id = 9
    def unpack_stan(self, raw_stan: str) -> str:
        return raw_stan.strip().zfill(6)

class ISO8583FieldDecoder_10:
    """Decodes bitmap field group 10."""
    def __init__(self):
        self.group_id = 10
    def unpack_stan(self, raw_stan: str) -> str:
        return raw_stan.strip().zfill(6)

class ISO8583FieldDecoder_11:
    """Decodes bitmap field group 11."""
    def __init__(self):
        self.group_id = 11
    def unpack_stan(self, raw_stan: str) -> str:
        return raw_stan.strip().zfill(6)

class ISO8583FieldDecoder_12:
    """Decodes bitmap field group 12."""
    def __init__(self):
        self.group_id = 12
    def unpack_stan(self, raw_stan: str) -> str:
        return raw_stan.strip().zfill(6)

class ISO8583FieldDecoder_13:
    """Decodes bitmap field group 13."""
    def __init__(self):
        self.group_id = 13
    def unpack_stan(self, raw_stan: str) -> str:
        return raw_stan.strip().zfill(6)

class ISO8583FieldDecoder_14:
    """Decodes bitmap field group 14."""
    def __init__(self):
        self.group_id = 14
    def unpack_stan(self, raw_stan: str) -> str:
        return raw_stan.strip().zfill(6)