from starlette.routing import Route


from apps.patient.controllers.patient import *


patient_routes = [
    Route('/list', endpoint=PatientList, name='list'),
    Route('/{id}', endpoint=PatientDelete, name='delete'),

]