""" User type. """
from typing import Optional, TYPE_CHECKING, Annotated, List
import strawberry

@strawberry.type
class UserType:
    """ User type """
    first_name: str
    id: str
    last_name: Optional[str]
    username: str
