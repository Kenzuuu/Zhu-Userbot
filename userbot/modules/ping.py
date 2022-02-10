# Copyright (C) 2019 The Raphielscape Company LLC.
#klo fork atau clone gausah hapus atau ganti credit
#credit by Kenzuuu/Zhu-Usebot
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

import asyncio
import random
import time
from datetime import datetime

import redis
from speedtest import Speedtest

from userbot import ALIVE_NAME, CMD_HELP, DEVS, PING_PIC, StartTime
from userbot.events import register
