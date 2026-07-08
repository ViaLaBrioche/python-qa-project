import pytest
import allure


@pytest.mark.ui
@allure.title("test open website url")
def test_open_url(driver, ui_url):
    with allure.step("site was open"):
        pass

