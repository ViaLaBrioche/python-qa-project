import pytest
import allure


from page_objects.inventory_page import InventoryPage
from page_objects.login_page import LoginPage


@pytest.mark.ui
@allure.title("Сортировка товаров")
@allure.description("Пользователь сортирует товары на странице Products")
@pytest.mark.parametrize(
    "sort_value",
    ["az", "za", "lohi", "hilo"],
    ids=["name_a_to_z", "name_z_to_a", "price_low_to_high", "price_high_to_low"],
)
def test_products_sorting(driver, ui_url, sort_value):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    with allure.step("Открываем страницу авторизации"):
        login_page.open(ui_url)

    with allure.step("Авторизуемся"):
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Проверяем, что страница товаров загрузилась"):
        inventory_page.wait_until_loaded()

    with allure.step(f"Выбираем сортировку: {sort_value}"):
        inventory_page.select_sorting(sort_value)

    if sort_value == "az":
        assert inventory_page.get_product_names() == sorted(
            inventory_page.get_product_names()
        )

    elif sort_value == "za":
        assert inventory_page.get_product_names() == sorted(
            inventory_page.get_product_names(),
            reverse=True,
        )

    elif sort_value == "lohi":
        assert inventory_page.get_product_prices() == sorted(
            inventory_page.get_product_prices()
        )

    elif sort_value == "hilo":
        assert inventory_page.get_product_prices() == sorted(
            inventory_page.get_product_prices(),
            reverse=True,
        )
