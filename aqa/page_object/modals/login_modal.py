from playwright.sync_api import Page, ElementHandle

from aqa.helpers.logger import log
from aqa.page_object.modals.base_modal import BaseModal


class LoginModal(BaseModal):
    _USERNAME_INPUT = "#username-modal"
    _PASSWORD_INPUT = "#password-modal"
    _LOGIN_BUTTON = "#login-modal p button"
    _CLOSE_BUTTON = "#login-modal div div div.modal-header button"

    def set_username(self, username: str = None):
        log.info(f"Set username '{username}' to login input field")
        self.page.fill(self._USERNAME_INPUT, username)

    def set_password(self, password: str = None):
        log.info("Set password to password input field")
        self.page.fill(self._PASSWORD_INPUT, password)

    def click_login_button(self):
        log.info("Press Login button")
        self.page.click(self._LOGIN_BUTTON)

    def click_close_login_button(self):
        log.info("Press close button for login form")
        self.page.click(self._CLOSE_BUTTON)

    def login(self, username: str = None, password: str = None):
        self.set_username(username)
        self.set_password(password)
        self.click_login_button()
        self.page.screenshot(path='shot.png')
        self.click_close_login_button()
