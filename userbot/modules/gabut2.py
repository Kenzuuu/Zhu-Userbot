from time import sleep
from userbot import CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import Zhu_cmd


@Zhu_cmd(pattern='zhu(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hai Perkenalkan Namaku Zhu`")
    sleep(3)
    await typew.edit("`20 Tahun`")
    sleep(1)
    await typew.edit("`Tinggal Di rumah 😁😁, Salam Kenal:)`")
# Create by myself @localheart


@Zhu_cmd(pattern='sayang(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`Aku Sayang Kamu`")
    sleep(1)
    await typew.edit("`I LOVE YOU 💞`")
# Create by myself @localheart


@Zhu_cmd(pattern='semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Bernapas`")
    sleep(1)
    await typew.edit("`Dan Selalu Bersyukur`")
# Create by myself @localheart


CMD_HELP.update({
    "oi": f"⦿ Cᴏᴍᴍᴀɴᴅ : `{cmd}zhu`\
    \n✗ Fᴜɴɢsɪᴏɴ : perkenalan Zhu\
    \n\n⦿ Cᴏᴍᴍᴀɴᴅ : `{cmd}sayang`\
    \n✗ Fᴜɴɢsɪᴏɴ : Gombalan maut`\
    \n\n⦿ Cᴏᴍᴍᴀɴᴅ : `{cmd}semangat`\
    \n✗ Fᴜɴɢsɪᴏɴ : Jan Lupa Semangat."
})
