import requests
import allure
import string
import random

from data import base_url_scooter, courier_endpoint, courier_login_endpoint


class CourierMethods:

    @allure.step('Создание курьера через POST запрос.')
    def create_courier(self, payload):
        response = requests.post(f"{base_url_scooter}{courier_endpoint}", data=payload)
        return response

    @allure.step('Логин курьера через POST запрос.')
    def courier_login(self, payload):
        response = requests.post(f"{base_url_scooter}{courier_login_endpoint}", data=payload)
        return response

    @allure.step('Логин курьера через POST запрос.')
    def courier_login_and_return_courier_track(self, payload):
        response = requests.post(f"{base_url_scooter}{courier_login_endpoint}", data=payload)
        courier_track = response.json()["id"]
        return courier_track

    @allure.step('Удаление курьера через DELETE запрос.')
    def delete_courier(self, id):
        response = requests.delete(f"{base_url_scooter}{courier_endpoint}/{id}")
        return response

    @allure.step('Регистрация нового курьреа и получение его данных.')
    def register_new_courier_and_return_login_password(self):
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
