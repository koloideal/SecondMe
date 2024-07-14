from telethon.tl.types import InputStickerSetItem, InputDocument, InputStickerSetID
from telethon.tl.functions.messages import UploadMediaRequest, GetStickerSetRequest, GetAllStickersRequest
from telethon.tl.functions.stickers import AddStickerToSetRequest
from telethon.tl.types import InputMediaUploadedDocument, DocumentAttributeFilename
from PIL import Image, ImageDraw, ImageFont
import os
from telethon import TelegramClient, events
from configparser import ConfigParser


config = ConfigParser()
config.read('secret_data/config.ini')

path_to_font = config['System']['path_to_font']


def size_font(len_text):

    max_font_size = 64
    coef = 1.5
    font_size = int(max_font_size - coef * len_text)

    return max(12, font_size)


def create_image_with_text(avatar_path, text, output_path):

    width = 512
    height = 128

    img = Image.new('RGBA', (width, height), (24, 27, 34, 255))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(path_to_font, size_font(len(text)))

    avatar = Image.open(avatar_path).resize((height, height)).convert("RGBA")
    mask = Image.new("L", (height, height), 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.ellipse((0, 0, height, height), fill=255)
    avatar.putalpha(mask)

    img.paste(avatar, (20, 0), avatar)

    draw.text((160, 30), text, font=font, fill=(255, 255, 255, 255))

    img.save(output_path)


async def sticker(event: events, client: TelegramClient):

    if event.is_reply:

        chat = await event.get_chat()

        topic_id = await event.get_reply_message()

        topic_id = topic_id.reply_to_msg_id

        replied_msg = await event.get_reply_message()

        if replied_msg.text:

            if len(replied_msg.text) < 4 or len(replied_msg.text) > 20:

                await event.reply('<code>The message should be 4 < len < 20 characters</code>', parse_mode='HTML')

                return

            in_progress = await event.reply('In progress...')

            user = await client.get_entity(replied_msg.sender_id)
            avatar = await client.download_profile_photo(user, file=bytes)

            if not avatar:

                await in_progress.delete()

                await event.reply('<code>User must have an avatar</code>', parse_mode='HTML')

                return

            text = replied_msg.text

            avatar_path = 'stickers_data/avatar.png'
            with open(avatar_path, 'wb') as f:
                f.write(avatar)

            output_path = 'stickers_data/sticker.png'
            create_image_with_text(avatar_path, text, output_path)

            file = await client.upload_file(output_path)
            uploaded_media = await client(UploadMediaRequest(
                peer=await event.get_input_chat(),
                media=InputMediaUploadedDocument(
                    file=file,
                    mime_type='image/png',
                    attributes=[DocumentAttributeFilename('sticker_data/sticker.png')]
                )
            ))

            document = uploaded_media.document

            sticker_item = InputStickerSetItem(
                document=InputDocument(
                    id=document.id,
                    access_hash=document.access_hash,
                    file_reference=document.file_reference
                ),
                emoji="🙂"
            )

            sticker_sets = await client(GetAllStickersRequest(0))
            sticker_set = [x for x in sticker_sets.sets if x.title == 'kolo set'][0]

            await client(AddStickerToSetRequest(
                stickerset=InputStickerSetID(
                    id=sticker_set.id,
                    access_hash=sticker_set.access_hash),
                sticker=sticker_item
            ))

            stickers = await client(GetStickerSetRequest(
                stickerset=InputStickerSetID(
                    id=sticker_set.id, access_hash=sticker_set.access_hash
                ), hash=0
            ))

            os.remove(avatar_path)
            os.remove(output_path)

            await client.send_file(chat, stickers.documents[-1], reply_to=topic_id)

            await in_progress.delete()

        else:
            await event.reply('<code>Usage: [reply to a text message]</code>', parse_mode='HTML')
    else:
        await event.reply('<code>Usage: [reply to a text message]</code>', parse_mode='HTML')
