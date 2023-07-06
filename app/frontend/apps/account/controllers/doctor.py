from starlette.authentication import requires
from starlette.endpoints import HTTPEndpoint
from starlette.responses import JSONResponse, RedirectResponse

from request_sender import RequestSender
from settings import templates


class DoctorList(HTTPEndpoint):
    @requires('authenticated', redirect='account:login')
    async def get(self, request):
        resp = RequestSender().get('doctor/list/')

        response = templates.TemplateResponse('account/doctor/list.html', {'request': request,
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
        resp = RequestSender().post('doctor/create/', data=req_data)

        response = RedirectResponse(url=request.url_for("account:doctor_list"), status_code=302)
        return response


class DoctorDelete(HTTPEndpoint):
    @requires('authenticated', redirect='account:login')
    async def delete(self, request):
        doctor_id = request.path_params['id']
        resp = RequestSender().delete(f'doctor/{doctor_id}/')
        return JSONResponse({"status": "ok"})