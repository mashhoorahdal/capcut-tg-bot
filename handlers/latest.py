import logging
import config
from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)


async def latest_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    logger.info(
        "Command /latest | user=%s | chat_id=%s | chat_type=%s",
        getattr(user, "username", "unknown"),
        update.effective_chat.id,
        update.effective_chat.type,
    )

    text = (
        "📲 *CapCut Latest Version*\n\n"
        "Download the latest CapCut version here:\n\n"
        f"👉 [Download CapCut]({config.CAPCUT_LATEST_LINK})\n\n"
        "_Having issues? Contact admin._"
    )

    await update.message.reply_text(text, parse_mode="Markdown")
