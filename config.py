from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "24946423"
# -------------------------------------------------------------
API_HASH = "30ba9fa7064625f3d952b8adb75f636c"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
STRING1 = getenv("STRING_SESSION", None)
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "1808943146"))
SUPPORT_GRP = "stickers_Channell"
UPDATE_CHNL = "FRIENDS_ZONE_GP"
OWNER_USERNAME = ""
