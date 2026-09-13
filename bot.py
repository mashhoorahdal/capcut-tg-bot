import logging
import config
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from handlers.capcut import capcut_command
from handlers.greet import greet_on_message

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def main() -> None:
    config.validate()
    logger.info("Starting CapCut Bot...")

    app = Application.builder().token(config.BOT_TOKEN).build()
    app.add_handler(CommandHandler("capcut", capcut_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, greet_on_message))

    logger.info("Handlers registered. Polling for updates...")
    app.run_polling(allowed_updates=["message"])


if __name__ == "__main__":
    main()
