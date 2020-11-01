from subprocess import run, STDOUT, PIPE
from pyrogram import Client, filters


@Client.on_message(filters.command("t", prefixes=".") & filters.me)
async def watcher(client, message):
    command = message.text.split(".t ", maxsplit=1)[1]
    terminal = str(run(['powershell', command], capture_output=True, shell=True).stdout)
    output = terminal.replace("\\n", "\n").replace("\\r", "").replace("\\\\", "\\")[2:-1]
    await message.edit(f"<pre>{output}</pre>")
