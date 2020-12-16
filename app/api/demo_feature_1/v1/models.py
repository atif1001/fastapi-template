from pydantic import BaseModel, Field


class CreateRequestModel(BaseModel):
    name: str
    age: int = Field(ge=18, le=150)


class CreateResponseModel(BaseModel):
    record_id: int
    message: str


class UpdateResponseModel(BaseModel):
    message: str


class ErrorResponseDetailModel(BaseModel):
    error_type: str
    error_message: str


class ErrorResponseModel(BaseModel):
    error: ErrorResponseDetailModel
