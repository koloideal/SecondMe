from telethon import TelegramClient
from telethon.events import NewMessage


async def clean(event: NewMessage.Event, client: TelegramClient):

    chat = await event.get_chat()

    try:
        messages = await client.get_messages(chat, limit=None)
        await client.delete_messages(chat, message_ids=messages)
        await client.send_message(chat, '<code>clean</code>', parse_mode='HTML')
    except Exception as e:
        await client.send_message(chat, f'<code>error:</code><pre>{e}</pre>', parse_mode='HTML')
