import os
from dotenv import load_dotenv
from fastapi.applications import FastAPI
from fastapi.datastructures import UploadFile
from fastapi.exceptions import HTTPException
from fastapi.param_functions import File, Body
from s3_events.s3_utils import S3_SERVICE
from utils.utils import *
from dotenv import load_dotenv
import datetime


load_dotenv()
project_name = "FastAPI"


AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.environ.get("AWS_REGION")
S3_Bucket = os.environ.get("S3_Bucket")
S3_Key = os.environ.get("S3_Key")

app = FastAPI(title="FastAPI")

# Object of S3_SERVICE Class
s3_client = S3_SERVICE(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION)


@app.get("/ping", status_code=200, description="***** Liveliness Check *****")
async def ping():
    return {"ping": "pong"}


@app.post("/upload", status_code=200, description="***** Upload png asset to S3 *****")
async def upload(fileobject: UploadFile = File(...)):
    filename = fileobject.filename
    current_time = datetime.datetime.now()
    split_file_name = os.path.splitext(filename)   #split the file name into two different path (string + extention)
    file_name_unique = str(current_time.timestamp()).replace('.','')  #for realtime application you must have genertae unique name for the file
    file_extension = split_file_name[1]  #file extention
    data = fileobject.file._file  # Converting tempfile.SpooledTemporaryFile to io.BytesIO
    uploads3 = await s3_client.upload_fileobj(bucket=S3_Bucket, key=S3_Key + file_name_unique+  file_extension, fileobject=data)
    if uploads3:
        s3_url = f"https://{S3_Bucket}.s3.{AWS_REGION}.amazonaws.com/{S3_Key}{file_name_unique +  file_extension}"
        return {"status": "success", "image_url": s3_url}  #response added 
    else:
        raise HTTPException(status_code=400, detail="Failed to upload in S3")
