# Port By @IDnyaKosong From Kyy-Userbot
# # Copyright (C) 2021 Kyy-Userbot

from userbot.utils import edit_or_reply, edit_delete, Zhu_cmd
from userbot import CMD_HELP, CMD_HANDLER as cmd
import asyncio


@Zhu_cmd(pattern="ftyping(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await edit_delete(event, "Iɴᴄᴏʀʀᴇᴄᴛ ғᴏʀᴍᴀᴛ ✘")
    await edit_or_reply(event, f"sᴛᴀʀᴛ Fᴀᴋᴇ ᴛʏᴘɪɴɢ ғᴏʀ {t} Sᴇᴄᴏɴᴅ.")
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(t)


@Zhu_cmd(pattern="faudio(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await edit_delete(event, "Iɴᴄᴏʀʀᴇᴄᴛ ғᴏʀᴍᴀᴛ ✘")
    await edit_or_reply(event, f"Sᴛᴀʀᴛ ʀᴇᴄᴏʀᴅɪɴɢ ғᴀᴋᴇ ᴀᴜᴅɪᴏ ғᴏʀ {t} Sᴇᴄᴏɴᴅ")
    async with event.client.action(event.chat_id, "record-audio"):
        await asyncio.sleep(t)


@Zhu_cmd(pattern="fvideo(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await edit_delete(event, "Iɴᴄᴏʀʀᴇᴄᴛ ғᴏʀᴍᴀᴛ ✘")
    await edit_or_reply(event, f"Sᴛᴀʀᴛ ʀᴇᴄᴏʀᴅɪɴɢ ғᴀᴋᴇ ᴠɪᴅᴇᴏ ғᴏʀ {t} sᴇᴄᴏɴᴅ ")
    async with event.client.action(event.chat_id, "record-video"):
        await asyncio.sleep(t)


@Zhu_cmd(pattern="fgame(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await edit_delete(event, "Iɴᴄᴏʀʀᴇᴄᴛ ғᴏʀᴍᴀᴛ ✘")
    await edit_or_reply(event, f"Sᴛᴀʀᴛ ᴘʟᴀʏɪɴɢ ғᴀᴋᴇ ɢᴀᴍᴇ ғᴏʀ {t} Sᴇᴄᴏᴜɴᴅ")
    async with event.client.action(event.chat_id, "game"):
        await asyncio.sleep(t)


@Zhu_cmd(pattern="fround(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await edit_delete(event, "Iɴᴄᴏʀʀᴇᴄᴛ ғᴏʀᴍᴀᴛ ✘")
    xx = await edit_delete(event, f"Sᴛᴀʀᴛ ʀᴇᴄᴏʀᴅɪɴɢ ғᴀᴋᴇ ᴠɪᴅᴇᴏ ᴍᴇssᴀɢᴇ ғᴏʀ {t} Sᴇᴄᴏɴᴅ")
    await asyncio.sleep(3)
    await xx.delete()
    async with event.client.action(event.chat_id, "record-round"):
        await asyncio.sleep(t)


@Zhu_cmd(pattern="fphoto(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await edit_delete(event, "Iɴᴄᴏʀʀᴇᴄᴛ ғᴏʀᴍᴀᴛ ✘")
    xx = await edit_or_reply(event, f"Sᴛᴀʀᴛ sᴇɴᴅɪɴɢ ғᴀᴋᴇ ᴘɪᴄᴛᴜʀᴇ ғᴏʀ {t} Sᴇᴄᴏɴᴅ")
    await asyncio.sleep(3)
    await xx.delete()
    async with event.client.action(event.chat_id, "photo"):
        await asyncio.sleep(t)


@Zhu_cmd(pattern="fdocument(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await edit_delete(event, "Iɴᴄᴏʀʀᴇᴄᴛ ғᴏʀᴍᴀᴛ ✘")
    xx = edit_or_reply(
        event, f"Sᴛᴀʀᴛ sᴇɴᴅɪɴɢ ғᴀᴋᴇ ᴅᴏᴄᴜᴍᴇɴᴛ ғᴏʀ {t} Sᴇᴄᴏɴᴅ")
    await asyncio.sleep(3)
    await xx.delete()
    async with event.client.action(event.chat_id, "document"):
        await asyncio.sleep(t)


@Zhu_cmd(pattern="flocation(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await edit_delete(event, "Iɴᴄᴏʀʀᴇᴄᴛ ғᴏʀᴍᴀᴛ ✘")
    xx = await edit_or_reply(event, f"Sᴛᴀʀᴛ ғᴀᴋᴇ ʟᴏᴄᴀᴛɪᴏɴ ғᴏʀ {t} Sᴇᴄᴏɴᴅ")
    await asyncio.sleep(3)
    await xx.delete()
    async with event.client.action(event.chat_id, "location"):
        await asyncio.sleep(t)


@Zhu_cmd(pattern="fcontact(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await edit_delete(event, "Iɴᴄᴏʀʀᴇᴄᴛ ғᴏʀᴍᴀᴛ ✘")
    xx = await edit_or_reply(event, f"Sᴛᴀʀᴛ sᴇɴᴅɪɴɢ ғᴀᴋᴇ ᴄᴏɴᴛᴀᴄ ғᴏʀ {t} Sᴇᴄᴏɴᴅ")
    await asyncio.sleep(3)
    await xx.delete()
    async with event.client.action(event.chat_id, "contact"):
        await asyncio.sleep(t)


CMD_HELP.update({
    "fakeaction":
    f"⦿ Cᴏᴍᴍᴀɴᴅ : `{cmd}ftyping` <jumlah teks>\
   \n✗ Fᴜɴɢsɪᴏɴ : Seakan akan sedang mengetik padahal tidak\
   \n\n⦿ Cᴏᴍᴍᴀɴᴅ : `{cmd}faudio` <jumlah teks>\
   \n✗ Fᴜɴɢsɪᴏɴ : Berfungsi sama seperti ftyping tapi ini dalam bentuk fake audio\
   \n\n⦿ Cᴏᴍᴍᴀɴᴅ : `{cmd}video` <jumlah teks>\
   \n✗ Fᴜɴɢsɪᴏɴ : Berfungsi sama seperti ftyping tapi ini dalam bentuk fake video\
   \n\n⦿ Cᴏᴍᴍᴀɴᴅ : `{cmd}fgame` <jumlah teks>\
   \n✗ Fᴜɴɢsɪᴏɴ : Berfungsi sama seperti ftyping tapi ini dalam bentuk fake game\
   \n\n⦿ Cᴏᴍᴍᴀɴᴅ : `{cmd}fphoto` <jumlah teks>\
   \n✗ Fᴜɴɢsɪᴏɴ : Berfungsi sama seperti ftyping tapi ini dalam bentuk fake foto\
   \n\n⦿ Cᴏᴍᴍᴀɴᴅ : `{cmd}fdocument` <jumlah teks>\
   \n✗ Fᴜɴɢsɪᴏɴ : Berfungsi sama seperti ftyping tapi ini dalam bentuk fake document\
   \n\n⦿ Cᴏᴍᴍᴀɴᴅ : `{cmd}flocation` <jumlah teks>\
   \n✗ Fᴜɴɢsɪᴏɴ : Berfungsi sama seperti ftyping tapi ini dalam bentuk fake location\
   \n\n⦿ Cᴏᴍᴍᴀɴᴅ : `{cmd}fcontact` <jumlah teks>\
   \n✗ Fᴜɴɢsɪᴏɴ : Berfungsi sama seperti ftyping tapi ini dalam bentuk fake contact"
})
