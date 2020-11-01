from time import sleep
from pyrogram import Client, filters


@Client.on_message(filters.command("d", prefixes=".") & filters.me)
async def downloader(client, message):
    async def progress(current, total):
        counter = f"{current * 100 / total:.0f}"
        # bar = "#" * int(starter) + " " * int(10 - int(starter))
        await message.edit(
            f"<b>Uploading:</b> <code>{counter}%</code>\n<b>Identifier:</b> <code>[]</code>")
        sleep(1)
    file = open(message.text.split(".d ", maxsplit=1)[1], "rb")
    await client.send_document(message.chat.id, file, progress=progress, force_document=True, caption="<b>Completed!</b>")
    await message.delete()
