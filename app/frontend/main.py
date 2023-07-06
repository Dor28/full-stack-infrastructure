from starlette.applications import Starlette
from router import routes
from settings import middleware

app = Starlette(debug=True, routes=routes, middleware=middleware)
