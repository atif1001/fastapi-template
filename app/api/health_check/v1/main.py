from fastapi import APIRouter

router = APIRouter()


@router.get('/health-check')
async def health_check():
    return {'online': 'true'}


@router.get('/health-check/details')
async def health_check_details():

    response = {
        'online': True,
        'dependencies': {
            'online_service_1': True,
            'online_service_2': False
            }
        }

    return response
