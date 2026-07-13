import pytest
import allure

from page_objects.login_page import LoginPage
from page_objects.inventory_page import InventoryPage


@pytest.mark.ui
@allure.title("Успешная авторизация пользователя")
@allure.description("Пользователь успешно осуществляет авторизацию по логину и паролю")
@pytest.mark.parametrize(
    "user",
    [
        "standard_user",
        "problem_user",
        "performance_glitch_user",
        "error_user",
        "visual_user",
    ],
    ids=["standard", "problem", "performance", "error", "visual"],
)
def test_login(driver, ui_url, user):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    password = "secret_sauce"

    with allure.step("Открываем браузер и страницу сайта"):
        login_page.open(ui_url)

    with allure.step("Авторизуемся по логину и пароль"):
        login_page.login(user, password)

    with allure.step("Ожидаем пока главная страница загрузится"):
        inventory_page.wait_until_loaded()


@pytest.mark.ui
@allure.title("Авторизация заблокированного пользователя")
@allure.description("Заблокированный пользователь не может авторизоваться")
def test_locked_out_user_login(driver, ui_url):

    login_page = LoginPage(driver)
    password = "secret_sauce"

    with allure.step("Открываем браузер и страницу сайта"):
        login_page.open(ui_url)

    with allure.step("Ожидаем загрузки страницы"):
        login_page.wait_until_loaded()

    with allure.step("Авторизуемся заблокированным пользователем"):
        login_page.login("locked_out_user", password)

    with allure.step("Проверяем сообщение об ошибке"):
        error_message = login_page.get_error_message()

        assert "Epic sadface: Sorry, this user has been locked out." in error_message
