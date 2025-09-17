import pytest
import requests

import logging


def test_get_addoption(locale, url, project, base_url):
    assert locale == 'en'
    assert url == 'en'