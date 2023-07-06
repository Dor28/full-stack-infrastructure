from starlette.authentication import requires
from starlette.endpoints import HTTPEndpoint

from settings import templates


class IndexController(HTTPEndpoint):
    @requires('authenticated', redirect='account:login')
    async def get(self, request):
        response = templates.TemplateResponse('index.html', {'request': request, 'user': request.user})
        return response
