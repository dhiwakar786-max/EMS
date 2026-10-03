import pytest

from notify.interface import BaseNotificationSender


def test_base_sender_cannot_be_instantiated():
    with pytest.raises(TypeError):
        BaseNotificationSender()


def test_subclass_must_implement_send():
    class Incomplete(BaseNotificationSender):
        pass

    with pytest.raises(TypeError):
        Incomplete()


def test_subclass_with_send_is_usable():
    class Recorder(BaseNotificationSender):
        def __init__(self):
            self.sent = []

        def send(self, recipient: str, message: str) -> None:
            self.sent.append((recipient, message))

    recorder = Recorder()
    recorder.send("dev@example.com", "hello")

    assert recorder.sent == [("dev@example.com", "hello")]
