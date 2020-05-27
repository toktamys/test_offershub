# **Тестовое задание от Offershub**

#### Необходимые шаги для развертывания:
1) ~~Скачать репозиторий~~
2) В папке asana_offershub создать файл local_settings.py с таким содержанием: <br>
`from .settings import *` <br>
`PERSONAL_ACCESS_TOKEN = 'здесь Ваш токен от Asana'`
3) Далее, будучи в корне проекта выполнить команды <br>
`docker-compose build` <br>
`docker-compose up -d`
4) Внутри контейнера **asana_project** выполнить команду `python manage.py migrate`
5) Внутри контейнера **asana_project** выполнить команду `python manage.py createsuperuser` и создать суперпользователя
6) Внутри контейнера **asana_project** выполнить команду `python manage.py import_admin_from_asana`
7) По адресу `0.0.0.0:8000/admin` будет доступна админка