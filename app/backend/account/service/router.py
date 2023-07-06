from fastapi import APIRouter
from routers import user, administration, doctor, reception, patient, visit, analysis

api_router = APIRouter()
#
api_router.include_router(user.api_router, prefix="/user", tags=["user"])
api_router.include_router(administration.api_router, prefix="/administration", tags=["administration"])
api_router.include_router(doctor.api_router, prefix="/doctor", tags=["doctor"])
api_router.include_router(reception.api_router, prefix="/reception", tags=["reception"])
api_router.include_router(patient.api_router, prefix="/patient", tags=["patient"])
api_router.include_router(visit.api_router, prefix="/visit", tags=["visit"])
api_router.include_router(analysis.api_router, prefix="/analysis", tags=["analysis"])