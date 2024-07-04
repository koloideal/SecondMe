import os


async def you(event, client):
    chat = await event.get_chat()

    caption = f'<pre>id = {chat.id}</pre>\n' \
              f'<pre>bot = {chat.bot}</pre>\n' \
              f'<pre>premium = {chat.premium}</pre>\n' \
              f'<pre>first name = {chat.first_name}</pre>\n' \
              f'<pre>last name = {chat.last_name}</pre>\n' \
              f'<pre>username = {chat.username}</pre>\n'

    path = 'stickers_data/your_ava.png'
    avatar = await client.download_profile_photo(chat.id, file=path)

    if not avatar:

        await client.send_message(chat, caption, parse_mode='HTML')

    else:
        await client.send_file(chat, avatar, caption=caption, parse_mode='HTML')

    os.remove(path)
