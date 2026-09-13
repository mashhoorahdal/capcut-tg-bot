import logging
import config
from telegram.ext import Application, CommandHandler
from handlers.capcut import capcut_command

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

    logger.info("Handlers registered. Polling for updates...")
    app.run_polling(allowed_updates=["message"])


if __name__ == "__main__":
    main()
