""" JWT token """
from datetime import datetime, timedelta
from typing import Union, Any
import jwt

# This is a test, this params should be an environment variable.
ACCESS_TOKEN_EXPIRE_MINUTES: float = 9999
REFRESH_TOKEN_EXPIRE_MINUTES: float = 9999
JWT_SECRET_KEY: str = "secret"
ALGORITHM: str = "HS256"

def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    """ Create a new access token """
    expire_minutes: float = float(ACCESS_TOKEN_EXPIRE_MINUTES)
    jwt_secret_key: str = JWT_SECRET_KEY
    algorithm: str = ALGORITHM
    delta = expires_delta or timedelta(minutes=expire_minutes)
    exp = datetime.utcnow() + delta

    to_encode = {"exp": exp, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, jwt_secret_key, algorithm)
    return encoded_jwt

def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    """ Creates a refresh token """
    expire_minutes: float = float(REFRESH_TOKEN_EXPIRE_MINUTES)
    jwt_secret_key: str = JWT_SECRET_KEY
    algorithm: str = ALGORITHM

    delta = expires_delta or timedelta(minutes=expire_minutes)
    exp = datetime.utcnow() + delta

    to_encode = {"exp": exp, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, jwt_secret_key, algorithm)
    return encoded_jwt

def decode_user_id_from_token(token:str) -> str:
    """ Decode token """
    try:
        jwt_secret_key: str = JWT_SECRET_KEY
        algorithm: str = ALGORITHM
        payload = jwt.decode(token, jwt_secret_key, algorithms=[algorithm])

        return payload.get('sub')

    except Exception: # pylint: disable=broad-except
        return None

def decode_timestamp_from_token(token:str) -> str:
    """ Decode token """
    try:
        jwt_secret_key: str = JWT_SECRET_KEY
        algorithm: str = ALGORITHM
        payload = jwt.decode(token, jwt_secret_key, algorithms=[algorithm])

        return payload.get('exp')

    except Exception: # pylint: disable=broad-except
        return None
