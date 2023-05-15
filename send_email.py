import smtplib
import ssl
from dotenv import load_dotenv
import os
import certifi


def send_email(email_address, message, name):
    load_dotenv()
    username = os.getenv("EMAIL_USERNAME")
    password = os.getenv("EMAIL_PASSWORD")
    to_address = os.getenv("TO_EMAIL_ADDRESS")

    host = "smtp.gmail.com"
    port = 465

    context = ssl.create_default_context(cafile=certifi.where())

    my_message = f"Subject: New email\r\n" \
                 f"From: {username}\r\n" \
                 f"To: {to_address}\r\n\r\n" \
                 f"New message from {name} at {email_address}: " \
                 f"{message}"

    print(my_message)
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, to_address, my_message)
