# CapCut VPN Bot

Telegram bot for CapCut VPN group. Sends VPN download link via `/vpn` command.

## Commands

| Command | Description |
|---------|-------------|
| `/start` | Welcome message |
| `/vpn` | Get VPN download link |

## Local Setup

1. Clone the repo
2. Create virtual environment and install dependencies:
   ```bash
   uv venv --python 3.12
   uv pip install -r requirements.txt
   ```
3. Copy env template:
   ```bash
   cp .env.example .env
   ```
4. Edit `.env` — add your `BOT_TOKEN` and `VPN_LINK`
5. Run:
   ```bash
   python bot.py
   ```

## Getting a Bot Token

1. Open Telegram, search for `@BotFather`
2. Send `/newbot` and follow prompts
3. Copy the token into `.env` as `BOT_TOKEN`

## Deploy to Railway (Free)

1. Push this repo to GitHub
2. Go to [railway.app](https://railway.app) → New Project → Deploy from GitHub
3. Select your repo
4. Add environment variables in Railway dashboard:
   - `BOT_TOKEN` — your Telegram bot token
   - `VPN_LINK` — your VPN download link
5. Railway auto-deploys. Bot runs 24/7.

## Adding New Commands

1. Create `handlers/<command>.py` with an async handler function:
   ```python
   import logging
   from telegram import Update
   from telegram.ext import ContextTypes

   logger = logging.getLogger(__name__)

   async def mycommand_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
       await update.message.reply_text("Your response here")
   ```
2. Register it in `bot.py`:
   ```python
   from handlers.mycommand import mycommand_command
   app.add_handler(CommandHandler("mycommand", mycommand_command))
   ```
3. Write tests in `tests/test_handlers/test_mycommand.py`

## Tests

```bash
python -m pytest -v
```
