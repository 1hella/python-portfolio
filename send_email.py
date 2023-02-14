import smtplib
import ssl
from dotenv import load_dotenv
import os

load_dotenv()
username = os.getenv("EMAIL_USERNAME")
password = os.getenv("EMAIL_PASSWORD")
def send_email(email_address, message):
    host = "smtp.gmail.com"
    port = 465

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, email_address, message)

