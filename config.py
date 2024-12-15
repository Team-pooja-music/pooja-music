import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID",13404637))
API_HASH = getenv("API_HASH","a069bf02806468fe18427ab6b9a3bb6c")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN","7751992632:AAHPHGL7y-RjCWzvCBTOg2K6pXFtreH5KmI")
# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME","ll_hunter_lll")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME","riyaXmusicbot")
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME")
# ---------------------------------------------------------


# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://theriyamusic94:f67KlgTyzr3TTutn@cluster0.lym5x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1002356335631))

# Get this value from @RIYAXMUSICBOT on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 7425303918))

# make your bots privacy from telegra.ph and put your url here 
PRIVACY_LINK = getenv("PRIVACY_LINK", "https://graph.org/PRIVACY-FOR-TEAM-PURVI-BOTS-09-18")


## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Ksdofficial8/BIT_MUSIC",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/KSD_BOT_NETWORK")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/team_riya_support")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @KsdStringSessionbot on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/ydu29x.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/ka8vh6.jpg"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/ydu29x.jpg"
STATS_IMG_URL = "https://files.catbox.moe/ka8vh6.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/ydu29x.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/ydu29x.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/ydu29x.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/ydu29x.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/ydu29x.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/ydu29x.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/ydu29x.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/ydu29x.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
