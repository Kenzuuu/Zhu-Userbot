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

from userbot import CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import edit_or_reply, edit_delete, Zhu_cmd
from userbot.events import register

GCAST_BLACKLIST = [
    -1001380293847,  # NastySupport
    -1001473548283,  # SharingUserbot
    -1001578091827,  # PrimeSupportGroup
    -1001752592753,  # SkyzuSupport
    -1001430568914,  # FlicksSupport
    -1001267233272,  # PocongUserbot
    -1001736842222,  # Kenzusupport
    -1001687155877,  # CilikSupport
]


@Zhu_cmd(pattern="gcast(?: |$)(.*)")
async def gcast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        return await edit_delete(event, "Gɪᴠᴇᴍᴇ ᴍᴇssᴀɢᴇ ᴏʀ ʀᴇᴘʟʏ ᴍᴇssᴀɢᴇ ✘")
    kk = await edit_or_reply(event, "Usᴇʀʙᴏᴛ Gᴄᴀsᴛ Sᴛᴀʀᴛɪɴɢ ✔")
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
        f"Sᴇɴᴅ ᴛᴏ `{done}` Gʀᴏᴜᴘ, Eʀʀᴏʀ sᴇɴᴅ `{er}` Gʀᴏᴜᴘ."
    )


@Zhu_cmd(pattern="gucast(?: |$)(.*)")
async def gucast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        return await edit_delete(event, "Gɪᴠᴇᴍᴇ ᴍᴇssᴀɢᴇ ᴏʀ ʀᴇᴘʟʏ ᴍᴇssᴀɢᴇ ✘")
    kk = await edit_or_reply(event, "Usᴇʀʙᴏᴛ Gᴜᴄᴀsᴛ Sᴛᴀʀᴛɪɴɢ ✔")
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
        f"Sᴇɴᴅ ᴛᴏ `{done}` Cʜᴀᴛs, Eʀʀᴏʀ sᴇɴᴅ `{er}` Cʜᴀᴛs"
    )


CMD_HELP.update(
    {
        "gcast": f"⧠ Mᴏᴅᴜʟᴇ : `gcast`\
        \n\n⦿ Cᴏᴍᴍᴀɴᴅ : `{cmd}gcast` <text/reply media>\
        \n✗ Fᴜɴɢsɪᴏɴ : Mengirim Global Broadcast pesan ke Seluruh Grup yang kamu masuk. (Bisa Mengirim Media/Sticker)\
        \n\n⦿ Cᴏᴍᴍᴀɴᴅ : `{cmd}gucast` <text/reply media>\
        \n✗ Fᴜɴɢsɪᴏɴ : Mengirim Global Broadcast pesan ke Seluruh Private Massage / PC yang masuk. (Bisa Mengirim Media/Sticker)\
    "
    }
)
