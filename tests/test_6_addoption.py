import pytest
import requests

import logging


def test_get_addoption(locale, project, base_url):
    assert locale == 'en'
    assert project == 'terminal'