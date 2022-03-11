# Copyright (C) 2019 The Raphielscape Company LLC.
# Upload by Kenzuuu/Zhu-Userbot
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for getting information about the server. """


import asyncio
import time
from datetime import datetime

from userbot import (
    ZHU_LOGO,
    DEVS,
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
@register(incoming=True, from_users=DEVS, pattern=r"^/ping$")
async def redis(ping):
    user = await bot.get_me()
    uptime = await get_readable_time((time.time() - StartTime)) 
    start = datetime.now()
    await ping.edit("💥")
    await asyncio.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    output = (
        f"𝕻𝖔𝖓𝖌 : `%sms` \n"
        f"𝖀𝖕𝖙𝖎𝖒𝖊 : `{uptime}` \n"
        f"𝕭𝖔𝖙 𝕹𝖆𝖒𝖊 : 𝐙𝖍𝖚-𝖀𝖘𝖊𝖗𝖇𝖔𝖙 \n" % (duration))
    if ZHU_LOGO:
        try:
            logo = ZHU_LOGO
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


