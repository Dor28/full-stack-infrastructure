from starlette.routing import Route

from apps.index.controllers.indox import IndexController

index_routes = [
    Route('/', endpoint=IndexController, name='index'),
]