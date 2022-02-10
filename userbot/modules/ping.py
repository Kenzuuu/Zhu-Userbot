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

from userbot import ALIVE_NAME, CMD_HELP, DEVS, PING_LOGO, StartTime
from userbot.events import register

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

@register(outgoing=True, pattern="^.ping$")
@register(incoming=True, from_users=DEVS, pattern=r"^.cping$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("💝")
    await asyncio.sleep(3)
    end = datetime.now()
    output = (
         f"duration = (end - start).microseconds / 1000 \n"
         f"**Pong !!** `%sms` \n"
         f"**Uptime **- `{uptime}`\n" % (duration)
          ) 
    if PING_LOGO:
        try:
            logo = PING_LOGO
            await pong.delete()
            msg = await bot.send_file(pong.chat_id, logo, caption=output)
            await asyncio.sleep(500)
            await msg.delete()
        except BaseException:
            await pong.edit(
                output + "\n\n *Logo Yang Disediakan Tidak Valid."
                "\nPastikan Tautan Yang Anda Gunakan Valid"
            )
            await asyncio.sleep(100)
            await pong.delete()
    else:
        await pong.edit(output)
        await asyncio.sleep(100)
        await pong.delete()
     
