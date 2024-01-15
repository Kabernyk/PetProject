from playwright.sync_api import Page

from aqa.page_object.modals.login_modal import LoginModal
from aqa.page_object.modals.register_modal import RegisterModal
from aqa.page_object.pages.base_page import BasePage
from aqa.helpers.logger import log


class HomePage(BasePage):
    _REGISTER_LINK = "#register"
    _LOGIN_LINK = "#login"
    _LOGGED_USER_TEXT = "#howdy a"
    _ACCOUNT_TAB = "#tabAccount"
    _LOGIN_ERROR = "#login-message div"

    def click_register_link(self):
        log.info("Click on register link")
        self.page.click(self._REGISTER_LINK)
        return RegisterModal(self.page)

    def click_login_link(self):
        log.info("Click on login link")
        self.page.click(self._LOGIN_LINK)
        return LoginModal(self.page)

    def get_logged_user_text(self):
        log.info("Get logged user text from home page")
        return self.page.inner_text(self._LOGGED_USER_TEXT)

    def is_account_tab_displayed(self):
        log.info("Is ACCOUNT tab displayed")
        return self.page.wait_for_selector(self._ACCOUNT_TAB).is_visible()

    def is_sign_in_error_displayed(self):
        log.info("Is validation message displayed")
        return self.page.inner_text(self._LOGIN_ERROR)
