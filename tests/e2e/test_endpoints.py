from fastapi import status as HttpStatus
from fastapi import Response
import pytest
import pytest_asyncio


pytestmark = pytest.mark.asyncio


async def test_post_command(async_client):
    data = {
  "command": "ON",
  "metadata": 0
}
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    print(data)
    response: Response = await async_client.post(
        '/v1/control/command', 
        json=data, headers=headers)
    assert response.json() == {
                "state": "ON",
                "color": 0
            }


async def test_get_state(async_client):
    await test_post_command(async_client)
    response: Response = await async_client.get('/v1/control/')
    assert response.json() == {
                "state": "ON",
                "color": 0
            }