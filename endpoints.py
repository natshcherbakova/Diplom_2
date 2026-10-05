# API ручки
class Endpoints:
    # создание пользователя
    create_user = "/api/auth/register"

    # авторизация пользователя
    login_user = "/api/auth/login"

    # изменение данных пользователя
    update_user = "/api/auth/user"

    # создание заказа 
    create_order = "/api/orders"

    # получение заказа конкретного пользователя
    get_user_orders = "/api/orders"
    