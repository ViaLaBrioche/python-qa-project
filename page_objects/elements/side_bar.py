from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class SideBar(BasePage):
    ALL_ITEMS = (By.ID, "inventory_sidebar_link")
    ABOUT = (By.ID, "about_sidebar_link")
    LOGOUT = (By.ID, "logout_sidebar_link")
    RESET = (By.ID, "reset_sidebar_link")

    def wait_until_loaded(self):
        self.wait_visible(self.ALL_ITEMS)
        self.wait_visible(self.ABOUT)
        self.wait_visible(self.LOGOUT)
        self.wait_visible(self.RESET)

    def logout(self):
        self.click(self.LOGOUT)

    def reset(self):
        self.click(self.RESET)
