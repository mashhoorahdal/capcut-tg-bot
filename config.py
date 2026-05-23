import os
from dotenv import load_dotenv


def _load_config() -> tuple[str, str, str]:
    load_dotenv()
    bot_token = os.getenv("BOT_TOKEN", "")
    vpn_link = os.getenv("VPN_LINK", "")
    capcut_latest_link = os.getenv("CAPCUT_LATEST_LINK", "")

    if not bot_token:
        raise ValueError("BOT_TOKEN is not set. Add it to your .env file.")
    if not vpn_link:
        raise ValueError("VPN_LINK is not set. Add it to your .env file.")
    if not capcut_latest_link:
        raise ValueError("CAPCUT_LATEST_LINK is not set. Add it to your .env file.")

    return bot_token, vpn_link, capcut_latest_link


BOT_TOKEN, VPN_LINK, CAPCUT_LATEST_LINK = _load_config()
