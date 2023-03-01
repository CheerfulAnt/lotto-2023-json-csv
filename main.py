import os
import sys
import email_reports
from dotenv import load_dotenv
import logging
import traceback


load_dotenv()
logging.basicConfig(filename='sys.log', level=logging.DEBUG, format='%(asctime)s - %(message)s')

try:
    1/0
except:
    logging.exception("Surprise, error occurred when divided by zero.")
    email_reports.send_email(subject='[ERROR]', message=traceback.format_exc())
