from telethon import events, TelegramClient
import configparser
from events.for_all_events.me_file import me
from events.for_all_events.weather_file import weather
from events.only_my_events.you_file import you
from events.for_all_events.currency_file import currency
from events.only_my_events.sticker_file import sticker
from events.only_my_events.ban_file import ban
from events.only_my_events.clean_file import clean


config = configparser.ConfigParser()
config.read('secret_data/config.ini')

api_id = int(config['Telegram']['api_id'])
api_hash = config['Telegram']['api_hash']


client = TelegramClient('me', api_id=api_id, api_hash=api_hash)


@client.on(events.NewMessage(pattern=r'(?i)(^-me$)',
                             func=lambda event: event.is_private or event.is_group))
async def me_event(event):

    await me(event, client)


@client.on(events.NewMessage(pattern=r'(?i)(^-weather(\s+\w+){0,2}$)',
                             func=lambda event: event.is_private or event.is_group))
async def weather_event(event):

    await weather(event, client)


@client.on(events.NewMessage(pattern=r'(?i)(^_you$)',
                             func=lambda event: event.is_private,
                             outgoing=True))
async def you_event(event):

    await you(event, client)


@client.on(events.NewMessage(pattern=r'(?i)(^-currency$)',
                             func=lambda event: event.is_private or event.is_group))
async def currency_event(event):

    await currency(event, client)


@client.on(events.NewMessage(pattern=r'(?i)(^_sticker$)',
                             outgoing=True))
async def sticker_event(event):

    await sticker(event, client)


@client.on(events.NewMessage(pattern=r'(?i)(^_ban$)',
                             func=lambda event: event.is_private,
                             outgoing=True))
async def ban_event(event):

    await ban(event, client)


@client.on(events.NewMessage(pattern=r'(?i)(^_clean$)',
                             func=lambda event: event.is_private,
                             outgoing=True))
async def clean_event(event):

    await clean(event, client)
