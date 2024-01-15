from aqa.page_object.pages.home_page import HomePage
from aqa.helpers.fake_data import Fake


def test_register_invalid_user(driver):
    # Arrange
    username = Fake.name(self=Fake())
    firstname = Fake.name(self=Fake())
    lastname = Fake.name(self=Fake())
    password = Fake.password(self=Fake())

    # Act
    home_page = HomePage(driver.page)
    register_modal = home_page.click_register_link()
    register_modal.invalid_register(username, firstname, lastname, password)

    # Assert
    assert f"Logged in as {firstname} {lastname}" != home_page.get_logged_user_text(), "Expected email validation"

