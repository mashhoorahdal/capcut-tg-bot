import logging
from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)

REPLY = "👋 Send /capcut to get the CapCut file."


async def greet_on_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message or not update.message.text:
        return

    user = update.effective_user
    logger.info(
        "Greeting | user=%s | chat_id=%s | chat_type=%s",
        getattr(user, "username", "unknown"),
        update.effective_chat.id,
        update.effective_chat.type,
    )

    await update.message.reply_text(REPLY)
