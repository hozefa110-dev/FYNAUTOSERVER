from fastapi import FastAPI , APIRouter, UploadFile, File
from typing import List
import os

UPLOAD_DIR = f"src/tenant"
os.makedirs(UPLOAD_DIR, exist_ok=True)

async def files_upload(files: List[UploadFile] = File(...)):
    try:
        saved = []
        for file in files:
            print(f"Received file: {file.filename}")
            contents = await file.read()
            file_path = os.path.join(UPLOAD_DIR, file.filename)
            with open(file_path, "wb") as f:
                f.write(contents)
            saved.append(file.filename)
        return {"uploaded": saved}
    except Exception as e:
        print(f'error on file_upload {e}')