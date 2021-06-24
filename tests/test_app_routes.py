import http
from app import app


# Test root route of application with index page.
def test_root():
    client = app.test_client()
    resp = client.get('/')
    assert resp.status_code == http.HTTPStatus.OK


# Test /graphql get background page.
def test_graphql():
    client = app.test_client()
    resp = client.get('/graphql')
    assert resp.status_code == http.HTTPStatus.OK
