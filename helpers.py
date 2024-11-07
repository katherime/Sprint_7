import requests
import string
import random
from faker import Faker




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