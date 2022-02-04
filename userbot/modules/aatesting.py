# Credit to @triplenineee
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

import asyncio
import time
import os
from datetime import datetime

import redis

from userbot import DEVS, StartTime
from userbot.events import register

LOVE_IMG = os.environ.get(
    "PING_PIC", "https://telegra.ph/file/bc6244cbc8574b6a0afac.jpg"
)


@register(outgoing=True, pattern="^.aping$")
@register(incoming=True, from_users=DEVS, pattern=r"^.cping$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("💝")
    await asyncio.sleep(3)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    if LOVE_IMG:
        Love_caption = (
            f"**Pong !!** `%sms` \n"
            f"**Uptime **- `{uptime}`\n" % (duration)
        )
    await pong.edit(LOVE_IMG, caption=Love_caption)
    await pong.delete()
