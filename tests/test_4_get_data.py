import csv

import pytest
from allpairspy import AllPairs

def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)


CSV_FILE_PATH = get_path(filename="auth_endpoints.csv")


def get_auth_endpoints():
    with open(CSV_FILE_PATH, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for el in reader:
            yield el


auth_endpoints = get_auth_endpoints()

parametrs = [
    ['Windows', 'MacOs', "Linux"],
    ['Chrome', 'FF', "Yandex"],
    ['EN', 'RU', "KO", "IN"]
]



@pytest.mark.parametrize(["os", "browser", "lang"], [values for values in AllPairs(parametrs)])
def test_allpairspy(os, browser, lang):
    print(os, browser, lang)

def id_val(val):
    return val[0]


auth_endpoints = get_data_from_csv("../files/auth_endpoints.csv")


@pytest.mark.parametrize("data", auth_endpoints, ids=id_val)
def test_with_generator(data):
    assert data[0] == 'login'


data = get_data_from_json("../files/file.json")


class Player(BaseModel):
    name: str
    rank: int
    gold: str
    dead: bool


@pytest.mark.parametrize("data", data)
def test_json(data):
    print(data)
    assert data['name'] in ('Dominator', 'TheKiller', 'Vasya666', 'Cheater')


@pytest.mark.parametrize("data", data)
def test_json_2(data):
    obj = {
        "name": "Dominator",
        "rank": 1,
        "gold": "100000",
        "dead": False
    },
    player = Player.model_validate_json(obj)