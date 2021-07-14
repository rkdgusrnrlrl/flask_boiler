from app import create_app
import pytest
import json
from exception import InvalidUsage


@pytest.fixture
def client():
    app = create_app()
    client = app.test_client()
    return client


def test_not_allow_json_user(client):
    response = client.post("/users")
    assert response.status_code == 400

    dd = response.json
    mm = InvalidUsage.ERROR_MESSAGE['allow_json']
    assert dd['message'] == mm


def test_require_param(client):
    dd = {
        'id': 'abcd'
    }
    response = client.post("/users", data=json.dumps(dd), content_type='application/json')
    dd = response.json

    assert response.status_code == 400
    assert InvalidUsage.ERROR_MESSAGE['require_param'] in dd['message']


def test_200(client):
    dd = {
        'id': 'abcd',
        'password': 'abcd'
    }
    response = client.post("/users", data=json.dumps(dd), content_type='application/json')
    dd = response.json

    assert response.status_code == 200
    assert 'success' == dd['result']
