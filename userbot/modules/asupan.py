# 🍀 © @tofik_dn
# ⚠️ Do not remove credits


from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import Zhu_cmd
import random
from userbot import owner
from telethon.tl.types import InputMessagesFilterVideo


@Zhu_cmd(pattern="asupan$")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@AsupanZhu", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"Asᴜᴘᴀɴ Bʏ : [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan video asupan.")


CMD_HELP.update(
    {
        "asupan": f"Mᴏᴅᴜʟᴇ : `asupan`\
        \n\n  ✗ Cᴏᴍᴍᴀɴᴅ : `{cmd}asupan`\
        \n  ✗ Fᴜɴɢsɪᴏɴ : Untuk Mengirim video asupan secara random.\
    "
    }
)
