from jsonschema import validate
from api_services.sock_shop_api.user_api_service import SockShopUserApiService
from configs import config
from helpers.fake_data import Fake


def test_should_sign_up_user_valid():
    # Arrange
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
        },
    }

    fake = Fake()
    body = {
        "username": fake.name(),
        "password": fake.password(),
        "email": fake.email()
    }
    user_service = SockShopUserApiService()
    res = user_service.register(body)
    # Assert
    assert res.status_code == 200, "Response is not 200 for /register"
    assert validate(res.json(), schema) is None, "'id' property does not exist or not a string"


def test_should_sing_in_user_valid():
    # Arrange
    username = config.SEED_USERNAME
    password = config.SEED_PASSWORD

    # Act
    user_service = SockShopUserApiService()
    res = user_service.login(username, password)

    assert res.cookies.get("logged_in"), "logged_in Cookie is not set"
