import logging
import os
import sys
from pathlib import Path

from playwright_captcha import CaptchaType
from playwright_captcha.utils.camoufox_add_init_script.add_init_script import (
    get_addon_path,
)

LOG_LEVEL = logging.getLevelNamesMapping()[os.getenv("LOG_LEVEL", "INFO").upper()]

VERSION = os.getenv("VERSION", "unknown").removeprefix("v")

ADDON_PATH = str(Path(get_addon_path()).absolute())
MAX_ATTEMPTS = sys.maxsize

PROXY_SERVER = os.getenv("PROXY_SERVER")
PROXY_USERNAME = os.getenv("PROXY_USERNAME")
PROXY_PASSWORD = os.getenv("PROXY_PASSWORD")

HOST = os.getenv("HOST", "0.0.0.0")  # noqa: S104
PORT = int(os.getenv("PORT", "8191"))

DEFAULT_MAX_TIMEOUT = int(os.getenv("DEFAULT_MAX_TIMEOUT", "30"))
DEFAULT_WAIT_STATE = os.getenv("DEFAULT_WAIT_STATE", "domcontentloaded")

# Ad‑blocking route interceptor
BLOCKED_URL_PATTERNS: list[str] = [
    pattern.strip()
    for pattern in os.getenv(
        "BLOCKED_URL_PATTERNS",
        "doubleclick.net,googleadservices.com,googlesyndication.com,google-analytics.com,adsystem.com,adservice.google.com,pagead2.googlesyndication.com,yandex.ru,mc.yandex,facebook.net,fbcdn.net,pubfuture.com,pubfuture-ad.com,googletagmanager.com,cloudflareinsights.com,widgetlogic.org",
    ).split(",")
    if pattern.strip()
]

CHALLENGE_TITLES_MAP: dict[CaptchaType, list[str]] = {
    # Cloudflare
    CaptchaType.CLOUDFLARE_INTERSTITIAL: ["Just a moment..."],
}

CHALLENGE_TITLES = [
    title for titles in CHALLENGE_TITLES_MAP.values() for title in titles
]
