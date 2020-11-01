from time import sleep
from pyrogram import Client, filters
from pyrogram.errors import FloodWait


@Client.on_message(filters.command("tp", prefixes=".") & filters.me)
async def typer(client, message):
    original_text = message.text.split(".tp ", maxsplit=1)[1]
    text = original_text
    printing = ""  # to be printed
    typing_symbol = "▒"

    while printing != original_text:
        try:
            await message.edit(printing + typing_symbol)
            sleep(0.05)

            printing = printing + text[0]
            text = text[1:]

            await message.edit(printing)
            sleep(0.05)

        except FloodWait as e:
            sleep(e.x)
