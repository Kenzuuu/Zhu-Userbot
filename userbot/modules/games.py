from userbot import CMD_HELP, bot
from userbot.events import register


@register(outgoing=True, pattern=r"^\.xogame(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    botusername = "@xobot"
    noob = "play"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, noob)
    await tap[0].click(event.chat_id)
    await event.delete()


@register(outgoing=True, pattern=r"^\.whisp(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    wwwspr = event.pattern_match.group(1)
    botusername = "@whisperBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, wwwspr)
    await tap[0].click(event.chat_id)
    await event.delete()


@register(outgoing=True, pattern=r"^\.mod(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    modr = event.pattern_match.group(1)
    botusername = "@PremiumAppBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, modr)
    await tap[0].click(event.chat_id)
    await event.delete()

CMD_HELP.update({
    "games": "\
⦿ Cᴏᴍᴍᴀɴᴅ : `.xogame`\
\n✗ Fᴜɴɢsɪᴏɴ : Mainkan game XO bersama temanmu.\
\n\n⦿ Cᴏᴍᴍᴀɴᴅ : `.mod <nama app>`\
\n✗ Fᴜɴɢsɪᴏɴ : Dapatkan applikasi mod\
\n\n⦿ Cᴏᴍᴍᴀɴᴅ : `.whisp <teks> <username/ID>`\
\n✗ Fᴜɴɢsɪᴏɴ : Berikan pesan rahasia"})
