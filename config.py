from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "24490966"))
API_HASH = getenv("API_HASH", "b4f88272b2258c3824caea93e74c99ef")
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_NAME = getenv("BOT_NAME","NexaMusicBot")
BOT_USERNAME = getenv("BOT_USERNAME", "NexaMusicBot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "SuppieNoodles")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Thesupportchat")
CHANNEL_UPDATES = getenv("CHANNEL_UPDATES", "TheUpdatesChannel")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://graph.org/file/5b4857166fc3f3f07cba8.jpg")
PING_IMG = getenv("PING_IMG", "https://graph.org/file/5b4857166fc3f3f07cba8.jpg")
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5654525889").split()))
