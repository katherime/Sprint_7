import requests
import allure
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
