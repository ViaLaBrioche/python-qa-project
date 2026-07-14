import pytest
import allure

from page_objects.cart_page import CartPage
from page_objects.checkout_complete_page import CheckoutComplete
from page_objects.checkout_step_one_page import CheckoutOneStep
from page_objects.checkout_step_two_page import CheckoutTwoStep
from page_objects.elements.header import Header
from page_objects.inventory_page import InventoryPage
from page_objects.login_page import LoginPage


@pytest.mark.ui
@allure.title("Успешное оформление заказа")
@allure.description("Пользователь успешно оформляет товары из корзины")
def test_successful_checkout(driver, ui_url, checkout_user_information_data):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    header = Header(driver)
    checkout_one_step = CheckoutOneStep(driver)
    checkout_two_step = CheckoutTwoStep(driver)
    checkout_complete = CheckoutComplete(driver)

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

    with allure.step("Выполяем переход в корзину"):
        header.click_cart()

    with allure.step("Ожидаем загрузку страницы корзины"):
        cart_page.wait_until_loaded()

    with allure.step("Нажимаем кнопку checkout"):
        cart_page.click_checkout()

    with allure.step("Ожидаем загрузку страницы оформления заказа (Шаг 1)"):
        checkout_one_step.wait_until_loaded()

    with allure.step("Заполняем поле First Name"):
        checkout_one_step.enter_first_name(checkout_user_information_data["first_name"])

    with allure.step("Заполняем поле Last name"):
        checkout_one_step.enter_last_name(checkout_user_information_data["last_name"])

    with allure.step("Заполняем поле Zip/Postal-Code"):
        checkout_one_step.enter_postal_code(
            checkout_user_information_data["postal_code"]
        )

    with allure.step("Нажимаем кнопку continue"):
        checkout_one_step.click_continue()

    with allure.step("Ожидаем загрузку страницы оформления заказа (Шаг 1)"):
        checkout_two_step.wait_until_loaded()

    with allure.step("Нажимаем кнопку finish"):
        checkout_two_step.click_finish()

    with allure.step(
        "Ожидаем загрузку страницы успешного завершения оформления заказа"
    ):
        checkout_complete.wait_until_loaded()
