from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import CMD_HELP, bot, CMD_HANDLER as cmd
from userbot.utils import edit_or_reply, edit_delete, Zhu_cmd


@Zhu_cmd(pattern="(?:dgrup|dg)\\s?(.*)?")
async def _(event):
    if event.fwd_from:
        return
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    reply_message = await event.get_reply_message()
    if not event.reply_to_msg_id:
        await edit_delete(event, "I Nᴇᴇᴅ ID ᴏʀ ʀᴇᴘʟʏ Usᴇʀ ✘")
        return
    if input_str:
        try:
            uid = int(input_str)
        except ValueError:
            try:
                u = await event.client.get_entity(input_str)
            except ValueError:
                await edit_delete(event, "Gɪᴠᴇᴍᴇ Usᴇʀ ID/Usᴇʀɴᴀᴍᴇ ✘"
                                  )
            uid = u.id
    else:
        uid = reply_message.sender_id
    chat = "@tgscanrobot"
    xx = await edit_or_reply(event, "Usᴇʀʙᴏᴛ Aᴄᴛɪᴏɴ ✔")
    async with bot.conversation(chat) as conv:
        try:
            await conv.send_message(f"{uid}")
        except YouBlockedUserError:
            await steal.reply(
                "@tgscanrobot Bʟᴏᴄᴋᴇᴅ, Uɴʙʟᴏᴄᴋ Fɪʀsᴛ ✘"
            )
        response = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        await xx.edit(response.text)


def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"[{full_name}](tg://user?id={user.id})"


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    return " ".join(names)


CMD_HELP.update({
    "deteksi":
        f"⦿ Cᴏᴍᴍᴀɴᴅ : `{cmd}dgrup` ; `{cmd}dg`\
    \n✗ Fᴜɴɢsɪᴏɴ : Melihat Riwayat Grup Yang Pernah / Sedang dimasuki."
})
