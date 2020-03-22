# Response Model
from fastapi.datastructures import UploadFile
from fastapi.param_functions import Body
from fastapi.params import File
from pydantic.main import BaseModel
from typing import List


class AssestRequestOne(BaseModel):
    _id: str
    image_url: str
    updated_at: str
    created_at: str


class AssestRequestModel(BaseModel):
    data: List[AssestRequestOne] = []


class AssetUploadModel(BaseModel):
    fileobject: UploadFile = File(...)
    filename: str = Body(default=None)


