import os

import requests
from dotenv import load_dotenv

load_dotenv()

GORES_TOKEN = os.getenv("GORES_TOKEN")


class HttpClient:
    BASE_URL = 'https://gorest.co.in'

    def request(self, method, path: str, body: dict = None, code: int = 200):
        headers = {
            'Authorization': f'Bearer {GORES_TOKEN}',
            'Accept': 'application/json',
        }

        response = requests.request(method, f'{self.BASE_URL}/{path}', headers=headers, data=body)

        response_json = response.json()

        assert response.status_code == code
        return response_json

    def get(self, path: str, code: int = 200):
        return self.request('GET', path=path, code=code)

    def post(self, path: str, body: dict = None, code: int = 200):
        return self.request('POST', path=path, body=body, code=code)
