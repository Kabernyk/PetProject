from playwright.sync_api import sync_playwright
from aqa.page_object.pages.catalogue_page import Catalogue
from aqa.helpers.fake_data import Fake
from aqa.configs import config


def test_shipping_update(driver):
    # Arrange
    username = config.SEED_USERNAME
    password = config.SEED_PASSWORD
    house_number = Fake.house_number(Fake())
    street_name = Fake.street(Fake())
    city = Fake.city(Fake())
    post_code = Fake.post_code(Fake())
    country = Fake.country(Fake())
    credit_card = Fake.credit_card(Fake())
    credit_card_expire = Fake.credit_card_expire(Fake())
    credit_card_cvv = Fake.credit_card_cvv(Fake())

    # Act
    home_page = Catalogue(driver.page)
    driver.page.screenshot(path='shot.png')
    login_modal = home_page.click_login_link()
    login_modal.login(username, password)
    home_page.click_catalogue_tab()
    home_page.click_item_button()
    catalogue_page = home_page.click_shipping_change_button()
    catalogue_page.shipping_update(house_number, street_name, city, post_code, country)
    payment_page = home_page.click_payment_change_button()
    payment_page.payment_update(credit_card, credit_card_expire, credit_card_cvv)
