import logging
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from telegram import Update, Message, User
from telegram.ext import ContextTypes

from handlers.latest import latest_command


@pytest.mark.asyncio
async def test_latest_sends_message_with_link():
    update = MagicMock(spec=Update)
    update.message = MagicMock(spec=Message)
    update.message.reply_text = AsyncMock()
    update.effective_user = MagicMock(spec=User)
    update.effective_user.username = "testuser"
    update.effective_chat = MagicMock()
    update.effective_chat.id = 99999
    update.effective_chat.type = "group"

    context = MagicMock(spec=ContextTypes.DEFAULT_TYPE)

    with patch("handlers.latest.config.CAPCUT_LATEST_LINK", "https://test-capcut.com/download"):
        await latest_command(update, context)

    update.message.reply_text.assert_called_once()
    message_text = update.message.reply_text.call_args[0][0]
    assert "https://test-capcut.com/download" in message_text


@pytest.mark.asyncio
async def test_latest_uses_markdown_parse_mode():
    update = MagicMock(spec=Update)
    update.message = MagicMock(spec=Message)
    update.message.reply_text = AsyncMock()
    update.effective_user = MagicMock(spec=User)
    update.effective_user.username = "testuser"
    update.effective_chat = MagicMock()
    update.effective_chat.id = 99999
    update.effective_chat.type = "group"

    context = MagicMock(spec=ContextTypes.DEFAULT_TYPE)

    with patch("handlers.latest.config.CAPCUT_LATEST_LINK", "https://test-capcut.com/download"):
        await latest_command(update, context)

    call_kwargs = update.message.reply_text.call_args[1]
    assert call_kwargs.get("parse_mode") == "Markdown"


@pytest.mark.asyncio
async def test_latest_logs_invocation(caplog):
    update = MagicMock(spec=Update)
    update.message = MagicMock(spec=Message)
    update.message.reply_text = AsyncMock()
    update.effective_user = MagicMock(spec=User)
    update.effective_user.username = "loggeduser"
    update.effective_chat = MagicMock()
    update.effective_chat.id = 11111
    update.effective_chat.type = "private"

    context = MagicMock(spec=ContextTypes.DEFAULT_TYPE)

    with patch("handlers.latest.config.CAPCUT_LATEST_LINK", "https://test-capcut.com"):
        with caplog.at_level(logging.INFO, logger="handlers.latest"):
            await latest_command(update, context)

    assert any("latest" in record.message.lower() for record in caplog.records)
