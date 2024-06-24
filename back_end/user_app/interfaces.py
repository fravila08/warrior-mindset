from typing import TypedDict, Optional


class UserData(TypedDict):
    first_name: Optional[str]
    last_name: Optional[str]
    email: str
    password: str

class SerializedUser(TypedDict):
    id : int
    first_name: str
    last_name: str
    email: str
    username: str
    is_active: bool
    date_joined: str

class UserRegistrationData(TypedDict):
    user: SerializedUser
    token: str