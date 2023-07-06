import requests
from starlette.endpoints import HTTPEndpoint
import urllib.parse

from starlette.responses import RedirectResponse

from settings import templates, controller1_base_url


class LoginController(HTTPEndpoint):
    async def get(self, request):
        response = templates.TemplateResponse('login.html', {'request': request, 'user': request.user})
        return response

    async def post(self, request):
        data = await request.form()
        if data.get('username') and data.get('password'):

            login_req_url = urllib.parse.urljoin(controller1_base_url, 'user/token')
            login_resp = requests.post(login_req_url,
                                 data={'username': data.get('username'),
                                       'password': data.get('password')})
            if login_resp.status_code != 200:
                return templates.TemplateResponse('login.html', {'request': request, 'login_error': True})

            resp = RedirectResponse(url=request.url_for("index:index"), status_code=302)
            resp.set_cookie(key='token', value=login_resp.json().get('access_token'))
        return resp