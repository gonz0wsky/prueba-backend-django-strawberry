""" Login resolver"""
from asgiref.sync import sync_to_async
from strawberry.types import Info
from historiasapp.auth.strategy import create_access_token, decode_user_id_from_token
from historiasapp.auth.hash import check_password, hash_password
from historiasapp.users.inputs import ChangePasswordInput
from historiasapp.users.types import UserType
from .models import User
from .inputs import LoginInput, RegisterInput

async def login_user(data: LoginInput) -> str:
    """ Login """
    try:
        user: User = await sync_to_async(User.objects.get)(email=data.email)

        if user is None:
            raise Exception("Invalid credentials")

        is_valid_password: bool = check_password(data.password, user.hash)

        if not is_valid_password:
            raise Exception("Invalid credentials")

        return create_access_token(user.id)

    except Exception as error:
        raise Exception("Invalid credentials") from error

async def create_user(data: RegisterInput) -> str:
    """ Register an user """
    try:
        hashed_password: str = hash_password(data.password)

        user: User = await sync_to_async(User.objects.create)(
            email=data.email,
            first_name=data.first_name,
            hash=hashed_password,
            last_name=data.last_name,
            username=data.username)

        token = create_access_token(user.id)
        return token

    except Exception as error:
        raise Exception("Error creating user") from error

async def change_user_password(data: ChangePasswordInput, info: Info) -> bool:
    """ Change password """
    try:
        token: str = info.context.request.headers['Authorization']
        user_id: str = decode_user_id_from_token(token)
        user: User = await sync_to_async(User.objects.get)(id=user_id)
        is_valid_password: bool = check_password(data.current_password, user.hash)

        if not is_valid_password:
            raise Exception("Error changing password")

        user.hash = hash_password(data.new_password)
        await sync_to_async(User.save)(user)

        return True

    except Exception as error:
        raise Exception("Error changing password") from error

async def get_user(info: Info) -> UserType:
    """Get logged user resolver"""
    try:
        token: str = info.context.request.headers['Authorization']
        user_id: str = decode_user_id_from_token(token)

        user: User = await sync_to_async(User.objects.get)(id=user_id)

        return UserType(
            id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            username=user.username)

    except Exception as error:
        raise Exception("Error getting user") from error