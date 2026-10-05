import allure
import json

from data import UserData, OrderData, IngredientsData
from methods.user_methods import UserMethods
from methods.order_methods import OrderMethods


class TestCreateOrder:

    @allure.title("Проверка создания заказа с авторизацией")
    @allure.description('''
    1. Генерируем данные нового пользователя;
    2. Создаём пользователя;
    3. Получаем токен созданного пользователя;
    4. Передаём токен в фикстуру для удаления пользователя;
    5. Формируем данные заказа с ингредиентами;
    6. Создаём заказ с авторизацией;
    7. Проверяем статус-код ответа;
    8. Проверяем тело ответа.
    ''')
    def test_create_order_with_auth(self, user_cleanup):
        user_data = UserData.generate_user_data()
        response = UserMethods.create_user(user_data)

        token = response.json()["accessToken"]
        user_cleanup["token"] = token

        headers = {
            "Authorization": token,
            "Content-type": "application/json"
        }

        data = json.dumps(IngredientsData.correct_ingredients_data)
        response = OrderMethods.create_order(data, headers)

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Проверка создания заказа без авторизации")
    @allure.description('''
    1. Формируем данные заказа с ингредиентами;
    2. Создаём заказ без авторизации;
    3. Проверяем статус-код ответа;
    4. Проверяем тело ответа.
    ''')
    def test_create_order_without_auth(self):
        headers = {
            "Content-type": "application/json"
        }

        data = json.dumps(IngredientsData.correct_ingredients_data)
        response = OrderMethods.create_order(data, headers)

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Проверка создания заказа без ингредиентов")
    @allure.description('''
    1. Формируем данные заказа без ингредиентов;
    2. Отправляем запрос на создание заказа;
    3. Проверяем статус-код ответа;
    4. Проверяем сообщение об ошибке.
    ''')
    def test_create_order_without_ingredients(self):
        headers = {
            "Content-type": "application/json"
        }

        data = json.dumps(OrderData.empty_ingredients_data)
        response = OrderMethods.create_order(data, headers)

        status_code, success, message = (
            OrderData.empty_ingredients_error_data
        )

        assert response.status_code == status_code
        assert response.json()["success"] is success
        assert response.json()["message"] == message

    @allure.title("Проверка создания заказа с невалидным хэшем ингредиента")
    @allure.description('''
    1. Формируем данные заказа с невалидным хэшем ингредиента;
    2. Отправляем запрос на создание заказа;
    3. Проверяем статус-код ответа;
    4. Проверяем сообщение об ошибке.
    ''')
    def test_create_order_invalid_ingredient(self):
        headers = {
            "Content-type": "application/json"
        }

        data = json.dumps(OrderData.incorrect_ingredients_data)
        response = OrderMethods.create_order(data, headers)

        status_code, message = OrderData.invalid_ingredient_error_data

        assert response.status_code == status_code
        assert message in response.text
