# Продуктовый помощник Foodgram
## Ссылка на сайт [http://84.252.129.194](http://84.252.129.194)
может не работать в связи с окончанием срока действия облачных сервисов

На этом сервисе пользователи смогут публиковать рецепты, подписываться на публикации
других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом
в магазин скачивать сводный список продуктов, необходимых для приготовления одного или
нескольких выбранных блюд.


Статус: [![Foodgram project workflow](https://github.com/dude-inn/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)](https://github.com/dude-inn/foodgram-project-react/actions/workflows/foodgram_workflow.yml)

### Как запустить проект:

Клонировать репозиторий и перейти в каталог infra в командной строке:

```
git clone https://github.com/dude-inn/foodgram-project-react.git
cd foodgram-project-react/infra/
```
Заполнить файл infra/.env (пример заполнения ниже).
### Требования и пример заполнения файла .env
Файл .env может содержать следующие переменные:
```
DB_ENGINE - драйвер СУБД для Django
DB_HOST - имя хоста (docker-контейнера)
DB_NAME - имя базы данных
DB_PORT - порт для подключения к базе данных
POSTGRES_PASSWORD - пароль пользователя из предыдущего пункта
POSTGRES_USER - имя пользователя, владельца базы данных или администратора СУБД
SECRET_KEY - секретный ключ для нужд Django
DEBUG - значение Debug (True/False) для настройки Django
```

Из папки infra выполните:
```
docker-compose up -d --build
```
Узнайте id существующих контейнеров
```
docker container ls
```
Скопируйте id backend-контейнера и войдите в него
```
docker exec -it <CONTAINER ID> sh
```
Сделайте миграцию БД и сбор статики
```
python manage.py migrate
python manage.py collectstatic
```

Импорт данных выполняется при миграции БД (реализован импорт для ингредиентов из файла ingredients.json)
Файлы для импорта хранятся в папке app/data/

### Создание суперпользователя вручную

Для создания суперпользователя вручную воспользуйтесь командой bp backend-контейнера

`python manage.py createsuperuser`

### Документация доступна по ссылке:

`http://84.252.129.194/api/docs/redoc.html`

### Требования:

Docker 20.10.14

docker-compose 1.25.0
