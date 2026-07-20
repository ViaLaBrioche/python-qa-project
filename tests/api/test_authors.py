import pytest
import allure
import requests


@pytest.mark.api
@allure.title("Получение списка авторов")
def test_get_authors(api_url):
    with allure.step("Отправляем GET-запрос на получение списка авторов"):
        res = requests.get(f"{api_url}/api/v1/Authors", timeout=10)

    with allure.step("Проверяем статус ответа"):
        assert res.status_code == 200

    with allure.step("Проверяем, что ответ содержит список авторов"):
        data = res.json()

        assert isinstance(data, list)
        assert len(data) > 0
        for authors in data:
            assert isinstance(authors["id"], int)
            assert isinstance(authors["idBook"], int)
            assert isinstance(authors["firstName"], str)
            assert isinstance(authors["lastName"], str)


@pytest.mark.api
@allure.title("Получение автора по id")
@pytest.mark.parametrize(
    "authors_id",
    [1, 250, 500],
)
def test_get_authors_by_id(api_url, authors_id):
    with allure.step("Отправляем GET-запрос на получение автора"):
        res = requests.get(f"{api_url}/api/v1/Authors/{authors_id}", timeout=10)

    with allure.step("Проверяем статус ответа"):
        assert res.status_code == 200

    with allure.step("Проверяем, что ответ содержит автора"):
        data = res.json()

        assert isinstance(data, dict)
        assert data["id"] == authors_id
        assert data["idBook"]
        assert data["firstName"] == f"First Name {authors_id}"
        assert data["lastName"] == f"Last Name {authors_id}"


@pytest.mark.api
@allure.title("Добавление автора")
def test_add_authors(api_url, author_data):
    with allure.step("Отправляем POST-запрос на добавление автора"):
        res = requests.post(f"{api_url}/api/v1/Authors", json=author_data, timeout=10)

    with allure.step("Проверяем статус ответа"):
        assert res.status_code == 200

    with allure.step("Проверяем данные добавленного автора"):
        data = res.json()

        assert isinstance(data, dict)
        assert data["id"] == author_data["id"]
        assert data["idBook"] == author_data["idBook"]
        assert data["firstName"] == author_data["firstName"]
        assert data["lastName"] == author_data["lastName"]


@pytest.mark.api
@allure.title("Изменение автора по ID")
@pytest.mark.parametrize(
    "idBook, authors_id", [(1, 1), (2, 250), (3, 594)], ids=["min", "middle", "max"]
)
def test_update_authors(api_url, idBook, authors_id, author_data):
    updated_authors = author_data.copy()
    updated_authors["idBook"] = idBook

    with allure.step(f"Отправляем PUT-запрос для автора с ID {authors_id}"):
        res = requests.put(
            f"{api_url}/api/v1/Authors/{authors_id}", json=updated_authors, timeout=10
        )

    with allure.step("Проверяем статус ответа"):
        assert res.status_code == 200

    with allure.step("Проверяем измененные данные автора"):
        data = res.json()

        assert isinstance(data, dict)
        assert data["idBook"] == idBook


@pytest.mark.api
@allure.title("Удаление автора по ID")
@pytest.mark.parametrize(
    "authors_id",
    [1, 250, 594],
    ids=["min", "middle", "max"],
)
def test_delete_authors(api_url, authors_id):
    with allure.step(f"Отправляем DELETE-запрос для автора с ID {authors_id}"):
        res = requests.delete(f"{api_url}/api/v1/Authors/{authors_id}", timeout=10)

    with allure.step("Проверяем статус ответа"):
        assert res.status_code == 200


@pytest.mark.api
@allure.title("Получение автора с несуществующим ID")
def test_get_authors_invalid_id(api_url):
    res = requests.get(f"{api_url}/api/v1/Authors/999999", timeout=10)

    with allure.step("Проверяем статус ответа"):
        assert res.status_code == 404


@pytest.mark.api
@allure.title("Получение автора с отрицательным ID")
def test_get_authors_negative_id(api_url):
    res = requests.get(f"{api_url}/api/v1/Authors/-1", timeout=10)

    assert res.status_code == 404
