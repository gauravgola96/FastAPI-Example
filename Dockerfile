FROM python:3.6.9

LABEL maintainer="<gauravgola96@gmail.com>"
LABEL description="FastAPI Dockerfile"

ARG AWS_ACCESS_KEY_ID
ENV AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
ARG ENV
ENV ENV=${ENVIRONMENT}
ARG AWS_SECRET_ACCESS_KEY
ENV AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
ARG S3_ENDPOINT
ENV S3_ENDPOINT=${S3_ENDPOINT}
ARG AWS_REGION
ENV AWS_REGION=${AWS_REGION}


ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
COPY . /srv/FastAPI
WORKDIR /srv/FastAPI
RUN pip install -r requirements.txt
EXPOSE 5050
CMD uvicorn api:app --host 0.0.0.0 --port 5050