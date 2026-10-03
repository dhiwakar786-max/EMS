from abc import ABC, abstractmethod

# 1. Define the Abstract Product Interface
class BaseNotificationSender(ABC):
    """Abstract Base Class for all notification channels."""
    
    @abstractmethod
    def send(self, recipient: str, message: str) -> None:
        pass