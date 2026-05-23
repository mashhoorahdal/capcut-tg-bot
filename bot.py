import logging
import config  # validates env vars at import — fail fast before doing anything
from telegram.ext import Application, CommandHandler
from handlers.start import start_command
from handlers.vpn import vpn_command
from handlers.latest import latest_command

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def main() -> None:
    logger.info("Starting CapCut VPN Bot...")

    app = Application.builder().token(config.BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("vpn", vpn_command))
    app.add_handler(CommandHandler("latest", latest_command))

    logger.info("Handlers registered. Polling for updates...")
    app.run_polling(allowed_updates=["message"])


if __name__ == "__main__":
    main()
