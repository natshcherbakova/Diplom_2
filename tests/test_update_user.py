import allure

from data import UserData, UpdateUserData
from methods.user_methods import UserMethods


class TestUpdateUser:

    @allure.title("Проверка изменения данных пользователя")
    @allure.description('''
    1. Генерируем данные нового пользователя;
    2. Создаём пользователя;
    3. Получаем токен созданного пользователя;
    4. Передаём токен в фикстуру для удаления пользователя;
    5. Генерируем новые данные пользователя;
    6. Изменяем данные пользователя;
    7. Проверяем статус-код ответа;
    8. Проверяем изменённые данные.
    ''')
    def test_update_user_success(self, user_cleanup):
        user_data = UserData.generate_user_data()
        response = UserMethods.create_user(user_data)

        token = response.json()["accessToken"]
        user_cleanup["token"] = token

        update_user_data = UserData.generate_user_data()
        update_response = UserMethods.update_user(update_user_data, token)

        assert update_response.status_code == 200
        assert update_response.json()["user"]["email"] == update_user_data["email"]
        assert update_response.json()["user"]["name"] == update_user_data["name"]

    @allure.title("Проверка изменения данных пользователя без авторизации")
    @allure.description('''
    1. Генерируем данные нового пользователя;
    2. Создаём пользователя;
    3. Получаем токен созданного пользователя;
    4. Передаём токен в фикстуру для удаления пользователя;
    5. Генерируем новые данные пользователя;
    6. Отправляем запрос на изменение данных без авторизации;
    7. Проверяем статус-код ответа;
    8. Проверяем тело ответа.
    ''')
    def test_update_user_without_authorization(self, user_cleanup):
        user_data = UserData.generate_user_data()
        response = UserMethods.create_user(user_data)

        token = response.json()["accessToken"]
        user_cleanup["token"] = token

        update_user_data = UserData.generate_user_data()
        update_response = UserMethods.update_user(update_user_data)

        status_code, success, message = (
            UpdateUserData.unauthorized_update_error_data
        )

        assert update_response.status_code == status_code
        assert update_response.json()["success"] is success
        assert update_response.json()["message"] == message
        