from fastapi import APIRouter, Depends

from app.api.dependencies.database import get_repository
from app.db.repositories.state import StateRepository
from app.models.domain.state import State


router = APIRouter(prefix="/control", tags=["control"])


@router.post("/command")
async def post_command(
    data: State, 
    repository: StateRepository = Depends(get_repository(StateRepository))
) -> State:
    response: State = await repository.create_state(data)
    return response

@router.get('/')
async def get_state(
    repository: StateRepository = Depends(get_repository(StateRepository))
) -> State:
    response: State = await repository.get_state()
    return response