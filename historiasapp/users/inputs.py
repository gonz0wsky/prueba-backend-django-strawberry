
""" User inputs """
from typing import Optional
import strawberry

@strawberry.input
class LoginInput:
    """ Login Input """
    email: str
    password: str

@strawberry.input
class RegisterInput:
    """ Register Input """
    email: str
    first_name: str
    last_name: Optional[str]
    password: str
    username: str

@strawberry.input
class ChangePasswordInput:
    """ Change password input """
    current_password: str
    new_password: str
