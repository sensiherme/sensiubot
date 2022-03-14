# 🍀 © @tofik_dn
# ⚠️ Do not remove credits
# Rewrite @AyiinXd


from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import ayiin_cmd
import random
from userbot import owner
from telethon.tl.types import InputMessagesFilterVideo


@ayiin_cmd(pattern="bokp$")
async def _(ayiin):
    try:
        asuyins = [
            asupan
            async for asupan in ayiin.client.iter_messages(
                "@YinsAsuCache", filter=InputMessagesFilterVideo
            )
        ]
        awake = await ayiin.client.get_me()
        await ayiin.client.send_file(
            ayiin.chat_id,
            file=random.choice(asuyins),
            caption=f"Kena Tipu Ya Tod [{owner}](tg://user?id={awake.id})",
        )
        await ayiin.delete()
    except Exception:
        await ayiin.edit("**Maaf tod tidak bisa menemukan video asupan.**")


ayiin_cmd(pattern="okp$")
async def _(yins):
    try:
        okepyins = [
            asupan
            async for asupan in yins.client.iter_messages(
                "@okpyins", filter=InputMessagesFilterVideo
            )
        ]
        awake = await yins.client.get_me()
        await yins.client.send_file(
            event.chat_id,
            file=random.choice(okepyins),
            caption=f"Ini Bokp Lu Tod [{owner}](tg://user?id={awake.id})",
        )
        await yins.delete()
    except Exception:
        await yins.edit("**Maaf tod tidak bisa menemukan video asupan.**")


CMD_HELP.update(
    {
        "yinsubot6": f"**Plugin : **yinsubot6\
        \n\n  •  **Syntax :** {cmd}bokp\
        \n  •  **Function : **Untuk Mengirim bokp tiktok secara random.\
        \n\n  •  **Syntax :** {cmd}okp\
        \n  •  **Function : **Untuk Mengirim bokp secara random.\
    "
    }
)
