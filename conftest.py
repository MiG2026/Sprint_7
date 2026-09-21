import pytest
import requests
from data import Data
from urls import Urls


@pytest.fixture(scope="session", autouse=True)
def create_courier_for_tests():
    payload = {
        'login': Data.valid_login,
        'password': Data.valid_password,
        'firstName': Data.valid_firstname
    }
    response = requests.post(Urls.URL_courier_create, data=payload)
    assert response.status_code in (201, 409), (
        f"Не удалось подготовить курьера: {response.status_code} {response.text}"
    )
    yield