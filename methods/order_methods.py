import allure
import requests

import urls
import endpoints


class OrderMethods:

    @staticmethod
    @allure.step("Создание заказа")
    def create_order(params, headers=None):
        response = requests.post(
            urls.Urls.BASE_URL + endpoints.Endpoints.create_order,
            headers=headers,
            data=params,
        )

        return response

    @staticmethod
    @allure.step("Получение заказов пользователя")
    def get_user_orders(token=None):
        headers = {}
        
        if token:
            headers["Authorization"] = token

        response = requests.get(
            urls.Urls.BASE_URL + endpoints.Endpoints.get_user_orders,
            headers=headers,
        )
            
        return response
    