from pyrogram import Client, filters


@Client.on_message(filters.text & filters.private)
async def watcher(client, message):
    await message.reply(
        "<b>Howdy? Look, I'm user bot which was</b> " +
        "<b>created by Genemator... Please, contact with him ;)</b> @genemator")
