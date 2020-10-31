from time import sleep
from pyrogram import Client, filters
from pyrogram.errors import FloodWait


@Client.on_message(filters.command("type", prefixes=".") & filters.me)
def typer(client, message):
    orig_text = message.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = ""  # to be printed
    typing_symbol = "▒"

    while tbp != orig_text:
        try:
            message.edit(tbp + typing_symbol)
            sleep(0.05)  # 50 ms

            tbp = tbp + text[0]
            text = text[1:]

            message.edit(tbp)
            sleep(0.05)

        except FloodWait as e:
            sleep(e.x)
