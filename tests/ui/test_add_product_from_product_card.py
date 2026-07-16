import pytest
import allure

from page_objects.elements.header import Header
from page_objects.inventory_page import InventoryPage
from page_objects.login_page import LoginPage
from page_objects.product_page import ProductPage


@pytest.mark.ui
@allure.title("Успешное оформление заказа")
@allure.description("Пользователь успешно оформляет товары из корзины")
def test_open_product_card(driver, ui_url):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    product_page = ProductPage(driver)
    header = Header(driver)

    with allure.step("Открываем страницу авторизации"):
        login_page.open(ui_url)

    with allure.step("Ожидаем загрузки страницы"):
        login_page.wait_until_loaded()

    with allure.step("Авторизуемся"):
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Проверяем, что страница товаров загрузилась"):
        inventory_page.wait_until_loaded()

    with allure.step("Проверяем, что страница товаров загрузилась"):
        inventory_page.wait_until_loaded()

    with allure.step("Открываем карточку товара"):
        inventory_page.open_product()

    with allure.step("Ожидаем загрузку страницы товара"):
        product_page.wait_until_loaded()

    with allure.step("Нажимаем Add to cart"):
        product_page.wait_until_loaded()

    with allure.step("Нажимаем Add to cart"):
        product_page.click_add_to_cart()

    with allure.step("Проверяем, что кнопка изменилась на remove"):
        product_page.wait_until_visible_remove()

    with allure.step("Проверяем, что товар добавлен в корзину"):
        inventory_page.wait_product_added()
        assert header.get_cart_badge_text() == "1"
