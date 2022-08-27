from typing import Protocol


class Snowflake(Protocol):
    id: bytes

class Message(Protocol):
    contents: str
    id: Snowflake

class User(Protocol):
    name: str
    pubkey: str
    discriminator: int
    id: Snowflake
