import allure
import requests

import urls
import endpoints


class UserMethods:

    @staticmethod
    @allure.step('Создание пользователя')
    def create_user(user_data):
        response = requests.post(
            urls.Urls.BASE_URL + endpoints.Endpoints.create_user,
            json=user_data,
        )

        return response

    @staticmethod
    @allure.step('Изменение данных пользователя')
    def update_user(user_data, token=None):
        headers = {}

        if token:
            headers["Authorization"] = token

        response = requests.patch(
            urls.Urls.BASE_URL + endpoints.Endpoints.update_user,
            headers=headers, 
            json=user_data,
            )

        return response

    @staticmethod
    @allure.step('Удаление пользователя')
    def delete_user(token):
        response = requests.delete(
            urls.Urls.BASE_URL + endpoints.Endpoints.update_user,
            headers={"Authorization": token},
        )

        return response
    