# Copyright (C) 2020  sandeep.n(π.$)
# button post makker for catuserbot thanks to uniborg for the base
# by @sandy1709 (@mrconfused)
# Man-Userbot

import re

from telethon import Button

from userbot import BOT_USERNAME
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import edit_delete, Zhu_cmd, reply_id

# regex obtained from:
# https://github.com/PaulSonOfLars/tgbot/blob/master/tg_bot/modules/helper_funcs/string_handling.py#L23
BTN_URL_REGEX = re.compile(
    r"(\[([^\[]+?)\]\<buttonurl:(?:/{0,2})(.+?)(:same)?\>)")


@Zhu_cmd(pattern="button(?:\\s|$)([\\s\\S]*)")
async def _(event):
    reply_to_id = await reply_id(event)
    reply_message = await event.get_reply_message()
    if reply_message:
        markdown_note = reply_message.text
    else:
        markdown_note = "".join(event.text.split(maxsplit=1)[1:])
    if not markdown_note:
        return await edit_delete(
            event, "Gɪᴠᴇᴍᴇ ᴀɴʏ ᴛᴇxᴛ"
        )
    catinput = "Inline buttons " + markdown_note
    results = await event.client.inline_query(BOT_USERNAME, catinput)
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    await event.delete()


def build_keyboard(buttons):
    keyb = []
    for btn in buttons:
        if btn[2] and keyb:
            keyb[-1].append(Button.url(btn[0], btn[1]))
        else:
            keyb.append([Button.url(btn[0], btn[1])])
    return keyb


CMD_HELP.update(
    {
        "button": f"⧉ Mᴏᴅᴜʟᴇ : `button`\
        \n\n  ⦿ Cᴏᴍᴍᴀɴᴅ `{cmd}button` <text> [Name on button]<buttonurl:link you want to open>\
        \n  ✗ Fᴜɴɢsɪᴏɴ : Untuk membuat pesan button melalui inline\
        \n  ✔ Exᴀᴍᴘʟᴇs : `{cmd}button test [Rᴇᴘᴏ]<buttonurl:http://github.com/kenzuuu/Zhu-Userbot> [Cʜᴀɴɴᴇʟ]<buttonurl:https://t.me/inibotsaya:same> [Sᴜᴘᴘᴏʀᴛ]<buttonurl:https://t.me/Kenzusupport>`\
    "
    }
)
