from fastapi import APIRouter, Response, status as http_status
from fastapi.requests import Request


router = APIRouter()


@router.get(
    "/healthcheck",
    name="service:healthcheck",
)
async def healthcheck(request: Request):
    return Response(status_code=http_status.HTTP_200_OK)


