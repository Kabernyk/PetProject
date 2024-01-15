from playwright.sync_api import Page, TimeoutError
from playwright.sync_api import sync_playwright

class PlaywrightPage:
    def __init__(self, page: Page):
        self.page = page

    def wait_till_element_is_displayed(self, locator, timeout: int = 4):
        try:
            self.page.wait_for_selector(locator, state="visible", timeout=timeout)
            return True
        except TimeoutError:
            return False

class PlaywrightListener:
    def __init__(self, page: Page):
        self.page = page

    def before_find(self, by, value, **kwargs):
        self.page.wait_for_selector(value)
