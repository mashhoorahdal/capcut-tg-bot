import logging
from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    name = user.first_name if user else "there"

    logger.info(
        "Command /start | user=%s | chat_id=%s | chat_type=%s",
        getattr(user, "username", "unknown"),
        update.effective_chat.id,
        update.effective_chat.type,
    )

    text = (
        f"👋 Hi {name}! Welcome to *CapCut VPN Bot*.\n\n"
        "I help you get a VPN so CapCut works without restrictions.\n\n"
        "Use /vpn to get the download link."
    )

    await update.message.reply_text(text, parse_mode="Markdown")
