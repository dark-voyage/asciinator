from core import app
from pyrogram import Client, filters


@Client.on_message(filters.command("session", prefixes="$") & filters.me)
async def session(client, message):
    await message.reply(
        f"<b>Session string:</b>\n<code>{await app.export_session_string()}</code>")
