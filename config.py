import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")
CAPCUT_FILE_ID: str = os.getenv("CAPCUT_FILE_ID", "")
WEBHOOK_SECRET: str = os.getenv("WEBHOOK_SECRET", "")
WEBHOOK_URL: str = os.getenv("WEBHOOK_URL", "")


def validate() -> None:
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN is not set. Add it to your .env file.")
    if not CAPCUT_FILE_ID:
        raise ValueError("CAPCUT_FILE_ID is not set. Add it to your .env file.")
