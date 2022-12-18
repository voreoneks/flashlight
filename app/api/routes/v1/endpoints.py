from fastapi import APIRouter

router = APIRouter(
    prefix='/control',
    tags=['control']
)

@router.post('/command')
def get_command():
    pass