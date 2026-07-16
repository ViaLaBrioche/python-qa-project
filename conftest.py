import os
import logging
import pytest
import datetime
import allure

from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption(
        "--executor",
        default="local",
        choices=["local", "remote"],
        help="Формат запуска тестов: локально или удаленно",
    )
    parser.addoption(
        "--browser",
        default="chrome",
        choices=["chrome", "firefox"],
        help="Выбор браузера для запуска UI тестов",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        help="Запуск тестов без открытия окна браузера",
    )
    parser.addoption(
        "--ui_url", default="https://www.saucedemo.com/", help="URL для UI тестов"
    )
    parser.addoption(
        "--api_url",
        default="https://fakerestapi.azurewebsites.net",
        help="URL для API тестов",
    )
    parser.addoption(
        "--remote_url",
        default="http://localhost:4444/wd/hub",
        help="URL для удаленного запуска",
    )


@pytest.fixture
def ui_url(request):
    return request.config.getoption("--ui_url")


@pytest.fixture
def api_url(request):
    return request.config.getoption("--api_url")


@pytest.fixture
def driver(request):
    executor = request.config.getoption("--executor")
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    remote_url = request.config.getoption("--remote_url")

    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger(request.node.name)
    logger.handlers.clear()
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(
        f"logs/{request.node.name}.log",
        mode="w",
        encoding="utf-8",
    )

    file_handler.setFormatter(
        logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    )

    logger.addHandler(file_handler)
    logger.info("Test started")

    if browser == "chrome":
        options = ChromeOptions()

        if headless:
            options.add_argument("--headless=new")

    else:
        options = FirefoxOptions()

        if headless:
            options.add_argument("--headless")

    if executor == "local":
        if browser == "chrome":
            driver = webdriver.Chrome(options=options)
        else:
            driver = webdriver.Firefox(options=options)

    else:
        driver = webdriver.Remote(command_executor=remote_url, options=options)

    driver.logger = logger
    request.node.driver = driver

    driver.maximize_window()

    yield driver

    logger.info("===> Test finished at %s", datetime.datetime.now())
    driver.quit()
    file_handler.close()
    logger.removeHandler(file_handler)


@pytest.fixture
def checkout_user_information_data():
    fake = Faker()

    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "postal_code": fake.postalcode(),
    }


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")

        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Screenshot on failure",
                attachment_type=allure.attachment_type.PNG,
            )
