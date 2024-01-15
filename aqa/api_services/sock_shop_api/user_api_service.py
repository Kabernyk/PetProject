from requests.auth import HTTPBasicAuth

from api_services.sock_shop_api.api_service import SockShopApiService
from routes.user_routes import UserRoutes
from helpers.logger import log


class SockShopUserApiService(SockShopApiService):

    def login(self, username: str = None, password: str = None):
        log.info(f"Login new user: {username}")
        return self._get(UserRoutes.LOGIN, auth=HTTPBasicAuth(username, password))

    def register(self, body: dict):
        log.info("Register new user")
        return self._post(UserRoutes.REGISTER, body)
