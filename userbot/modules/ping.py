# Copyright (C) 2019 The Raphielscape Company LLC.
# Upload by Kenzuuu/Zhu-Userbot
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
    PING_LOGO,
    ALIVE_NAME,
    CMD_HELP,
    StartTime,
    bot,
)
from userbot.events import register

modules = CMD_HELP


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]

    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time

@register(outgoing=True, pattern=r"^\.ping$")
async def redis(ping):
    user = await bot.get_me()
    await get_readable_time((time.time() - StartTime))
    await ping.edit("💥")
    await asyncio.sleep(2)
    output = (
        f"**★ PONG !!** `%sms` \n"
        f"**Bot of :** {ALIVE_NAME} \n"
         )
    if PING_LOGO:
        try:
            logo = PING_LOGO
            await ping.delete()
            msg = await bot.send_file(ping.chat_id, logo, caption=output)
            await asyncio.sleep(500)
            await msg.delete()
        except BaseException:
            await ping.edit(
                output + "\n\n *Logo Yang Disediakan Tidak Valid."
                "\nPastikan Tautan Yang Anda Gunakan Valid"
            )
            await asyncio.sleep(100)
            await ping.delete()
    else:
        await ping.edit(output)
        await asyncio.sleep(100)
        await ping.delete()


