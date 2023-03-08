#!/usr/bin/python3
# Project Name: lotto-2023
# Description: I don't know what is this, work in progress :-)
#              Tested on Linux, Ubuntu 22.04.2
# Usage: main.py :-)
# Author: CheerfulAnt@outlook.com
# Version: 0.1.0
# Date: 1 March 2023 - 21:00 (GMT+01:00)

import cfg
import event_report
import fetch_draw
# -------------------
import sys
import json


if sys.version_info < (3, 10):
    raise Exception('Tested only on Python 3.10 :-)')

# check modules in the project :-)
