from unittest.mock import AsyncMock, MagicMock

import config
from handlers.capcut import capcut_command


async def test_capcut_sends_document():
    update = MagicMock()
    update.message.reply_document = AsyncMock()

    await capcut_command(update, MagicMock())

    update.message.reply_document.assert_awaited_once()
    kwargs = update.message.reply_document.await_args.kwargs
    assert kwargs["document"] == config.CAPCUT_FILE_ID
    assert kwargs["parse_mode"] == "Markdown"
