# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot start point """

import sys
from importlib import import_module

from userbot import ALIVE_NAME, BOT_VER, BOTLOG_CHATID, LOGS, UPSTREAM_REPO_BRANCH, bot
from userbot.modules import ALL_MODULES
from userbot.utils.tools import ya_kali_ngga

try:
    for module_name in ALL_MODULES:
        imported_module = import_module("userbot.modules." + module_name)
    bot.start()
    LOGS.info(f"👩‍💻ZHU-USERBOT👩‍💻 ⚙️ V{BOT_VER} [ TELAH DIAKTIFKAN! ]")
except BaseException as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)


async def userbot_on():
    try:
        if BOTLOG_CHATID != 0:
            await bot.send_message(
                BOTLOG_CHATID,
                f"**👩‍💻 ZHU-USERBOT** Berhasil Diaktfikan\n\n**🧰 BOT VERSI :** {BOT_VER} ZHU\n**👩‍💻 OWNER BOT :** [𝗭𝗛𝗨](https://t.me/TripleNineee)\n🏷️** SUPPORT :** [𝗚𝗥𝗢𝗨𝗣](https://t.me/Kenzusupport)\n**🔗 CHANNEL :** [𝗖𝗛𝗔𝗡𝗡𝗘𝗟](https://t.me/inibotsaya)",
            )
    except Exception as e:
        LOGS.info(str(e))


bot.loop.run_until_complete(userbot_on())
bot.loop.run_until_complete(ya_kali_ngga())
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
