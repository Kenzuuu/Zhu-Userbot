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
                caption="ð¢ **ð­ðð¨-ð¨ð¦ðð¥ðð¢ð§ Has Been Actived**!!\nâââââââââââââââ\nâ  **Userbot Version** - 1.1 Â©Zhu\nâââââââââââââââ\nâ  **Powered By:** @TripleNineee ",
                buttons=[(Button.url("ê±á´á´á´á´Êá´", "https://t.me/Kenzusupport"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
