from subprocess import run, STDOUT, PIPE
from pyrogram import Client, filters


@Client.on_message(filters.command("terminal", prefixes=".") & filters.me)
async def watcher(client, message):
    command = message.text.split(".terminal ", maxsplit=1)[1]
    terminal = str(run(['powershell', command], capture_output=True, shell=True, cwd="C:\\Users\\Genemator").stdout)
    output = terminal.replace("\\n", "\n")[2:-1]
    await message.edit(f"<pre>{output}</pre>")
