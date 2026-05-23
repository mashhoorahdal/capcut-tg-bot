import asyncio
import json
import logging
import os
import sys
from http.server import BaseHTTPRequestHandler

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import config
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler

from handlers.latest import latest_command
from handlers.start import start_command
from handlers.vpn import vpn_command

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


async def _process_update(update_data: dict) -> None:
    app = Application.builder().token(config.BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("vpn", vpn_command))
    app.add_handler(CommandHandler("latest", latest_command))
    async with app:
        await app.process_update(Update.de_json(update_data, app.bot))


async def _register_webhook() -> str:
    webhook_url = f"{config.WEBHOOK_URL}/webhook"
    async with Bot(token=config.BOT_TOKEN) as bot:
        await bot.set_webhook(url=webhook_url, secret_token=config.WEBHOOK_SECRET)
    return webhook_url


class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        path = self.path.split("?")[0].rstrip("/")
        if path not in ("/webhook",):
            self.send_response(404)
            self.end_headers()
            return

        config.validate()

        secret = self.headers.get("X-Telegram-Bot-Api-Secret-Token", "")
        if not config.WEBHOOK_SECRET or secret != config.WEBHOOK_SECRET:
            self.send_response(403)
            self.end_headers()
            return

        try:
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length)
            asyncio.run(_process_update(json.loads(body)))
            self.send_response(200)
        except Exception:
            logger.exception("Failed to process update")
            self.send_response(500)
        finally:
            self.end_headers()

    def do_GET(self):
        path = self.path.split("?")[0].rstrip("/")
        if path == "/setup":
            try:
                config.validate()
                webhook_url = asyncio.run(_register_webhook())
                self.send_response(200)
                self.end_headers()
                self.wfile.write(f"Webhook registered: {webhook_url}".encode())
            except Exception:
                logger.exception("Failed to register webhook")
                self.send_response(500)
                self.end_headers()
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"CapCut TG Bot is running!")

    def log_message(self, *args):
        pass
