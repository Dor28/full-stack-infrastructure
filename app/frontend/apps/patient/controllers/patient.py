from starlette.authentication import requires
from starlette.endpoints import HTTPEndpoint
from starlette.responses import RedirectResponse, JSONResponse

from request_sender import RequestSender
from settings import templates


class PatientList(HTTPEndpoint):
    @requires('authenticated', redirect='account:login')
    async def get(self, request):
        resp = RequestSender().get('patient/list/')

        response = templates.TemplateResponse('patient/list.html', {'request': request,
                                                                                  'patient_list': resp.json()['list']})
        return response

    async def post(self, request):
        data = await request.form()
        req_data = {
            'first_name': data.get('first_name'),
            'last_name': data.get('last_name'),
            'father_name': data.get('father_name'),
            'address': data.get('address'),
            'phone': data.get('phone')
        }
        resp = RequestSender().post('patient/create/', data=req_data)

        response = RedirectResponse(url=request.url_for("patient:list"), status_code=302)
        return response

class PatientDelete(HTTPEndpoint):
    @requires('authenticated', redirect='account:login')
    async def delete(self, request):
        patient_id = request.path_params['id']
        resp = RequestSender().delete(f'patient/{patient_id}/')
        return JSONResponse({"status": "ok"})