from fastapi import APIRouter, Depends

from app.api.dependencies.database import get_repository
from app.db.repositories.state import StateRepository
from app.models.domain.state import State


router = APIRouter(prefix="/control", tags=["control"])


@router.post("/command")
async def get_command(
    data: State, repository: StateRepository = Depends(get_repository(StateRepository))
):
    response: State = await repository.create_state(data)
    return response
