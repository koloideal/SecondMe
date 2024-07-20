import os
from telethon.events import NewMessage


async def all_fonts(event: NewMessage.Event) -> None:

    path: str = 'fonts/'

    all_fonts_files = os.listdir(path)

    if all_fonts_files:

        all_fonts_files = '\n\n'.join([f'<code>{x}</code>' for x in all_fonts_files])

        await event.reply(all_fonts_files, parse_mode='HTML')

    else:

        await event.reply('<code>No fonts found</code>', parse_mode='HTML')
