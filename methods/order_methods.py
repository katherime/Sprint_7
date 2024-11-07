import requests
import allure
from data import (base_url_scooter, orders_accept_endpoint, orders_tracking_endpoint,
                  orders_endpoint)


class OrderMethods:

    @allure.step('Создание заказа через POST запрос.')
    def create_new_order(self, data):
        response = requests.post(f'{base_url_scooter}{orders_endpoint}', json=data)
        return response

    @allure.step('Получение списка заказов через GET запрос.')
    def get_list_of_orders(self):
        response = requests.get(f'{base_url_scooter}{orders_endpoint}')
        return response

    @allure.step('Принятие заказа через PUT запрос.')
    def accept_order(self, id_order, courier_id):
        response = requests.put(f'{base_url_scooter}{orders_accept_endpoint}{id_order}?courierId={courier_id}')
        return response

    @allure.step('Получить заказ по его номеру через GET запрос.')
    def get_order_by_number(self, order_track):
        response = requests.get(f'{base_url_scooter}{orders_tracking_endpoint}?t={order_track}')
        return response
