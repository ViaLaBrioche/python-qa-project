import pytest
import allure

from page_objects.elements.header import Header
from page_objects.inventory_page import InventoryPage
from page_objects.login_page import LoginPage


@pytest.mark.ui
@allure.title("Добавление товара в корзину")
@allure.description("Пользователь успешно добавляет товар в корзину")
def test_add_product_to_cart(driver, ui_url):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
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

    with allure.step("Проверяем, что товар добавлен в корзину"):
        inventory_page.wait_product_added()
        assert header.get_cart_badge_text() == "1"
