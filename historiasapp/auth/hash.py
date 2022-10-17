
""" hash """
import bcrypt

def hash_password(password: str) -> str:
    """ Hash a password """
    hasshed_password: bytes = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hasshed_password.decode()

def check_password(password: str, hashed: str) -> bool:
    """ Check if a password matches a hashed password """
    return bcrypt.checkpw(password.encode(), hashed.encode())