from playwright.sync_api import sync_playwright, Page
from aqa.page_object.pages.home_page import HomePage
from aqa.helpers.logger import log
from aqa.page_object.modals.catalogue_modal import CatalogueModal


class Catalogue(HomePage):
    _CATALOGUE_TAB = "#tabCatalogue"
    _SELECT_FILTER = "#filters div:nth-child(9) label input[type=checkbox]"
    _APPLY_FILTER = "#filters-form a"
    _ADD_ITEMS = "#products div div div.text p.buttons a.btn.btn-primary"
    _CART_ITEM = "#basket-overview > a > i"
    _SHIPPING_CHANGE = "#basket div:nth-child(2) div:nth-child(1) div div.box-header p a"
    _PAYMENT_CHANGE = "#basket > div:nth-child(2) div:nth-child(2) div div.box-header p a"
    _ORDER_TEXT = "#address"

    def click_catalogue_tab(self):
        log.info("Click on the catalogue tab")
        self.page.click(self._CATALOGUE_TAB)
        log.info("Select product filter")
        self.page.click(self._SELECT_FILTER)
        log.info("Click on the filter apply button")
        self.page.click(self._APPLY_FILTER)
        log.info("Click on the filter apply button")
        self.page.click(self._ADD_ITEMS)
        return CatalogueModal(self.page)

    def click_item_button(self):
        log.info("Click on the cart item button ")
        self.page.click(self._CART_ITEM)
        return CatalogueModal(self.page)

    def click_shipping_change_button(self):
        log.info("Click on the Change shipping button")
        self.page.click(self._SHIPPING_CHANGE)
        return CatalogueModal(self.page)

    def click_payment_change_button(self):
        log.info("Click on the Change payment button")
        self.page.click(self._PAYMENT_CHANGE)
        return CatalogueModal(self.page)

    def is_order_displayed(self):
        log.info("Is SHIPPING text is displayed on a tab")
        return self.page.inner_text(self._ORDER_TEXT)
