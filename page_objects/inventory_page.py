import random
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from selenium.webdriver.support.select import Select


class InventoryPage(BasePage):
    random_product_id = random.randint(0, 5)
    PRODUCT = (
        By.XPATH,
        f'//a[@id="item_{random_product_id}_title_link"]'
        '/ancestor::div[@class="inventory_item"]',
    )
    MENU = (By.ID, "menu_button_container")
    INVENTORY = (By.ID, "inventory_container")
    BTN_ADD_TO_CART = (By.XPATH, "//button[contains(., 'Add to cart')]")
    BTN_REMOVE = (By.XPATH, "//button[contains(., 'Remove')]")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    SORT_SELECT = (By.CLASS_NAME, "product_sort_container")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_DESCRIPTION = (By.CLASS_NAME, "inventory_item_desc")
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")

    def wait_until_loaded(self):
        self.wait_visible(self.MENU)
        self.wait_visible(self.INVENTORY)

    def add_to_cart(self):
        self.click(self.BTN_ADD_TO_CART)

    def wait_product_added(self):
        self.wait_visible(self.BTN_REMOVE)
        self.wait_visible(self.CART_BADGE)

    def get_product_names(self):
        elements = self.driver.find_elements(*self.PRODUCT_NAME)
        return [element.text for element in elements]

    def get_product_prices(self):
        elements = self.driver.find_elements(*self.PRODUCT_PRICE)
        return [float(element.text.replace("$", "")) for element in elements]

    def select_sorting(self, value):
        sort = Select(self.wait_visible(self.SORT_SELECT))
        sort.select_by_value(value)

    def get_product_name(self):
        product = self.wait_visible(self.PRODUCT)
        return product.find_element(*self.PRODUCT_NAME).text.strip()

    def get_product_description(self):
        product = self.wait_visible(self.PRODUCT)
        return product.find_element(*self.PRODUCT_DESCRIPTION).text.strip()

    def get_product_price(self):
        product = self.wait_visible(self.PRODUCT)
        return product.find_element(*self.PRODUCT_PRICE).text.strip()

    def open_product(self):
        product = self.wait_visible(self.PRODUCT)
        product.find_element(*self.PRODUCT_NAME).click()
