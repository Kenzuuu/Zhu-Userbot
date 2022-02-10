# Copyright (C) 2019 The Raphielscape Company LLC.
# Created by Kenzhu 2022
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for getting information about the server. """


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
    ZHU_LOGO,
    BOT_VER,
    CMD_HELP,
    StartTime,
    bot,
)
from userbot.events import register
