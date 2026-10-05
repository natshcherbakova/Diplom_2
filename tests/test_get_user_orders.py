import allure

from data import UserData, UserOrdersData
from methods.user_methods import UserMethods
from methods.order_methods import OrderMethods


class TestGetUserOrders:

    @allure.title("Проверка получения заказов авторизованного пользователя")
    @allure.description('''
    1. Генерируем данные нового пользователя;
    2. Создаём пользователя;
    3. Получаем токен созданного пользователя;
    4. Передаём токен в фикстуру для удаления пользователя;
    5. Получаем заказы авторизованного пользователя;
    6. Проверяем статус-код ответа;
    7. Проверяем тело ответа.
    ''')
    def test_get_user_orders_with_authorization(self, user_cleanup):
        user_data = UserData.generate_user_data()
        response = UserMethods.create_user(user_data)

        token = response.json()["accessToken"]
        user_cleanup["token"] = token

        get_user_orders = OrderMethods.get_user_orders(token)

        assert get_user_orders.status_code == 200
        assert get_user_orders.json()["success"] is True

    @allure.title("Проверка получения заказов неавторизованного пользователя")
    @allure.description('''
    1. Отправляем запрос на получение заказов без авторизации;
    2. Проверяем статус-код ответа;
    3. Проверяем тело ответа.
    ''')
    def test_get_user_orders_without_authorization(self):
        response = OrderMethods.get_user_orders()

        status_code, success, message = (
            UserOrdersData.unauthorized_orders_error_data
        )

        assert response.status_code == status_code
        assert response.json()["success"] is success
        assert response.json()["message"] == message
