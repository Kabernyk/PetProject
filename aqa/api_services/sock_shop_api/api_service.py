from abc import ABC
import requests

from requests.auth import HTTPBasicAuth

from configs import config
from routes.user_routes import UserRoutes


class SockShopApiService(ABC):

    def __init__(self):
        self.url = config.BASE_URL
        self._session = requests.session()

    def auth(self, username: str = None, password: str = None):
        res = self._session.get(f"{self.url}/{UserRoutes.LOGIN.value}", auth=HTTPBasicAuth(username, password))
        token = res.cookies.get("logged_in")
        if not token:
            raise ValueError("'logged_in' property is not set to cookie")
        self._session.cookies.set("logged_in", token)

    def _get(self, route: UserRoutes, **kwargs):
        return self._session.get(f"{self.url}/{route.value}", **kwargs)

    def _post(self, route: UserRoutes, body: dict, **kwargs):
        return self._session.post(f"{self.url}/{route.value}", json=body, **kwargs)
