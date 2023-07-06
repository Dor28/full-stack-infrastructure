import os

from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.templating import Jinja2Templates
import dotenv
from middlewares.auth import BasicAuthBackend, JWTAuthBackend


templates = Jinja2Templates(directory='templates')

middleware = [
    Middleware(AuthenticationMiddleware, backend=JWTAuthBackend())
]

controller1_base_url = os.getenv('PROVIDER_URL')

# JWT

