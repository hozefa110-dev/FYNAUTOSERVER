from fastapi import FastAPI , APIRouter, UploadFile, File
from typing import List
from fynautoserver.controller.file_config_crud import files_upload

app = FastAPI()

router = APIRouter()

@router.post('/fileConfigsUpload')
async def file_configs_upload(files: List[UploadFile] = File(...)):
    response = await files_upload(files)
    return response
