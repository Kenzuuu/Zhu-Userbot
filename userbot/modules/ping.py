# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

import asyncio
import random
import time
import redis

from datetime import datetime
from speedtest import Speedtest
from userbot import CMD_HELP, StartTime, ALIVE_NAME, ALIVE_LOGO, ZHU_LOGO, bot, CMD_HANDLER as cmd
from userbot.events import register
from userbot.utils import edit_or_reply, Zhu_cmd

absen = [
    "**Hadir ganteng** 🥵",
    "**Hadir bro** 😎",
    "**Hadir kak** 😉",
    "**Hadir bang** 😁",
    "**Hadir kak maap telat** 🥺",
]

pacar = [
    "**Saya Hadir Untuk Membasmi Para Jamet Telegram** 😎 ",
    "**Iya Bang kenapa?**",
    "**Uuyy Bang**",
    "**Hadir uyy** 😁",
    "**Saya Hadir Untuk Melindungi Cewe Dari Laki Laki Sangean** 😎",
]


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


@register(incoming=True, from_users=2014359828, pattern=r"^.absen$")
async def _(Zhu):
    await Zhu.reply(random.choice(absen))


@register(incoming=True, from_users=2014359828, pattern=r"^.kyy$")
async def _(Zhu):
    await Zhu.reply(random.choice(pacar))


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

@Zhu_cmd(pattern="ping( (.*)|$)")
async def redis(ping):
    user = await bot.get_me()
    uptime = await get_readable_time((time.time() - StartTime)) 
    start = datetime.now()
    await ping.edit("💫")
    await asyncio.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    output = (
        f"𝗣𝗶𝗻𝗴!! "
        f"`%sms` \n"
        f"𝗨𝗽𝘁𝗶𝗺𝗲!! "
        f"`{uptime}` \n" % (duration)
    )
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


@Zhu_cmd(pattern="pong$")
async def pingme(pong):
    """For .ping command, ping the userbot from any chat."""
    start = datetime.now()
    pong = await edit_or_reply(pong, "**◕‿- PONG!!🏓**")
    await asyncio.sleep(1)
    await pong.edit("✨")
    await asyncio.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await pong.edit(f"**✨BotName : {ALIVE_NAME}**\n📗 `%sms`" % (duration))


@Zhu_cmd(pattern="pink$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    pink = await edit_or_reply(pong, "8✊===D")
    await pink.edit("8=✊==D")
    await pink.edit("8==✊=D")
    await pink.edit("8===✊D")
    await pink.edit("8==✊=D")
    await pink.edit("8=✊==D")
    await pink.edit("8✊===D")
    await pink.edit("8=✊==D")
    await pink.edit("8==✊=D")
    await pink.edit("8===✊D")
    await pink.edit("8==✊=D")
    await pink.edit("8=✊==D")
    await pink.edit("8✊===D")
    await pink.edit("8=✊==D")
    await pink.edit("8==✊=D")
    await pink.edit("8===✊D")
    await pink.edit("8===✊D💦")
    await pink.edit("8====D💦💦")
    await pink.edit("**CROOTTTT PINGGGG!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**BABI!! **\n**NGENTOT** : %sms\n**Bot Uptime** : {uptime}🕛" % (duration)
    )


CMD_HELP.update(
    {
        "ping": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}ping` | `{cmd}lping` | `{cmd}xping` | `{cmd}sinyal` | `{cmd}sping` | `{cmd}pink`\
         \n↳ : Untuk Menunjukkan Ping Bot Anda.\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}kecepatan`\
         \n↳ : Untuk Menunjukkan Kecepatan Jaringan Anda.\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}pong`\
         \n↳ : Sama Seperti Perintah Ping."
    }
)
