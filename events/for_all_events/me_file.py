async def me(event, client):

    chat = await event.get_chat()
    sender = await event.get_sender()

    await client.send_message(chat, f'<pre>id = {sender.id}</pre>\n'
                                    f'<pre>bot = {sender.bot}</pre>\n'
                                    f'<pre>premium = {sender.premium}</pre>\n'
                                    f'<pre>first name = {sender.first_name}</pre>\n'
                                    f'<pre>last name = {sender.last_name}</pre>\n'
                                    f'<pre>username = {sender.username}</pre>\n', parse_mode='HTML')
