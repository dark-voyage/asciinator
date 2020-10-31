from pyrogram import Client, filters


@Client.on_message(filters.text & filters.private)
async def watcher(client, message):
    await message.reply(
        "<b>Currently, Genemator is busy with works...</b>\n" +
        "<i>Can you write little bit later?</i>")
