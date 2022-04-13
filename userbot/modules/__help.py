import logging

from userbot import BOT_USERNAME
from userbot.events import register
from userbot.utils import edit_or_reply, Zhu_cmd

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.WARNING)


@Zhu_cmd(pattern="helpme( (.*)|$)")
async def yardim(event):
    try:
        tgbotusername = BOT_USERNAME
        if tgbotusername is not None:
            results = await event.client.inline_query(tgbotusername, "@TripleNineee")
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        else:
            await event.edit(
                "`🔐 Can't Find Your Bot, Please go to @botfather`"
            )
    except Exception:
        return await event.edit(
            "`🔐 Error, Please send code .inlineon`"
        )
