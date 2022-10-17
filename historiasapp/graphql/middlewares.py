""" Token middleware """
from strawberry.extensions import Extension
from historiasapp.auth.strategy import decode_user_id_from_token

SKIP = ['IntrospectionQuery']

class TokenMiddleware(Extension):
    """ Add user_id to context """

    def on_request_start(self):
        operation_name: str = self.execution_context.operation_name
        if operation_name in SKIP:
            return

        request = self.execution_context.context['request']
        if "Authorization" in request.headers:
            token = request.headers["Authorization"]
            user_id: str = decode_user_id_from_token(token)
