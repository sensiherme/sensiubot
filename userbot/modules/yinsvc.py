# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.


from pytgcalls import GroupCallFactory
from pytgcalls.exceptions import GroupCallNotFoundError
from telethon.errors.rpcerrorlist import (
    ParticipantJoinMissingError,
    ChatSendMediaForbiddenError,
)
from pytgcalls.exceptions import NotConnectedError

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils.vc import get_string
from userbot.events import register
from userbot.utils import edit_delete, edit_or_reply, ayiin_cmd, yins_asst


@ayiin_cmd(pattern="joinvc(?: |$)(.*)")
@register(pattern=r"^\.joinvcs$", sudo=True)
async def join_(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        try:
            chat = await event.client.parse_id(chat)
        except Exception as e:
            return await event.eor(get_string("vcbot_2").format(str(e)))
    else:
        chat = event.chat_id
    yinSongs = Player(chat, event)
    if not yinSongs.group_call.is_connected:
        await yinSongs.vc_joiner()


@ayiin_cmd(pattern="leavevc(?: |$)(.*)")
@register(pattern=r"^\.leavevcs$", sudo=True)
async def leaver(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        try:
            chat = await event.client.parse_id(chat)
        except Exception as e:
            return await event.eor(get_string("vcbot_2").format(str(e)))
    else:
        chat = event.chat_id
    yinSongs = Player(chat)
    await yinSongs.group_call.stop()
    if CLIENTS.get(chat):
        del CLIENTS[chat]
    if VIDEO_ON.get(chat):
        del VIDEO_ON[chat]
    await event.eor(get_string("vcbot_1"))


@ayiin_cmd(pattern="rejoin(?: |$)(.*)")
@register(pattern=r"^\.rejoinvcs$", sudo=True)
async def rejoiner(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        try:
            chat = await event.client.parse_id(chat)
        except Exception as e:
            return await event.eor(get_string("vcbot_2").format(str(e)))
    else:
        chat = event.chat_id
    yinSongs = Player(chat)
    try:
        await yinSongs.group_call.reconnect()
    except NotConnectedError:
        return await event.eor(get_string("vcbot_6"))
    await event.eor(get_string("vcbot_5"))


CMD_HELP.update(
    {
        "yinsvc": f"**Plugin : **`yinsvc`\
        \n\n  •  **Syntax :** `{cmd}joinvc` **<optional chat id/username>**\
        \n  •  **Function : **bergabung dengan obrolan suara.\
        \n\n  •  **Syntax :** `{cmd}leavevc`\
        \n  •  **Function : **Meninggalkan obrolan suara.\
        \n\n  •  **Syntax :** `{cmd}rejoin`\
        \n  •  **Function : **Bergabung kembali dengan obrolan suara, jika terjadi kesalahan.\
    "
    }
)
