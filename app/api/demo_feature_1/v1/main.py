import traceback

from fastapi import APIRouter, responses, status, Depends

from app.config import get_settings
from app.libs.logging import logger
from app.api.auth.v1.main import get_current_active_user
from app.api.auth.v1.models import (User)
from app.libs.responses import error_response
from app.api.demo_feature_1.v1.models import (
    CreateRequestModel,
    CreateResponseModel,
    UpdateResponseModel,
    ErrorResponseModel
)
from app.api.demo_feature_1.v1.data import dummy_data


router = APIRouter()
config = get_settings()


@router.get('/demo-feature-1')
def list(current_user: User = Depends(get_current_active_user)):
    try:
        return dummy_data
    except Exception:
        logger.exception('Exception: ')


@router.post(
    '/demo-feature-1',
    summary='Create a new record',
    response_model=CreateResponseModel,
    responses={
        406: {'model': ErrorResponseModel}
        }
    # response_description="Success Response"
)
def create(payload: CreateRequestModel, current_user: User = Depends(get_current_active_user)):
    """
    Create a new record. Age parameter can be from 18 to 150.

    Additional description shown in swagger docs. (Markdown format allowed.)
    - **name**: Limted to 100 characters
    - **age**: Age from 18 to 150
    """
    try:
        name = payload.name
        age = payload.age
        body_data = {'record_id': 1003, 'message': f'Name: {name} and Age: {age}'}

        if age < 21:
            # raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail='Age less than 21 not allowed')
            return responses.JSONResponse(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                content=error_response('VALUE_NOT_ALLOWED', 'Age less than 21 is not allowed')
                                          )

        return body_data

    except Exception:
        logger.exception('Exception: ')
        return error_response('SERVER_ERROR', traceback.format_exc())


@router.get('/demo-feature-1/{feature_id}')
def read(feature_id: str, current_user: User = Depends(get_current_active_user)):
    try:
        response_data = f' App named [{config.APP_NAME}] got the value: {feature_id}'
        return response_data
    except Exception:
        logger.exception('Exception: ')


@router.put('/demo-feature-1/{feature_id}', response_model=UpdateResponseModel)
def update(feature_id: str, payload: CreateRequestModel, current_user: User = Depends(get_current_active_user)):
    try:
        response_data = {'message': f'Updating record: {feature_id} -> {payload}'}
        return response_data
    except Exception:
        logger.exception('Exception: ')


@router.delete('/demo-feature-1/{feature_id}')
def delete(current_user: User = Depends(get_current_active_user)):
    try:
        return dummy_data
    except Exception:
        logger.exception('Exception: ')
