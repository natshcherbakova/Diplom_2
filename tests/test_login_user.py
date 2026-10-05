import allure

from data import UserData, LoginData
from methods.user_methods import UserMethods
from methods.auth_methods import LoginMethods


class TestLoginUser:

    @allure.title("Проверка авторизации пользователя")
    @allure.description('''
    1. Генерируем данные нового пользователя;
    2. Создаём пользователя;
    3. Авторизуемся с данными созданного пользователя;
    4. Получаем токен авторизованного пользователя;
    5. Передаём токен в фикстуру для удаления пользователя;
    6. Проверяем статус-код ответа;
    7. Проверяем тело ответа.
    ''')
    def test_login_user_success(self, user_cleanup):
        user_data = UserData.generate_user_data()
        response = UserMethods.create_user(user_data)

        authorization = LoginMethods.login_user(user_data)

        token = authorization.json()["accessToken"]
        user_cleanup["token"] = token

        assert authorization.status_code == 200
        assert authorization.json()["success"] is True

    @allure.title("Проверка авторизации пользователя с неверными данными")
    @allure.description('''
    1. Генерируем данные нового пользователя;
    2. Создаём пользователя;
    3. Изменяем данные для авторизации;
    4. Отправляем запрос на авторизацию;
    5. Проверяем статус-код ответа;
    6. Проверяем тело ответа.
    ''')
    def test_login_user_invalid_data(self, user_cleanup):
        user_data = UserData.generate_user_data()
        response = UserMethods.create_user(user_data)

        token = response.json()["accessToken"]
        user_cleanup["token"] = token

        user_data["password"] = "wrong_password"
        login_response = LoginMethods.login_user(user_data)

        status_code, success, message = (
            LoginData.invalid_login_error_data
        )

        assert login_response.status_code == status_code
        assert login_response.json()["success"] is success
        assert login_response.json()["message"] == message
