from unittest.mock import AsyncMock, MagicMock

from handlers.greet import REPLY, greet_on_message


async def test_greet_replies_to_any_text():
    update = MagicMock()
    update.message.text = "anything at all"
    update.message.reply_text = AsyncMock()

    await greet_on_message(update, MagicMock())

    update.message.reply_text.assert_awaited_once_with(REPLY)


async def test_greet_ignores_non_text():
    update = MagicMock()
    update.message.text = None
    update.message.reply_text = AsyncMock()

    await greet_on_message(update, MagicMock())

    update.message.reply_text.assert_not_awaited()
