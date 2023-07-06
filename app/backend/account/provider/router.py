from fastapi import APIRouter
from routers import user, reception, doctor, administration, patient

api_router = APIRouter()

api_router.include_router(user.api_router, prefix="/user", tags=["user"])
api_router.include_router(reception.api_router, prefix="/reception", tags=["reception"]),
api_router.include_router(doctor.api_router, prefix="/doctor", tags=["doctor"]),
api_router.include_router(administration.api_router, prefix="/administration", tags=["administration"]),
api_router.include_router(patient.api_router, prefix="/patient", tags=["patient"]),