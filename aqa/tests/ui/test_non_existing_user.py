from playwright.sync_api import sync_playwright
from aqa.configs import config
from aqa.helpers.fake_data import Fake

from aqa.page_object.pages.catalogue_page import Catalogue


def test_valid_user_login(driver):
    # Arrange
    username = Fake.text(self=Fake())
    password = config.SEED_PASSWORD
    home_page = Catalogue(driver.page)
    login_modal = home_page.click_login_link()
    # Use the password from real user to test security
    login_modal = driver.page.click_login_link()
    login_modal.login(username, password)
    driver.page.screenshot(path='shot.png')
    # Assert
    assert "Invalid login credentials" == driver.page.is_sign_in_error_displayed(), \
        "Expected validation message"
    assert f"Logged in as {username} {username}" == driver.page.get_logged_user_text(), \
        "User exist or critical error was detected"
