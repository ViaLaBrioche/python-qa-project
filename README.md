# Автоматизация Frontend-тестирования веб-приложения SauceDemo и Backend-тестирования API FakeRESTApi

Проект по автоматизации тестирования пользовательского интерфейса веб-приложения SauceDemo и REST API FakeRESTApi с использованием Python, Selenium, Pytest, Docker, Jenkins и Allure.

## Стек

- Python
- Pytest
- Selenium
- Requests
- Faker
- Allure
- Docker
- Docker Compose
- Jenkins
- Selenoid

## Структура проекта

```
page_objects/
tests/
    api/
    ui/

jenkins/
selenoid/
logs/

conftest.py
pytest.ini
Dockerfile
docker-compose.yml
Jenkinsfile
requirements.txt
README.md
```

## Установка

```bash
git clone https://github.com/ViaLaBrioche/python-qa-project.git
cd python-qa-project

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

## Запуск тестов

API

```bash
pytest tests/api -v
```

UI

```bash
pytest tests/ui -v --executor=local --browser=chrome
```

UI через Selenoid

```bash
pytest tests/ui -v \
--executor=remote \
--remote_url=http://localhost:4444/wd/hub
```

## Запуск проекта

```bash
docker compose up -d
```

## Jenkins

Pipeline автоматически:

- собирает Docker-образы
- запускает API и UI тесты
- формирует Allure Report

## Реализовано

- UI-тестирование веб-приложения SauceDemo
- API-тестирование сервиса FakeRESTApi
- Allure Report
- логирование
- скриншоты при падении UI-тестов
- запуск через Docker
- автоматический запуск через Jenkins

## Allure Report

После выполнения тестов отчет формируется автоматически в Jenkins

Для локального просмотра:

```bash
allure serve allure-results
```

## Логирования

Логи каждого теста сохраняются в директории `logs/`