from fastapi import FastAPI

from app.api.routes.v1 import endpoints
from app.core.logging import app_logger
from app.api.routes.v1 import health


app = FastAPI()

app.include_router(endpoints.router, prefix="/v1")
app.include_router(health.router, prefix="/v1")
app.logger = app_logger
