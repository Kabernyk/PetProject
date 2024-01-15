from playwright.sync_api import sync_playwright
from aqa.helpers.fake_data import Fake
from aqa.page_object.pages.home_page import HomePage

def test_register_valid_user(driver):
    # Arrange
    username = Fake.name(self=Fake())
    firstname = Fake.name(self=Fake())
    lastname = Fake.name(self=Fake())
    email = Fake.email(self=Fake())
    password = Fake.password(self=Fake())
    home_page = HomePage(driver.page)
    register_modal = home_page.click_register_link()
    register_modal.valid_register(username, firstname, lastname, email, password)

        # Assert
    assert f"Logged in as {firstname} {lastname}" == home_page.get_logged_user_text(), \
            "Username is not displayed after sign in"
    assert home_page.is_account_tab_displayed(), "Account tab is not displayed after sign in"