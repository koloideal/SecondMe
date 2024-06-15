async def you(event, client):

    chat = await event.get_chat()

    await client.send_message(chat, f'<pre>id = {chat.id}</pre>\n'
                                    f'<pre>bot = {chat.bot}</pre>\n'
                                    f'<pre>premium = {chat.premium}</pre>\n'
                                    f'<pre>first name = {chat.first_name}</pre>\n'
                                    f'<pre>last name = {chat.last_name}</pre>\n'
                                    f'<pre>username = {chat.username}</pre>\n', parse_mode='HTML')
