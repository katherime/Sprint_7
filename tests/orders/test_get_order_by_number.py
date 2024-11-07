import allure
from methods.order_methods import OrderMethods
from data import right_data_for_order_creation
from data import TextsErrors


class TestGetOrderByNumber:

    @allure.title('Проверка, что успешный запрос возвращает объект с заказом')
    def test_successful_get_order_by_number(self, login_pass):
        order_methods = OrderMethods()
        create_response = order_methods.create_new_order(right_data_for_order_creation)
        id_order = create_response.json()["track"]
        response = order_methods.get_order_by_number(id_order)
        assert response.status_code == 200 and response.json()["order"] is not None

    @allure.title('Проверка, что запрос без номера заказа возвращает ошибку')
    def test_successful_get_order_by_number_without_order_id(self, login_pass):
        order_methods = OrderMethods()
        id_order = ""
        response = order_methods.get_order_by_number(id_order)
        assert (response.status_code == 400 and response.json()["message"] ==
                TextsErrors.response_not_enough_data_for_search)

    @allure.title('Проверка, что запрос с несуществующим заказом возвращает ошибку')
    def test_successful_get_order_by_number_with_wrong_order_id(self, login_pass):
        order_methods = OrderMethods()
        id_order = "123456"
        response = order_methods.get_order_by_number(id_order)
        assert (response.status_code == 404 and response.json()["message"] ==
                TextsErrors.response_order_not_exist)
