import json

import pytest
import requests
from requests import HTTPError


def test_post():
    url = 'https://api.github.com/some/endpoint'
    payload = {'some': 'data'}

    response = requests.post(url, data=json.dumps(payload))
    response_json = response.json()
    print(response_json)
    assert response.status_code == 404
    assert response_json['message'] == 'Not Found'
    assert response_json['documentation_url'] == "https://docs.github.com/rest"
    assert response_json['status'] == "404"


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
    response = requests.get("https://api.thecatapi.com/v1/images/search?limit=5")

    ids = [u["id"] for u in response.json()]
    assert len(ids) == len(set(ids)), "Есть дубликаты ID!"

STATUS_CODE = [
    (200, requests.codes.ok),  # OK
    (300, requests.codes.multiple_choices),  # Multiple Choices
    (400, requests.codes.bad_request),  # Bad Request
    (418, requests.codes.im_a_teapot),  # im a teapot
    (404, requests.codes.not_found),  # Not Found
    (500, requests.codes.internal_server_error),  # Internal Server Error
    (511, requests.codes.network_authentication),  # Network Authentication Required
]


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
    print(response.json())
    for r in response.json():
        assert r.get('id')
        assert r['height']
        assert r['width']
    assert 'https://cdn2.thecatapi.com/images/' in response_json[0]['url']


def test_raise_for_status_200():
    url = "https://httpbin.org/status/500"
    r = requests.get(url)

    try:
        r.raise_for_status()
        print("Запрос успешен.")
        assert True
    except requests.exceptions.HTTPError as err:
        assert False, f"Ошибка HTTP: {err}"


def test_raise_for_status_500():
    url = "https://httpbin.org/status/500"
    r = requests.get(url)

    with pytest.raises(HTTPError):
        r.raise_for_status()

    try:
        r.raise_for_status()
        assert False, "Запрос успешен."
    except requests.exceptions.HTTPError as err:
        assert True, f"Ошибка HTTP: {err}"


@pytest.mark.parametrize("status_code, codes", STATUS_CODE)
def test_status_codes(status_code, codes):
    response = requests.get(f'https://httpbin.org/status/{status_code}')

    assert response.status_code == codes, f"Expected {codes}, but got {response.status_code}"

def test_send_csv_file():
    text = 'some, data, to, send\nanother, row, to, send\n'
    url = 'https://httpbin.org/post'
    files = {'file': ('report.csv', text)}
    response = requests.post(url, files=files)
    response_json = response.json()
    assert response_json['files']['file'] == text


def test_send_image():
    url = 'https://petstore.swagger.io/v2/pet/1/uploadImage'
    with open('/Users/elenayanushevskaya/QAP/otus-api-testing/files/expected_image.png', 'rb') as fp:
        files = {'file': ('img.png', fp, 'image/png', {'Expires': '0'})}
        response = requests.post(url, files=files)

    assert response.status_code == requests.codes.ok
    assert 'File uploaded to' in response.text


def test_get_file():
    url = 'https://httpbin.org/image/png'
    response = requests.get(url)
    content = response.content
    assert response.status_code == 200

    with open('/Users/elenayanushevskaya/QAP/otus-api-testing/files/expected_image.png', 'rb') as local_file:
        local_file_content = local_file.read()

    assert content == local_file_content, "Files are not identical"