import asyncio
import platform
import sys
import time
from asyncio import create_subprocess_exec as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from datetime import datetime
from os import remove
from platform import python_version, uname
from shutil import which

import psutil
from telethon import __version__, version

from userbot import (
    ALIVE_LOGO,
    ALIVE_NAME,
    BOT_VER,
    CMD_HELP,
    UPSTREAM_REPO_BRANCH,
    StartTime,
    bot,
)
from userbot.events import register
