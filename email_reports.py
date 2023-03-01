import os
import smtplib
import ssl
from email.message import EmailMessage


def send_email(subject="No subject.", message='No message.'):

    user = os.getenv('EMRE_USER')
    password = os.getenv('EMRE_PASS')
    server = os.getenv('EMRE_SMTP_SRV')
    port = int(os.getenv('EMRE_SMTP_PORT'))

    msg = EmailMessage()
    msg['Subject'] = '[lotto-2023] ' + subject
    msg['From'] = user
    msg['To'] = user
    msg.set_content(message)

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP(server, port) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(user, password)
            server.send_message(msg)
            server.quit()
    except Exception as e:
        pass