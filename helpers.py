import requests
import string
import random
from faker import Faker


def register_new_courier_and_return_login_password():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = []
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)
    return payload


def generate_courier_login():
    faker = Faker()
    login = faker.user_name() + '1'
    return login

def generate_courier_password():
    faker = Faker()
    password = faker.password()
    return password

def generate_courier_firstname():
    faker = Faker()
    firstname = faker.first_name()
    return firstname

def generate_data_courier_without_login():
    data  = {
        "login" : "",
        "password" : generate_courier_password(),
    }
    return data

def generate_data_courier_without_password():
    data  = {
        "login": generate_courier_login(),
        "password": "",
    }
    return data

def generate_data_courier_without_firstname():
    data  = {
        "login": generate_courier_login(),
        "password": generate_courier_password(),
        "firstName": ""
    }
    return data

def generate_right_data_for_new_courier():
    payload = {
        "login": generate_courier_login(),
        "password": generate_courier_password(),
        "firstName": generate_courier_firstname()
    }
    return payload