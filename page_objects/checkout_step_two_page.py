from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class CheckoutTwoStep(BasePage):
    PAGE_URL = "checkout-step-two.html"
    BTN_FINISH = (By.ID, "finish")
    CART_LIST = (By.CSS_SELECTOR, '[data-test="cart-list"]')
    PAYMENT_INFO = (By.CSS_SELECTOR, '[data-test="payment-info-label"]')
    SHIPPING_INFO = (By.CSS_SELECTOR, '[data-test="shipping-info-label"]')

    def wait_until_loaded(self):
        self.wait_visible(self.SHIPPING_INFO)
        self.wait_visible(self.PAYMENT_INFO)
        self.wait_visible(self.CART_LIST)

    def click_finish(self):
        self.driver.logger.info("Нажимаем кнопку Finish")
        self.click(self.BTN_FINISH)
