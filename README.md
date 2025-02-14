## Описание
Веб-приложение для тестового задания. 

Техническое задание:
- Реализовать вёрстку страниц из макета;
- Реализовать бэкенд:
    - Страница "Посты" - получение массива постов с названием и содержанием каждого поста;
    - Страница "Пользователи" - получение массива пользователей с ФИО и e-mail каждого пользователя;
    - Запрос на получение детализации по конкретному выбранному пользователю (ФИО, e-mail, адрес ...)
    - Главная страница - содержание на усмотрение разработчика

Примечание.

Поскольку в задании не было требования реализации регистрации пользователей, модель "Пользователь" 
наследуется от класса Model. Для реализации регистрации, авторизации и аутентификации пользователей 
необходимо наследоваться от класса AbstractUser.

В модальном окне кнопка "Сохранить" просто закрывает окно, так как в задании было требование на получение данных о конкретном пользователе,
 а не об изменении их. 

## Технологии
- Python
- Django
- jquery
- HTML
- CSS
- Bootstrap

К проекту подключена база SQLite. 

## Локальный запуск проекта

1. ### Перейдите в нужную папку и склонируйте репозиторий:
```
git clone https://github.com/Svetlana-Zimina/metro-test.git
```

2. ### Создайте и активируйте виртуальное окружение:
Команда для установки виртуального окружения на Mac или Linux:
```
cd metro-test
python3 -m venv env
source env/bin/activate
```

Команда для установки виртуального окружения на Windows:
```
cd metro-test
python -m venv venv
source venv/Scripts/activate
```
3. ### Установите зависимости:
```
pip install -r requirements.txt
```

4. ### Проведите миграции:
```
cd metro
python manage.py migrate
```

5. ### Наполните базу:
```
python manage.py loaddata fixtures/users.json
python manage.py loaddata fixtures/posts.json
```

6. ### При необходимости создайте суперпользователя:
```
python manage.py createsuperuser
```

7. ### Запустите локальный сервер:
```
python manage.py runserver
```

## Авторы
Светлана Зимина
https://github.com/Svetlana-Zimina