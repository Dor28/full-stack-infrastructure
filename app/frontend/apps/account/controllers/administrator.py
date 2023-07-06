from starlette.authentication import requires
from starlette.endpoints import HTTPEndpoint
from starlette.responses import RedirectResponse, JSONResponse

from request_sender import RequestSender
from settings import templates


class AdministratorList(HTTPEndpoint):
    @requires('authenticated', redirect='account:login')
    async def get(self, request):
        resp = RequestSender().get('administration/list/')

        response = templates.TemplateResponse('account/administrator/list.html', {'request': request,
                                                                                  'user_list': resp.json()['list']})
        return response

    @requires('authenticated', redirect='account:login')
    async def post(self, request):
        data = await request.form()
        req_data = {
            'first_name': data.get('first_name'),
            'last_name': data.get('last_name'),
            'father_name': data.get('father_name'),
            'user': {
                'username': data.get('username'),
                'password': data.get('password')
            }
        }
        resp = RequestSender().post('administration/create/', data=req_data)

        response = RedirectResponse(url=request.url_for("account:administrator_list"), status_code=302)
        return response

class AdministratorDelete(HTTPEndpoint):
    @requires('authenticated', redirect='account:login')
    async def delete(self, request):
        administrator_id = request.path_params['id']
        resp = RequestSender().delete(f'administration/{administrator_id}/')
        return JSONResponse({"status": "ok"})
