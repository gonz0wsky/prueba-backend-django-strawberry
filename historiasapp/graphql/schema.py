
""" Graphql Mutation Schema """
from typing import Any
import strawberry
from strawberry.django.views import AsyncGraphQLView
from historiasapp.auth.context import StrawberryDjangoContext
from strawberry.schema.config import StrawberryConfig
from historiasapp.auth.auth_guard import AuthGuard
from historiasapp.graphql.middlewares import TokenMiddleware
from historiasapp.users.resolvers import change_user_password, create_user, get_user, login_user

from django.http import HttpRequest, HttpResponse

class MyGraphQLView(AsyncGraphQLView):
    async def get_context(self, request: HttpRequest, response: HttpResponse) -> Any:
        return {"example": 1}

@strawberry.type
class Query:
    """ Queries """
    user = strawberry.field(permission_classes=[AuthGuard], resolver=get_user)

@strawberry.type
class Mutation:
    """ Mutations """
    change_password = strawberry.mutation(permission_classes=[AuthGuard], resolver=change_user_password)
    login = strawberry.mutation(resolver=login_user)
    register = strawberry.mutation(resolver=create_user)

schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    config=StrawberryConfig(auto_camel_case=True),
    extensions=[
        TokenMiddleware
    ])