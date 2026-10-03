

# 3. Create the Factory
from notify.interface import BaseNotificationSender
from notify.start import EmailSender, SMSSender
from notify.whatsaapp import Whatsappsender


class NotificationFactory:
    """Factory class to handle instantiation logic."""
    
    # Mapping channels to their respective classes (Cleans up messy if/else chains)
    _registry = {
        "email": EmailSender,
        "sms": SMSSender,
        "whatsapp": Whatsappsender
    }

    @classmethod
    def get_sender(cls, channel: str) -> BaseNotificationSender:
        """Looks up the target class and returns an instantiated object."""
        channel_lower = channel.strip().lower()
        sender_class = cls._registry.get(channel_lower)
        
        if not sender_class:
            raise ValueError(f"Unsupported notification channel: '{channel}'")
            
        return sender_class()


def dispatch_alert(user_contact: int, channel_type: str, alert_msg: str):
    try:
        # Client asks factory for the tool, completely agnostic to how it works
        notifier = NotificationFactory.get_sender(channel_type)
        notifier.send(recipient=user_contact, message=alert_msg)
    except ValueError as e:
        print(f"Error: {e}")

# from notify import NotificationFactory, dispatch_alert

# dispatch_alert("dev@example.com", "email", "Server CPU usage is over 90%!")

# or grab a sender yourself
sender = NotificationFactory.get_sender("whatsapp")
sender.send(recipient='+916382468421', message="Your code is 4821.",time_hour=9,time_min=14)