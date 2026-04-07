import json
from os import access

import pytest
import requests


def test_login():
    body = {"email": "charlie@example.com", "password": "password123"}
    response = requests.post('http://localhost:8000/auth/login', data=json.dumps(body))
    assert response.status_code == 200

    access_token = response.json().get('access_token')

    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get('http://localhost:8000/users/me', headers=headers)

    assert response.status_code == 200

    user = response.json()
    assert user['id'] == 4
    assert user['username'] == 'charlie'
    assert user['email'] == 'charlie@example.com'
    assert user['role'] == 'user'
    assert user['avatar_url'] is None
    assert user['created_at'] == '2026-03-16T18:29:46.995703'


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



