try:
    from pyrogram import Client, filters
except ImportError as Error:
    print("Error occurred while importing:", Error)

plugins = dict(root="plugins")

app = Client(
    session_name="main",
    app_version="0.0.3",
    device_model="Geolinda V3.1.3 (Sara Edition)",
    system_version="OSS Linux by Genemator",
    lang_code="en",
    phone_number="+998998711546",
    password="Mogulkahn2001",
    parse_mode="html",
    config_file="./config.ini",
    hide_password=True,
    plugins=plugins
)

