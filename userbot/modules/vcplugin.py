# Credits: @mrismanaziz
# Thanks To @tofik_dn || https://github.com/tofikdn
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

from pytgcalls import StreamType
from pytgcalls.types import Update
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.input_stream.quality import (
    HighQualityAudio,
    HighQualityVideo,
    LowQualityVideo,
    MediumQualityVideo,
)
from telethon.tl import types
from telethon.utils import get_display_name
from youtubesearchpython import VideosSearch

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot import PLAY_PIC as fotoplay
from userbot import QUEUE_PIC as ngantri
from userbot import call_py
from userbot.utils import bash, edit_delete, edit_or_reply, Zhu_cmd
from userbot.utils.chattitle import CHAT_TITLE
from userbot.utils.queues.queues import (
    QUEUE,
    add_to_queue,
    clear_queue,
    get_queue,
    pop_an_item,
)
from userbot.utils.thumbnail import gen_thumb


def vcmention(user):
    full_name = get_display_name(user)
    if not isinstance(user, types.User):
        return full_name
    return f"[{full_name}](tg://user?id={user.id})"


def ytsearch(query: str):
    try:
        search = VideosSearch(query, limit=1).result()
        data = search["result"][0]
        songname = data["title"]
        url = data["link"]
        duration = data["duration"]
        thumbnail = f"https://i.ytimg.com/vi/{data['id']}/hqdefault.jpg"
        return [songname, url, duration, thumbnail]
    except Exception as e:
        print(e)
        return 0


async def ytdl(format: str, link: str):
    stdout, stderr = await bash(f'yt-dlp -g -f "{format}" {link}')
    if stdout:
        return 1, stdout.split("\n")[0]
    return 0, stderr


async def skip_item(chat_id: int, x: int):
    if chat_id not in QUEUE:
        return 0
    chat_queue = get_queue(chat_id)
    try:
        songname = chat_queue[x][0]
        chat_queue.pop(x)
        return songname
    except Exception as e:
        print(e)
        return 0


async def skip_current_song(chat_id: int):
    if chat_id not in QUEUE:
        return 0
    chat_queue = get_queue(chat_id)
    if len(chat_queue) == 1:
        await call_py.leave_group_call(chat_id)
        clear_queue(chat_id)
        return 1
    songname = chat_queue[1][0]
    url = chat_queue[1][1]
    link = chat_queue[1][2]
    type = chat_queue[1][3]
    RESOLUSI = chat_queue[1][4]
    if type == "Audio":
        await call_py.change_stream(
            chat_id,
            AudioPiped(
                url,
            ),
        )
    elif type == "Video":
        if RESOLUSI == 720:
            hm = HighQualityVideo()
        elif RESOLUSI == 480:
            hm = MediumQualityVideo()
        elif RESOLUSI == 360:
            hm = LowQualityVideo()
        await call_py.change_stream(
            chat_id, AudioVideoPiped(url, HighQualityAudio(), hm)
        )
    pop_an_item(chat_id)
    return [songname, link, type]


@Zhu_cmd(pattern="play(?:\\s|$)([\\s\\S]*)")
async def vc_play(event):
    title = event.pattern_match.group(1)
    replied = await event.get_reply_message()
    sender = await event.get_sender()
    chat = await event.get_chat()
    chat_id = event.chat_id
    from_user = vcmention(event.sender)
    if (
        replied
        and not replied.audio
        and not replied.voice
        and not title
        or not replied
        and not title
    ):
        return await edit_or_reply(event, "𝗚𝗶𝘃𝗲𝗺𝗲 𝘀𝗼𝗻𝗴 𝗻𝗮𝗺𝗲 ✘")
    elif replied and not replied.audio and not replied.voice or not replied:
        botman = await edit_or_reply(event, "𝗦𝗲𝗮𝗿𝗰𝗵𝗶𝗻𝗴 𝗦𝗼𝗻𝗴 . . .")
        query = event.text.split(maxsplit=1)[1]
        search = ytsearch(query)
        if search == 0:
            await botman.edit(
                "𝗘𝗿𝗿𝗼𝗿 : 𝗖𝗮𝗻'𝘁 𝗙𝗶𝗻𝗱 𝘀𝗼𝗻𝗴 ✘"
            )
        else:
            songname = search[0]
            title = search[0]
            url = search[1]
            duration = search[2]
            thumbnail = search[3]
            userid = sender.id
            titlegc = chat.title
            ctitle = await CHAT_TITLE(titlegc)
            thumb = await gen_thumb(thumbnail, title, userid, ctitle)
            format = "best[height<=?720][width<=?1280]"
            hm, ytlink = await ytdl(format, url)
            if hm == 0:
                await botman.edit(f"`{ytlink}`")
            elif chat_id in QUEUE:
                pos = add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                caption = f"💡 𝗤𝘂𝗲𝘂𝗲 » `#{pos}`\n\n🏷 𝗦𝗼𝗻𝗴: [{songname}]({url})\n⏱ 𝗗𝘂𝗿𝗮𝘁𝗶𝗼𝗻: `{duration}`\n👩‍💻 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝗕𝘆: {from_user}"
                await botman.delete()
                await event.client.send_file(chat_id, thumb, caption=caption)
            else:
                try:
                    await call_py.join_group_call(
                        chat_id,
                        AudioPiped(
                            ytlink,
                        ),
                        stream_type=StreamType().pulse_stream,
                    )
                    add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                    caption = f"🏷 𝗦𝗼𝗻𝗴: [{songname}]({url})\n⏱ 𝗗𝘂𝗿𝗮𝘁𝗶𝗼𝗻: `{duration}`\n👩‍💻 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝗕𝘆 : {from_user}"
                    await botman.delete()
                    await event.client.send_file(chat_id, thumb, caption=caption)
                except Exception as ep:
                    clear_queue(chat_id)
                    await botman.edit(f"`{ep}`")

    else:
        botman = await edit_or_reply(event, "📥 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗶𝗻𝗴")
        dl = await replied.download_media()
        link = f"https://t.me/c/{chat.id}/{event.reply_to_msg_id}"
        if replied.audio:
            songname = "Telegram Music Player"
        elif replied.voice:
            songname = "Voice Note"
        if chat_id in QUEUE:
            pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            caption = f"💡 𝗤𝘂𝗲𝘂𝗲 »** `#{pos}`\n\n🏷 𝗦𝗼𝗻𝗴: [{songname}]({link})\n👥 𝗖𝗵𝗮𝘁 𝗜𝗗 `{chat_id}`\n🎧 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝗕𝘆: {from_user}"
            await event.client.send_file(chat_id, ngantri, caption=caption)
            await botman.delete()
        else:
            try:
                await call_py.join_group_call(
                    chat_id,
                    AudioPiped(
                        dl,
                    ),
                    stream_type=StreamType().pulse_stream,
                )
                add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                caption = f"🏷️ 𝗦𝗼𝗻𝗴: [{songname}]({link})\n👥 𝗖𝗵𝗮𝘁 𝗜𝗗: `{chat_id}`\n👩‍💻 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝗕𝘆: {from_user}"
                await event.client.send_file(chat_id, fotoplay, caption=caption)
                await botman.delete()
            except Exception as ep:
                clear_queue(chat_id)
                await botman.edit(f"`{ep}`")


@Zhu_cmd(pattern="vplay(?:\\s|$)([\\s\\S]*)")
async def vc_vplay(event):
    title = event.pattern_match.group(1)
    replied = await event.get_reply_message()
    sender = await event.get_sender()
    userid = sender.id
    chat = await event.get_chat()
    titlegc = chat.title
    chat_id = event.chat_id
    from_user = vcmention(event.sender)
    if (
        replied
        and not replied.video
        and not replied.document
        and not title
        or not replied
        and not title
    ):
        return await edit_or_reply(event, "𝗚𝗶𝘃𝗲𝗺𝗲 𝗩𝗶𝗱𝗲𝗼 𝗻𝗮𝗺𝗲 ✘")
    if replied and not replied.video and not replied.document:
        xnxx = await edit_or_reply(event, "𝗦𝗲𝗮𝗿𝗰𝗵𝗶𝗻𝗴 𝗩𝗶𝗱𝗲𝗼 . . .")
        query = event.text.split(maxsplit=1)[1]
        search = ytsearch(query)
        RESOLUSI = 720
        hmmm = HighQualityVideo()
        if search == 0:
            await xnxx.edit(
                "𝗘𝗿𝗿𝗼𝗿 : 𝗖𝗮𝗻'𝘁 𝗙𝗶𝗻𝗱 𝘀𝗼𝗻𝗴 ✘"
            )
        else:
            songname = search[0]
            title = search[0]
            url = search[1]
            duration = search[2]
            thumbnail = search[3]
            ctitle = await CHAT_TITLE(titlegc)
            thumb = await gen_thumb(thumbnail, title, userid, ctitle)
            format = "best[height<=?720][width<=?1280]"
            hm, ytlink = await ytdl(format, url)
            if hm == 0:
                await xnxx.edit(f"`{ytlink}`")
            elif chat_id in QUEUE:
                pos = add_to_queue(
                    chat_id, songname, ytlink, url, "Video", RESOLUSI)
                caption = f"💡 𝗤𝘂𝗲𝘂𝗲 » `#{pos}`\n\n🏷 𝗦𝗼𝗻𝗴: [{songname}]({url})\n⏱ 𝗗𝘂𝗿𝗮𝘁𝗶𝗼𝗻: `{duration}`\n👩‍💻 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝗕𝘆: {from_user}"
                await xnxx.delete()
                await event.client.send_file(chat_id, thumb, caption=caption)
            else:
                try:
                    await call_py.join_group_call(
                        chat_id,
                        AudioVideoPiped(ytlink, HighQualityAudio(), hmmm),
                        stream_type=StreamType().pulse_stream,
                    )
                    add_to_queue(
                        chat_id,
                        songname,
                        ytlink,
                        url,
                        "Video",
                        RESOLUSI)
                    await xnxx.edit(
                        f"🏷 𝗦𝗼𝗻𝗴: [{songname}]({url})\n⏱ 𝗗𝘂𝗿𝗮𝘁𝗶𝗼𝗻: `{duration}`\n👩‍💻 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝗕𝘆: {from_user}",
                        link_preview=False,
                    )
                except Exception as ep:
                    clear_queue(chat_id)
                    await xnxx.edit(f"`{ep}`")

    elif replied:
        xnxx = await edit_or_reply(event, "📥 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗶𝗻𝗴")
        dl = await replied.download_media()
        link = f"https://t.me/c/{chat.id}/{event.reply_to_msg_id}"
        if len(event.text.split()) < 2:
            RESOLUSI = 720
        else:
            pq = event.text.split(maxsplit=1)[1]
            RESOLUSI = int(pq)
        if replied.video or replied.document:
            songname = "Telegram Video Player"
        if chat_id in QUEUE:
            pos = add_to_queue(chat_id, songname, dl, link, "Video", RESOLUSI)
            caption = f"💡 𝗤𝘂𝗲𝘂𝗲 »** `#{pos}`\n\n🏷 𝗦𝗼𝗻𝗴: [{songname}]({link})\n👥 𝗖𝗵𝗮𝘁 𝗜𝗗 `{chat_id}`\n🎧 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝗕𝘆: {from_user}"
            await event.client.send_file(chat_id, ngantri, caption=caption)
            await xnxx.delete()
        else:
            if RESOLUSI == 360:
                hmmm = LowQualityVideo()
            elif RESOLUSI == 480:
                hmmm = MediumQualityVideo()
            elif RESOLUSI == 720:
                hmmm = HighQualityVideo()
            try:
                await call_py.join_group_call(
                    chat_id,
                    AudioVideoPiped(dl, HighQualityAudio(), hmmm),
                    stream_type=StreamType().pulse_stream,
                )
                add_to_queue(chat_id, songname, dl, link, "Video", RESOLUSI)
                caption = f"🏷 𝗦𝗼𝗻𝗴: [{songname}]({link})\n👥 𝗖𝗵𝗮𝘁 𝗜𝗗: `{chat_id}`\n🎧 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝗕𝘆 : {from_user}"
                await xnxx.delete()
                await event.client.send_file(chat_id, fotoplay, caption=caption)
            except Exception as ep:
                clear_queue(chat_id)
                await xnxx.edit(f"`{ep}`")
    else:
        xnxx = await edit_or_reply(event, "𝗨𝘀𝗲𝗿𝗯𝗼𝘁 𝗔𝗰𝘁𝗶𝗼𝗻 ✅")
        query = event.text.split(maxsplit=1)[1]
        search = ytsearch(query)
        RESOLUSI = 720
        hmmm = HighQualityVideo()
        if search == 0:
            await xnxx.edit("𝗘𝗿𝗿𝗼𝗿 : 𝗖𝗮𝗻'𝘁 𝗙𝗶𝗻𝗱 𝗦𝗼𝗻𝗴 ✘")
        else:
            songname = search[0]
            title = search[0]
            url = search[1]
            duration = search[2]
            thumbnail = search[3]
            ctitle = await CHAT_TITLE(titlegc)
            thumb = await gen_thumb(thumbnail, title, userid, ctitle)
            format = "best[height<=?720][width<=?1280]"
            hm, ytlink = await ytdl(format, url)
            if hm == 0:
                await xnxx.edit(f"`{ytlink}`")
            elif chat_id in QUEUE:
                pos = add_to_queue(
                    chat_id, songname, ytlink, url, "Video", RESOLUSI)
                caption = f"💡 𝗤𝘂𝗲𝘂𝗲 »** `#{pos}`\n\n🏷 𝗦𝗼𝗻𝗴 : [{songname}]({url})\n⏱ 𝗗𝘂𝗿𝗮𝘁𝗶𝗼𝗻: `{duration}``\n👩‍💻 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝗕𝘆:** {from_user}"
                await xnxx.delete()
                await event.client.send_file(chat_id, thumb, caption=caption)
            else:
                try:
                    await call_py.join_group_call(
                        chat_id,
                        AudioVideoPiped(ytlink, HighQualityAudio(), hmmm),
                        stream_type=StreamType().pulse_stream,
                    )
                    add_to_queue(
                        chat_id,
                        songname,
                        ytlink,
                        url,
                        "Video",
                        RESOLUSI)
                    caption = f"🏷 𝗦𝗼𝗻𝗴 : [{songname}]({url})\n⏱ 𝗗𝘂𝗿𝗮𝘁𝗶𝗼𝗻: `{duration}``\n👩‍💻 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝗕𝘆:** {from_user}"
                    await xnxx.delete()
                    await event.client.send_file(chat_id, thumb, caption=caption)
                except Exception as ep:
                    clear_queue(chat_id)
                    await xnxx.edit(f"`{ep}`")


@Zhu_cmd(pattern="end$")
async def vc_end(event):
    chat_id = event.chat_id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await edit_or_reply(event, "𝗦𝘁𝗼𝗽𝗲𝗱 𝗔𝗰𝘁𝗶𝗼𝗻 ✅")
        except Exception as e:
            await edit_delete(event, f"𝗘𝗿𝗿𝗼𝗿 : `{e}`")
    else:
        await edit_delete(event, "𝗘𝗿𝗿𝗼𝗿 : 𝗣𝗹𝗮𝘆 𝗳𝗶𝗿𝘀𝘁 ✘")


@Zhu_cmd(pattern="skip(?:\\s|$)([\\s\\S]*)")
async def vc_skip(event):
    chat_id = event.chat_id
    if len(event.text.split()) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await edit_delete(event, "𝗘𝗿𝗿𝗼𝗿 : 𝗣𝗹𝗮𝘆 𝗙𝗶𝗿𝘀𝘁 ✘")
        elif op == 1:
            await edit_delete(event, "Empty queue, Userbot Leave ✘", 10)
        else:
            await edit_or_reply(
                event,
                f"**⏭ 𝖭𝖾𝗑𝗍**\n**🎧 𝖭𝗈𝗐 𝖯𝗅𝖺𝗒𝗂𝗇𝗀** - [{op[0]}]({op[1]})",
                link_preview=False,
            )
    else:
        skip = event.text.split(maxsplit=1)[1]
        DELQUE = "𝗨𝗽𝗱𝗮𝘁𝗶𝗻𝗴 𝗣𝗹𝗮𝘆𝗹𝗶𝘀𝘁 ✅"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x != 0:
                    hm = await skip_item(chat_id, x)
                    if hm != 0:
                        DELQUE = DELQUE + "\n" + f"**#{x}** - {hm}"
            await event.edit(DELQUE)


@Zhu_cmd(pattern="pause$")
async def vc_pause(event):
    chat_id = event.chat_id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await edit_or_reply(event, "𝗣𝗮𝘂𝘀𝗲 𝗔𝗰𝘁𝗶𝗼𝗻 ✅")
        except Exception as e:
            await edit_delete(event, f"𝗘𝗿𝗿𝗼𝗿 : `{e}`")
    else:
        await edit_delete(event, "𝗘𝗿𝗿𝗼𝗿 : 𝗣𝗹𝗮𝘆 𝗙𝗶𝗿𝘀𝘁 ✘")


@Zhu_cmd(pattern="resume$")
async def vc_resume(event):
    chat_id = event.chat_id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await edit_or_reply(event, "𝗥𝗲𝘀𝘂𝗺𝗲 𝗔𝗰𝘁𝗶𝗼𝗻 ✅")
        except Exception as e:
            await edit_or_reply(event, f"𝗘𝗿𝗿𝗼𝗿 : `{e}`")
    else:
        await edit_delete(event, "𝗘𝗿𝗿𝗼𝗿 : 𝗣𝗹𝗮𝘆 𝗙𝗶𝗿𝘀𝘁 ✘")


@Zhu_cmd(pattern=r"volume(?: |$)(.*)")
async def vc_volume(event):
    query = event.pattern_match.group(1)
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    chat_id = event.chat_id

    if not admin and not creator:
        return await edit_delete(event, f"𝗘𝗿𝗿𝗼𝗿 : 𝗔𝗱𝗺𝗶𝗻 𝗙𝗶𝗿𝘀𝘁 ✘", 30)

    if chat_id in QUEUE:
        try:
            await call_py.change_volume_call(chat_id, volume=int(query))
            await edit_or_reply(
                event, f"𝗩𝗼𝗹𝘂𝗺𝗲 𝘀𝗲𝘁 𝘁𝗼 : `{query}%`"
            )
        except Exception as e:
            await edit_delete(event, f"𝗘𝗿𝗿𝗼𝗿 : `{e}`", 30)
    else:
        await edit_delete(event, "𝗘𝗿𝗿𝗼𝗿 : 𝗣𝗹𝗮𝘆 𝗙𝗶𝗿𝘀𝘁 ✘")


@Zhu_cmd(pattern="playlist$")
async def vc_playlist(event):
    chat_id = event.chat_id
    if chat_id in QUEUE:
        chat_queue = get_queue(chat_id)
        if len(chat_queue) == 1:
            await edit_or_reply(
                event,
                f"**🎧 𝗣𝗹𝗮𝘆𝗶𝗻𝗴 :**\n• [{chat_queue[0][0]}]({chat_queue[0][2]}) | `{chat_queue[0][3]}`",
                link_preview=False,
            )
        else:
            PLAYLIST = f"**🎧 𝗣𝗹𝗮𝘆𝗶𝗻𝗴 :**\n**• [{chat_queue[0][0]}]({chat_queue[0][2]})** | `{chat_queue[0][3]}` \n\n**⦿ 𝗣𝗹𝗮𝘆𝗹𝗶𝘀𝘁 :**"
            l = len(chat_queue)
            for x in range(1, l):
                hmm = chat_queue[x][0]
                hmmm = chat_queue[x][2]
                hmmmm = chat_queue[x][3]
                PLAYLIST = PLAYLIST + "\n" + \
                    f"**#{x}** - [{hmm}]({hmmm}) | `{hmmmm}`"
            await edit_or_reply(event, PLAYLIST, link_preview=False)
    else:
        await edit_delete(event, "𝗘𝗿𝗿𝗼𝗿 : 𝗣𝗹𝗮𝘆 𝗙𝗶𝗿𝘀𝘁 ✘")


#credits by @vckyaz < vicky \>
# FROM GeezProjects < https://github.com/vckyou/GeezProjects \>
# ambil boleh apus credits jangan ya ka:)

@Zhu_cmd(pattern="joinvc(?: |$)(.*)")
async def join_(event):
    xnxx = await edit_or_reply(event, f"𝗨𝘀𝗲𝗿𝗯𝗼𝘁 𝗔𝗰𝘁𝗶𝗼𝗻 ✅")
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        try:
            chat = await event.client(GetFullUserRequest(chat))
        except Exception as e:
            await edit_delete(event, f"𝗨𝘀𝗲𝗿𝗯𝗼𝘁 𝗲𝗿𝗿𝗼𝗿 ✘ : `{e}`", 30)
    else:
        chat = event.chat_id
        vcmention(event.sender)
    if not call_py.is_connected:
        await call_py.start()
    await call_py.join_group_call(
        chat,
        AudioPiped(
            'http://duramecho.com/Misc/SilentCd/Silence01s.mp3'
        ),
        stream_type=StreamType().pulse_stream,
    )
    try:
        await xnxx.edit("𝘜𝘴𝘦𝘳𝘣𝘰𝘵 𝘑𝘰𝘪𝘯𝘦𝘥 ✅")
    except Exception as ex:
        await edit_delete(event, f"𝗨𝘀𝗲𝗿𝗯𝗼𝘁 𝗲𝗿𝗿𝗼𝗿 ✘ : `{ex}`")


@Zhu_cmd(pattern="leavevc(?: |$)(.*)")
async def leavevc(event):
    """ leave video chat """
    xnxx = await edit_or_reply(event, "𝗨𝘀𝗲𝗿𝗯𝗼𝘁 𝗔𝗰𝘁𝗶𝗼𝗻 ✅")
    chat_id = event.chat_id
    from_user = vcmention(event.sender)
    if from_user:
        try:
            await call_py.leave_group_call(chat_id)
        except (NotInGroupCallError, NoActiveGroupCall):
            pass
        await xnxx.edit("𝘜𝘴𝘦𝘳𝘣𝘰𝘵 𝘓𝘦𝘢𝘷𝘦 ✘")
    else:
        await edit_delete(event, f"𝗘𝗿𝗿𝗼𝗿 : 𝗝𝗼𝗶𝗻 𝗙𝗶𝗿𝘀𝘁 ✘ ")

@call_py.on_stream_end()
async def stream_end_handler(_, u: Update):
    chat_id = u.chat_id
    print(chat_id)
    await skip_current_song(chat_id)


@call_py.on_closed_voice_chat()
async def closedvc(_, chat_id: int):
    if chat_id in QUEUE:
        clear_queue(chat_id)


@call_py.on_left()
async def leftvc(_, chat_id: int):
    if chat_id in QUEUE:
        clear_queue(chat_id)


@call_py.on_kicked()
async def kickedvc(_, chat_id: int):
    if chat_id in QUEUE:
        clear_queue(chat_id)


CMD_HELP.update(
    {
        "vcplugin": f"⧠ 𝗠𝗼𝗱𝘂𝗹𝗲:`vcplugin`\
        \n\n┍☯ 𝗖𝗼𝗺𝗺𝗮𝗻𝗱: `{cmd}play` 𝗝𝘂𝗱𝘂𝗹\
        \n┕☯ 𝗙𝘂𝗻𝗴𝘀𝗶𝗼𝗻: 𝖬𝖾𝗆𝗎𝗍𝖺𝗋 𝗅𝖺𝗀𝗎\
        \n\n┍☯ 𝗖𝗼𝗺𝗺𝗮𝗻𝗱: `{cmd}vplay` 𝗝𝘂𝗱𝘂𝗹\
        \n┕☯ 𝗙𝘂𝗻𝗴𝘀𝗶𝗼𝗻: 𝖬𝖾𝗆𝗎𝗍𝖺𝗋 𝖵𝗂𝖽𝖾𝗈\
        \n\n┍☯ 𝗖𝗼𝗺𝗺𝗮𝗻𝗱: `{cmd}end`\
        \n┕☯ 𝗙𝘂𝗻𝗴𝘀𝗶𝗼𝗻: 𝖬𝖾𝗆𝖺𝗍𝗂𝗄𝖺𝗇 𝖫𝖺𝗀𝗎/𝖵𝗂𝖽𝖾𝗈\
        \n\n┍☯ 𝗖𝗼𝗺𝗺𝗮𝗻𝗱: `{cmd}skip`\
        \n┕☯ 𝗙𝘂𝗻𝗴𝘀𝗶𝗼𝗻: 𝖡𝖾𝗋𝗉𝗂𝗇𝖽𝖺𝗁 𝖫𝖺𝗀𝗎\
        \n\n┍☯ 𝗖𝗼𝗺𝗺𝗮𝗻𝗱: `{cmd}pause`\
        \n┕☯ 𝗙𝘂𝗻𝗴𝘀𝗶𝗼𝗻: 𝖡𝖾𝗋𝗁𝖾𝗇𝗍𝗂𝗄𝖺𝗇 𝖫𝖺𝗀𝗎/𝖵𝗂𝖽𝖾𝗈\
        \n\n┍☯ 𝗖𝗼𝗺𝗺𝗮𝗻𝗱: `{cmd}resume`\
        \n┕☯ 𝗙𝘂𝗻𝗴𝘀𝗶𝗼𝗻: 𝖬𝖾𝗅𝖺𝗇𝗃𝗎𝗍𝗄𝖺𝗇 𝖫𝖺𝗀𝗎/𝖵𝗂𝖽𝖾𝗈\
        \n\n┍☯ 𝗖𝗼𝗺𝗺𝗮𝗻𝗱: `{cmd}volume` 1-200\
        \n┕☯ 𝗙𝘂𝗻𝗴𝘀𝗶𝗼𝗻: 𝖬𝖾𝗇𝗀𝖺𝗍𝗎𝗋 𝖵𝗈𝗅𝗎𝗆𝖾 (𝖠𝖣𝖬𝖨𝖭)\
        \n\n┍☯ 𝗖𝗼𝗺𝗺𝗮𝗻𝗱: `{cmd}playlist`\
        \n┕☯ 𝗙𝘂𝗻𝗴𝘀𝗶𝗼𝗻: 𝖬𝖾𝗅𝗂𝗁𝖺𝗍 𝖣𝖺𝖿𝗍𝖺𝗋 𝗉𝗎𝗍𝖺𝗋\
        \n\n┍☯ 𝗖𝗼𝗺𝗺𝗮𝗻𝗱: `{cmd}joinvc`\
        \n┕☯ 𝗙𝘂𝗻𝗴𝘀𝗶𝗼𝗻: Menaikkan akun ke VCG\
        \n\n┍☯ 𝗖𝗼𝗺𝗺𝗮𝗻𝗱: `{cmd}`leavevc\
        \n┕☯ 𝗙𝘂𝗻𝗴𝘀𝗶𝗼𝗻: Menurunkan akun dari VCG\
    "
    }
)
