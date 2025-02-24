import requests
from faker import Faker
from curl import Url




fake = Faker()

def register_new_user():
    return {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.name()
    }


class DataForUser:
    EMAIL = fake.email()
    PASSWORD = fake.password()







