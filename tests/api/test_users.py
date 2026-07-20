import pytest
import allure
import requests


@pytest.mark.api
@allure.title("Получение списка пользователей")
def test_get_users(api_url):
    with allure.step("Отправляем GET-запрос на получение списка пользователей"):
        res = requests.get(f"{api_url}/api/v1/Users", timeout=10)

    with allure.step("Проверяем статус ответа"):
        assert res.status_code == 200

    with allure.step("Проверяем, что ответ содержит список пользователей"):
        data = res.json()

        assert isinstance(data, list)
        assert len(data) > 0
        for user in data:
            assert isinstance(user["id"], int)
            assert isinstance(user["userName"], str)
            assert isinstance(user["password"], str)


@pytest.mark.api
@allure.title("Получение пользователя по id")
@pytest.mark.parametrize(
    "user_id",
    [1, 5, 10],
    ids=["min", "middle", "max"],
)
def test_get_user_by_id(api_url, user_id):
    with allure.step("Отправляем GET-запрос на получение пользователя"):
        res = requests.get(f"{api_url}/api/v1/Users/{user_id}", timeout=10)

    with allure.step("Проверяем статус ответа"):
        assert res.status_code == 200

    with allure.step("Проверяем, что ответ содержит пользователя"):
        data = res.json()

        assert isinstance(data, dict)
        assert data["id"] == user_id
        assert data["userName"] == f"User {user_id}"
        assert data["password"]


@pytest.mark.api
@allure.title("Добавление пользователя")
def test_add_user(api_url, user_data):
    with allure.step("Отправляем POST-запрос на добавление пользователя"):
        res = requests.post(f"{api_url}/api/v1/Users", json=user_data, timeout=10)

    with allure.step("Проверяем статус ответа"):
        assert res.status_code == 200

    with allure.step("Проверяем данные добавленного пользователя"):
        data = res.json()

        assert isinstance(data, dict)
        assert data["id"] == user_data["id"]
        assert data["userName"] == user_data["userName"]
        assert data["password"] == user_data["password"]


@pytest.mark.api
@allure.title("Изменение пользователя по ID")
@pytest.mark.parametrize(
    "user_id",
    [1, 5, 10],
    ids=["min", "middle", "max"],
)
def test_update_user(api_url, user_id, user_data):
    updated_user = user_data.copy()
    updated_user["id"] = user_id

    with allure.step(f"Отправляем PUT-запрос для пользователя с ID {user_id}"):
        res = requests.put(
            f"{api_url}/api/v1/Users/{user_id}",
            json=updated_user,
            timeout=10,
        )

    with allure.step("Проверяем статус ответа"):
        assert res.status_code == 200

    with allure.step("Проверяем измененные данные пользователя"):
        data = res.json()

        assert isinstance(data, dict)
        assert data["id"] == user_id
        assert data["userName"] == updated_user["userName"]
        assert data["password"] == updated_user["password"]


@pytest.mark.api
@allure.title("Удаление пользователя по ID")
@pytest.mark.parametrize(
    "user_id",
    [1, 5, 10],
    ids=["min", "middle", "max"],
)
def test_delete_user(api_url, user_id):
    with allure.step(f"Отправляем DELETE-запрос для пользователя с ID {user_id}"):
        res = requests.delete(f"{api_url}/api/v1/Users/{user_id}", timeout=10)

    with allure.step("Проверяем статус ответа"):
        assert res.status_code == 200


@pytest.mark.api
@allure.title("Получение пользователя с несуществующим ID")
def test_get_user_invalid_id(api_url):
    res = requests.get(f"{api_url}/api/v1/Users/999999", timeout=10)

    assert res.status_code == 404


@pytest.mark.api
@allure.title("Получение пользователя с отрицательным ID")
def test_get_user_negative_id(api_url):
    res = requests.get(f"{api_url}/api/v1/Users/-1", timeout=10)

    with allure.step("Проверяем статус ответа"):
        assert res.status_code == 404
