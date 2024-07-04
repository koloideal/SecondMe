from telethon.tl.functions.contacts import BlockRequest
from telethon.events import NewMessage


async def ban(event: NewMessage.Event, client):

    chat = await event.get_chat()

    try:
        await client(BlockRequest(chat.id))
        await event.message.delete()
        await client.send_message(chat, '<code>block</code>', parse_mode='HTML')
    except Exception as e:
        await client.send_message(chat, f'<code>error:</code><pre>{e}</pre>', parse_mode='HTML')
