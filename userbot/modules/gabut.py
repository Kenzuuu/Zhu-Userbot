from platform import uname
from userbot import ALIVE_NAME, CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import Zhu_cmd

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@Zhu_cmd(pattern="p(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ`")
# Salam


@Zhu_cmd(pattern="l(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ`")
# Menjawab Salam


@Zhu_cmd(pattern="istigfar(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit("`اَسْتَغْفِرُاللهَ الْعَظِيْم`")
# Istigfar


@Zhu_cmd(pattern="perkenalan(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`Hai Guys , Perkenalkan Nama Gw {DEFAULTUSER}`")
    sleep(2)
    await event.edit(f"`Gw Tinggal Di {WEATHER_DEFCITY}`")
    sleep(2)
    await event.edit("`Salam Kenal...`")
    sleep(2)
    await event.edit("`Udah Gitu Aja :v`")
# Perkenalan


CMD_HELP.update({
    "gabut": f" ⧠ Mᴏᴅᴜʟᴇ : `Gabut`\
    \n\n⦿ Cᴏᴍᴍᴀɴᴅ : `{cmd}l`\
    \n✗ Fᴜɴɢsɪᴏɴ : Untuk Menjawab Salam\
    \n\n⦿ Cᴏᴍᴍᴀɴᴅ : `{cmd}perkenalan`\
    \n✗ Fᴜɴɢsɪᴏɴ : Memperkenalkan Diri\
    \n\n⦿ Cᴏᴍᴍᴀɴᴅ : `{cmd}p`\
    \n✗ Fᴜɴɢsɪᴏɴ : Untuk Memberi Salam."
})
