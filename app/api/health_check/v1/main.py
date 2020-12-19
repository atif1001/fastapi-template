from fastapi import APIRouter, Depends

from app.api.auth.v1.main import get_current_active_user
from app.api.auth.v1.models import (User)


router = APIRouter()


@router.get('/health-check')
async def health_check():
    return {'online': 'true'}


@router.get('/health-check/dependencies')
async def health_check_dependencies(current_user: User = Depends(get_current_active_user)):

    response = {
        'online': True,
        'dependencies': {
            'online_service_1': True,
            'online_service_2': False
            }
        }

    return response
