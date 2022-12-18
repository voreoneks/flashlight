from fastapi import FastAPI

from app.api.routes.v1 import endpoints


app = FastAPI()

app.include_router(endpoints.router, prefix="/v1")
