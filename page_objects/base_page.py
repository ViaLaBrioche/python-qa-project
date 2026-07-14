from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    PAGE_URL = ""

    def __init__(self, driver):
        self.driver = driver

    def open(self, base_url):
        self.driver.get(base_url + self.PAGE_URL)

    def wait_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Не появился элемент {locator}",
        )

    def wait_not_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator),
            message=f"Элемент не исчез {locator}",
        )

    def wait_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент не кликабелен {locator}",
        )

    def click(self, locator):
        self.wait_clickable(locator).click()

    def get_text(self, locator):
        return self.wait_visible(locator).text.strip()

    def send_keys(self, locator, text):
        self.wait_visible(locator).send_keys(text)
