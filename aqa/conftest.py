import pytest
from playwright.sync_api import sync_playwright

from aqa.helpers.web_driver.web_driver import PlaywrightPage
from aqa.helpers.web_driver.web_driver import PlaywrightListener

playwright = sync_playwright().start()

@pytest.fixture()
def driver():
    # before test
    browser = playwright.webkit.launch()
    context = browser.new_context()
    _page = context.new_page()
    ef_driver = PlaywrightPage(_page)  # Ініціалізація без другого аргумента

    _page.goto("http://localhost")
    yield ef_driver
    # after test
    context.close()
    browser.close()

@pytest.fixture()
def hello():
    print("Before test")
    yield
    print("After test")

