from omar6995_browserforge.download import DownloadIfNotExists

DownloadIfNotExists(fingerprints=True, headers=True)

from omar6995_browserforge.headers import Browser

from .generator import (
    Fingerprint,
    FingerprintGenerator,
    NavigatorFingerprint,
    Screen,
    ScreenFingerprint,
    VideoCard,
)

__all__ = [
    "Browser",
    "Fingerprint",
    "FingerprintGenerator",
    "NavigatorFingerprint",
    "Screen",
    "ScreenFingerprint",
    "VideoCard",
]
