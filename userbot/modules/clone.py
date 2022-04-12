# Coded by KenHV
# Recode by @mrismanaziz
# FORM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import DeletePhotosRequest, UploadProfilePhotoRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import InputPhoto

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, LOGS, STORAGE
from userbot.utils import Zhu_cmd

if not hasattr(STORAGE, "userObj"):
    STORAGE.userObj = False


@Zhu_cmd(pattern=r"clone ?(.*)")
async def impostor(event):
    inputArgs = event.pattern_match.group(1)

    if "restore" in inputArgs:
        await event.edit("Usᴇʀʙᴏᴛ Aᴄᴛɪᴏɴ ✔")
        if not STORAGE.userObj:
            return await event.edit(
                "Nᴏᴛ ɪɴ ᴄʟᴏɴᴇ ✘"
            )
        await updateProfile(STORAGE.userObj, restore=True)
        return await event.edit("Rᴇsᴛᴏʀᴇ Dᴏɴᴇ ✔")
    if inputArgs:
        try:
            user = await event.client.get_entity(inputArgs)
        except BaseException:
            return await event.edit("Iɴᴠᴀʟɪᴅ Usᴇʀ ✘")
        userObj = await event.client(GetFullUserRequest(user))
    elif event.reply_to_msg_id:
        replyMessage = await event.get_reply_message()
        if replyMessage.sender_id is None:
            return await event.edit("Cᴀɴ'ᴛ Cʟᴏɴᴇ Aɴᴏɴɪᴍ Aᴅᴍɪɴ ✘")
        userObj = await event.client(GetFullUserRequest(replyMessage.sender_id))
    else:
        return await event.edit("Usᴀɢᴇ: `{cmd}help clone` Fᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ")

    if not STORAGE.userObj:
        STORAGE.userObj = await event.client(GetFullUserRequest(event.sender_id))

    LOGS.info(STORAGE.userObj)

    await event.edit("Usᴇʀʙᴏᴛ Aᴄᴛɪᴏɴ ✔")
    await updateProfile(userObj)
    await event.edit("Cʟᴏɴᴇ Sᴜᴄᴄᴇss ✔")


async def updateProfile(userObj, restore=False):
    firstName = (
        "Deleted Account"
        if userObj.user.first_name is None
        else userObj.user.first_name
    )
    lastName = "" if userObj.user.last_name is None else userObj.user.last_name
    userAbout = userObj.about if userObj.about is not None else ""
    userAbout = "" if len(userAbout) > 70 else userAbout
    if restore:
        userPfps = await bot.get_profile_photos("me")
        userPfp = userPfps[0]
        await bot(
            DeletePhotosRequest(
                id=[
                    InputPhoto(
                        id=userPfp.id,
                        access_hash=userPfp.access_hash,
                        file_reference=userPfp.file_reference,
                    )
                ]
            )
        )
    else:
        try:
            userPfp = userObj.profile_photo
            pfpImage = await bot.download_media(userPfp)
            await bot(UploadProfilePhotoRequest(await bot.upload_file(pfpImage)))
        except BaseException:
            pass
    await bot(
        UpdateProfileRequest(about=userAbout, first_name=firstName, last_name=lastName)
    )


CMD_HELP.update(
    {
        "clone": f"Mᴏᴅᴜʟᴇ : `clone`\
        \n\n⦿ Cᴏᴍᴍᴀɴᴅ : `{cmd}clone` <reply/username/ID>\
        \n  ✗ Fᴜɴɢsɪᴏɴ : Untuk mengclone identitas dari username/ID Telegram yang diberikan.\
        \n\n⦿ Cᴏᴍᴍᴀɴᴅ : `{cmd}clone restore`\
        \n  ✗ Fᴜɴɢsɪᴏɴ : Mengembalikan ke identitas asli anda.\
        \n\n♻ Nᴏᴛᴇ : `{cmd}clone restore` terlebih dahulu sebelum mau nge `{cmd}clone` lagi.\
    "
    }
)
