import os
from dotenv import load_dotenv


def _load_config() -> tuple[str, str]:
    load_dotenv()
    bot_token = os.getenv("BOT_TOKEN", "")
    vpn_link = os.getenv("VPN_LINK", "")

    if not bot_token:
        raise ValueError("BOT_TOKEN is not set. Add it to your .env file.")
    if not vpn_link:
        raise ValueError("VPN_LINK is not set. Add it to your .env file.")

    return bot_token, vpn_link


BOT_TOKEN, VPN_LINK = _load_config()
