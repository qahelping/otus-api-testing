import csv
import os
from datetime import datetime, timedelta

import pytest
import requests
from allpairspy import AllPairs

FILES_DIR = os.path.dirname(__file__)


def get_data_from_csv():
    with open("/Users/elenayanushevskaya/QAP/otus-api-testing/files/auth_endpoints.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        for el in reader:
            yield el


parametrs = [
    ['Windows', 'MacOs', "Linux"],
    ['Chrome', 'FF', "Yandex"],
    ['EN', 'RU', "KO", "IN"]
]


def test_params():
    param = {'limit': '1'}
    response = requests.get('https://api.thecatapi.com/v1/images/search', params=param)
    assert response.status_code == 200


def test_query_params():
    limit = '5'
    response = requests.get(f'https://api.thecatapi.com/v1/images/search?limit={limit}')
    assert response.status_code == 200

@pytest.mark.parametrize(["os", "browser", "lang"], [values for values in AllPairs(parametrs)])
def test_allpairspy(os, browser, lang):
    print(os, browser, lang)

def id_val(val):
    return val[0]


auth_endpoints = get_data_from_csv()


@pytest.mark.parametrize("data", auth_endpoints, ids=id_val)
def test_with_generator(data):
    assert data[0] == 'login'

testdata = [
    (datetime(2001, 12, 12), datetime(2001, 12, 11), timedelta(1)),
    (datetime(2001, 12, 11), datetime(2001, 12, 12), timedelta(-1)),
]

@pytest.mark.parametrize("a,b,expected", testdata, ids=["forward", "backward"])
def test_timedistance_v1(a, b, expected):
    diff = a - b
    assert diff == expected