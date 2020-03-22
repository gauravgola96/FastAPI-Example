# FastAPI
API for uploading object(.png) to S3 bucket asynchronously

Put your AWS Credentials 
```
./config_env/.dev.env
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