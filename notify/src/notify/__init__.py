"""Multi-channel notification library."""

from notify.interface import BaseNotificationSender
from notify.service import NotificationFactory, dispatch_alert
from notify.start import EmailSender, PushSender, SMSSender
from notify.whatsaapp import Whatsappsender

__version__ = "0.1.0"

__all__ = [
    "BaseNotificationSender",
    "EmailSender",
    "NotificationFactory",
    "PushSender",
    "SMSSender",
    "Whatsappsender",
    "dispatch_alert",
]
