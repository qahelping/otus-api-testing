import pytest
import requests

import logging

@pytest.mark.add
def test_get_addoption(locale, project, base_url):
    assert locale == 'en'
    assert project == 'terminal'