import pytest
import requests


def test_params():
    param = {'limit': '1'}
    response = requests.get('https://api.thecatapi.com/v1/images/search', params=param)
    assert response.status_code == 200


def test_query_params():
    limit = '5'
    response = requests.get(f'https://api.thecatapi.com/v1/images/search?limit={limit}')
    assert response.status_code == 200

def test_get():
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    assert response.status_code == 200
    assert 'message' in response.text


def test_simple_example():
    url = "https://reqres.in/api/"

    response_1 = requests.request("GET", url)
    # response_2 = requests.post(url)

    assert 'name' in response_1.text
    assert response_1.status_code == 200
    print(response_1.text)

    # assert response_2.status_code == 401
    # print(response_2.text)
@pytest.mark.only
def test_post():
    response = requests.post('https://httpbin.org/post', data={'key': 'value'})
    res_json = response.json()

    assert response.status_code != 100
    assert response.status_code in ['100', '100']
    assert res_json['headers']['Host'] == 'httpbin.org'


def test_put():
    response = requests.put('https://httpbin.org/put', data={'key': 'value'})
    assert response.status_code == 200


def test_delete():
    response = requests.delete('https://httpbin.org/delete')
    assert response.status_code == 200


def test_head():
    response = requests.head('https://httpbin.org/head')
    assert response.status_code == 404


def test_options():
    response = requests.options('https://httpbin.org/options')
    assert response.status_code == 404