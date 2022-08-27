from typing import Protocol

class Totp(Protocol):
    needs_totp: bool