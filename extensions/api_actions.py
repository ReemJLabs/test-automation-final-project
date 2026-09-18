
import allure
import requests
from requests.auth import HTTPBasicAuth
header = {'Content-Type': 'application/json', 'Accept': 'application/json'}


class APIActions:
    @staticmethod
    @allure.step('Get Request')
    def get(path, user, password):
        response = requests.get(path, auth=HTTPBasicAuth(user, password))
        return response

    @staticmethod
    @allure.step('Extract value from response')
    def extract_value_from_response(response, nodes):
        # Walk JSON by path length, e.g. ['teams', 0, 'name'] -> response['teams'][0]['name']
        extracted_value = None
        response_json = response.json()
        if len(nodes) == 1:
            extracted_value = response_json[nodes[0]]
        elif len(nodes) == 2:
            extracted_value = response_json[(nodes[0])][(nodes[1])]
        elif len(nodes) == 3:
            extracted_value = response_json[(nodes[0])][(nodes[1])][(nodes[2])]
        return extracted_value

    @staticmethod
    @allure.step('POST Request')
    def post(path, payload, user, password):
        response = requests.post(path, json=payload, headers=header, auth=HTTPBasicAuth(user, password))
        return response.status_code

    @staticmethod
    @allure.step('PUT Request')
    def put(path, payload, user, password):
        response = requests.put(path, json=payload, headers=header, auth=HTTPBasicAuth(user, password))
        return response.status_code

    @staticmethod
    @allure.step('DELETE Request')
    def delete(path, user, password):
        response = requests.delete(path, auth=HTTPBasicAuth(user, password))
        return response.status_code