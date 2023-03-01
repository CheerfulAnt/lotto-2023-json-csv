import os
import logging
import traceback
import smtplib
import ssl
from email.message import EmailMessage


def event_log(event='[UNKNOWN]', message='No message.', exception_show=eval(os.getenv('EXCEPTION_SHOW')),
              eml_error_log=eval(os.getenv('EMAIL_ERROR_LOG')), eml_event=eval(os.getenv('EMAIL_OK_LOG'))):
    if event == '[ERROR]':
        logging.exception("Surprise, error occurred.")
        if exception_show:
            print('\033[91m' + traceback.format_exc() + '\033[0m')
        if eml_error_log:
            send_email(subject=event, message=traceback.format_exc())
    else:
        logging.info(message)
        if eml_event:
            send_email(subject=event, message=message)


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


