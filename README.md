# praktikum_new_diplom:

![workflow](https://github.com/dementevaleksander/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)

# Дипломный проект:
Проект: приложение «Продуктовый помощник»

# Описание:
Разработано приложение «Продуктовый помощник» и собрано в в контейнер Docker.

# Проект доступен по ссылкам:

```
http://51.250.109.233/
http://51.250.109.233/admin/
http://51.250.109.233/api/docs/
```

# Логин и пароль администратора:
```
почта: reviewer@mail.ru
пароль: reviewerparol9999
```

##### Шаблон наполнения env-файла:
```
infra/.env
```

# Инструкция по запуску:
##### 1) Клонировать репозиторий и перейти в него в командной строке:
```
git@github.com:DementevAleksander/foodgram-project-react.git
```
```
cd backend/
```
##### 2) Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
```

```
source env/bin/activate
```

##### 3) Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

##### 4) Запустить приложение в контейнерах:

из директории infra/
```
docker-compose up -d --build
```

##### 5) Выполнить миграции:
```
docker-compose exec web python manage.py migrate
```

##### 6) Создать суперпользователя:

из директории infra/
```
docker-compose exec web python manage.py createsuperuser
```

##### 7) Собрать статику:

из директории infra/
```
docker-compose exec web python manage.py collectstatic --no-input
```

### Регистрация пользователя (примеры запросов):
1. Отправить POST-запрос с параметром email и username на `/api/v1/auth/signup`.
2. Получить код подтверждения (confirm_code) на адрес email (эмуляция почтовго сервера).
3. Отправить POST-запрос с параметрами email и confirmation_code на `/api/v1/auth/token/`.
4. В ответ на запрос получен token.

### Использованные технологии:
```
Python 3.9
Django 2.2.19
DRF
Nginx
Docker
Docker-compose
Postgresql
Github Actions.
```

### Об авторе:
Дементьев Александр (с) 2023
