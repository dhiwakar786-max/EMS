import smtplib
from email.message import EmailMessage

# 1. Configure configuration and credentials
SMTP_SERVER = "smtp.gmail.com"  # Replace with your provider's SMTP server
SMTP_PORT = 587                 # Use 587 for TLS
SENDER_EMAIL = "your_email@gmail.com"
# For Gmail/Outlook, use an "App Password" here, NOT your regular password!
SENDER_PASSWORD = "your_app_password"  
RECEIVER_EMAIL = "recipient_email@example.com"

# 2. Build the email message
msg = EmailMessage()
msg["Subject"] = "Hello from Python!"
msg["From"] = SENDER_EMAIL
msg["To"] = RECEIVER_EMAIL
msg.set_content("This is a test email sent automatically using Python script.")

try:
    # 3. Connect to the server and send the email
    print("Connecting to server...")
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()  # Secure the connection with TLS
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        
        print("Sending email...")
        server.send_message(msg)
        
    print("Success! Email sent.")
    
except Exception as e:
    print(f"An error occurred: {e}")
