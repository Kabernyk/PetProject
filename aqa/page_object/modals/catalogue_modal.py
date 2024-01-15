from playwright.sync_api import Page, ElementHandle


class BaseModal:
    def __init__(self, page: Page):
        self.page = page


class PaymentModal(BaseModal):
    _CARD_NUMBER = "#form-card-number"
    _CARD_EXPIRES = "#form-expires"
    _CCV = "#form-ccv"
    _PAYMENT_UPDATE = "#card-modal div div div.modal-body p button"

    def set_card_number(self, card_number: str = None):
        self.page.fill(self._CARD_NUMBER, card_number)

    def set_card_expires(self, card_expires: str = None):
        self.page.fill(self._CARD_EXPIRES, card_expires)

    def set_ccv(self, ccv: str = None):
        self.page.fill(self._CCV, ccv)

    def click_payment_update_button(self):
        self.page.click(self._PAYMENT_UPDATE)

    def payment_update(self, card_number: str = None, card_expires: str = None, ccv: str = None):
        self.set_card_number(card_number)
        self.set_card_expires(card_expires)
        self.set_ccv(ccv)
        self.click_payment_update_button()


class CatalogueModal(PaymentModal):
    _HOUSE_NUMBER = "#form-number"
    _STREET_NAME = "#form-street"
    _CITY = "#form-city"
    _POST_CODE = "#form-post-code"
    _COUNTRY = "#form-country"
    _SHIPPING_UPDATE = "#form-address p button"

    def set_house_number(self, house_number: str = None):
        self.page.fill(self._HOUSE_NUMBER, house_number)

    def set_street_name(self, street_name: str = None):
        self.page.fill(self._STREET_NAME, street_name)

    def set_city(self, city: str = None):
        self.page.fill(self._CITY, city)

    def set_post_code(self, post_code: str = None):
        self.page.fill(self._POST_CODE, post_code)

    def set_country(self, country: str = None):
        self.page.fill(self._COUNTRY, country)

    def click_update_button(self):
        self.page.click(self._SHIPPING_UPDATE)

    def shipping_update(self, house_number: str = None, street_name: str = None, city: str = None,
                        post_code: str = None, country: str = None):
        self.set_house_number(house_number)
        self.set_street_name(street_name)
        self.set_city(city)
        self.set_post_code(post_code)
        self.set_country(country)
        self.click_update_button()


class OrderCheckout(CatalogueModal):
    _CHECKOUT_BUTTON = "#orderButton"

    def click_checkout_button(self):
        self.page.click(self._CHECKOUT_BUTTON)
