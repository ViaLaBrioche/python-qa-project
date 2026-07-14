from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class LoginPage(BasePage):
    USER_NAME = (By.XPATH, '//input[@id="user-name"]')
    PASSWORD = (By.XPATH, '//input[@id="password"]')
    LOGIN_BTN = (By.XPATH, '//input[@id="login-button"]')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-test="error"]')

    def enter_user_name(self, username):
        self.send_keys(self.USER_NAME, username)

    def enter_password(self, password):
        self.send_keys(self.PASSWORD, password)

    def click_login(self):
        self.click(self.LOGIN_BTN)

    def login(self, username, password):
        self.enter_user_name(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def wait_until_loaded(self):
        self.wait_visible(self.USER_NAME)
        self.wait_visible(self.PASSWORD)
