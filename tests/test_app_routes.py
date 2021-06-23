import http
from app import app


def test_root():
    client = app.test_client()
    resp = client.get('/')
    assert resp.status_code == http.HTTPStatus.OK


def test_graphql():
    client = app.test_client()
    resp = client.get('/graphql')
    assert resp.status_code == http.HTTPStatus.OK
