# Продуктовый помощник Foodgram
## Ссылка на сайт [http://dudeinn.sytes.net](http://dudeinn.sytes.net)


На этом сервисе пользователи смогут публиковать рецепты, подписываться на публикации
других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом
в магазин скачивать сводный список продуктов, необходимых для приготовления одного или
нескольких выбранных блюд.

#### для проверки админки юзернейм: mix38 пароль: 880607

### Деплой

Автоматически выполняется деплой на сервер в облаке Яндекса.

Статус: [![Foodgram project workflow](https://github.com/dude-inn/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)](https://github.com/dude-inn/foodgram-project-react/actions/workflows/foodgram_workflow.yml)

### Как запустить проект:

Клонировать репозиторий и перейти в каталог infra в командной строке:

```
git clone https://github.com/dude-inn/foodgram-project-react.git
cd foodgram-project-react/infra/
```

Заполнить файл infra/.env (пример заполнения ниже).

### Создание суперпользователя вручную

Для создания суперпользователя вручную воспользуйтесь командой

`docker-compose exec backend python manage.py createsuperuser`

### Требования и пример заполнения файла .env

Файл .env может содержать следующие переменные:
Обязательные:

```
DB_ENGINE - драйвер СУБД для Django
DB_HOST - имя хоста (docker-контейнера)
DB_NAME - имя базы данных
DB_PORT - порт для подключения к базе данных
POSTGRES_PASSWORD - пароль пользователя из предыдущего пункта
POSTGRES_USER - имя пользователя, владельца базы данных или администратора СУБД
SECRET_KEY - секретный ключ для нужд Django
```

### Документация доступна по ссылке:

`http://localhost/api/docs/`

### Требования:

Docker 20.10.14

docker-compose 1.25.0
