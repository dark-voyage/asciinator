from core import app
from time import sleep
from pyrogram import errors


def launcher():
    try:
        app.run()
    except errors.FloodWait as err:
        sleep(10)