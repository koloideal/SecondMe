from datetime import datetime
from telethon.events import NewMessage
from telethon import TelegramClient


async def logs(event: NewMessage.Event, client: TelegramClient) -> None:

    chat = await event.get_chat()

    file: str = 'secret_data/logs.txt'

    caption: str = f'before {datetime.now().strftime("%d-%m-%Y")}'

    await client.send_file(chat, file=file, caption=caption, reply_to=event.message)
