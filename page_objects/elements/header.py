from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class Header(BasePage):
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART = (By.ID, "shopping_cart_container")

    def open_side_bar(self):
        self.click(self.BURGER_MENU)

    def wait_until_reset(self):
        self.wait_not_visible(self.CART_BADGE)

    def get_cart_badge_text(self):
        return self.get_text(self.CART_BADGE)

    def click_cart(self):
        self.click(self.CART)
