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
    BOT_VER,
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

@register(outgoing=True, pattern=r"^\.userbot$")
async def redis(versi):
    user = await bot.get_me()
    uptime = await get_readable_time((time.time() - StartTime)) 
    start = datetime.now()
    await versi.edit("😡")
    await asyncio.sleep(2)
    end = datetime.now()
    output = (
        f"★ REPO ZHU-USERBOT :\n➡ [𝗗𝗜𝗦𝗜𝗡𝗜](https://github.com/Kenzuuu/Zhu-Userbot) \n\n"
        f"★ DEPLOY VIA BOT :\n➡ [𝗗𝗜𝗦𝗜𝗡𝗜](https://telegram.dog/XTZ_HerokuBot?start=S2VuenV1dS9aaHUtVXNlcmJvdCBLZW56aHU)\n\n"
        f"★ DEPLOY VIA WEB :\n➡ [𝗗𝗜𝗦𝗜𝗡𝗜](heroku.com/deploy?template=https://github.com/Kenzuuu/Zhu-Userbot)\n\n"
        f"★ AMBIL API KEY :\n➡ [𝗗𝗜𝗦𝗜𝗡𝗜](https://t.me/ZhuXScrapperBot)\n\n"
        f"★ AMBIL STRING :\n➡ [𝗗𝗜𝗦𝗜𝗡𝗜](https://t.me/ZhuXSessionBot)\n"
    if ZHU_LOGO:
        try:
            logo = ZHU_LOGO
            await versi.delete()
            msg = await bot.send_file(versi.chat_id, logo, caption=output)
            await asyncio.sleep(500)
            await msg.delete()
        except BaseException:
            await versi.edit(
                output + "\n\n *Logo Yang Disediakan Tidak Valid."
                "\nPastikan Tautan Yang Anda Gunakan Valid"
            )
            await asyncio.sleep(100)
            await versi.delete()
    else:
        await versi.edit(output)
        await asyncio.sleep(100)
        await versi.delete()
