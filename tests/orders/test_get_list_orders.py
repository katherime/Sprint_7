import allure
from methods.order_methods import OrderMethods


class TestGetListOfOrders:

    @allure.title('Проверка, что возможно получить список заказов')
    def test_successful_get_list_of_orders(self):
        order_methods = OrderMethods()
        response = order_methods.get_list_of_orders()
        assert response.status_code == 200 and response.json()["orders"] is not None
