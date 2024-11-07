import pytest

from methods.couriers_methods import CourierMethods

@pytest.fixture
def login_pass():
    courier_methods = CourierMethods()
    login_pass = courier_methods.register_new_courier_and_return_login_password()
    yield login_pass
    response = courier_methods.courier_login(login_pass)
    id = response.json()["id"]
    courier_methods.delete_courier(id)