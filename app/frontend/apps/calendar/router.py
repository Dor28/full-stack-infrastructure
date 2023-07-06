from starlette.routing import Route

from apps.account.controllers.login import LoginController
from apps.calendar.controllers.calendar import *

calendar_routes = [
    Route('/list', endpoint=CalendarList, name='list'),

]