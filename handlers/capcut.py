import logging
import config
from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)

CAPTION = (
    "📲 *CapCut Latest Version*\n\n"
    "_Having issues? Contact admin._"
)


async def capcut_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    logger.info(
        "Command /capcut | user=%s | chat_id=%s | chat_type=%s",
        getattr(user, "username", "unknown"),
        update.effective_chat.id,
        update.effective_chat.type,
    )

    await update.message.reply_document(
        document=config.CAPCUT_FILE_ID,
        caption=CAPTION,
        parse_mode="Markdown",
    )
