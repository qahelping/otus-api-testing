import json

import pytest
import requests

from service_example.regress import RegressService


def test_get_user():
    regress_service = RegressService()
    response = regress_service.get_users()
    regress_service.assert_response_user(response)