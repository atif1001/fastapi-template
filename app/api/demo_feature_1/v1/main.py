import traceback

from fastapi import APIRouter, HTTPException, responses, status

from .models import CreateRequestModel, CreateResponseModel, UpdateResponseModel, ErrorResponseModel
from ...libs.responses import error_response
from .data import dummy_data

router = APIRouter()


@router.get('/demo-feature-1')
async def list():
    return dummy_data


@router.post(
    '/demo-feature-1',
    summary='Create a new record',
    response_model=CreateResponseModel,
    responses={406: {'model': ErrorResponseModel}},
    # response_description="Success Response"
)
async def create(payload: CreateRequestModel):
    """
    Create a new record, age range allowed is 18 - 150

    Additional description in markdown format, shown in swagger docs.
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

    except Exception as e:
        print(f'Error: {e} \n {traceback.format_exc()}')
        return error_response('SERVER_ERROR', traceback.format_exc())


@router.get('/demo-feature-1/{feature_id}')
async def read(feature_id: str):
    return feature_id


@router.put('/demo-feature-1/{feature_id}', response_model=UpdateResponseModel)
async def update(feature_id: str, payload: CreateRequestModel):
    response_data = {'message': f'Updating record: {feature_id} -> {payload}'}
    return response_data


@router.delete('/demo-feature-1/{feature_id}')
async def delete():
    return dummy_data
