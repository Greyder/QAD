import configuration
import requests
import data


# Функция создания нового пользователя
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,
                         json=body)


response = post_new_order(data.order_body)
print(response.status_code)
print(response.json())


def get_orders(body):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDERS_PATH,
                        json=body,
                        params={"t": 642980})


response = get_orders(data.order_body)
assert response.status_code == 200
print(response.status_code)
print(response.json())
