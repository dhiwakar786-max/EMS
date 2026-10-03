# notify

A small Python library for sending notifications over several channels (email, SMS,
WhatsApp) behind one factory, so callers pick a channel by name instead of wiring up
each provider themselves.

## Layout

```
notify/
├── pyproject.toml
├── src/notify/
│   ├── __init__.py      # version metadata only
│   ├── interface.py     # BaseNotificationSender abstract base class
│   ├── start.py         # EmailSender, SMSSender, PushSender
│   ├── whatsaapp.py     # Whatsappsender (needs pywhatkit)
│   └── service.py       # NotificationFactory + dispatch_alert
├── examples/            # standalone SMTP scripts, not part of the package
└── tests/
```

## Install

```bash
pip install -e ".[dev]"          # library + test tooling
pip install -e ".[whatsapp]"     # adds pywhatkit for the WhatsApp channel
```

## Usage

```python
from notify.service import NotificationFactory

sender = NotificationFactory.get_sender("email")
sender.send(recipient="dev@example.com", message="Server CPU usage is over 90%!")
```

Adding a channel means subclassing `BaseNotificationSender` and registering the class
in `NotificationFactory._registry`.

## WhatsApp channel

`Whatsappsender` drives WhatsApp Web through `pywhatkit`, which types the message with
`pyautogui`. That means it needs a graphical desktop session with WhatsApp Web already
logged in — it will not work headless, over SSH, or in CI. Recipients must include a
country code (`+918072398384`), or `send()` raises `ValueError`.

`pywhatkit` is imported lazily inside `send()`, so the rest of the library stays
importable on machines where it isn't installed or where there's no display.

## Known rough edges

- `start.py` is an odd name for the module holding `EmailSender`/`SMSSender`/`PushSender`;
  `senders.py` would read better.
- `PushSender` exists but isn't in `NotificationFactory._registry`, so the factory can't
  return it.
- `dispatch_alert()` catches `ValueError` and prints it, which suits a demo more than a
  library — callers can't tell success from failure.
- `examples/email.py` and `examples/sms.py` open SMTP connections at import time, which
  is why they live outside the package. `sms.py` also calls `server.quit()` in a
  `finally` block that raises `NameError` if the connection never opened.
