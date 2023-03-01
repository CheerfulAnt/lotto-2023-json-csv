#!/usr/bin/python3
# Project Name: lotto-2023
# Description: I don't know what is this, work in progress :-)
#              Tested on Linux, Ubuntu 22.04.2
# Usage: main.py :-)
# Author: CheerfulAnt@outlook.com
# Version: 0.1.0
# Date: 1 March 2023 - 21:00 (GMT+01:00)

import os
import sys
import email_reports
from dotenv import load_dotenv
import logging
import traceback
import json

if __name__ == '__main__':

    if sys.version_info < (3, 10):
        raise Exception('Tested only on Python 3.10, comment this if, to try run on another Python version :-)')

    load_dotenv()

    logging.basicConfig(filename=os.getenv('LOG_FILE'), level=logging.DEBUG, format='%(asctime)s - %(message)s')

    def event_log(event='[UNKNOWN]', message='No message.', exception_show=eval(os.getenv('EXCEPTION_SHOW')),
                  eml_error_log=eval(os.getenv('EMAIL_ERROR_LOG')), eml_event=eval(os.getenv('EMAIL_OK_LOG'))):

        if event == '[ERROR]':
            logging.exception("Surprise, error occurred.")
            if exception_show:
                print('\033[91m' + traceback.format_exc() + '\033[0m')
            if eml_error_log:
                email_reports.send_email(subject=event, message=traceback.format_exc())
        else:
            logging.info(message)
            if eml_event:
                email_reports.send_email(subject=event, message=message)


    event_log(event='[UPDATE]', message='Database updated successfully.')


    try:
        with open(os.getenv('CONFIG_JSON_FILE'), 'r', encoding="utf-8") as j_file:
            j_data = json.load(j_file)
    except:
        event_log(event='[ERROR]')
