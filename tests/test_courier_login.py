import allure
import pytest
import requests
from data import Data
from urls import Urls
from helpers import create_random_login, create_random_password


class TestCourierLogin:

    @allure.title('Проверка успешной аутентификации курьера')
    def test_courier_login_success(self):
        response = requests.post(Urls.URL_courier_login, data=Data.valid_courier_data)
        assert response.status_code == 200
        assert 'id' in response.json()

    @allure.title('Проверка ошибки при неверных данных')
    @pytest.mark.parametrize('nonexistent_credentials', [
        {'login': create_random_login(), 'password': create_random_password()},
        Data.courier_data_with_wrong_password
    ])
    def test_courier_login_nonexistent_data_not_found(self, nonexistent_credentials):
        response = requests.post(Urls.URL_courier_login, data=nonexistent_credentials)
        assert response.status_code == 404
        assert response.json()['message'] == 'Учетная запись не найдена'

    @allure.title('Проверка ошибки при пустом логине или пароле')
    @pytest.mark.parametrize('empty_credentials', [
        {'login': '', 'password': create_random_password()},
        {'login': Data.valid_login, 'password': ''}
    ])
    def test_courier_login_empty_credentials_bad_request(self, empty_credentials):
        response = requests.post(Urls.URL_courier_login, data=empty_credentials)
        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для входа'