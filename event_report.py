import traceback
import smtplib
import ssl
from email.message import EmailMessage
import logging
from logging.handlers import RotatingFileHandler
import cfg


# Log rotation
logger = logging.getLogger(cfg.config['PROJECT_NAME'])
logger.setLevel(logging.DEBUG)
fh = RotatingFileHandler(filename=cfg.config['LOG_FILE'], maxBytes=cfg.config['LOG_SIZE'],
                         backupCount=cfg.config['LOG_COUNT'], encoding=cfg.config['ENCODING'])
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('[{asctime}] - [{name}] - [{levelname}] - {message}', style="{")
fh.setFormatter(formatter)
logger.addHandler(fh)


def event_log(exception_show=cfg.config['EXCEPTION_SHOW'],
              email_error_log=cfg.config['EMAIL_ERROR_LOG'],
              email_event_log=cfg.config['EMAIL_EVENT_LOG'],
              event='[UNKNOWN]',
              message='No message.'):

    if event == '[ERROR]':
        logger.exception('Surprise, [ERROR] occurred.')
        if exception_show:
            print('\033[91m' + traceback.format_exc() + '\033[0m')
        if email_error_log:
            send_email(subject=event, message=traceback.format_exc())
    else:
        logger.info(message)
        if email_event_log:
            send_email(subject=event, message=message)


def send_email(emre_user=cfg.config['EMRE_USER'],
               emre_pass=cfg.config['EMRE_PASS'],
               emre_smtp_srv=cfg.config['EMRE_SMTP_SRV'],
               emre_smtp_port=cfg.config['EMRE_SMTP_PORT'],
               project_name=cfg.config['PROJECT_NAME'],
               subject="No subject.",
               message='No message.'):

    msg = EmailMessage()
    msg['Subject'] = '[' + project_name + '] ' + subject
    msg['From'] = emre_user
    msg['To'] = emre_user
    msg.set_content(message)

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP(emre_smtp_srv, emre_smtp_port, timeout=2) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(emre_user, emre_pass)
            server.send_message(msg)
            server.quit()
    except Exception:
        logger.exception('Surprise, [ERROR] occurred. Can\'t sent e-mail.')
