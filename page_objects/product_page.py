from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class ProductPage(BasePage):
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_details_name")
    PRODUCT_DESCRIPTION = (By.CLASS_NAME, "inventory_details_desc")
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_details_price")

    def wait_until_loaded(self):
        self.wait_visible(self.PRODUCT_NAME)
        self.wait_visible(self.PRODUCT_DESCRIPTION)
        self.wait_visible(self.PRODUCT_PRICE)

    def get_product_name(self):
        return self.get_text(self.PRODUCT_NAME)

    def get_product_description(self):
        return self.get_text(self.PRODUCT_DESCRIPTION)

    def get_product_price(self):
        return self.get_text(self.PRODUCT_PRICE)
