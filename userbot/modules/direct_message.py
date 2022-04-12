from userbot.utils import edit_delete, edit_or_reply, Zhu_cmd
from userbot import CMD_HELP, CMD_HANDLER as cmd


@Zhu_cmd(pattern="(?:dm)\\s?(.*)?")
async def remoteaccess(event):

    p = event.pattern_match.group(1)
    m = p.split(" ")

    chat_id = m[0]
    try:
        chat_id = int(chat_id)
    except BaseException:

        pass

    msg = ""
    mssg = await event.get_reply_message()
    if event.reply_to_msg_id:
        await event.client.send_message(chat_id, mssg)
        await edit_or_reply(event, "Sᴜᴄᴄᴇss ✔")
    for i in m[1:]:
        msg += i + " "
    if msg == "":
        return
    try:
        await event.client.send_message(chat_id, msg)
        await edit_or_reply(event, "Sᴜᴄᴄᴇss ✔")
    except BaseException:
        await edit_delete(event, "Eʀʀᴏʀ : Mᴇssᴀɢᴇ Nᴏᴛ sᴇɴᴅ ✘")

CMD_HELP.update(
    {
        "message": f"⦿ Cᴏᴍᴍᴀɴᴅ : `{cmd}dm`\
    \n✗ Fᴜɴɢsɪᴏɴ : Mengirim Pesan Dengan Jarak Jauh Dengan .dm <username> <pesan>."
    })
