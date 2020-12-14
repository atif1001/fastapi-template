from fastapi import APIRouter

router = APIRouter()


@router.get('/admin')
async def index():
    return {'message': 'Admin APIs'}
