# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot start point """

import sys
from importlib import import_module

import requests
from telethon.tl.functions.channels import InviteToChannelRequest as Addbot

from userbot import (
    BOTLOG_CHATID,
    BOT_USERNAME,
    BOT_TOKEN,
    BOT_VER,
    LOGS,
    ALIVE_NAME,
    ZhuUserbot,
    bot,
    call_py,
)
from userbot.modules import ALL_MODULES
from userbot.utils import autobot

try:
    bot.start()
    call_py.start()
    user = bot.get_me()
    ZhuUserbot = requests.get(
        "https://raw.githubusercontent.com/Kenzhu02/ZhuBlacklist/Blacklist/ZhuUserbot.json"
    ).json()
    if user.id in ZhuUserbot:
        LOGS.warning(
            "🔰 Zhu-Userbot\nID anda Sudah dilaporkan dan masuk dalam Daftar Hitam/nAjukan banding di @Kenzusupport"
        )
        sys.exit(1)
except Exception as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

LOGS.info(
    f"Jika {ALIVE_NAME} Membutuhkan Bantuan, Silahkan Tanyakan di Grup https://t.me/Kenzusupport")
LOGS.info(
    f"🔰 ZHU-USERBOT  [Telah Aktif]\n\n👾Bot Versi : V{BOT_VER}")


async def check_alive():
    try:
        if BOTLOG_CHATID != 0:
            await bot.send_message(BOTLOG_CHATID, "**🔰 ZHU USERBOT** Berhasil Diaktifkan!!\n\n **Versi ** : V{BOT_VER}\n📒 **Group support : [𝗚𝗥𝗢𝗨𝗣](https://t.me/Kenzusupport)\n 👩‍💻 **Owner Bot :** [𝗭𝗛𝗨](https://t.me/triplenineee)\n\n🏷️ Gunakan perintah **.help** Untuk mempelajari fitur **🔰 ZHU-USERBOT**")
    except Exception as e:
        LOGS.info(str(e))
    try:
        await bot(Addbot(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass

bot.loop.run_until_complete(check_alive())
if not BOT_TOKEN:
    LOGS.info(
        "BOT_TOKEN Vars tidak terisi, Memulai Membuat BOT Otomatis di @Botfather..."
    )
    bot.loop.run_until_complete(autobot())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
