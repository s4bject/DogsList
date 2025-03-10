# DogsList

## Описание проекта
Приложение **DogsList** предназначено для добавления собак и их пород.

## Архитектура проекта

Проект состоит из следующих компонентов:

### 1. dogs_django (основное приложение)
- **migrations/**: Папка, содержащая миграции базы данных для приложения `dogs`. Каждая миграция описывает изменения в структуре базы данных (создание таблиц, добавление или изменение полей).
- **admin.py**: Конфигурация административной панели Django для модели `Dog`. Здесь можно настроить, как модели отображаются и управляются в интерфейсе администратора.
- **apps.py**: Конфигурация приложения `dogs`. Django использует этот файл для регистрации приложения.
- **models.py**: Определение моделей базы данных. Включает модель `Dog`, описывающую собак, их характеристики и связи с другими моделями.
- **serializers.py**: Описание сериализаторов для преобразования данных моделей в JSON-формат и обратно. 
  - **DogListSerializer**: Используется для отображения списка собак с информацией о породе и среднем возрасте.
  - **DogDetailSerializer**: Используется для отображения подробной информации о собаке, включая количество собак той же породы.
- **tests.py**: Файл для написания тестов, проверяющих функциональность приложения.
- **views.py**: Содержит ViewSet `DogViewSet` для обработки запросов к API. Реализованы методы для получения списка, создания, редактирования и удаления собак.
  - **GET** запрос к списку добавляет информацию о среднем возрасте собак породы.
  - **GET** запрос к детальной записи добавляет количество собак той же породы.

### 2. dogs_project (конфигурация проекта)
- **settings.py**: Настройки проекта, включая базы данных, установленные приложения, middleware и конфигурацию REST Framework.
- **urls.py**: Определяет маршруты URL-адресов проекта, включая маршруты для ViewSet'ов `DogViewSet` и `BreedViewSet`. Использует `SimpleRouter` для автоматической генерации маршрутов.
- **asgi.py**: Настройка ASGI-сервера для асинхронного взаимодействия.
- **wsgi.py**: Настройка WSGI-сервера для развертывания проекта.

### 3. Корневые файлы проекта
- **Dockerfile** и **docker-compose.yml**: Скрипты для контейнеризации проекта с использованием Docker.
- **manage.py**: Инструмент для управления проектом (запуск сервера, выполнение миграций, создание суперпользователя и т. д.).
- **requirements.txt**: Список зависимостей проекта, необходимых для его работы.

## API Эндпоинты

### 1. `/api/dogs/` (GET, POST)
- **GET**: Возвращает список всех собак с информацией о средней возрасте их породы.
- **POST**: Создаёт новую запись о собаке.

### 2. `/api/dogs/<id>/` (GET, PUT, DELETE)
- **GET**: Возвращает детальную информацию о собаке, включая количество собак той же породы.
- **PUT**: Обновляет информацию о собаке.
- **DELETE**: Удаляет запись о собаке.

### 3. `/api/breeds/` (GET, POST)
- **GET**: Возвращает список всех пород.
- **POST**: Создаёт новую породу.

## Запуск проекта

1. Установите зависимости из `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

2. Выполните миграции базы данных:
    ```bash
    python manage.py migrate
    ```

3. Запустите сервер разработки:
    ```bash
    python manage.py runserver
    ```

## Использование Docker

Для запуска проекта в контейнере:

1. Постройте Docker-образ:
    ```bash
    docker-compose build
    ```

2. Запустите контейнеры:
    ```bash
    docker-compose up
    ```
3. Выполните миграции базы данных:
   ```bash
   docker-compose exec web python manage.py migrate
   ```

Проект будет доступен по адресу `http://localhost:8000/`.
---

## Функционал для породы

### 1. Добавление породы
- Пользователь может добавить собаку указав:
  - name (строка символов)
  - size (строка символов) [должно принимать значения Tiny, Small, Medium, Large]
  - friendliness (поле целого числа) [должно принимать значения от 1 до 5]
  - trainability (поле целого числа) [должно принимать значения от 1 до 5]
  - shedding_amount (поле целого числа) [должно принимать значения от 1 до 5]
  - exercise_needs (поле целого числа) [должно принимать значения от 1 до 5]


### 2. Удаление породу по ID

### 3. Просмотр всех пород или по ID

### 5. Изменение породы
- Пользователь может поменять все параметры породы

## Функционал для собак

### 1. Добавление собаки
- Пользователь может добавить собаку указав:
  - name (строка символов)
  - age (целое число)
  - breed (внешний ключ к модели Breed)
  - gender (строка символов)
  - color (строка символов)
  - favorite_food (строка символов)
  - favorite_toy (строка символов)


### 2. Удаление собаку по ID

### 3. Просмотр всех собак или по ID

### 5. Изменение собаки
- Пользователь может поменять все параметры собаки
---
## Примеры использования API

### Собаки (Dogs)

#### Получение списка собак
**Запрос:**
```http
GET /api/dogs/
```
**Пример ответа:**
```json
[
  {
    "id": 1,
    "name": "Buddy",
    "age": 3,
    "breed_avg_age": 7.5,
    "breed_name": "Labrador",
    "gender": "Male",
    "color": "Brown",
    "favorite_food": "Bones",
    "favorite_toy": "Ball",
    "breed": 1
  }
]
```

#### Создание новой собаки
**Запрос:**
```http
POST /api/dogs/
Content-Type: application/json
```
**Тело запроса:**
```json
{
  "name": "Charlie",
  "age": 1,
  "breed": 1,
  "gender": "Male",
  "color": "Black",
  "favorite_food": "Meat",
  "favorite_toy": "Stick"
}
```

#### Получение деталей собаки
**Запрос:**
```http
GET /api/dogs/1/
```
**Пример ответа:**
```json
{
  "id": 1,
  "name": "Buddy",
  "age": 3,
  "breed_name": "Labrador",
  "gender": "Male",
  "color": "Brown",
  "favorite_food": "Bones",
  "favorite_toy": "Ball",
  "breed": 1,
  "breed_count": 4
}
```

#### Обновление данных собаки
**Запрос:**
```http
PUT /api/dogs/1/
Content-Type: application/json
```
**Тело запроса:**
```json
{
  "name": "Buddy",
  "age": 4,
  "breed": 1,
  "gender": "Male",
  "color": "Brown",
  "favorite_food": "Bones",
  "favorite_toy": "Ball"
}
```

#### Удаление собаки
**Запрос:**
```http
DELETE /api/dogs/1/
```

### Породы (Breeds)

#### Получение списка пород
**Запрос:**
```http
GET /api/breeds/
```
**Пример ответа:**
```json
[
  {
    "id": 1,
    "name": "Labrador",
    "dog_count": 2,
    "size": "Large",
    "friendliness": 5,
    "trainability": 5,
    "shedding_amount": 4,
    "exercise_needs": 5
  },
  {
    "id": 2,
    "name": "Beagle",
    "dog_count": 1,
    "size": "Medium",
    "friendliness": 4,
    "trainability": 4,
    "shedding_amount": 3,
    "exercise_needs": 4
  }
]
```

#### Создание новой породы
**Запрос:**
```http
POST /api/breeds/
Content-Type: application/json
```
**Тело запроса:**
```json
{
  "name": "Golden Retriever",
  "size": "Large",
  "friendliness": 5,
  "trainability": 5,
  "shedding_amount": 4,
  "exercise_needs": 5
}
```
