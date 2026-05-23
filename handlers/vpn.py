import logging
import config
from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)


async def vpn_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    logger.info(
        "Command /vpn | user=%s | chat_id=%s | chat_type=%s",
        getattr(user, "username", "unknown"),
        update.effective_chat.id,
        update.effective_chat.type,
    )

    text = (
        "🔐 *CapCut VPN*\n\n"
        "Get your VPN to use CapCut without restrictions:\n\n"
        f"👉 [Download VPN]({config.VPN_LINK})\n\n"
        "_Having issues? Contact admin._"
    )

    await update.message.reply_text(text, parse_mode="Markdown")
