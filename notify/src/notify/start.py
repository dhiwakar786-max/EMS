from notify.interface import BaseNotificationSender


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
