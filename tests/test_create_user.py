import allure
import pytest

from data import UserData
from methods.user_methods import UserMethods


class TestCreateUser:

    @allure.title("Проверка создания нового пользователя")
    @allure.description('''
    1. Генерируем данные нового пользователя;
    2. Создаём пользователя;
    3. Получаем токен созданного пользователя;
    4. Передаём токен в фикстуру для удаления пользователя;
    5. Проверяем статус-код ответа;
    6. Проверяем тело ответа.
    ''')
    def test_create_user_success(self, user_cleanup):
        user_data = UserData.generate_user_data()
        response = UserMethods.create_user(user_data)

        token = response.json()["accessToken"]
        user_cleanup["token"] = token

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание уже зарегистрированного пользователя")
    @allure.description('''
    1. Генерируем данные нового пользователя;
    2. Создаём пользователя;
    3. Повторно отправляем запрос на создание пользователя с теми же данными;
    4. Проверяем статус-код ответа;
    5. Проверяем тело ответа.
    ''')
    def test_create_duplicate_user(self, user_cleanup):
        user_data = UserData.generate_user_data()
        response = UserMethods.create_user(user_data)

        token = response.json()["accessToken"]
        user_cleanup["token"] = token

        duplicate_response = UserMethods.create_user(user_data)

        status_code, success, message = (
            UserData.duplicate_user_error_data
        )

        assert duplicate_response.status_code == status_code
        assert duplicate_response.json()["success"] is success
        assert duplicate_response.json()["message"] == message

    @pytest.mark.parametrize(
        "user_data_generator, expected_status_code, expected_success, expected_message",
        [
            (
                UserData.generate_data_incorrect_user_without_email,
                UserData.create_user_without_required_field_error_data[0],
                UserData.create_user_without_required_field_error_data[1],
                UserData.create_user_without_required_field_error_data[2]
            ),
            (
                UserData.generate_data_incorrect_user_without_password,
                UserData.create_user_without_required_field_error_data[0],
                UserData.create_user_without_required_field_error_data[1],
                UserData.create_user_without_required_field_error_data[2]
            ),
            (
                UserData.generate_data_incorrect_user_without_name,
                UserData.create_user_without_required_field_error_data[0],
                UserData.create_user_without_required_field_error_data[1],
                UserData.create_user_without_required_field_error_data[2]
            )
        ]
    )
    @allure.title("Создание пользователя без обязательного поля")
    @allure.description('''
    1. Генерируем данные пользователя без обязательного поля;
    2. Отправляем запрос на создание пользователя;
    3. Проверяем статус-код ответа;
    4. Проверяем тело ответа.
    ''')
    def test_create_user_without_required_field(
        self,
        user_data_generator,
        expected_status_code,
        expected_success,
        expected_message
    ):
        user_data = user_data_generator()
        response = UserMethods.create_user(user_data)

        assert response.status_code == expected_status_code
        assert response.json()["success"] is expected_success
        assert response.json()["message"] == expected_message
        