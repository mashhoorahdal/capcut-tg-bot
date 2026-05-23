import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")
VPN_LINK: str = os.getenv("VPN_LINK", "")
CAPCUT_LATEST_LINK: str = os.getenv("CAPCUT_LATEST_LINK", "")
WEBHOOK_SECRET: str = os.getenv("WEBHOOK_SECRET", "")
WEBHOOK_URL: str = os.getenv("WEBHOOK_URL", "")


def validate() -> None:
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN is not set. Add it to your .env file.")
    if not VPN_LINK:
        raise ValueError("VPN_LINK is not set. Add it to your .env file.")
    if not CAPCUT_LATEST_LINK:
        raise ValueError("CAPCUT_LATEST_LINK is not set. Add it to your .env file.")
