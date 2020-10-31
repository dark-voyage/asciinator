try:
    from os import environ
    from actions import msg, importer
    from pyrogram import Client, filters
except ImportError as err:
    importer("import")
except Exception as err:
    importer("import")

app = Client(
    api_id=environ.get("API_ID"),
    api_hash=environ.get("API_HASH"),
    session_name="main",
    app_version="1.0.3",
    device_model="Geolinda V3.1.3 (Sara Edition)",
    system_version="OSS Linux by Genemator",
    lang_code="en",
    phone_number=environ.get("PHONE"),
    password=environ.get("PASSWORD"),
    parse_mode="html",
    hide_password=True,
    plugins=dict(root="plugins")
)
