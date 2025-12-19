import json

import pytest
import requests


def test_simple_auth():
    url = 'https://httpbin.org/basic-auth/user/password'

    response = requests.get(url, auth=('user', 'password'))

    assert response.status_code == 200
    assert response.json().get('authenticated') == True
    assert response.json().get('user') == 'user'

# https://jwt.qa.studio/api/v1/docs
@pytest.fixture
def token():
    url_token = 'https://jwt.qa.studio/api/v1/jwt/token'

    body = {
        "login": "example@qa.studio",
        "password": "wfdswhHXIAUDTQ"
    }

    response = requests.post(url_token, data=json.dumps(body))

    response_json = response.json()
    yield response_json['access_token']


def test_jwt_token(token):
    url_data = 'https://jwt.qa.studio/api/v1/jwt/data'

    headers = {'accept': 'application/json', 'Authorization': f'Bearer {token}'}

    response_data = requests.get(url_data, headers=headers)


    response_data_json = response_data.json()
    print(response_data_json['success'])
    assert response_data_json['success'] == "my secure data"
    assert response_data.status_code == 200


def test_jwt_token_failed():
    url_data = 'https://jwt.qa.studio/api/v1/jwt/data'

    headers = {'accept': 'application/json'}

    response_data = requests.get(url_data, headers=headers)

    response_data_json = response_data.json()
    assert response_data.status_code == 200
    assert response_data_json['success'] == "my secure data"
    assert response_data.status_code == 200



