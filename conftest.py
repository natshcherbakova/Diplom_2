import pytest

from data import UserData
from methods.user_methods import UserMethods


# фикстура для создания уникального пользователя
@pytest.fixture
def user():
    user_data = UserData.generate_user_data()
    response = UserMethods.create_user(user_data)
    access_token = response.json()["accessToken"]

    yield {
        "email": user_data["email"],
        "password": user_data["password"],
        "name": user_data["name"],
        "token": access_token
    }
    
    UserMethods.delete_user(access_token)

# фикстура для удаления пользователя после завершения теста
@pytest.fixture
def user_cleanup():
    user = {}

    yield user
    
    if "token" in user:
        UserMethods.delete_user(user["token"])
