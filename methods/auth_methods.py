import allure
import requests

import urls
import endpoints


class LoginMethods:

    @staticmethod
    @allure.step('Авторизация пользователя')
    def login_user(user_data):
        response = requests.post(
            urls.Urls.BASE_URL + endpoints.Endpoints.login_user,
            json=user_data,
        )

        return response
    