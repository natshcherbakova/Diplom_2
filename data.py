from faker import Faker


fake = Faker()


class UserData:

    # генерация данных нового пользователя
    @staticmethod
    def generate_user_data():
        return {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.user_name()
        }

    # генерация данных без обязательного поля email
    @staticmethod
    def generate_data_incorrect_user_without_email():
        return {
                "password": fake.password(),
                "name": fake.user_name()
        }
    
    # генерация данных без обязательного поля password
    @staticmethod
    def generate_data_incorrect_user_without_password():
        return {
                "email": fake.email(),
                "name": fake.user_name()
        }
    
    # генерация данных без обязательного поля name
    @staticmethod
    def generate_data_incorrect_user_without_name():
        return {
                "email": fake.email(),
                "password": fake.password()
        }

    # данные для проверки создания дубликата пользователя
    duplicate_user_error_data = (
        403,
        False,
        "User already exists"
    )

    # данные для проверки создания пользователя без обязательного поля
    create_user_without_required_field_error_data = (
        403,
        False,
        "Email, password and name are required fields"
    )


class LoginData:
    
    # данные для проверки авторизации с неверными данными
    invalid_login_error_data = (
        401,
        False,
        "email or password are incorrect"
    )


class UpdateUserData:

    # данные для проверки изменения данных пользователя без авторизации
    unauthorized_update_error_data = (
        401,
        False,
        "You should be authorised"
    )


class OrderData:

    # данные для проверки создания заказа без ингредиентов
    empty_ingredients_data = {
        "ingredients": []
    }

    empty_ingredients_error_data = (
        400,
        False,
        "Ingredient ids must be provided"
    )

    # данные для проверки создания заказа с неверным хэшем ингредиента
    incorrect_ingredients_data = {
        "ingredients": [
            "60d3b41abdacsdf6a733c6",
            "609646e4dcsfdf0276b2870"
        ]
    }

    invalid_ingredient_error_data = (
        500,
        "Internal Server Error"
    )


class UserOrdersData:

    # данные для проверки получения заказов без авторизации
    unauthorized_orders_error_data = (
        401,
        False,
        "You should be authorised"
    )


class IngredientsData:

    # корректные данные ингредиентов
    correct_ingredients_data = {
        "ingredients": [
            "6acef97852135b001b21a32c",
            "6acef97852135b001b21a32d",
            "6acef97852135b001b21a331"
        ]
    }
