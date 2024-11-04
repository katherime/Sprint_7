import pytest
import allure
from methods.couriers_methods import CourierMethods
from helpers import (generate_right_data_for_new_courier,
                     generate_data_courier_without_login, generate_data_courier_without_password)
from data import TextsErrors

class TestCreateCourier:

    @allure.step('Проверка создания нового курьера')
    def test_create_new_courier(self):
        courier_methods = CourierMethods()
        payload = generate_right_data_for_new_courier()
        response = courier_methods.create_courier(payload)
        assert response.status_code == 201 and response.text == TextsErrors.response_succesful_text

    @allure.step('Проверка, что невозможно создать двух одинаковым курьеров')
    def test_create_two_identical_courier(self):
        courier_methods = CourierMethods()
        payload = generate_right_data_for_new_courier()
        first_response = courier_methods.create_courier(payload)
        second_response = courier_methods.create_courier(payload)
        assert second_response.status_code == 409 and second_response.json()[
            "message"] == TextsErrors.response_login_already_exist

    @allure.step('Проверка, что невозможно создать курьера с незаполненными обязательными полями')
    @pytest.mark.parametrize("data", [
        (generate_data_courier_without_login()),
        (generate_data_courier_without_password())
    ])
    def test_create_courier_without_required_fields(self, data):
        courier_methods = CourierMethods()
        payload = data
        response = courier_methods.create_courier(payload)
        assert response.status_code == 400 and response.json()[
            "message"] == TextsErrors.response_not_enough_data

