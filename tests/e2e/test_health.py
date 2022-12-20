from fastapi import status as HttpStatus
import pytest
import pytest_asyncio


pytestmark = pytest.mark.asyncio


async def test_healthcheck(async_client):
    response = await async_client.get("/v1/healthcheck")

    assert response.status_code == HttpStatus.HTTP_200_OK

