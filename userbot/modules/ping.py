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

@register(outgoing=True, pattern=r"^\.repo$")
async def redis(repo):
    user = await bot.get_me()
    await get_readable_time((time.time() - StartTime))
    await repo.edit("💥")
    await asyncio.sleep(2)
    output = (
        f"**[★ REPO ★](https://github.com/kenzuuu/Zhu-Userbot)**\n"
        f"**[★ BRANCH ★](https://t.me/triplenineee)**\n"
        f"**Bot of :** {ALIVE_NAME} \n"
         )
    if REPO_LOGO:
        try:
            logo = REPO_LOGO
            await repo.delete()
            msg = await bot.send_file(repo.chat_id, logo, caption=output)
            await asyncio.sleep(500)
            await msg.delete()
        except BaseException:
            await repo.edit(
                output + "\n\n *Logo Yang Disediakan Tidak Valid."
                "\nPastikan Tautan Yang Anda Gunakan Valid"
            )
            await asyncio.sleep(100)
            await repo.delete()
    else:
        await repo.edit(output)
        await asyncio.sleep(100)
        await repo.delete()

@register(outgoing=True, pattern="^.ping$")
@register(incoming=True, from_users=DEVS, pattern=r"^.cping$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("💝")
    await asyncio.sleep(3)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**Pong !!** `%sms` \n"
        f"**Uptime **- `{uptime}`\n" % (duration)
    )
