# Credit to @triplenineee
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

import asyncio
import time
from datetime import datetime

import redis

from userbot import DEVS, StartTime
from userbot.events import register

LOVE_IMG = os.environ.get(
    "PING_PIC", "https://te.legra.ph/file/a59da36828333262c9848.jpg"
)


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
