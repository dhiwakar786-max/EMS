from abc import ABC, abstractmethod

# 1. Define the Abstract Product Interface
class BaseNotificationSender(ABC):
    """Abstract Base Class for all notification channels."""
    
    @abstractmethod
    def send(self, recipient: str, message: str) -> None:
        pass

# 2. Implement Concrete Products
class EmailSender(BaseNotificationSender):
    def send(self, recipient: str, message: str) -> None:
        print(f"📧 Sending Email to {recipient}: {message}")

class SMSSender(BaseNotificationSender):
    def send(self, recipient: str, message: str) -> None:
        print(f"💬 Sending SMS to {recipient}: {message}")

class PushSender(BaseNotificationSender):
    def send(self, recipient: str, message: str) -> None:
        print(f"📱 Sending Push Notification to {recipient}: {message}")

# 3. Create the Factory
class NotificationFactory:
    """Factory class to handle instantiation logic."""
    
    # Mapping channels to their respective classes (Cleans up messy if/else chains)
    _registry = {
        "email": EmailSender,
        "sms": SMSSender,
        "push": PushSender
    }

    @classmethod
    def get_sender(cls, channel: str) -> BaseNotificationSender:
        """Looks up the target class and returns an instantiated object."""
        channel_lower = channel.strip().lower()
        sender_class = cls._registry.get(channel_lower)
        
        if not sender_class:
            raise ValueError(f"Unsupported notification channel: '{channel}'")
            
        return sender_class()


def dispatch_alert(user_contact: str, channel_type: str, alert_msg: str):
    try:
        # Client asks factory for the tool, completely agnostic to how it works
        notifier = NotificationFactory.get_sender(channel_type)
        notifier.send(recipient=user_contact, message=alert_msg)
    except ValueError as e:
        print(f"Error: {e}")


dispatch_alert("dev@example.com", "email", "Server CPU usage is over 90%!")
dispatch_alert("+15550199", "sms", "Your verification code is 4821.")
dispatch_alert("user_dev_id_99", "push", "Someone liked your post.")
dispatch_alert("123-456", "carrier_pigeon", "Hello?") # Raises unsupported error
