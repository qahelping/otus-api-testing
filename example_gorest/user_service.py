import allure

from example_gorest.http_client import HttpClient
from models.user import UserResponse


class UserService:

    @staticmethod
    @allure.step('Get user {user_id}')
    def get_user(user_id):
        path = f'public/v2/users/{user_id}'
        http_client = HttpClient()
        response = http_client.get(path)

        return UserResponse(**response)

    def get_user_list(self):
        pass

    def create_user(self, body):
        pass
