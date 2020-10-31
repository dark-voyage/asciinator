import random
from time import sleep
from pyrogram import Client, filters
from pyrogram.errors import FloodWait


@Client.on_message(filters.command("hack", prefixes="$") & filters.me)
async def hack(client, message):
    loader = 0

    while loader < 100:
        try:
            text = "👮‍ Hacking Intranet ..." + str(loader) + "%"
            await message.edit(text)

            loader += random.randint(1, 3)
            sleep(0.1)

        except FloodWait as e:
            sleep(e.x)

    await message.edit("🟢 Successfully gained access!")
    sleep(3)

    await message.edit("👽 Searching for ready cws from Intranet ...")
    sleep(3)

    loader = 0

    while loader < 100:
        try:
            text = "👽 Searching for ready cws ..." + str(loader) + "%"
            await message.edit(text)

            loader += random.randint(1, 5)
            sleep(0.15)

        except FloodWait as e:
            sleep(e.x)

    await message.edit("😎 Relax it's just a joke...")
