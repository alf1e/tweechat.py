from aiohttp import ClientSession
from .event_handler import EventHandle
from .totp import Totp


class Client(EventHandle):
    def __init__(self):
        super().__init__()

        self.headers = {
            "content-type": "application/json"
        }
        self.session = ClientSession(headers=self.headers, base_url="https://api.twee.chat")
        self.token = None

    def login(self, email: str, password: str):
        resp = await self.session.post("/auth/token", json={"email": email, "password": password}).json()
        if resp["needs_totp"]:
            totp = Totp.needs_totp = True
            self.call("totp", totp)

        self.token = resp["token"]

    def totp(self, otp: int):
        resp = await self.session.post("/auth/totp", json={"token": self.token, "one_time_password": otp}).json()
        self.token = resp["token"]
        self.headers["Authorization"] = f"Bearer {self.token}"
        self.session = ClientSession(headers=self.headers, base_url="https://api.twee.chat")



