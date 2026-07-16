from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class CheckoutComplete(BasePage):
    PAGE_URL = "checkout-complete.html"
    BTN_BACK_TO_PRODUCTS = (By.ID, "back-to-products")
    COMPLETE_TEXT = (By.CSS_SELECTOR, '[data-test="complete-text"]')
    COMPLETE_HEADER = (By.CSS_SELECTOR, '[data-test="complete-header"]')
    PONY_EXPRESS = (By.CSS_SELECTOR, '[data-test="pony-express"]')

    def wait_until_loaded(self):
        self.wait_visible(self.PONY_EXPRESS)
        self.wait_visible(self.COMPLETE_HEADER)
        self.wait_visible(self.COMPLETE_TEXT)

    def click_back_to_products(self):
        self.driver.logger.info("Нажимаем на кнопку возврата на страницу товаров")
        self.click(self.BTN_BACK_TO_PRODUCTS)
