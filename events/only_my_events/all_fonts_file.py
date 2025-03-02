import os
from telethon.events import NewMessage
from configparser import ConfigParser


async def all_fonts(event: NewMessage.Event) -> None:
    path: str = "fonts/"

    all_fonts_files = os.listdir(path)

    config = ConfigParser()
    config.read("secret_data/config.ini")

    now_font = config["System"]["path_to_font"]

    if all_fonts_files:
        all_fonts_files = "\n\n".join([f"<code>{x}</code>" for x in all_fonts_files])

        await event.reply(
            f"<pre>Now font:</pre>{now_font}\n\n<pre>All Fonts:</pre>{all_fonts_files}",
            parse_mode="HTML",
        )

    else:
        await event.reply("<code>No fonts found</code>", parse_mode="HTML")
