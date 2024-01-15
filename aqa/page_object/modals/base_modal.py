from playwright.sync_api import Page


class BaseModal:
    def __init__(self, page: Page):
        self.page = page
