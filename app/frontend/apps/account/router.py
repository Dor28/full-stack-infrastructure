from starlette.routing import Route

from apps.account.controllers.login import LoginController
from apps.account.controllers.logout import LogoutController
from apps.account.controllers.administrator import *
from apps.account.controllers.doctor import *
from apps.account.controllers.reception import *

account_routes = [
    Route('/login', endpoint=LoginController, name='login'),
    Route('/logout', endpoint=LogoutController, name='logout'),

    Route('/administrator/list', endpoint=AdministratorList, name='administrator_list'),
    Route('/administrator/{id}', endpoint=AdministratorDelete, name='administrator_delete'),

    Route('/doctor/list', endpoint=DoctorList, name='doctor_list'),
    Route('/doctor/{id}', endpoint=DoctorDelete, name='doctor_delete'),

    Route('/reception/list', endpoint=ReceptionList, name='reception_list'),
    Route('/reception/{id}', endpoint=ReceptionDelete, name='reception_delete'),
]