import sys, os
from starlette.testclient import TestClient

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + "/../")

from api import app


client = TestClient(app)


def test_read_main():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong"}


def test_upload():
    filename = "test/test_image.png"
    file={"fileobject": ("filename", open(filename, "rb"), "image/png")}
    response = client.post(
        "/upload", files=file
    )
    assert response.status_code == 200

