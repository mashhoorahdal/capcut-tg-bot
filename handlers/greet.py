import logging
from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)

KEYWORDS = {"vpn", "capcut", "help", "link", "download", "latest"}


async def greet_on_keyword(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message or not update.message.text:
        return

    text_lower = update.message.text.lower()
    if not any(kw in text_lower for kw in KEYWORDS):
        return

    user = update.effective_user
    name = user.first_name if user else "there"

    logger.info(
        "Keyword trigger | user=%s | chat_id=%s",
        getattr(user, "username", "unknown"),
        update.effective_chat.id,
    )

    reply = (
        f"👋 Hi {name}! Need help?\n\n"
        "Use these commands:\n"
        "• /vpn — Get VPN download link\n"
        "• /latest — Get latest CapCut version"
    )

    await update.message.reply_text(reply, parse_mode="Markdown")
