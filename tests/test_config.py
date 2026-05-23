import pytest
from unittest.mock import patch


def _all_vars(monkeypatch, *, bot_token="tok", vpn="https://vpn.com",
              capcut="https://capcut.com", secret="sec", url="https://x.vercel.app"):
    monkeypatch.setenv("BOT_TOKEN", bot_token)
    monkeypatch.setenv("VPN_LINK", vpn)
    monkeypatch.setenv("CAPCUT_LATEST_LINK", capcut)
    monkeypatch.setenv("WEBHOOK_SECRET", secret)
    monkeypatch.setenv("WEBHOOK_URL", url)


def test_config_loads_bot_token(monkeypatch):
    _all_vars(monkeypatch, bot_token="test-token-123")
    import config
    with patch("config.load_dotenv"):
        token, *_ = config._load_config()
    assert token == "test-token-123"


def test_config_loads_vpn_link(monkeypatch):
    _all_vars(monkeypatch, vpn="https://test-link.com")
    import config
    with patch("config.load_dotenv"):
        _, link, *_ = config._load_config()
    assert link == "https://test-link.com"


def test_config_loads_capcut_latest_link(monkeypatch):
    _all_vars(monkeypatch, capcut="https://test-capcut.com")
    import config
    with patch("config.load_dotenv"):
        _, _, capcut_link, *_ = config._load_config()
    assert capcut_link == "https://test-capcut.com"


def test_config_loads_webhook_secret(monkeypatch):
    _all_vars(monkeypatch, secret="my-secret-token")
    import config
    with patch("config.load_dotenv"):
        _, _, _, secret, _ = config._load_config()
    assert secret == "my-secret-token"


def test_config_loads_webhook_url(monkeypatch):
    _all_vars(monkeypatch, url="https://my-bot.vercel.app")
    import config
    with patch("config.load_dotenv"):
        _, _, _, _, url = config._load_config()
    assert url == "https://my-bot.vercel.app"


def test_config_raises_if_bot_token_missing(monkeypatch):
    _all_vars(monkeypatch)
    monkeypatch.delenv("BOT_TOKEN", raising=False)
    import config
    with patch("config.load_dotenv"):
        with pytest.raises(ValueError, match="BOT_TOKEN"):
            config._load_config()


def test_config_raises_if_vpn_link_missing(monkeypatch):
    _all_vars(monkeypatch)
    monkeypatch.delenv("VPN_LINK", raising=False)
    import config
    with patch("config.load_dotenv"):
        with pytest.raises(ValueError, match="VPN_LINK"):
            config._load_config()


def test_config_raises_if_capcut_latest_link_missing(monkeypatch):
    _all_vars(monkeypatch)
    monkeypatch.delenv("CAPCUT_LATEST_LINK", raising=False)
    import config
    with patch("config.load_dotenv"):
        with pytest.raises(ValueError, match="CAPCUT_LATEST_LINK"):
            config._load_config()
