base_url_scooter = 'https://qa-scooter.praktikum-services.ru'
courier_endpoint = '/api/v1/courier/'
courier_login_endpoint = '/api/v1/courier/login/'
orders_endpoint = '/api/v1/orders/'
orders_accept_endpoint = '/api/v1/orders/accept/'
orders_tracking_endpoint = '/api/v1/orders/track'

incorrect_data = {
    "login": "123456",
    "password": "123456"
}

correct_data = {
    "login": "123456",
    "password": "123456"
    "first"
}


data_for_order = {
    "id": "12",
    "courierId": "12"
}

right_data_for_order_creation = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": []
}


class TextsErrors:
    response_succesful_text = '{"ok":true}'
    response_login_already_exist = "Этот логин уже используется. Попробуйте другой."
    response_not_enough_data = "Недостаточно данных для создания учетной записи"
    response_wrong_id_courier = "Курьера с таким id нет."
    response_not_enough_data_for_login = "Недостаточно данных для входа"
    response_not_enough_data_for_search = "Недостаточно данных для поиска"
    response_account_not_exist = "Учетная запись не найдена"
    response_order_not_exist = "Заказ не найден"
    response_id_courier_not_exist = "Курьера с таким id не существует"
    response_id_order_not_exist = "Заказа с таким id не существует"