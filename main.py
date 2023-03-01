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
from dotenv import load_dotenv
import logging
import json
import functions

if __name__ == '__main__':

    if sys.version_info < (3, 10):
        raise Exception('Tested only on Python 3.10, comment this if, to try run on another Python version :-)')

    load_dotenv()

    logging.basicConfig(filename=os.getenv('LOG_FILE'), level=logging.DEBUG, format='%(asctime)s - %(message)s')

    functions.event_log(event='[UPDATE]', message='Database updated successfully.')

    try:
        with open(os.getenv('CONFIG_JSON_FILE'), 'r', encoding="utf-8") as j_file:
            j_data = json.load(j_file)
    except:
        functions.event_log(event='[ERROR]')
