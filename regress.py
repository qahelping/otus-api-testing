from service import BaseService


class RegressService(BaseService):
    def __init__(self):
        self.DOMEN = 'https://reqres.in'

    def get_url(self, url):
        return f'{self.DOMEN}/{url}'

    def get_users(self):
        return self.get(self.get_url('api/users'), params={'page': 1})

    def assert_response_user(self, response):
        assert response['page'] == 1
        assert response['per_page'] == 6
        assert len(response['data']) == 6
        assert response['data'][0]['id'] == 1
        assert response['data'][0]['email'] == 'george.bluth@reqres.in'
        assert response['data'][0]['first_name'] == 'George'
        assert response['data'][0]['last_name'] == 'Bluth'
        assert response['data'][0]['avatar'] == 'https://reqres.in/img/faces/1-image.jpg'
