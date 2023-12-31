from fastapi import FastAPI

import settings
from router import api_router


app = FastAPI()
app.include_router(api_router, prefix='/api/v1')