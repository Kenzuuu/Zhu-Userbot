# Ported by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/Lunatic0de & t.me/SharingUserbot

import os
import random

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import edit_delete, edit_or_reply, Zhu_cmd
from userbot.utils.misc import Carbon

from .vcg import vcmention

all_col = [
    "Black",
    "Navy",
    "DarkBlue",
    "MediumBlue",
    "Blue",
    "DarkGreen",
    "Green",
    "Teal",
    "DarkCyan",
    "DeepSkyBlue",
    "DarkTurquoise",
    "MediumSpringGreen",
    "Lime",
    "SpringGreen",
    "Aqua",
    "Cyan",
    "MidnightBlue",
    "DodgerBlue",
    "LightSeaGreen",
    "ForestGreen",
    "SeaGreen",
    "DarkSlateGray",
    "DarkSlateGrey",
    "LimeGreen",
    "MediumSeaGreen",
    "Turquoise",
    "RoyalBlue",
    "SteelBlue",
    "DarkSlateBlue",
    "MediumTurquoise",
    "Indigo  ",
    "DarkOliveGreen",
    "CadetBlue",
    "CornflowerBlue",
    "RebeccaPurple",
    "MediumAquaMarine",
    "DimGray",
    "DimGrey",
    "SlateBlue",
    "OliveDrab",
    "SlateGray",
    "SlateGrey",
    "LightSlateGray",
    "LightSlateGrey",
    "MediumSlateBlue",
    "LawnGreen",
    "Chartreuse",
    "Aquamarine",
    "Maroon",
    "Purple",
    "Olive",
    "Gray",
    "Grey",
    "SkyBlue",
    "LightSkyBlue",
    "BlueViolet",
    "DarkRed",
    "DarkMagenta",
    "SaddleBrown",
    "DarkSeaGreen",
    "LightGreen",
    "MediumPurple",
    "DarkViolet",
    "PaleGreen",
    "DarkOrchid",
    "YellowGreen",
    "Sienna",
    "Brown",
    "DarkGray",
    "DarkGrey",
    "LightBlue",
    "GreenYellow",
    "PaleTurquoise",
    "LightSteelBlue",
    "PowderBlue",
    "FireBrick",
    "DarkGoldenRod",
    "MediumOrchid",
    "RosyBrown",
    "DarkKhaki",
    "Silver",
    "MediumVioletRed",
    "IndianRed ",
    "Peru",
    "Chocolate",
    "Tan",
    "LightGray",
    "LightGrey",
    "Thistle",
    "Orchid",
    "GoldenRod",
    "PaleVioletRed",
    "Crimson",
    "Gainsboro",
    "Plum",
    "BurlyWood",
    "LightCyan",
    "Lavender",
    "DarkSalmon",
    "Violet",
    "PaleGoldenRod",
    "LightCoral",
    "Khaki",
    "AliceBlue",
    "HoneyDew",
    "Azure",
    "SandyBrown",
    "Wheat",
    "Beige",
    "WhiteSmoke",
    "MintCream",
    "GhostWhite",
    "Salmon",
    "AntiqueWhite",
    "Linen",
    "LightGoldenRodYellow",
    "OldLace",
    "Red",
    "Fuchsia",
    "Magenta",
    "DeepPink",
    "OrangeRed",
    "Tomato",
    "HotPink",
    "Coral",
    "DarkOrange",
    "LightSalmon",
    "Orange",
    "LightPink",
    "Pink",
    "Gold",
    "PeachPuff",
    "NavajoWhite",
    "Moccasin",
    "Bisque",
    "MistyRose",
    "BlanchedAlmond",
    "PapayaWhip",
    "LavenderBlush",
    "SeaShell",
    "Cornsilk",
    "LemonChiffon",
    "FloralWhite",
    "Snow",
    "Yellow",
    "LightYellow",
    "Ivory",
    "White",
]


@Zhu_cmd(pattern="(rc|c)arbon")
async def crbn(event):
    from_user = vcmention(event.sender)
    xxxx = await edit_or_reply(event, "Usᴇʀʙᴏᴛ Aᴄᴛɪᴏɴ ✔")
    te = event.text
    col = random.choice(all_col) if te[1] == "r" else "Grey"
    if event.reply_to_msg_id:
        temp = await event.get_reply_message()
        if temp.media:
            b = await event.client.download_media(temp)
            with open(b) as a:
                code = a.read()
            os.remove(b)
        else:
            code = temp.message
    else:
        try:
            code = event.text.split(" ", maxsplit=1)[1]
        except IndexError:
            return await edit_delete(
                xxxx, "Rᴇᴘʟʏ ᴛᴇxᴛ ғᴏʀ ᴄᴀʀʙᴏɴɪsᴇᴅ", 30
            )
    xx = await Carbon(code=code, file_name="carbon_man", backgroundColor=col)
    await xxxx.delete()
    await event.reply(
        f"Cᴀʀʙᴏɴɪsᴇᴅ Bʏ : {from_user}",
        file=xx,
    )


@Zhu_cmd(pattern="ccarbon ?(.*)")
async def crbn(event):
    from_user = vcmention(event.sender)
    match = event.pattern_match.group(1).strip()
    if not match:
        return await edit_or_reply(
            event, "Cᴏʟᴏʀ Nᴏᴛ ғᴏᴜɴᴅ ✘"
        )
    msg = await edit_or_reply(event, "Usᴇʀʙᴏᴛ Aᴄᴛɪᴏɴ ✔")
    if event.reply_to_msg_id:
        temp = await event.get_reply_message()
        if temp.media:
            b = await event.client.download_media(temp)
            with open(b) as a:
                code = a.read()
            os.remove(b)
        else:
            code = temp.message
    else:
        try:
            match = match.split(" ", maxsplit=1)
            code = match[1]
            match = match[0]
        except IndexError:
            return await edit_delete(
                msg, "Rᴇᴘʟʏ ᴛᴇxᴛ ғᴏʀ ᴄᴀʀʙᴏɴɪsᴇᴅ", 30
            )
    xx = await Carbon(code=code, backgroundColor=match)
    await msg.delete()
    await event.reply(
        f"Cᴀʀʙᴏɴɪsᴇᴅ Bʏ : {from_user}",
        file=xx,
    )


CMD_HELP.update(
    {
        "carbon": f"⧉ Mᴏᴅᴜʟᴇ : `carbon`\
        \n\n⦿ Cᴏᴍᴍᴀɴᴅ : `{cmd}carbon` <text/reply>\
        \n  ✗ Fᴜɴɢsɪᴏɴ : Carbonisasi teks dengan pengaturan default.\
        \n\n⦿ Cᴏᴍᴍᴀɴᴅ : `{cmd}rcarbon` <text/reply>\
        \n  ✗ Fᴜɴɢsɪᴏɴ : Carbonisasi teks, dengan warna background acak.\
        \n\n⦿ Cᴏᴍᴍᴀɴᴅ : `{cmd}ccarbon` <warna> <text/reply>\
        \n  ✗ Fᴜɴɢsɪᴏɴ : Carbonisasi teks, dengan warna background custom.\
    "
    }
)
