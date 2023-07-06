from starlette.routing import Route, Mount

from starlette.staticfiles import StaticFiles
from apps.account.router import account_routes
from apps.index.router import index_routes
from apps.patient.router import patient_routes
from apps.calendar.router import calendar_routes

routes = [
    Mount('/account', routes=account_routes, name='account'),
    Mount('/patient', routes=patient_routes, name='patient'),
    Mount('/calendar', routes=calendar_routes, name='calendar'),
    Mount('/static', StaticFiles(directory='static'), name='static'),
    Mount('', routes=index_routes, name='index'),

]