from fastapi import APIRouter, Depends

from app.api.auth.v1.main import get_current_active_user
from app.api.auth.v1.models import (User)


router = APIRouter()


@router.get('/admin')
async def index(current_user: User = Depends(get_current_active_user)):
    return {'message': 'Admin APIs'}
