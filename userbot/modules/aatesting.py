#Credit to @triplenineee

import asyncio
import random
import time
from datetime import datetime

import redis
from speedtest import Speedtest

from userbot import ALIVE_NAME, CMD_HELP, DEVS, StartTime
from userbot.events import register

LOVE_IMG = os.environ.get(
    "PING_PIC", "https://te.legra.ph/file/a59da36828333262c9848.jpg"
)
