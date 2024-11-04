import allure
from methods.order_methods import OrderMethods
from methods.couriers_methods import CourierMethods
from data import right_data_for_order_creation
from data import TextsErrors

class TestAcceptOrder:

    @allure.step('Проверка, что заказ можно принять и успешный запрос возвратится корректно')
    def test_successful_accept_order(self, login_pass):
        order_methods = OrderMethods()
        courier_methods = CourierMethods()
        courier_id = courier_methods.courier_login_and_return_courier_track(login_pass)
        create_response = order_methods.create_new_order(right_data_for_order_creation)
        id_order = create_response.json()["track"]
        response = order_methods.accept_order(id_order, courier_id)
        assert response.status_code == 200 and response.text == TextsErrors.response_succesful_text

    @allure.step('Проверка, что если не передать id курьера, запрос вернёт ошибку')
    def test_successful_accept_order_without_id_courier(self, login_pass):
        order_methods = OrderMethods()
        courier_id = ""
        create_response = order_methods.create_new_order(right_data_for_order_creation)
        id_order = create_response.json()["track"]
        response = order_methods.accept_order(id_order, courier_id)
        assert response.status_code == 400 and response.json()["message"] == TextsErrors.response_not_enough_data_for_search


    @allure.step('Проверка, что если передать неверный id курьера, запрос вернёт ошибку')
    def test_successful_accept_order_with_wrong_id_courier(self, login_pass):
        order_methods = OrderMethods()
        create_response = order_methods.create_new_order(right_data_for_order_creation)
        id_order = create_response.json()["track"]
        response = order_methods.accept_order(id_order,"1")
        assert response.status_code == 404 and response.json()["message"] == 'Курьера с таким id не существует'


    @allure.step('Проверка, что если не передать id заказа, запрос вернёт ошибку;')
    def test_successful_accept_order_without_id_order(self, login_pass):
        order_methods = OrderMethods()
        courier_methods = CourierMethods()
        courier_id = courier_methods.courier_login_and_return_courier_track(login_pass)
        response = order_methods.accept_order("",courier_id)
        assert response.status_code == 404


    @allure.step('Проверка, что если передать неверный id заказа, запрос вернёт ошибку')
    def test_successful_accept_order_with_wrong_id_order(self, login_pass):
        order_methods = OrderMethods()
        courier_methods = CourierMethods()
        courier_id = courier_methods.courier_login_and_return_courier_track(login_pass)
        response = order_methods.accept_order("1234567", courier_id)
        assert response.status_code == 404 and response.json()["message"] == 'Заказа с таким id не существует'