import pytest
from unittest.mock import patch


def test_config_loads_bot_token(monkeypatch):
    monkeypatch.setenv("BOT_TOKEN", "test-token-123")
    monkeypatch.setenv("VPN_LINK", "https://test-link.com")

    import config
    with patch("config.load_dotenv"):
        token, _ = config._load_config()

    assert token == "test-token-123"


def test_config_loads_vpn_link(monkeypatch):
    monkeypatch.setenv("BOT_TOKEN", "test-token-123")
    monkeypatch.setenv("VPN_LINK", "https://test-link.com")

    import config
    with patch("config.load_dotenv"):
        _, link = config._load_config()

    assert link == "https://test-link.com"


def test_config_raises_if_bot_token_missing(monkeypatch):
    monkeypatch.delenv("BOT_TOKEN", raising=False)
    monkeypatch.setenv("VPN_LINK", "https://test-link.com")

    import config
    with patch("config.load_dotenv"):
        with pytest.raises(ValueError, match="BOT_TOKEN"):
            config._load_config()


def test_config_raises_if_vpn_link_missing(monkeypatch):
    monkeypatch.setenv("BOT_TOKEN", "test-token-123")
    monkeypatch.delenv("VPN_LINK", raising=False)

    import config
    with patch("config.load_dotenv"):
        with pytest.raises(ValueError, match="VPN_LINK"):
            config._load_config()
