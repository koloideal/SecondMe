from telethon.events import NewMessage
from telethon import TelegramClient


async def add_font(event: NewMessage.Event, client: TelegramClient):

    if event.is_reply:

        replied_msg = await event.get_reply_message()

        document_name = replied_msg.media.document.attributes[0].file_name

        if (replied_msg.media is not None) and document_name[-4:] == '.ttf':

            try:

                await client.download_media(message=replied_msg, file='fonts')

            except Exception as e:

                await event.reply(f'<code>Error</code><pre>{e}</pre>', parse_mode='HTML')

            else:

                await event.reply('<code>Successfully added new font</code>', parse_mode='HTML')

        else:

            await event.reply('<code>Usage: [reply to a font file]</code>', parse_mode='HTML')

    else:

        await event.reply('<code>Usage: [reply to a font file]</code>', parse_mode='HTML')
