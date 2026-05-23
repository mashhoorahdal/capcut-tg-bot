import pytest
from unittest.mock import patch


def test_config_loads_bot_token(monkeypatch):
    monkeypatch.setenv("BOT_TOKEN", "test-token-123")

    import importlib, config
    importlib.reload(config)

    assert config.BOT_TOKEN == "test-token-123"


def test_config_loads_vpn_link(monkeypatch):
    monkeypatch.setenv("VPN_LINK", "https://test-link.com")

    import importlib, config
    importlib.reload(config)

    assert config.VPN_LINK == "https://test-link.com"


def test_config_loads_capcut_latest_link(monkeypatch):
    monkeypatch.setenv("CAPCUT_LATEST_LINK", "https://test-capcut.com")

    import importlib, config
    importlib.reload(config)

    assert config.CAPCUT_LATEST_LINK == "https://test-capcut.com"


def test_config_loads_webhook_secret(monkeypatch):
    monkeypatch.setenv("WEBHOOK_SECRET", "my-secret")

    import importlib, config
    importlib.reload(config)

    assert config.WEBHOOK_SECRET == "my-secret"


def test_config_loads_webhook_url(monkeypatch):
    monkeypatch.setenv("WEBHOOK_URL", "https://my-bot.vercel.app")

    import importlib, config
    importlib.reload(config)

    assert config.WEBHOOK_URL == "https://my-bot.vercel.app"


def test_validate_raises_if_bot_token_missing(monkeypatch):
    monkeypatch.setenv("BOT_TOKEN", "")

    import importlib, config
    with patch("config.load_dotenv"):
        importlib.reload(config)
        with pytest.raises(ValueError, match="BOT_TOKEN"):
            config.validate()


def test_validate_raises_if_vpn_link_missing(monkeypatch):
    monkeypatch.setenv("BOT_TOKEN", "tok")
    monkeypatch.setenv("VPN_LINK", "")

    import importlib, config
    with patch("config.load_dotenv"):
        importlib.reload(config)
        with pytest.raises(ValueError, match="VPN_LINK"):
            config.validate()


def test_validate_raises_if_capcut_latest_link_missing(monkeypatch):
    monkeypatch.setenv("BOT_TOKEN", "tok")
    monkeypatch.setenv("VPN_LINK", "https://vpn.com")
    monkeypatch.setenv("CAPCUT_LATEST_LINK", "")

    import importlib, config
    with patch("config.load_dotenv"):
        importlib.reload(config)
        with pytest.raises(ValueError, match="CAPCUT_LATEST_LINK"):
            config.validate()
