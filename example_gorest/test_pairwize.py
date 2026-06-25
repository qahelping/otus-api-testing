import pytest
from allpairspy import AllPairs

parameters = [
    ['Windows', 'MacOs', "Linux"],
    ['Chrome', 'FF', "Yandex"],
    ['EN', 'RU', "KO", "IN"]
]

all_pairs_parameters = [values for values in AllPairs(parameters)]

@pytest.mark.parametrize(["os", "browser", "local"], all_pairs_parameters)
def test_all_pairs(os, browser, local):
    print(os, browser, local)