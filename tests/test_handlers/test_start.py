import pytest
from unittest.mock import AsyncMock, MagicMock
from telegram import Update, Message, Chat, User
from telegram.ext import ContextTypes


@pytest.mark.asyncio
async def test_start_replies_with_welcome_message():
    update = MagicMock(spec=Update)
    update.message = MagicMock(spec=Message)
    update.message.reply_text = AsyncMock()
    update.effective_user = MagicMock(spec=User)
    update.effective_user.first_name = "Ali"

    context = MagicMock(spec=ContextTypes.DEFAULT_TYPE)

    from handlers.start import start_command
    await start_command(update, context)

    update.message.reply_text.assert_called_once()
    call_text = update.message.reply_text.call_args[0][0]
    assert "Ali" in call_text


@pytest.mark.asyncio
async def test_start_mentions_vpn_command():
    update = MagicMock(spec=Update)
    update.message = MagicMock(spec=Message)
    update.message.reply_text = AsyncMock()
    update.effective_user = MagicMock(spec=User)
    update.effective_user.first_name = "Test"

    context = MagicMock(spec=ContextTypes.DEFAULT_TYPE)

    from handlers.start import start_command
    await start_command(update, context)

    call_text = update.message.reply_text.call_args[0][0]
    assert "/vpn" in call_text
