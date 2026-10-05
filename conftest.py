import pytest

from data import UserData
from methods.user_methods import UserMethods


# фикстура для создания уникального пользователя
@pytest.fixture
def user():
    # генерируем данные нового пользователя
    user_data = UserData.generate_user_data()

    # создаём пользователя через API
    response = UserMethods.create_user(user_data)

    # получаем accessToken из ответа
    access_token = response.json()["accessToken"]

    # передаём данные пользователя и токен в тест
    yield {
        "email": user_data["email"],
        "password": user_data["password"],
        "name": user_data["name"],
        "token": access_token
    }
    
    # удаляем пользователя после завершения теста
    UserMethods.delete_user(access_token)

# фикстура для удаления пользователя после завершения теста
@pytest.fixture
def user_cleanup():
    
    # создаём пустой словарь для хранения данных пользователя
    user = {}

    # передаём словарь в тест
    yield user

    # удаляем пользователя после завершения теста
    if "token" in user:
        UserMethods.delete_user(user["token"])
