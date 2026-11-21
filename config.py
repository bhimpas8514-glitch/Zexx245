import os

API_ID = int(os.getenv("API_ID", "38138069"))
API_HASH = os.getenv("API_HASH", "2ed313ebcc45cbcf65d1fc736ec71681")
OWNER_ID = int(os.getenv("OWNER_ID", "8687845229"))

# Bot Token (@BotFather se mila hua token)
BOT_TOKEN = os.getenv(
    "BOT_TOKEN", "9075346019:AAHkAcG2KJD2cKHVfLfcx2ZpVDftmebDYtA"
)

# Start Image URL
START_IMG = os.getenv("START_IMG", "https://files.catbox.moe/nlluhz.jpg")

SESSION_DIR = "sessions"
os.makedirs(SESSION_DIR, exist_ok=True)
