from playwright.sync_api import Page
from playwright.sync_api import sync_playwright
from playwright.sync_api import BrowserContext, Browser, Page

from aqa.helpers.logger import log
from aqa.page_object.modals.base_modal import BaseModal


class RegisterModal(BaseModal):
    _REGISTER_USERNAME = "#register-username-modal"
    _FIRST_NAME = "#register-first-modal"
    _LAST_NAME = "#register-last-modal"
    _EMAIL = "#register-email-modal"
    _REGISTER_PASSWORD = "#register-password-modal"
    _REGISTER_BUTTON = "#register-modal p button"

    def set_register_username(self, register_name: str = None):
        log.info(f"Set username '{register_name}' to username register input field")
        self.page.fill(self._REGISTER_USERNAME, register_name)

    def set_first_name(self, first_name: str = None):
        log.info(f"Set firstname '{first_name}' to register input field")
        self.page.fill(self._FIRST_NAME, first_name)

    def set_last_name(self, last_name: str = None):
        log.info(f"Set lastname '{last_name}' to register input field")
        self.page.fill(self._LAST_NAME, last_name)

    def set_email(self, email: str = None):
        log.info(f"Set email '{email}' to register input field")
        self.page.fill(self._EMAIL, email)

    def set_register_password(self, register_password: str = None):
        log.info(f"Set password '{register_password}' to register input field")
        self.page.fill(self._REGISTER_PASSWORD, register_password)

    def click_register_button(self):
        log.info("Press Register button")
        self.page.click(self._REGISTER_BUTTON)

    def valid_register(self, register_username: str = None, first_name: str = None, last_name: str = None,
                       email: str = None,
                       register_password: str = None):
        self.set_register_username(register_username)
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_email(email)
        self.set_register_password(register_password)
        self.click_register_button()

    def invalid_register(self, register_username: str = None, first_name: str = None, last_name: str = None,
                         register_password: str = None):
        self.set_register_username(register_username)
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_register_password(register_password)
        self.click_register_button()
