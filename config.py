import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Required
API_ID = 26950458
API_HASH = "d818b8d530e4a9b209509815ab1b9c7c"
BOT_TOKEN = "8023030133:AAGlaP-jDQQ3fVYMui10qyIsIfwZMSiSkPE"
MONGO_DB_URI = "mongodb+srv://knight4563:knight4563@cluster0.a5br0se.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# LOGGER_ID: Directly hardcoded to avoid ValueError
LOGGER_ID = -1002881142866
OWNER_ID = 7926944005

# Optional/Extra
OWNER_USERNAME = getenv("OWNER_USERNAME", "ll_KUZE_ll")
BOT_USERNAME = getenv("BOT_USERNAME", "Gojo_X_Jinwoo_bot")
BOT_NAME = getenv("BOT_NAME", "LOVER MUSIC")
ASSUSERNAME = getenv("ASSUSERNAME", "LOVER_ASS")
EVALOP = [7926944005]

DURATION_LIMIT_MIN = 10000

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = "https://github.com/code663/DAXXMUSIC"
UPSTREAM_BRANCH = "Master"
GIT_TOKEN = None

SUPPORT_CHANNEL = "https://t.me/dark_x_knight_musiczz_support"
SUPPORT_CHAT = "https://t.me/+DbezTihsh_VlYzY1"

AUTO_LEAVING_ASSISTANT = False

SPOTIFY_CLIENT_ID = "1c21247d714244ddbb09925dac565aed"
SPOTIFY_CLIENT_SECRET = "709e1a2969664491b58200860623ef19"

PLAYLIST_FETCH_LIMIT = 100
TG_AUDIO_FILESIZE_LIMIT = 104857600  # 100 MB
TG_VIDEO_FILESIZE_LIMIT = 1073741824  # 1 GB

# Session string
STRING1 = "BQGbOzoABb-Ci3xqFpROac8kpohBmaAvXVwbH5CKeIq8_IehpzlXoDbCHey7YwojZCSXb2HTFsap-xVhRQoj43dnPAvpkt7UoB5JGjQ0mPwWkNvIfGY2l4EyLJLGP59UcphMuzJwUOoHbPuTNUilCXaQptDj_uaaiSbq96v5yLR3evWZRhmMRw0FtzAWVzlsxhHJp2NdOuyg9KRXgNkGuf8r62YhHXKiH5-YoxBNrqVfDp24kQVdaT1zK4ByNF0f8DqQTjvqktVU2_eEtviSWTsrUjvDha8UF1_bfY3UqSENeDcNA0RX1MzAQbncwb1NA6QJ7ujMtXZYwcqDKIiPTWu3T_c3EAAAAAGsmbxnAA"
STRING2 = STRING3 = STRING4 = STRING5 = None

# Bot internal structures
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# Image URLs
START_IMG_URL = "https://telegra.ph/file/982b01ba53c3d69b0d0ce.jpg"
PING_IMG_URL = "https://telegra.ph/file/29bf663a3b91c7e0086bc.jpg"
PLAYLIST_IMG_URL = "https://telegra.ph/file/982b01ba53c3d69b0d0ce.jpg"
STATS_IMG_URL = "https://telegra.ph/file/2abd798099b17a5a9b2fb.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/590f5404cdc7840b63a1c.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/590f5404cdc7840b63a1c.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/982b01ba53c3d69b0d0ce.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/590f5404cdc7840b63a1c.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/5eb646ee0bf810113af22.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/61024698bfc926e95d57a.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/61024698bfc926e95d57a.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/61024698bfc926e95d57a.jpg"

# Duration limit calculator
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")

# URL validations
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit("[ERROR] - SUPPORT_CHANNEL url must start with https://")

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit("[ERROR] - SUPPORT_CHAT url must start with https://")

# Optional Debug
print(f"[DEBUG] LOGGER_ID = {LOGGER_ID} (type: {type(LOGGER_ID)})")