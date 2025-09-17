import json

import pytest
import requests


def test_post():
    url = 'https://api.github.com/some/endpoint'
    payload = {'some': 'data'}

    response = requests.post(url, data=json.dumps(payload))
    response_json = response.json()
    assert response.status_code == 404
    assert response_json['message'] == 'Not Found'


def test_api_post():
    body = {
        "id": 1,
        "petId": 1,
        "quantity": 0,
        "shipDate": "2024-02-17T09:42:10.119Z",
        "status": "placed",
        "complete": 'true'
    }
    headers = {'accept': "application/json", 'Content-Type': 'application/json'}
    response = requests.post('https://petstore.swagger.io/v2/store/order', data=json.dumps(body), headers=headers)
    response_json = response.json()
    assert response.status_code == requests.codes.ok
    assert response_json['id'] == body['id']
    assert response_json['status'] == body['status']

def test_unique_ids():
    response = requests.get("https://reqres.in/api/users?page=2")
    ids = [u["id"] for u in response.json()["data"]]
    assert len(ids) == len(set(ids)), "Есть дубликаты ID!"

import pytest
import requests

from data.codes import STATUS_CODE


def test_text():
    response = requests.get('https://api.thecatapi.com/v1/images/search?limit=5')
    assert response.status_code == 200
    assert 'url' in response.text
    assert 'height' in response.text
    assert 'width' in response.text
    assert 'url' in response.text
    assert 'https://cdn2.thecatapi.com/images/' in response.text


def test_json():
    response = requests.get('https://api.thecatapi.com/v1/images/search?limit=5')
    response_json = response.json()
    assert response.status_code == 200
    assert response_json[0]['id']
    assert response_json[0]['height']
    assert response_json[0]['width']
    assert 'https://cdn2.thecatapi.com/images/' in response_json[0]['url']


def test_raise_for_status_200():
    url = "https://httpbin.org/status/200"
    r = requests.get(url)

    try:
        r.raise_for_status()
        print("Запрос успешен.")
        assert True
    except requests.exceptions.HTTPError as err:
        print(f"Ошибка HTTP: {err}")
        assert False


def test_raise_for_status_500():
    url = "https://httpbin.org/status/500"
    r = requests.get(url)

    try:
        r.raise_for_status()
        print("Запрос успешен.")
        assert False
    except requests.exceptions.HTTPError as err:
        print(f"Ошибка HTTP: {err}")
        assert True


@pytest.mark.parametrize("status_code, codes", STATUS_CODE)
def test_status_codes(status_code, codes):
    response = requests.get(f'https://httpbin.org/status/{status_code}')

    assert response.status_code == codes, f"Expected {codes}, but got {response.status_code}"