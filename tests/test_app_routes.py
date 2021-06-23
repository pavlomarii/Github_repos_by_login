import http
from app import app


def test_root():
    client = app.test_client()
    resp = client.get('/')
    assert resp.status_code == http.HTTPStatus.OK
