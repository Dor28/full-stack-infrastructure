from starlette.authentication import requires
from starlette.endpoints import HTTPEndpoint
from starlette.responses import JSONResponse, RedirectResponse

from request_sender import RequestSender
from settings import templates


class CalendarList(HTTPEndpoint):
    @requires('authenticated', redirect='account:login')
    async def get(self, request):

        response = templates.TemplateResponse('calendar/list.html', {'request': request})
        return response

