from pyrogram import Client, filters


@Client.on_message(filters.text & filters.private, group=1)
async def echo_reversed(client, message):
    await message.reply(message.text[::-1])
