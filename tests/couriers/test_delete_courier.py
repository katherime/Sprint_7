import allure
from methods.couriers_methods import CourierMethods
from data import TextsErrors


class TestDeleteCourier:

    @allure.title('Проверка удаления курьера c возвращением успешного запроса')
    def test_successful_delete_courier(self, login_pass):
        courier_methods = CourierMethods()
        payload = login_pass
        login_response = courier_methods.courier_login(payload)
        id_courier = login_response.json()["id"]
        delete_response = courier_methods.delete_courier(id_courier)
        assert delete_response.status_code == 200 and delete_response.json() == {'ok': True}

    @allure.title('Проверка, что если не передать id курьера, запрос вернёт ошибку')
    def test_delete_courier_without_id_courier(self):
        courier_methods = CourierMethods()
        courier_id = ""
        delete_response = courier_methods.delete_courier(courier_id)
        assert delete_response.status_code == 404

    @allure.title('Проверка, что если передать несуществующий id курьера, запрос вернёт ошибку')
    def test_delete_courier_with_wrong_id_courier(self):
        courier_methods = CourierMethods()
        id = "1"
        response = courier_methods.delete_courier(id)
        assert response.status_code == 404 and response.json()["message"] == TextsErrors.response_wrong_id_courier
