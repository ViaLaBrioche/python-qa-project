from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from selenium.webdriver.support.select import Select


class InventoryPage(BasePage):
    MENU = (By.ID, "menu_button_container")
    CART = (By.ID, "shopping_cart_container")
    INVENTORY = (By.ID, "inventory_container")
    BTN_ADD_TO_CART = (By.XPATH, "//button[contains(., 'Add to cart')]")
    BTN_REMOVE = (By.ID, "remove-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    SORT_SELECT = (By.CLASS_NAME, "product_sort_container")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")

    def wait_until_loaded(self):
        self.wait_visible(self.MENU)
        self.wait_visible(self.CART)
        self.wait_visible(self.INVENTORY)

    def add_to_cart(self):
        self.click(self.BTN_ADD_TO_CART)

    def wait_product_added(self):
        self.wait_visible(self.BTN_REMOVE)
        self.wait_visible(self.CART_BADGE)

    def select_sorting(self, value):
        sort = Select(self.wait_visible(self.SORT_SELECT))
        sort.select_by_value(value)

    def get_product_names(self):
        elements = self.driver.find_elements(*self.PRODUCT_NAMES)
        return [element.text for element in elements]

    def get_product_prices(self):
        elements = self.driver.find_elements(*self.PRODUCT_PRICES)
        return [float(element.text.replace("$", "")) for element in elements]
