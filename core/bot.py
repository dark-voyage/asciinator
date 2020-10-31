try:
    from pyrogram import Client, filters
except ImportError as Error:
    print("Error occurred while importing:", Error)

app = Client(
    session_name="main",
    app_version="0.0.3",
    device_model="OSS Linux by Genemator",
    system_version="Geolinda V3.1.3 (Sara Edition)",
    lang_code="en",
    parse_mode="html",
    config_file="./config.ini",
    hide_password=True,
    plugins=dict(root="plugins")
)

