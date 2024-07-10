import html
from telethon.events import NewMessage


async def help(event: NewMessage.Event):

    await event.reply('<code>Users commands</code>'
                      '<pre><code>-help</code> -- get help about commands</pre>'
                      '<pre><code>-currency</code> -- get actually information about currencies</pre>'
                      '<pre><code>-me</code> -- get information about you in Telegram</pre>'
                      f'<pre><code>-weather {html.escape("<city name>")}</code> -- get information about weather</pre>'
                      f'<code>Creators commands</code>'
                      f'<pre><code>_ban</code> -- block user in private chat</pre>'
                      f'<pre><code>_clean</code> -- remove history in private chat</pre>'
                      f'<pre><code>_sticker</code> -- make sticker from reply message</pre>'
                      f'<pre><code>_you</code> -- get information about user in private chat</pre>',
                      parse_mode='HTML', reply_to=event.message)
