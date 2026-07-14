from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class CheckoutOneStep(BasePage):
    PAGE_URL = "checkout-step-one.html"
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    BTN_CONTINUE = (By.ID, "continue")
    SECONDARY_HEADER = (By.CSS_SELECTOR, '[data-test="secondary-header"]')

    def wait_until_loaded(self):
        self.wait_visible(self.FIRST_NAME)
        self.wait_visible(self.BTN_CONTINUE)
        self.wait_visible(self.SECONDARY_HEADER)

    def enter_first_name(self, first_name):
        self.send_keys(self.FIRST_NAME, first_name)

    def enter_last_name(self, last_name):
        self.send_keys(self.LAST_NAME, last_name)

    def enter_postal_code(self, postal_code):
        self.send_keys(self.POSTAL_CODE, postal_code)

    def click_continue(self):
        self.click(self.BTN_CONTINUE)
