from litestar.testing import TestClient

from app import app


def test_sync() -> None:
    with TestClient(app=app) as client:
        assert client.get("/sync").json() == {"hello": "world"}


def test_async() -> None:
    with TestClient(app=app) as client:
        assert client.get("/async").json() == {"hello": "world"}
