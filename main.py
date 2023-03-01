# import os
import sys
import email_reports
from dotenv import load_dotenv
import logging
import traceback
import json


if sys.version_info < (3, 10):
    raise Exception('Tested only on Python 3.10, comment this if, to try run on another Python version :-)')

load_dotenv()
logging.basicConfig(filename='sys.log', level=logging.DEBUG, format='%(asctime)s - %(message)s')

with open('config.json', 'r', encoding="utf-8") as j_file:
    j_data = json.load(j_file)


# try:
#     1/0
# except:
#     logging.exception("Surprise, error occurred when divided by zero.")
#     email_reports.send_email(subject='[ERROR]', message=traceback.format_exc())
