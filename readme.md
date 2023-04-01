# Обрезка ссылок с помощью сервиса Bit.Ly

Эта программа предоставляет функциональность для обработки ссылок с использованием API Bit.ly.\
Она поддерживает три функции:

- `shorten_link(token, user_input)` - метод сокращает заданный URL user_input до Bit.ly-ссылки с использованием указанного токена token.
- `count_clicks(token, user_input)` - метод подсчитывает общее количество кликов по ссылке user_input на Bit.ly с использованием указанного токена token.
- `is_bitlink(token, user_input)` - метод проверяет, является ли указанный URL user_input ссылкой на Bit.ly с использованием указанного токена token.


### Использование:

Запустите программу с помощью следующей команды:

`python bitly.py <user_input>`\
где `<user_input>` - это URL, который должен быть обработан.

Если URL уже является ссылкой Bit.ly, программа вернет общее количество кликов для этой ссылки.\
Если это не ссылка Bit.ly, программа вернет сокращенную ссылку Bit.ly для указанного URL.

Например:\
`$ python bitly.py https://www.google.com`\
`Битлинк: https://bit.ly/2N6TtdT`

`$ python bitly.py https://bit.ly/3G07aH3`\
`По вашей ссылке прошли 7 раз(а)`

### Как установить:

1. Клонируйте репозиторий или загрузите программу.
2. Перейдите в каталог, содержащий программу, используя терминал или командную строку.
3. Установите необходимые модули Python с помощью `pip install -r requirements.txt.`
4. Создайте файл .env в том же каталоге и добавьте свой токен API Bit.ly в файл следующим образом: `BITLY_TOKEN=<ваш_токен_здесь>`.

Python3 должен быть уже установлен.\
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Цель проекта:

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).