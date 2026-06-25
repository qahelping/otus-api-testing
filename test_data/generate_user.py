from faker import Faker
from faker.providers import BaseProvider


class GenderProvider(BaseProvider):
    def get_gender(self) -> str:
        genders = ['female', 'male']
        return self.random_element(genders)


class SatusProvider(BaseProvider):
    def get_status(self) -> str:
        status = ['active', 'inactive']
        return self.random_element(status)


def generate_random_user():
    fake = Faker()
    fake.add_provider(GenderProvider)
    fake.add_provider(SatusProvider)
    return {
        "name": fake.name(),
        "email": fake.email(domain='otus.com'),
        "gender": fake.get_gender(),
        "status": fake.get_status()
    }


def generate_user_with_empty_field(empty_field):
    user = generate_random_user()
    user.pop(empty_field)
    return user


users_required_fields_testdata = [
    ('name', [{"field": 'name', "message": "can't be blank"}]),
    ('email', [{"field": 'email', "message": "can't be blank"}]),
    ('gender', [{'field': 'gender', 'message': "can't be blank, can be male of female"}]),
    ('status', [{"field": 'status', "message": "can't be blank"}])
]

USER_8517587 = {
    "id": 8517587,
    "name": "Claire Meyer",
    "email": "smullins@example.org",
    "gender": "male",
    "status": "active"
}
