from telethon import Button

from userbot import BOTLOG, BOTLOG_CHATID, LOGS, tgbot


async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/02f87cca391f9b9d627d5.jpg",
                caption="💢 **𝗭𝗛𝗨-𝗨𝗦𝗘𝗥𝗕𝗢𝗧 Has Been Actived**!!\n━━━━━━━━━━━━━━━\n➠ **Userbot Version** - 1.1 ©Zhu\n━━━━━━━━━━━━━━━\n➠ **Powered By:** @TripleNineee ",
                buttons=[(Button.url("ꜱᴜᴘᴘᴏʀᴛ", "https://t.me/Kenzusupport"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
