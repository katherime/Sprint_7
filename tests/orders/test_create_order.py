import pytest
import allure
from methods.order_methods import OrderMethods
from data import right_data_for_order_creation
from data import TextsErrors

class TestCreateOrder:

    @allure.step('Проверка возможности выбора цвета самоката при оформлении заказа')
    @pytest.mark.parametrize("color", [
        ["BLACK, GREY"],
        ["GREY"],
        ["BLACK"]
    ])
    def test_create_order_with_different_colors(self, color):
        order_methods = OrderMethods()
        payload = right_data_for_order_creation
        payload["color"] = color
        response = order_methods.create_new_order(payload)
        assert response.status_code == 201 and "track" in response.text

    @allure.step('Проверка, что при отсутствии выбранного цвета, запрос сформируется и заказ будет создан')
    def test_create_order_without_colors(self):
        order_methods = OrderMethods()
        payload = right_data_for_order_creation
        response = order_methods.create_new_order(payload)
        assert response.status_code == 201 and "track" in response.text

    @allure.step('Проверка, что заказ успешно создается и тело ответа содержит track.')
    def test_create_order_with_correct_data(self):
        order_methods = OrderMethods()
        payload = right_data_for_order_creation
        response = order_methods.create_new_order(payload)
        assert response.status_code == 201 and "track" in response.text
