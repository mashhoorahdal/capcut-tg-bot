import asyncio
import os
import sys
from http.server import BaseHTTPRequestHandler

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import config
from telegram import Bot

logger_name = __name__


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        webhook_url = f"{config.WEBHOOK_URL}/webhook"

        async def set_webhook():
            async with Bot(token=config.BOT_TOKEN) as bot:
                await bot.set_webhook(
                    url=webhook_url,
                    secret_token=config.WEBHOOK_SECRET,
                )

        asyncio.run(set_webhook())
        self.send_response(200)
        self.end_headers()
        self.wfile.write(f"Webhook registered: {webhook_url}".encode())

    def log_message(self, *args):
        pass
