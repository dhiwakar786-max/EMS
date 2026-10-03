import pytest

from notify.interface import BaseNotificationSender
from notify.service import NotificationFactory
from notify.start import EmailSender, SMSSender
from notify.whatsaapp import Whatsappsender


@pytest.mark.parametrize(
    "channel, expected",
    [
        ("email", EmailSender),
        ("sms", SMSSender),
        ("whatsapp", Whatsappsender),
    ],
)
def test_get_sender_returns_registered_class(channel, expected):
    assert isinstance(NotificationFactory.get_sender(channel), expected)


@pytest.mark.parametrize("channel", ["EMAIL", "  Sms  ", "WhatsApp"])
def test_channel_lookup_ignores_case_and_whitespace(channel):
    assert isinstance(NotificationFactory.get_sender(channel), BaseNotificationSender)


def test_unknown_channel_raises():
    with pytest.raises(ValueError, match="Unsupported notification channel"):
        NotificationFactory.get_sender("carrier_pigeon")


def test_every_sender_implements_the_interface():
    for channel in NotificationFactory._registry:
        assert isinstance(NotificationFactory.get_sender(channel), BaseNotificationSender)


def test_whatsapp_rejects_number_without_country_code():
    with pytest.raises(ValueError, match="country code"):
        Whatsappsender().send(recipient="8072398384", message="hi")
