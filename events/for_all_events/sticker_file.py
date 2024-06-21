from telethon.tl.types import InputStickerSetItem, InputDocument, InputStickerSetID, InputStickerSetShortName
from telethon.tl.functions.messages import UploadMediaRequest, GetStickerSetRequest, GetAllStickersRequest
from telethon.tl.functions.stickers import CreateStickerSetRequest, AddStickerToSetRequest
from telethon.tl.types import InputMediaUploadedDocument, DocumentAttributeFilename
from PIL import Image, ImageDraw, ImageFont
import os
from telethon import TelegramClient


def create_image_with_text(avatar_path, text, output_path):

    width = 512
    height = 128

    img = Image.new('RGBA', (width, height), (24, 27, 34, 255))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 37)

    avatar = Image.open(avatar_path).resize((height, height)).convert("RGBA")
    mask = Image.new("L", (height, height), 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.ellipse((0, 0, height, height), fill=255)
    avatar.putalpha(mask)

    img.paste(avatar, (20, 0), avatar)

    draw.text((160, 40), text, font=font, fill=(255, 255, 255, 255))

    img.save(output_path)


async def sticker(event, client: TelegramClient):
    chat = await event.get_chat()

    if event.is_reply:

        replied_msg = await event.get_reply_message()

        if replied_msg.text:

            in_progress = await event.reply('In progress...')

            user = await client.get_entity(replied_msg.sender_id)
            avatar = await client.download_profile_photo(user, file=bytes)
            text = replied_msg.text

            avatar_path = 'avatar.png'
            with open(avatar_path, 'wb') as f:
                f.write(avatar)

            output_path = 'sticker.png'
            create_image_with_text(avatar_path, text, output_path)

            file = await client.upload_file(output_path)
            uploaded_media = await client(UploadMediaRequest(
                peer=await event.get_input_chat(),
                media=InputMediaUploadedDocument(
                    file=file,
                    mime_type='image/png',
                    attributes=[DocumentAttributeFilename('sticker.png')]
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

            await client.send_file(chat, stickers.documents[-1])

            await in_progress.delete()

        else:
            await event.reply('Пожалуйста, ответьте на текстовое сообщение.')
    else:
        await event.reply('Пожалуйста, ответьте на текстовое сообщение.')
