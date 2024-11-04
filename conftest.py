import pytest

from helpers import register_new_courier_and_return_login_password
from methods.couriers_methods import CourierMethods

@pytest.fixture
def login_pass():
    login_pass = register_new_courier_and_return_login_password()
    yield login_pass
