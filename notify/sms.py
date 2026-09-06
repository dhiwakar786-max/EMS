import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from notify.interface import BaseNotificationSender


class SMSSender(BaseNotificationSender):
    def send(self, recipient: str, message: str) -> None:
        print(f"💬 Sending SMS to {recipient}: {message}")


# Define account and recipient information
sender_email = "your_gmail_username@gmail.com"
sender_password = "your_16_digit_app_password"  # Generated app password
recipient_phone_gateway = "1234567890@vtext.com" # Example: Verizon phone number

# Create the message structure
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = recipient_phone_gateway

# SMS messages do not need a subject line; put your text in the body
body = "Hello! This is a real text message sent using Python code."
message.attach(MIMEText(body, "plain"))

try:
    # Connect to Gmail's SMTP server
    server = smtplib.SMTP("://gmail.com", 587)
    server.starttls() # Secure the connection
    
    # Log in and send the text
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_phone_gateway, message.as_string())
    
    print("SMS sent successfully!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Always close the server connection
    server.quit()
