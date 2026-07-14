import pytest
import allure

from page_objects.cart_page import CartPage
from page_objects.elements.header import Header
from page_objects.inventory_page import InventoryPage
from page_objects.login_page import LoginPage


@pytest.mark.ui
@allure.title("Возврат к покупкам со страницы корзины")
@allure.description("Пользователь успешно возвращается на страницу продуктов со страницы корзины")
def test_continue_shopping(driver, ui_url):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    header = Header(driver)

    with allure.step("Открываем страницу авторизации"):
        login_page.open(ui_url)

    with allure.step("Ожидаем загрузки страницы"):
        login_page.wait_until_loaded()

    with allure.step("Авторизуемся"):
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Проверяем, что страница товаров загрузилась"):
        inventory_page.wait_until_loaded()

    with allure.step("Добавляем товар в корзину"):
        inventory_page.add_to_cart()

    with allure.step("Открываем корзину"):
        header.click_cart()

    with allure.step("Ожидаем загрузку страницы корзины"):
        cart_page.wait_until_loaded()

    with allure.step("Возвращаемся к покупкам"):
        cart_page.continue_shopping()

    with allure.step("Проверяем открытие страницы товаров"):
        inventory_page.wait_until_loaded()
        assert "inventory.html" in driver.current_url