import os


async def me(event, client):
    chat = await event.get_chat()
    sender = await event.get_sender()

    caption = f'<pre>id = {sender.id}</pre>\n' \
              f'<pre>bot = {sender.bot}</pre>\n' \
              f'<pre>premium = {sender.premium}</pre>\n' \
              f'<pre>first name = {sender.first_name}</pre>\n' \
              f'<pre>last name = {sender.last_name}</pre>\n' \
              f'<pre>username = {sender.username}</pre>\n'

    path = 'stickers_data/my_ava.png'
    avatar = await client.download_profile_photo(sender.id, file=path)

    if not avatar:

        await client.send_message(chat, caption, parse_mode='HTML')

    else:
        await client.send_file(chat, avatar, caption=caption, parse_mode='HTML')

    os.remove(path)
