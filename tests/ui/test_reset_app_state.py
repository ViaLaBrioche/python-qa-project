import pytest
import allure

from page_objects.elements.header import Header
from page_objects.elements.side_bar import SideBar
from page_objects.inventory_page import InventoryPage
from page_objects.login_page import LoginPage


@pytest.mark.ui
@allure.title("Очистка корзины через сброс состояния приложения")
@allure.description(
    "Пользователь добавляет товар в корзину, выполняет Reset App State и проверяет, что корзина очищена"
)
def test_reset_app_state(driver, ui_url):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    side_bar = SideBar(driver)
    header = Header(driver)

    with allure.step("Открываем страницу авторизации"):
        login_page.open(ui_url)

    with allure.step("Ожидаем загрузки страницы"):
        login_page.wait_until_loaded()

    with allure.step("Авторизуемся по логину и пароль"):
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Ожидаем пока главная страница загрузится"):
        inventory_page.wait_until_loaded()

    with allure.step("Добавляем товар в корзину"):
        inventory_page.add_to_cart()

    with allure.step("Проверяем, что товар добавлен в корзину"):
        inventory_page.wait_product_added()
        assert header.get_cart_badge_text() == "1"

    with allure.step("Открываем боковое меню"):
        header.open_side_bar()

    with allure.step("Ожидаем загрузку открытие боковой панели"):
        side_bar.wait_until_loaded()

    with allure.step("Выполняем сброс состояния приложения"):
        side_bar.reset()

    with allure.step("Проверяем, что сброс успешно выполнен"):
        header.wait_until_reset()
