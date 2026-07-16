from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class ProductPage(BasePage):
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_details_name")
    PRODUCT_DESCRIPTION = (By.CLASS_NAME, "inventory_details_desc")
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_details_price")
    BTN_ADD_TO_CART = (By.ID, "add-to-cart")
    BTN_REMOVE = (By.ID, "remove")

    def wait_until_loaded(self):
        self.wait_visible(self.PRODUCT_NAME)
        self.wait_visible(self.PRODUCT_DESCRIPTION)
        self.wait_visible(self.PRODUCT_PRICE)

    def get_product_name(self):
        self.driver.logger.info("Получаем имя товара")
        return self.get_text(self.PRODUCT_NAME)

    def get_product_description(self):
        self.driver.logger.info("Получаем описание товара")
        return self.get_text(self.PRODUCT_DESCRIPTION)

    def get_product_price(self):
        self.driver.logger.info("Получаем цену товара")
        return self.get_text(self.PRODUCT_PRICE)

    def click_add_to_cart(self):
        self.driver.logger.info("Нажимаем на кнопку Add to cart")
        self.click(self.BTN_ADD_TO_CART)

    def wait_until_visible_remove(self):
        self.wait_visible(self.BTN_REMOVE)
