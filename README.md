Созданы 3 модели (Title, Url, News). Подключена админка. Добавлен парсер новостей с сайта https://pythondigest.ru. Спарсенные данные сразу сохраняются в базу (в админке проверил, все работает). Для смены запроса на парсинг меняем значение переменной req по адресу parser_news/data_base/management/commands/fill_db.py.