from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.utils import edit_or_reply, edit_delete, Zhu_cmd
from userbot import bot, CMD_HELP, CMD_HANDLER as cmd


@Zhu_cmd(pattern="getid(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await edit_delete(event, "Rᴇᴘʟʏ ᴍᴇssᴀɢᴇ ✘")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await edit_delete(event, "Rᴇᴘʟʏ ᴍᴇssᴀɢᴇ ✘")
        return
    chat = "@getidsbot"
    reply_message.sender
    if reply_message.sender.bot:
        await edit_delete(event, "Rᴇᴘʟʏ ᴍᴇssᴀɢᴇ ✘")
        return
    xx = await edit_or_reply(event, "Fɪɴᴅɪɴɢ ID ✔")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1663258664))
            await bot.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("Usᴇʀʙᴏᴛ ᴇʀʀᴏʀ ✘")
            return
        if response.text.startswith("Forward"):
            await xx.edit("ID Nᴏᴛ ғɪɴᴅ")
        else:
            await xx.edit(f"{response.message.message}")


CMD_HELP.update({
    "getid":
    f"⦿ Cᴏᴍᴍᴀɴᴅ : `{cmd}getid`"
    "\n✗ Fᴜɴɢsɪᴏɴ : Balas Ke Pesan Pengguna Untuk Mendapatkan ID Nya."
})
