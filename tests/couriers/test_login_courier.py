import pytest
import allure
from methods.couriers_methods import CourierMethods
from data import incorrect_data
from helpers import (generate_data_courier_without_login, generate_data_courier_without_password)
from data import TextsErrors

class TestLoginCourier:

    @allure.step('Проверка авторизации курьера')
    def test_successful_login_new_courier(self, login_pass):
        courier_methods = CourierMethods()
        payload = login_pass
        response = courier_methods.courier_login(payload)
        assert response.status_code == 200 and response.json()["id"] is not None

    @allure.step('Авторизация не происходит без заполнения всех обязательных полей')
    @pytest.mark.parametrize("data", [
        (generate_data_courier_without_login()),
        (generate_data_courier_without_password())
    ])
    def test_login_new_courier_without_required_fields(self, data):
        courier_methods = CourierMethods()
        payload = data
        response = courier_methods.courier_login(payload)
        assert response.status_code == 400 and response.json()[
            "message"] == TextsErrors.response_not_enough_data_for_login

    @allure.step('При введении неверной пары логин-пароль возвращается ошибка')
    def test_login_new_courier_with_wrong_data(self):
        courier_methods = CourierMethods()
        payload = incorrect_data
        response = courier_methods.courier_login(payload)
        assert response.status_code == 404 and response.json()[
            "message"] == TextsErrors.response_account_not_exist