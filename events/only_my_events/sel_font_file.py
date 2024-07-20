import os
from telethon.events import NewMessage
from telethon import TelegramClient
from configparser import ConfigParser


async def sel_font(event: NewMessage.Event) -> None:

    config = ConfigParser()
    config.read('secret_data/config.ini')

    path: str = 'fonts/'

    all_fonts_files = os.listdir(path)

    if event.is_reply:

        replied_msg = await event.get_reply_message()

        if replied_msg.text is not None:

            if replied_msg.text.strip() in all_fonts_files:

                config.set('System', 'path_to_font', path + replied_msg.text.strip())

                with open('secret_data/config.ini', 'w') as configfile:

                    config.write(configfile)

                await event.reply('<code>Successful change font</code>', parse_mode='HTML')

            else:

                await event.reply('<code>Invalid font name</code>', parse_mode='HTML')

        else:

            await event.reply('<code>Usage: [reply to a font name]</code>', parse_mode='HTML')

    else:

        await event.reply('<code>Usage: [reply to a font name]</code>', parse_mode='HTML')
