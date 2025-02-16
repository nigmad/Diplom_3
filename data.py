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





class MethodsForApi:
    def register_user(self, user_data):
        response = requests.post(f'{Url.MAIN_SITE_URL}{Url.CREATE_USER}' , json=user_data)
        return response


    def login_user(self, user_data):
        response = requests.post(f'{Url.MAIN_SITE_URL}{Url.LOGIN_USER}', json=user_data)
        return response


    def delete_user(self, token):
        return requests.delete(f'{Url.MAIN_SITE_URL}{Url.DELETE_USER}', headers={"Authorization": f"{token}"})