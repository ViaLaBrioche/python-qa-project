import pytest
import allure

from page_objects.cart_page import CartPage
from page_objects.inventory_page import InventoryPage
from page_objects.login_page import LoginPage


@pytest.mark.ui
@allure.title("Удаление товара из корзины")
@allure.description("Пользователь успешно удаляет товар из корзины")
def test_delete_product_from_cart(driver, ui_url):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

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
        cart_page.open(ui_url)

    with allure.step("Ожидаем загрузку страницы корзины"):
        cart_page.wait_until_loaded()

    with allure.step("Удаляем товар из корзины"):
        cart_page.delete_product()

    with allure.step("Проверяем, что товар удален из корзины"):
        cart_page.wait_product_removed()
