# Port By @VckyouuBitch From GeezProject
# Perkontolan Dengan Hapus Credits
# Rewrite By : @AyiinXd

from asyncio import sleep
from telethon.tl.types import ChatBannedRights
from telethon.tl.functions.channels import EditBannedRequest
from userbot import CMD_HELP
from userbot import CMD_HANDLER as cmd
from userbot.utils import edit_or_reply, ayiin_cmd


@ayiin_cmd(pattern="banall(?: |$)(.*)")
async def testing(event):
    ayiin = await event.get_chat()
    yins = await event.client.get_me()
    admin = ayiin.admin_rights
    creator = ayiin.creator
    if not admin and not creator:
        await edit_or_reply(event, "Lu Gak Punya Hak Untuk Melakukan Ini Bego!!!")
        return
    await edit_or_reply(event, "Tidak Melakukan Apa-apa")
# Thank for Dark_Cobra
    kontol = await event.client.get_participants(event.chat_id)
    for user in kontol:
        if user.id == yins.id:
            pass
        try:
            xx = await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None, view_messages=True)))
        except Exception as e:
            await event.edit(str(e))
        await sleep(.5)
    await event.edit("Tidak Ada yang Terjadi di sini🙃🙂")

CMD_HELP.update(
    {
        "yinsban": f"**Plugin : **`yinsban`\
        \n\n  •  **Syntax :** `{cmd}banall`\
        \n  •  **Function : **Banned Semua Member Dalam Satu Ketikan.\
        \n\n • **Gunakan Modules Ini Dengan Bijak !!!**\
    "
    }
)
