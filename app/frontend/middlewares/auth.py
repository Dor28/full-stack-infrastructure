import base64
import binascii
import os

import dotenv
from jose import jwt
from starlette.authentication import AuthenticationBackend, AuthenticationError, AuthCredentials, SimpleUser
from starlette.requests import Request

dotenv.load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))

class BasicAuthBackend(AuthenticationBackend):
    async def authenticate(self, request):
        if "Authorization" not in request.headers:
            return

        auth = request.headers["Authorization"]
        try:
            scheme, credentials = auth.split()
            if scheme.lower() != 'basic':
                return
            decoded = base64.b64decode(credentials).decode("ascii")
        except (ValueError, UnicodeDecodeError, binascii.Error) as exc:
            raise AuthenticationError('Invalid basic auth credentials')

        username, _, password = decoded.partition(":")
        # TODO: You'd want to verify the username and password here.
        return AuthCredentials(["authenticated"]), SimpleUser(username)


class JWTAuthBackend(AuthenticationBackend):

    async def authenticate(self, request):
        jwt_token = request.cookies.get('token')
        if jwt_token:
            try:
                payload = jwt.decode(jwt_token, SECRET_KEY,
                                     algorithms=[ALGORITHM])
            except:
                return
        else:
            return
        return AuthCredentials(["authenticated"]), SimpleUser(payload['username'])