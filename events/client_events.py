from telethon import TelegramClient
import configparser
from events.for_all_events.me_file import me
from events.for_all_events.weather_file import weather
from events.only_my_events.add_font_file import add_font
from events.only_my_events.all_fonts_file import all_fonts
from events.only_my_events.logs_file import logs
from events.only_my_events.sel_font_file import sel_font
from events.only_my_events.you_file import you
from events.for_all_events.currency_file import currency
from events.only_my_events.sticker_file import sticker
from events.only_my_events.ban_file import ban
from events.only_my_events.clean_file import clean
from events.for_all_events.help_file import help
from telethon.events import NewMessage

config = configparser.ConfigParser()
config.read('secret_data/config.ini')

api_id = int(config['Telegram']['api_id'])
api_hash = config['Telegram']['api_hash']

client = TelegramClient('me', api_id=api_id, api_hash=api_hash)


@client.on(NewMessage(pattern=r'(?i)(^-me$)',
                      func=lambda event: event.is_private or event.is_group))
async def me_event(event: NewMessage.Event):
    await me(event, client)


@client.on(NewMessage(pattern=r'(?i)(^-weather(\s+\w+){0,2}$)',
                      func=lambda event: event.is_private or event.is_group))
async def weather_event(event: NewMessage.Event):
    await weather(event, client)


@client.on(NewMessage(pattern=r'(?i)(^_you$)',
                      func=lambda event: event.is_private or event.is_group,
                      outgoing=True))
async def you_event(event: NewMessage.Event):
    await you(event, client)


@client.on(NewMessage(pattern=r'(?i)(^-currency$)',
                      func=lambda event: event.is_private or event.is_group))
async def currency_event(event: NewMessage.Event):
    await currency(event, client)


@client.on(NewMessage(pattern=r'(?i)(^_sticker$)',
                      outgoing=True))
async def sticker_event(event: NewMessage.Event):
    await sticker(event, client)


@client.on(NewMessage(pattern=r'(?i)(^_ban$)',
                      func=lambda event: event.is_private,
                      outgoing=True))
async def ban_event(event: NewMessage.Event):
    await ban(event, client)


@client.on(NewMessage(pattern=r'(?i)(^_clean$)',
                      func=lambda event: event.is_private,
                      outgoing=True))
async def clean_event(event: NewMessage.Event):
    await clean(event, client)


@client.on(NewMessage(pattern=r'(?i)(^-help$)',
                      func=lambda event: event.is_private or event.is_group))
async def help_event(event: NewMessage.Event):
    await help(event)


@client.on(NewMessage(pattern=r'(?i)(^_logs$)',
                      func=lambda event: event.is_private or event.is_group,
                      outgoing=True))
async def logs_event(event: NewMessage.Event):
    await logs(event, client)


@client.on(NewMessage(pattern=r'(?i)(^_add_font$)',
                      func=lambda event: event.is_private or event.is_group,
                      outgoing=True))
async def add_font_event(event: NewMessage.Event):
    await add_font(event, client)


@client.on(NewMessage(pattern=r'(?i)(^_all_fonts$)',
                      func=lambda event: event.is_private or event.is_group,
                      outgoing=True))
async def all_fonts_event(event: NewMessage.Event):
    await all_fonts(event)


@client.on(NewMessage(pattern=r'(?i)(^_sel_font)',
                      func=lambda event: event.is_private or event.is_group,
                      outgoing=True))
async def sel_font_event(event: NewMessage.Event):
    await sel_font(event)
