# SecondMe

**SecondMe** - это юзербот на Python, расширяющий функционал и упрощающий функционал Telegram.

## Требования
- Учетная запись Telegram с полученными API-ключами (API_ID, API_HASH)
- Установленные зависимости, указанные в файле requirements.txt 
```
pip install -r requirements.txt
```

## Установка и настройка
- Склонируйте репозиторий
- Перед запуском юзербота создайте папку внутри репозитория с навзванием `secret_data`, в неё создайте файл `config.ini` с ключами и токенами
- config.ini должен иметь следующий вид:
```
[OpenWeather]
openweather_api_key=YOUR_API_KEY

[Telegram]
api_id=YOUR_API_ID
api_hash=YOUR_API_HASH

[System]
path_to_font=PATH_TO_FONT
```
- где api_id и api_hash - ваши Telegram API ключи(более подробная информация в интернете), openweather_api_key - ваш идентификатор, полученны с портала openweather, path_to_font - путь до шрифта, который будет использоваться при создании стикеров.
- установить зависмости консольной командой:
```
pip install -r requirements.txt
```

## Особенности использования
- Основной функционал юзербота:

  Users commands
  -help -- get help about commands
  -currency -- get actually information about currencies
  -me -- get information about you in Telegram
  -weather <city name> -- get information about weather
  Creators commands
  _ban -- block user in private chat
  _clean -- remove history in private chat
  _sticker -- make sticker from reply message
  _you -- get information about user in private chat
  

**Юзербот находится на стадии альфа-теста, поэтому баги и ошибки вполне вероятны и ожидаемы, в случае нахождения такого просьба скинуть скрины переписки с ботом в Telegram - <a href="https://t.me/kolo_id">@kolo_id<a>**


**Примечание:** Использование данного бота может быть ограничено правилами и политикой Telegram. Пожалуйста, убедитесь, что соблюдаете все правила Telegram при использовании этого бота.

