from starlette.endpoints import HTTPEndpoint
from starlette.responses import RedirectResponse

from settings import templates


class LogoutController(HTTPEndpoint):
    async def get(self, request):
        resp = RedirectResponse(url=request.url_for("index:index"), status_code=302)
        resp.delete_cookie(key='token')
        return resp