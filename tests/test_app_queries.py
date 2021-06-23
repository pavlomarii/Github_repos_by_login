import http
import json
from app import app


def test_graphql_post_success():
    query = "query fetch {user_repos(login: \"pavlomarii\") {success errors user_repo {user repos}}}"
    client = app.test_client()
    resp = client.post('/graphql', data=json.dumps({'query': query}), content_type='application/json',
                       follow_redirects=True)
    response = json.loads(resp.data.decode())
    assert resp.status_code == http.HTTPStatus.OK
    assert response['data']['user_repos']['success'] and response['data']['user_repos']['errors'] is None
