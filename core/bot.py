try:
    from os import environ
    from pyrogram import Client, filters
except ImportError as Error:
    print("Error occurred while importing:", Error)

app = Client(
    api_id=environ.get("API_ID"),
    api_hash=environ.get("API_HASH"),
    session_name="main",
    app_version="0.0.3",
    device_model="Geolinda V3.1.3 (Sara Edition)",
    system_version="OSS Linux by Genemator",
    lang_code="en",
    phone_number=environ.get("PHONE"),
    password=environ.get("PASSWORD"),
    parse_mode="html",
    hide_password=True,
    plugins=dict(root="plugins")
)

