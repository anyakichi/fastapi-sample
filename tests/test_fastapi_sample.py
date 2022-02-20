from fastapi.testclient import TestClient

from fastapi_sample import __version__, app

client = TestClient(app)


def test_version() -> None:
    assert __version__ == "0.1.0"


def test_root() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
