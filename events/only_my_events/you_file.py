import os
from telethon.events import NewMessage
from telethon import TelegramClient


async def you(event: NewMessage.Event, client: TelegramClient):

    chat = await event.get_chat()

    path = 'stickers_data/your_ava.png'

    if event.is_private:

        caption = f'<pre>id = {chat.id}</pre>\n' \
                  f'<pre>bot = {chat.bot}</pre>\n' \
                  f'<pre>premium = {chat.premium}</pre>\n' \
                  f'<pre>first name = {chat.first_name}</pre>\n' \
                  f'<pre>last name = {chat.last_name}</pre>\n' \
                  f'<pre>username = {chat.username}</pre>\n'

        avatar = await client.download_profile_photo(chat.id, file=path)

        if not avatar:

            await client.send_message(chat, caption, parse_mode='HTML', reply_to=event.message)

        else:
            await client.send_file(chat, avatar, caption=caption, parse_mode='HTML', reply_to=event.message)

        os.remove(path)

    else:

        reply_msg = await event.get_reply_message()

        user_entity = await client.get_entity(reply_msg.sender_id)

        caption = f'<pre>id = {user_entity.id}</pre>\n' \
                  f'<pre>bot = {user_entity.bot}</pre>\n' \
                  f'<pre>premium = {user_entity.premium}</pre>\n' \
                  f'<pre>first name = {user_entity.first_name}</pre>\n' \
                  f'<pre>last name = {user_entity.last_name}</pre>\n' \
                  f'<pre>username = {user_entity.username}</pre>\n'

        avatar = await client.download_profile_photo(user_entity.id, file=path)

        if not avatar:

            await client.send_message(chat, caption, parse_mode='HTML', reply_to=event.message)

        else:
            await client.send_file(chat, avatar, caption=caption, parse_mode='HTML', reply_to=event.message)

        os.remove(path)
