Django приложение для тестирования оплаты через Stripe

Запуск:
1) Клонируем репозиторий командой: 
```
git clone https://github.com/javlking/test_stripe_project.git
```
2) Создаем виртуальное окружение: 
```
python -m venv venv
```
5) Активируем виритуальное окружение через команду: 
```
Linux: source venv/bin/activate;
Windows: venv\Scripts\activate
```
6) Устанавливаем необходимые библиотеки: 
```
pip install -r requirements.txt
```
7) Запускаем проект командой: 
```
python manage.py runserver
```
8) Перейдя по ссылке /item/id если есть товар получим форму для покупки
------------------------------------------
Дополнительно:
1) Перейдя по /admin можно попасть на панель администратора и контролировать Item
```
Login: admin
Password: admin
````
