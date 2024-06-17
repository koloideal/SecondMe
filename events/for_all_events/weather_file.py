import configparser
import requests

config = configparser.ConfigParser()
config.read('secret_data/config.ini')

api_key = config['OpenWeather']['openweather_api_key']


async def weather(event, client):

    chat = await event.get_chat()

    if len(event.message.text.split()) == 1:

        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=Minsk&appid={api_key}&units=metric')

    else:

        city = ' '.join(event.message.text.split()[1:])

        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric')

    if response.status_code == 200:

        json = response.json()

        await client.send_message(chat, f'<pre>name: {json["name"]}</pre>\n'
                                        f'<pre>temp: {json["main"]["temp"]}C</pre>\n'
                                        f'<pre>temp feels like: {json["main"]["feels_like"]}C</pre>\n'
                                        f'<pre>pressure: {json["main"]["pressure"]}mm</pre>\n'
                                        f'<pre>humidity: {json["main"]["humidity"]}%</pre>\n'
                                        f'<pre>wind: {json["wind"]["speed"]}km/h</pre>\n', parse_mode='HTML')

    else:

        await client.send_message(chat, '<pre>Invalid city</pre>', parse_mode='HTML')
