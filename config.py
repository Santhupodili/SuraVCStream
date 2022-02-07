import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
MONGODB_URL = getenv("MONGODB_URL")
OWNER_NAME = getenv("OWNER_NAME")
ALIVE_NAME = getenv("ALIVE_NAME")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "santhuvc")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "santhubotupadates")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/38deca938d96e9d207b27.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/38deca938d96e9d207b27.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/b8e149a1c5ec867b244f0.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d54e875e74c71681b5f22.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/79b758a233448de919c1c.jpg")
