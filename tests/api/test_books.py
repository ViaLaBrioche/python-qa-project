import pytest
import allure
import requests


@pytest.mark.api
@allure.title("Получение списка книг")
def test_get_books(api_url):
    with allure.step("Отправляем GET-запрос на получение списка книг"):
        res = requests.get(f"{api_url}/api/v1/Books", timeout=10)

    with allure.step("Проверяем статус ответа"):
        assert res.status_code == 200

    with allure.step("Проверяем, что ответ содержит список книг"):
        data = res.json()

        assert isinstance(data, list)
        assert len(data) > 0


@pytest.mark.api
@allure.title("Получение книги по id")
@pytest.mark.parametrize(
    "id",
    [1, 50, 200],
    ids=["min", "middle", "max"],
)
def test_get_book_by_id(api_url, id):
    with allure.step("Отправляем GET-запрос на получение книги"):
        res = requests.get(f"{api_url}/api/v1/Books/{id}", timeout=10)

    with allure.step("Проверяем статус ответа"):
        assert res.status_code == 200

    with allure.step("Проверяем, что ответ содержит книгу"):
        data = res.json()

        assert isinstance(data, dict)
        assert data["id"] == id
        assert data["title"] == f"Book {id}"
        assert data["description"]
        assert data["pageCount"]
        assert data["excerpt"]
        assert data["publishDate"]


@pytest.mark.api
@allure.title("Добавление книги")
def test_add_book(api_url, book_data):
    with allure.step("Отправляем POST-запрос на добавление книги"):
        res = requests.post(f"{api_url}/api/v1/Books", json=book_data, timeout=10)

    with allure.step("Проверяем статус ответа"):
        assert res.status_code == 200

    with allure.step("Проверяем данные добавленной книги"):
        data = res.json()

        assert isinstance(data, dict)
        assert data["id"] == book_data["id"]
        assert data["title"] == book_data["title"]
        assert data["description"] == book_data["description"]
        assert data["pageCount"] == book_data["pageCount"]
        assert data["excerpt"] == book_data["excerpt"]


@pytest.mark.api
@allure.title("Изменение книги по ID")
@pytest.mark.parametrize(
    "book_id",
    [1, 50, 200],
    ids=["min", "middle", "max"],
)
def test_update_book(api_url, book_id, book_data):

    updated_book = book_data.copy()
    updated_book["id"] = book_id

    with allure.step(f"Отправляем PUT-запрос для книги с ID {book_id}"):
        res = requests.put(
            f"{api_url}/api/v1/Books/{book_id}",
            json=updated_book,
            timeout=10,
        )

    with allure.step("Проверяем статус ответа"):
        assert res.status_code == 200

    with allure.step("Проверяем измененные данные книги"):
        data = res.json()

        assert isinstance(data, dict)
        assert data["id"] == book_id
        assert data["title"] == updated_book["title"]
        assert data["description"] == updated_book["description"]
        assert data["pageCount"] == updated_book["pageCount"]
        assert data["excerpt"] == updated_book["excerpt"]


@pytest.mark.api
@allure.title("Удаление книги по ID")
@pytest.mark.parametrize(
    "book_id",
    [1, 50, 200],
    ids=["min", "middle", "max"],
)
def test_delete_book(api_url, book_id):
    with allure.step(f"Отправляем DELETE-запрос для книги с ID {book_id}"):
        res = requests.delete(f"{api_url}/api/v1/Books/{book_id}", timeout=10)

    with allure.step("Проверяем статус ответа"):
        assert res.status_code == 200


@pytest.mark.api
@allure.title("Получение книги с несуществующим ID")
def test_get_book_invalid_id(api_url):
    res = requests.get(f"{api_url}/api/v1/Books/999999", timeout=10)

    assert res.status_code == 404


@pytest.mark.api
@allure.title("Получение книги с отрицательным ID")
def test_get_book_negative_id(api_url):
    res = requests.get(f"{api_url}/api/v1/Books/-1", timeout=10)

    with allure.step("Проверяем статус ответа"):
        assert res.status_code == 404
