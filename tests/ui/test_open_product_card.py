import pytest
import allure

from page_objects.inventory_page import InventoryPage
from page_objects.login_page import LoginPage
from page_objects.product_page import ProductPage


@pytest.mark.ui
@allure.title("Успешное оформление заказа")
@allure.description("Пользователь успешно оформляет товары из корзины")
def test_open_product_card(driver, ui_url, checkout_user_information_data):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    product_page = ProductPage(driver)

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

    with allure.step("Находим имя товара на странице товаров"):
        product_name_inventory = inventory_page.get_product_name()

    with allure.step("Находим описание товара на странице товаров"):
        product_desc_inventory = inventory_page.get_product_description()

    with allure.step("Находим цену товара на странице товаров"):
        product_price_inventory = inventory_page.get_product_price()

    with allure.step("Открываем карточку товара"):
        inventory_page.open_product()

    with allure.step("Ожидаем загрузку страницы товара"):
        product_page.wait_until_loaded()

    with allure.step("Находим имя товара в карточке товара"):
        product_name_card = product_page.get_product_name()

    with allure.step("Находим описание товара в карточке товара"):
        product_desc_card = product_page.get_product_description()

    with allure.step("Находим цену товара в карточке товара"):
        product_price_card = product_page.get_product_price()

    with allure.step("Проверяем, что имя совпадает"):
        assert (
            product_name_inventory.lower().replace("...", "")
            in product_name_card.lower()
        )

    with allure.step("Проверяем, что описание совпадает"):
        assert (
            product_desc_inventory.lower().replace("...", "")
            in product_desc_card.lower()
        )

    with allure.step("Проверяем, что цена совпадает"):
        assert (
            product_price_inventory.lower().replace("...", "")
            in product_price_card.lower()
        )
