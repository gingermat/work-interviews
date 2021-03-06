# Тестовое задание - Arrival

### Сервер на aiohttp для сбора данных по websocket и доступа к ним через REST-интерфейс

Используется только aiohttp и aiomongo, без gunicorn, pydantic, uvloop))

По-умолчанию, для данных в MongoDB создается пользователь `test_user` c паролем `test_password` и база `test`. Данные сохраняются в коллекции `inventory`.

### Описание взаимодействия с сервисом

##### Сбор данных
Осуществляется по  протоколу Websocket по адресу ```ws://[адрес сервера:порт]/```

##### Отображение данных
Осуществляется по протоколу http с помощью GET запроса на адрес ```http://[адрес сервера:порт]/display```

Опционально с помощью параметров QUERY_STRING можно задать:
* ```page``` - Номер страницы отображаемых данных [по-умолчанию - 1]

##### Переменные окружения
В соответствии с рекомендациями Twelve-Factor App, управление приложением реализованно через переменные окружения

|    Название переменной     |                                      Назначение                                        |                           Значение по-умолчанию                    |
|:---------------------------|:---------------------------------------------------------------------------------------|:------------------------------------------------------------------:|
| DEBUG                      | Включает режим подробного логгирования                                                 |                                  False                             |
| LOG_LEVEL                  | Уровень логгирования запросов                                                          |                                   INFO                             |
| API_HOST                   | Адрес сервера                                                                          |                                  0.0.0.0                           |
| API_PORT                   | Порт сервиса                                                                           |                                   8080                             |
| MONGODB_URL                | URL для подключения к MongoDB                                                          |  mongodb://test_user:test_password@mongo:27017/test?maxpoolsize=5  |
| INVENTORY_COLLECTION_NAME  | Названия MongoDB коллекции для сохранения данных                                       |                                 inventory                          |
| INVENTORY_ITEMS_PER_PAGE   | Кол-во отображаемых на странице элементов коллекции|                                    50                              |




### Вариант запуска c помощью docker-compose

```
# docker-compose up
```

Сервис доступен по порту 8080. На порту 8081 доступен web-интерфейс к MongoDB.


### Вариант запуска как контейнера

```
# docker build -t inventory_service .
# docker run -p 8080:8080 -e MONGODB_URL=... inventory_service run_server
```

Сервис доступен по порту 8080

### Заполнение тестовыми данными

Для заполнение тестовыми данными можно использовать скрипт ```fill_data.py```
