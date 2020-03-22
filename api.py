import os
from dotenv import load_dotenv
from fastapi.applications import FastAPI
from fastapi.datastructures import UploadFile
from fastapi.exceptions import HTTPException
from fastapi.param_functions import File, Body
from s3_events.s3_utils import S3_SERVICE
from utils.utils import *


env = os.getenv('ENV', 'dev')
env_file_name_dict = {
    "dev": ".dev.env",
}

project_name = "FastAPI"
path_list = os.getcwd().split('/')
PROJECT_BASE_DIR = '/'.join(path_list[:path_list.index(project_name) + 1])
env_path = f"{PROJECT_BASE_DIR}/config_env/{env_file_name_dict[env]}"

logger = logging.getLogger(__name__)

logger.info("env_path :{}".format(env_path))

load_dotenv(dotenv_path=env_path, override=True)

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
S3_Bucket = os.getenv("S3_Bucket")
S3_Key = os.getenv("S3_Key")

app = FastAPI(title="FastAPI")

# Object of S3_SERVICE Class
s3_client = S3_SERVICE(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION)


@app.get("/ping", status_code=200, description="***** Liveliness Check *****")
async def ping():
    return {"ping": "pong"}


@app.post("/upload", status_code=200, description="***** Upload png asset to S3 *****")
async def upload(fileobject: UploadFile = File(...), filename: str = Body(default=None)):
    if filename is None:
        filename = generate_png_string()
    data = fileobject.file._file  # Converting tempfile.SpooledTemporaryFile to io.BytesIO
    uploads3 = await s3_client.upload_fileobj(bucket=S3_Bucket, key=S3_Key + filename, fileobject=data)
    if uploads3:
        s3_url = f"https://{S3_Bucket}.s3.{AWS_REGION}.amazonaws.com/{S3_Key}{filename}"
        doc = [{"image_url": s3_url}]
    else:
        raise HTTPException(status_code=400, detail="Failed to upload in S3")
