# CapCut TG Bot

Telegram bot for the CapCut group. One command: `/capcut` forwards the CapCut file.

## Commands

| Command | Description |
|---------|-------------|
| `/capcut` | Sends the CapCut file |

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `BOT_TOKEN` | Yes | Telegram bot token from @BotFather |
| `CAPCUT_FILE_ID` | Yes | Telegram `file_id` of the CapCut file (see below) |
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
   curl "https://your-project.vercel.app/?setup=1"
   ```
   The marker goes in the query string, not the path: `vercel.json` rewrites
   every request to `/api/index`, so the function never sees the original
   path. Query strings survive the rewrite.

### Bot Setup (one-time)

Register the command via `@BotFather` → `/setcommands`:

```
capcut - Get the CapCut file
```

## Getting the File ID

Telegram caches uploaded files, so the bot re-sends by `file_id` instead of
re-uploading each time.

1. Send the CapCut file to your bot in a private chat
2. Fetch the update:
   ```bash
   curl "https://api.telegram.org/bot<BOT_TOKEN>/getUpdates"
   ```
3. Copy `result[].message.document.file_id` into `.env` as `CAPCUT_FILE_ID`

Replacing the file later means repeating these steps with the new file.

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
