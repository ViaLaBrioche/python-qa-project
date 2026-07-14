from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class CartPage(BasePage):
    PAGE_URL = "cart.html"
    BTN_REMOVE_FROM_CART = (By.XPATH, "//button[contains(., 'Remove')]")
    BTN_CHECKOUT = (By.ID, "checkout")

    def wait_until_loaded(self):
        self.wait_visible(self.BTN_REMOVE_FROM_CART)
        self.wait_visible(self.BTN_CHECKOUT)

    def delete_product(self):
        self.click(self.BTN_REMOVE_FROM_CART)

    def wait_product_removed(self):
        self.wait_not_visible(self.BTN_REMOVE_FROM_CART)

    def click_checkout(self):
        self.click(self.BTN_CHECKOUT)
