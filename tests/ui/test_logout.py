import pytest
import allure

from page_objects.elements.header import Header
from page_objects.elements.side_bar import SideBar
from page_objects.inventory_page import InventoryPage
from page_objects.login_page import LoginPage


@pytest.mark.ui
@allure.title("Выход из учетной записи")
@allure.description("Пользователь успешно совершает выход из учетной записи")
def test_logout(driver, ui_url):
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

    with allure.step("Открываем боковое меню"):
        header.open_side_bar()

    with allure.step("Ожидаем загрузку открытие боковой панели"):
        side_bar.wait_until_loaded()

    with allure.step("Выполняем выход из учетной записи"):
        side_bar.logout()

    with allure.step("Выход из учетной записи успешно выполнен"):
        login_page.wait_until_loaded()
