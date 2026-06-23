import json
import os

import pytest
import requests
from dotenv import load_dotenv
from faker import Faker

from example_gorest.http_client import HttpClient

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
    fake = Faker()
    url = 'https://gorest.co.in/public/v2/users'

    headers = {
        'Authorization': f'Bearer {GORES_TOKEN}',
        'Accept': 'application/json',
        'Content-type': 'application/json'

    }

    body = {
        "name": fake.name(),
        "email": fake.email(),
        "gender": "male",
        "status": "active"
    }
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

    assert isinstance(response, dict)
    assert response == user
