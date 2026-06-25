import json
import os

import pytest
import requests
from dotenv import load_dotenv

from example_gorest.http_client import HttpClient
from example_gorest.user_service import UserService
from models.user import UserResponse
from test_data.generate_user import generate_random_user, generate_user_with_empty_field, \
    users_required_fields_testdata, USER_8517587

load_dotenv()

GORES_TOKEN = os.getenv("GORES_TOKEN")

user = {
    "id": 8515333,
    "name": "Manoj Guha",
    "email": "manoj_guha@murray.test",
    "gender": "male",
    "status": "active"
}


@pytest.mark.api_1
def test_public_v2_users():
    url = 'https://gorest.co.in/public/v2/users'
    response = requests.get(url)
    response_json = response.json()

    assert response.status_code == 200
    assert isinstance(response_json, list)
    assert response_json[0] == user


@pytest.mark.api_2
def test_public_v2_create_users():
    url = 'https://gorest.co.in/public/v2/users'

    headers = {
        'Authorization': f'Bearer {GORES_TOKEN}',
        'Accept': 'application/json',
        'Content-type': 'application/json'

    }

    body = generate_random_user()
    response = requests.post(url, data=json.dumps(body), headers=headers)

    response_json = response.json()
    assert response.status_code == 201
    assert response_json.get('id')
    assert response_json["name"] == body["name"]
    assert response_json["email"] == body["email"]
    assert response_json["gender"] == body["gender"]
    assert response_json["status"] == body["status"]

    # запрашиваем созданного из БД
    user_id = response_json.get('id')
    url = f'https://gorest.co.in/public/v2/users/{user_id}'
    response = requests.get(url, headers=headers)
    response_json_get_user = response.json()

    assert response.status_code == 200

    assert response_json_get_user.get('id') == user_id
    assert response_json_get_user["name"] == body["name"]
    assert response_json_get_user["email"] == body["email"]
    assert response_json_get_user["gender"] == body["gender"]
    assert response_json_get_user["status"] == body["status"]


@pytest.mark.api_3
def test_public_v2_users_http_client():
    user = {
        "id": 8517587,
        "name": "Claire Meyer",
        "email": "smullins@example.org",
        "gender": "male",
        "status": "active"
    }
    path = 'public/v2/users/8517587'
    http_client = HttpClient()
    response = http_client.get(path)

    user_response = UserResponse(**response)

    print(user_response)
    breakpoint()
    assert user_response == UserResponse(**user)


@pytest.mark.api_6
def test_public_v2_users_user_service():
    user_response = UserService().get_user('8517587')

    assert user_response == UserResponse(**USER_8517587)


@pytest.mark.api_4
@pytest.mark.parametrize("filed, expected", users_required_fields_testdata)
def test_public_v2_create_users_required_fields(filed, expected):
    url = 'https://gorest.co.in/public/v2/users'

    headers = {
        'Authorization': f'Bearer 1{GORES_TOKEN}',
        'Accept': 'application/json',
        'Content-type': 'application/json'

    }

    body = generate_user_with_empty_field(filed)
    response = requests.post(url, data=json.dumps(body), headers=headers)

    response_json = response.json()
    assert response.status_code == 422
    assert response_json == expected


healthcheck_token_testdata = [
    ('public/v2/users', 'GET', 401),
    ('public/v2/users/1', 'GET', 401),
    ('public/v2/users', 'POST', 401),
    ('public/v2/users/1', 'PUT', 401)
]

INVALID_GORES_TOKEN = '1234resasdfv'


@pytest.mark.api_4
@pytest.mark.parametrize("path, method, status_code", healthcheck_token_testdata)
def test_gorest_healthcheck_token(path, method, status_code):
    url = f'https://gorest.co.in/{path}'

    headers = {
        'Authorization': f'Bearer {INVALID_GORES_TOKEN}',
        'Accept': 'application/json',
        'Content-type': 'application/json'
    }

    body = generate_random_user()
    response = requests.request(method, url, data=json.dumps(body), headers=headers)

    response_json = response.json()
    assert response.status_code == status_code
    assert response_json == {"message": "Invalid token"}
