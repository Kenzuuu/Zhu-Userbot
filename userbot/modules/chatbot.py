# 🍀 © @tofik_dn
# ⚠️ Do not remove credits

import requests
from googletrans import Translator
from telethon import events
from telethon.tl.types import User

from userbot import CMD_HELP, LOGS, bot
from userbot import CMD_HANDLER as cmd
from userbot.utils import edit_or_reply, Zhu_cmd
from userbot.modules.sql_helper.tede_chatbot_sql import is_tede, rem_tede, set_tede

translator = Translator()
LANGUAGE = "id"

url = "https://api-tede.herokuapp.com/api/chatbot?message={message}"


async def ngapain_rep(message):
    hayulo_link_apa = url.format(message=message)
    try:
        data = requests.get(hayulo_link_apa)
        if data.status_code == 200:
            return (data.json())["msg"]
        else:
            LOGS.info("Eʀʀᴏʀ : API ᴄʜᴀᴛʙᴏᴛ Dᴏᴡɴ, Rᴇᴘᴏʀᴛ ᴛᴏ @Kenzusupport.")
    except Exception as e:
        LOGS.info(str(e))


async def chat_bot_toggle(event):
    status = event.pattern_match.group(1).lower()
    chat_id = event.chat_id
    if status == "on":
        if not is_tede(chat_id):
            set_tede(chat_id)
            return await edit_or_reply(event, "Cʜᴀᴛʙᴏᴛ Aᴄᴛɪᴠᴀᴛᴇᴅ ✔")
        await event.edit("Cʜᴀᴛʙᴏᴛ Aʟʀᴇᴀᴅʏ Aᴄᴛɪᴠᴀᴛᴇᴅ ✔")
    elif status == "off":
        if is_tede(chat_id):
            rem_tede(chat_id)
            return await edit_or_reply(event, "Cʜᴀᴛʙᴏᴛ Nᴏɴᴀᴄᴛɪᴠᴇ ✘")
        await event.edit("Cʜᴀᴛʙᴏᴛ Aʟʀᴇᴀᴅʏ ɴᴏɴᴀᴄᴛɪᴠᴇ ✘")
    else:
        await edit_or_reply(event, "Usᴀɢᴇ : `{cmd}chatbot` <on/off>")


@Zhu_cmd(pattern="chatbot(?: |$)(.*)")
async def on_apa_off(event):
    await chat_bot_toggle(event)


@bot.on(
    events.NewMessage(
        incoming=True,
        func=lambda e: (e.mentioned),
    ),
)
async def tede_chatbot(event):
    sender = await event.get_sender()
    if not is_tede(event.chat_id):
        return
    if not isinstance(sender, User):
        return
    if event.text:
        rep = await ngapain_rep(event.message.message)
        tr = translator.translate(rep, LANGUAGE)
        if tr:
            await event.reply(tr.text)
        else:
            await event.reply(rep)


CMD_HELP.update(
    {
        "chatbot": f"Mᴏᴅᴜʟᴇ : **`chatbot`\
      \n\n⦿ Cᴏᴍᴍᴀɴᴅ : `{cmd}chatbot` <on/off>\
      \n  ✗ Fᴜɴɢsɪᴏɴ : Untuk membalas chat dengan chatbot AI.\
      "
    }
)
