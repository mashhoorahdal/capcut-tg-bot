# CapCut TG Bot

Telegram bot for CapCut VPN group. Provides VPN download link, latest CapCut version download, and keyword-triggered greetings.

## Commands

| Command | Description |
|---------|-------------|
| `/start` | Welcome message with command list |
| `/vpn` | Get VPN download link |
| `/latest` | Get latest CapCut version download link |

## Smart Greetings

Bot listens for keywords in group messages and replies with available commands. Default keywords: `vpn`, `capcut`, `help`, `link`, `download`, `latest`.

Edit `KEYWORDS` in `handlers/greet.py` to customize.

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `BOT_TOKEN` | Yes | Telegram bot token from @BotFather |
| `VPN_LINK` | Yes | VPN download URL |
| `CAPCUT_LATEST_LINK` | Yes | CapCut APK/download URL |
| `WEBHOOK_SECRET` | Yes | Random string for webhook verification (`A-Za-z0-9_-` only) |
| `WEBHOOK_URL` | Yes | Your Vercel deployment URL (e.g. `https://your-project.vercel.app`) |

## Local Setup

1. Clone the repo
2. Install dependencies:
   ```bash
   uv sync
   ```
3. Copy env template:
   ```bash
   cp .env.example .env
   ```
4. Fill in `.env`
5. Run in polling mode:
   ```bash
   uv run python bot.py
   ```

## Deploy to Vercel

1. Push repo to GitHub
2. Import project at [vercel.com](https://vercel.com)
3. Add all environment variables in Vercel dashboard
4. After deploy, register the webhook once:
   ```
   GET https://your-project.vercel.app/setup
   ```

### Bot Setup (one-time)

1. Open `@BotFather` → your bot → **Bot Settings → Group Privacy → Turn Off**
   (required for the bot to read group messages)
2. Register commands via `@BotFather` → `/setcommands`:
   ```
   start - Welcome message
   vpn - Get VPN download link
   latest - Get latest CapCut version
   ```

## Getting a Bot Token

1. Open Telegram, search for `@BotFather`
2. Send `/newbot` and follow prompts
3. Copy the token into `.env` as `BOT_TOKEN`

## Adding New Commands

1. Create `handlers/<command>.py`:
   ```python
   import logging
   from telegram import Update
   from telegram.ext import ContextTypes

   logger = logging.getLogger(__name__)

   async def mycommand_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
       await update.message.reply_text("Your response here")
   ```
2. Register in `bot.py` and `api/index.py`:
   ```python
   from handlers.mycommand import mycommand_command
   app.add_handler(CommandHandler("mycommand", mycommand_command))
   ```
3. Write tests in `tests/test_handlers/test_mycommand.py`

## Tests

```bash
uv run pytest -v
```
