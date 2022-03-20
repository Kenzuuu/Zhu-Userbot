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
    ALIVE_LOGO,
    ZHU_LOGO
    ALIVE_NAME,
    BOT_VER,
    CMD_HELP,
    StartTime,
    bot,
)
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================

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

@register(outgoing=True, pattern=r"^\.(?:deploy)\s?(.)?")
async def amireallyalive(alive):
    await bot.get_me()
    await get_readable_time((time.time() - StartTime))
    output = (
        f"----『𝐙𝐇𝐔-𝐔𝐒𝐄𝐑𝐁𝐎𝐓』----\n\n"
        f"★ REPO ➡ [𝗗𝗜𝗦𝗜𝗡𝗜](https://github.com/Kenzuuu/Zhu-Userbot) \n"
        f"★ DEPLOY ➡ [𝗗𝗜𝗦𝗜𝗡𝗜](https://telegram.dog/XTZ_HerokuBot?start=S2VuenV1dS9aaHUtVXNlcmJvdCBLZW56aHU)\n"
        f"★ AMBIL API ➡ [𝗗𝗜𝗦𝗜𝗡𝗜](https://t.me/ZhuXScrapperBot)\n"
        f"★ AMBIL STRING ➡ [𝗗𝗜𝗦𝗜𝗡𝗜](https://t.me/ZhuXSessionBot)\n"
        f"★ ROBOT + MUSIC ➡ [𝗗𝗜𝗦𝗜𝗡𝗜](https://t.me/YZXRobot)\n"
    )
    if ZHU_LOGO:
        try:
            logo = ZHU_LOGO
            await alive.delete()
            msg = await bot.send_file(alive.chat_id, logo, caption=output)
            await asyncio.sleep(200)
            await msg.delete()
        except BaseException:
            await alive.edit(
                output + "\n\n *`The provided logo is invalid."
                "\nMake sure the link is directed to the logo picture`"
            )
            await asyncio.sleep(100)
            await alive.delete()
    else:
        await alive.edit(output)
        await asyncio.sleep(100)
        await alive.delete()
