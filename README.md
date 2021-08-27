# FastAPI
API for uploading object(.png) to S3 bucket asynchronously

Create a file .env and put all aws credential here
```
.env
```
aws credentials 

```
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_REGION = 
S3_Bucket = 
S3_Key = 

```


Run Server Locally (development environment)
```
python run_server.py
```

Swagger docs
```
http://0.0.0.0:5050/docs
```

Read only docs
```
http://0.0.0.0:5050/redoc
```

To provide environment and AWS credential explicitly use Dockerfile.
```
Path : ./Dockerfile
```