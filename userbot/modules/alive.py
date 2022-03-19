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




@register(outgoing=True, pattern=r"^\.(?:alive)\s?(.)?")
async def amireallyalive(alive):
    await bot.get_me()
    await get_readable_time((time.time() - StartTime))
    output = (
        f"• ᴏᴡɴᴇʀ : [Zhu](t.me/triplenineee)             ㅤ \n"
        f"• ꜱʏꜱᴛᴇᴍ. : Ubuntu 20.10            \n"
        f"• ᴛᴇʟᴇᴛʜᴏɴ : v.{version.__version__}                ㅤㅤ  \n"
        f"• ᴘʏᴛʜᴏɴ. : v.{python_version()} ㅤㅤ\n"
        f"• ʙᴏᴛ : v.{BOT_VER}                ㅤㅤㅤ \n"
        f"• ᴍᴏᴅᴜʟᴇ : {len(modules)} ㅤㅤㅤㅤㅤㅤㅤ   \n"
    )
    if ALIVE_LOGO:
        try:
            logo = ALIVE_LOGO
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
