# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
#
# Ported by Koala @manusiarakitann
# Recode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

from userbot import CMD_HELP
from userbot.events import register

GCAST_BLACKLIST = [
    -1001473548283,  # SharingUserbot
    -1001433238829,  # TedeSupport
    -1001476936696,  # AnosSupport
    -1001327032795,  # UltroidSupport
    -1001294181499,  # UserBotIndo
    -1001419516987,  # VeezSupportGroup
    -1001209432070,  # GeezSupportGroup
    -1001296934585,  # X-PROJECT BOT
    -1001481357570,  # UsergeOnTopic
    -1001459701099,  # CatUserbotSupport
    -1001109837870,  # TelegramBotIndonesia
    -1001752592753,  # Skyzusupport
    -1001736842222,  # Kenzusupport
    -1001380293847,  # Kyysupport
    -1001286943203,  # StaryGloss
]


@register(outgoing=True, pattern=r"^\.gcast(?: |$)(.*)")
async def gcast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit("𝐴𝑝𝑎 𝑦𝑎𝑛𝑔 ℎ𝑎𝑟𝑢𝑠 𝑠𝑎𝑦𝑎 𝑘𝑖𝑟𝑖𝑚? 😭")
        return
    kk = await event.edit("𝑀𝑒𝑛𝑔𝑖𝑟𝑖𝑚 𝑝𝑒𝑠𝑎𝑛 𝑔𝑙𝑜𝑏𝑎𝑙 𝐺𝑟𝑜𝑢𝑝 . . .")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                if chat not in GCAST_BLACKLIST:
                    await event.client.send_message(chat, msg)
                    done += 1
                elif chat not in GCAST_BLACKLIST:
                    pass
            except BaseException:
                er += 1
    await kk.edit(
        f"𝗚𝗰𝗮𝘀𝘁 :\n\n✅ 𝐁𝐞𝐫𝐡𝐚𝐬𝐢𝐥 : `{done}` Group\n𝐆𝐚𝐠𝐚𝐥 : `{er}` Group"
    )


@register(outgoing=True, pattern=r"^\.gucast(?: |$)(.*)")
async def gucast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit("𝐴𝑝𝑎 𝑦𝑎𝑛𝑔 ℎ𝑎𝑟𝑢𝑠 𝑠𝑎𝑦𝑎 𝑘𝑖𝑟𝑖𝑚? 😭")
        return
    kk = await event.edit("𝑀𝑒𝑛𝑔𝑖𝑟𝑖𝑚 𝑝𝑒𝑠𝑎𝑛 𝑔𝑙𝑜𝑏𝑎𝑙 . . .")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                done += 1
                await event.client.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(
        f"𝗚𝗰𝗮𝘀𝘁 :\n\n✅ 𝐁𝐞𝐫𝐡𝐚𝐬𝐢𝐥 : `{done}` Orang\n𝐆𝐚𝐠𝐚𝐥 : `{er}` Orang"
    )


CMD_HELP.update(
    {
        "gcast": "**Plugin : **`gcast`\
        \n\n  •  **Syntax :** `.gcast` <text/reply media>\
        \n  •  **Function : **Mengirim Global Broadcast pesan ke Seluruh Grup yang kamu masuk. (Bisa Mengirim Media/Sticker)\
    "
    }
)


CMD_HELP.update(
    {
        "gucast": "**Plugin : **`gucast`\
        \n\n  •  **Syntax :** `.gucast` <text/reply media>\
        \n  •  **Function : **Mengirim Global Broadcast pesan ke Seluruh Private Massage / PC yang masuk. (Bisa Mengirim Media/Sticker)\
    "
    }
)
