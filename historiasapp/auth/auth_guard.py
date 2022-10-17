""" Auth guard """
from datetime import datetime
from typing import Any, Union
from strawberry.permission import BasePermission
from strawberry.types import Info
from starlette.requests import Request
from starlette.websockets import WebSocket

from .strategy import decode_timestamp_from_token, decode_user_id_from_token

class AuthGuard(BasePermission):
    """ Auth guard """

    message = "Invalid token"

    def has_permission(self, _: Any, info: Info, **kwargs) -> bool:
        request: Union[Request, WebSocket] = info.context["request"]

        if "Authorization" in request.headers:

            token = request.headers["Authorization"]
            timestamp = decode_timestamp_from_token(token)

            if timestamp is not None and datetime.fromtimestamp(timestamp) < datetime.now():
                self.message = "Token expired"

            user: str = decode_user_id_from_token(token)
            if user is not None:
                return True

        return False
