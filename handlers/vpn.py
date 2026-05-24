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

    backup_line = (
        f"🔗 [Backup link]({config.VPN_BACKUP_LINK})\n\n"
        if config.VPN_BACKUP_LINK
        else "\n"
    )
    text = (
        "🔐 *Free VPN*\n\n"
        "100% free — no ads, no speed limits, unlimited bandwidth.\n"
        "Access 50+ regions with stable connection.\n\n"
        f"👉 [Download here]({config.VPN_LINK})\n"
        f"{backup_line}"
        "_Chrome recommended for best experience._"
    )

    await update.message.reply_text(text, parse_mode="Markdown")
