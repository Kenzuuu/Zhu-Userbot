# nyenyenyenye
# FROM skyzu-userbot <https://github.com/Skyzu/skyzu-userbot>

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest

from userbot import CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import edit_or_reply, Zhu_cmd

chat = "@BotFather"


@Zhu_cmd(pattern="botbaru ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        text, username = event.pattern_match.group(1).split()

    else:
        await edit_or_reply(event, "Gɪᴠᴇ ᴍᴇ Bᴏᴛ Nᴀᴍᴇ ᴀɴᴅ Bᴏᴛ Usᴇʀɴᴀᴍᴇ")
        return

    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/newbot")
            audio = await conv.get_response()
            await conv.send_message(text)
            audio = await conv.get_response()
            await conv.send_message(username)
            audio = await conv.get_response()
            await event.client.forward_messages(event.chat_id, audio)
            await event.delete()
        except YouBlockedUserError:
            await event.client(UnblockRequest("93372553"))
            await conv.send_message("/newbot")
            audio = await conv.get_response()
            await conv.send_message(text)
            audio = await conv.get_response()
            await conv.send_message(username)
            audio = await conv.get_response()
            await event.client.forward_messages(event.chat_id, audio)
            await event.delete()


CMD_HELP.update(
    {
        "botfather": f"⧉ Mᴏᴅᴜʟᴇ : Bᴏᴛғᴀᴛʜᴇʀ\
        \n\n⦿ Cᴏᴍᴍᴀɴᴅ : `{cmd}botbaru` <bot_name> <bot_username>\
        \n  ✗ Fᴜɴɢsɪᴏɴ : Untuk membuat bot di @botfather."
}
)
