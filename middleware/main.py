from core import app
from pyrogram import filters


async def handler():
    @app.on_message(filters.private)
    async def handlers(client, message):
        await message.reply_text(message)
    pass
