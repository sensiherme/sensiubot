# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
#
# Ported by @AyiinXd
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# t.me/AyiinXdSupport & t.me/AyiinSupport

# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


import asyncio
import os

import cv2
import numpy as np

from userbot import LOGS
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import ayiin_cmd, edit_or_reply, edit_delete


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


@ayiin_cmd(pattern=r"sketch(?: |$)(.*)")
async def sketch(e):
    ureply = await e.get_reply_message()
    xx = await edit_or_reply(e, "`Sabar Kentod...`")
    if not (ureply and (ureply.media)):
        return await edit_delete(e, "Maaf Gagal Memproses, Silahkan Mencoba Kembali")

    yins = await ureply.download_media()
    if yins.endswith(".tgs"):
        await xx.edit(get_string("sts_9"))
        cmd = ["lottie_convert.py", yins, "ayiin.png"]
        file = "ayiin.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await xx.edit("Sedang Memproses Tod Mohon Tunggu")
        img = cv2.VideoCapture(yins)
        heh, lol = img.read()
        cv2.imwrite("ayiin.png", lol)
        file = "ayiin.png"
    img = cv2.imread(file)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inverted_gray_image = 255 - gray_image
    blurred_img = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)
    inverted_blurred_img = 255 - blurred_img
    pencil_sketch_IMG = cv2.divide(
        gray_image, inverted_blurred_img, scale=256.0)
    cv2.imwrite("ayiinxd.png", pencil_sketch_IMG)
    await e.reply(file="ayiinxd.png")
    await xx.delete()
    os.remove(file)
    os.remove("ayiinxd.png")


@ayiin_cmd(pattern=r"grey(?: |$)(.*)")
async def xnxx(event):
    ureply = await event.get_reply_message()
    if not (ureply and (ureply.media)):
        return await edit_delete(event, "`Reply Pesannya Bego...`")

    ayiin = await ureply.download_media()
    if ayiin.endswith(".tgs"):
        edit_or_reply(event, "`Sabar Ya Kentod...`")
        cmd = ["lottie_convert.py", ayiin, "yin.png"]
        file = "yin.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await event.edit("`Gua Proses Sekarang Anj...`")
        img = cv2.VideoCapture(ayiin)
        heh, lol = img.read()
        cv2.imwrite("yin.png", lol)
        file = "yin.png"
    yin = cv2.imread(file)
    ayiinxd = cv2.cvtColor(yin, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("yin.jpg", ayiinxd)
    await event.client.send_file(
        event.chat_id,
        "yin.jpg",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    await xx.delete()
    os.remove("yin.png")
    os.remove("yin.jpg")
    os.remove(ayiin)


@ayiin_cmd(pattern=r"blur(?: |$)(.*)")
async def ayiin(event):
    ureply = await event.get_reply_message()
    if not (ureply and (ureply.media)):
        return await edit_delete(event, "`Balas Ke Pesannya Bego...`")

    yins = await ureply.download_media()
    if yins.endswith(".tgs"):
        xd = await edit_or_reply(event, "`Sabar Ya Babi...`")
        cmd = ["lottie_convert.py", yins, "yin.png"]
        file = "yin.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await event.edit("`Gua Proses Sekarang Babi...`")
        img = cv2.VideoCapture(yins)
        heh, lol = img.read()
        cv2.imwrite("yin.png", lol)
        file = "yin.png"
    yin = cv2.imread(file)
    ayiinxd = cv2.GaussianBlur(yin, (35, 35), 0)
    cv2.imwrite("yin.jpg", ayiinxd)
    await event.client.send_file(
        event.chat_id,
        "yin.jpg",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    await xd.delete()
    for i in ["yin.png", "yin.jpg", yins]:
        if os.path.exists(i):
            os.remove(i)


@ayiin_cmd(pattern=r"negative(?: |$)(.*)")
async def yinsxd(event):
    ureply = await event.get_reply_message()
    ayiin = await edit_or_reply(event, "`Sabar Ya Anj...`")
    if not (ureply and (ureply.media)):
        return await edit_delete(event, "`Balas Ke Pesannya Anj...`")

    ayiinxd = await ureply.download_media()
    if ayiinxd.endswith(".tgs"):
        await ayiin.edit("`Gua Proses Sekarang Anj...`")
        cmd = ["lottie_convert.py", ayiinxd, "yin.png"]
        file = "yin.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await ayiin.edit("`Anj Lu Yang Kebanyakan Dosa Gua Yang Terbebani, Sedang Berusaha Tod...`")
        img = cv2.VideoCapture(ayiinxd)
        heh, lol = img.read()
        cv2.imwrite("yin.png", lol)
        file = "yin.png"
    yinsex = cv2.imread(file)
    kntlxd = cv2.bitwise_not(yinsex)
    cv2.imwrite("yin.jpg", kntlxd)
    await event.client.send_file(
        event.chat_id,
        "yin.jpg",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    await ayiin.delete()
    os.remove("yin.png")
    os.remove("yin.jpg")
    os.remove(kntlxd)


@ayiin_cmd(pattern=r"mirror(?: |$)(.*)")
async def kntl(event):
    ureply = await event.get_reply_message()
    asu = await edit_or_reply(event, "`Sabar Ya Kentod`")
    if not (ureply and (ureply.media)):
        return await edit_delete(event, "`Balas Ke Pesannya Babi...`")

    xnxx = await ureply.download_media()
    if xnxx.endswith(".tgs"):
        await asu.edit("`Gua Proses Sekarang Tod...`")
        cmd = ["lottie_convert.py", xnxx, "yin.png"]
        file = "yin.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await asu.edit("`Anj Lu Yang Kebanyakan Dosa Gua Yang Terbebani`, **Sedang Berusaha Tod...**")
        img = cv2.VideoCapture(xnxx)
        kont, tol = img.read()
        cv2.imwrite("yin.png", tol)
        file = "yin.png"
    yin = cv2.imread(file)
    mmk = cv2.flip(yin, 1)
    ayiinxd = cv2.hconcat([yin, mmk])
    cv2.imwrite("yin.jpg", ayiinxd)
    await event.client.send_file(
        event.chat_id,
        "yin.jpg",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    await xx.delete()
    os.remove("yin.png")
    os.remove("yin.jpg")
    os.remove(xnxx)


@ayiin_cmd(pattern=r"flip(?: |$)(.*)")
async def ayiin(kontol):
    ureply = await kontol.get_reply_message()
    xd = await edit_or_reply(kontol, "`??????`")
    if not (ureply and (ureply.media)):
        return await edit_delete(kontol, "`Balas Ke Foto Atau Sticker Bego...`")

    ayiinxd = await ureply.download_media()
    if ayiinxd.endswith(".tgs"):
        await xd.edit("`Sabar Ya Kentod...`")
        cmd = ["lottie_convert.py", ayiinxd, "yins.png"]
        file = "yins.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await xd.edit("`Gua Proses Sekarang Tod...`")
        img = cv2.VideoCapture(ayiinxd)
        kon, tol = img.read()
        cv2.imwrite("yins.png", tol)
        file = "yins.png"
    ayin = cv2.imread(file)
    trn = cv2.flip(ayin, 1)
    asu = cv2.rotate(trn, cv2.ROTATE_180)
    yinz = cv2.vconcat([ayin, asu])
    cv2.imwrite("yins.jpg", yinz)
    await kontol.client.send_file(
        kontol.chat_id,
        "yins.jpg",
        force_document=False,
        reply_to=kontol.reply_to_msg_id,
    )
    await xd.delete()
    os.remove("yins.png")
    os.remove("yins.jpg")
    os.remove(ayiinxd)


@ayiin_cmd(pattern=r"quad(?: |$)(.*)")
async def ayiin(memek):
    ureply = await memek.get_reply_message()
    xd = await edit_or_reply(memek, "`Sabar Ya Kentod...`")
    if not (ureply and (ureply.media)):
        return await edit_delete(memek, "`Balas Ke Foto Atau Sticker Bego...`")

    yinsex = await ureply.download_media()
    if yinsex.endswith(".tgs"):
        await xd.edit("`Sedang Memproses Babi...`")
        cmd = ["lottie_convert.py", yinsex, "yins.png"]
        file = "yins.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await xd.edit("`Sedang Menggenjot Lebih Kenceng...`")
        img = cv2.VideoCapture(yinsex)
        kon, tol = img.read()
        cv2.imwrite("yins.png", tol)
        file = "yins.png"
    ayin = cv2.imread(file)
    xnxx = cv2.flip(ayin, 1)
    mici = cv2.hconcat([ayin, xnxx])
    fr = cv2.flip(mici, 1)
    trn = cv2.rotate(fr, cv2.ROTATE_180)
    ayiinxd = cv2.vconcat([mici, trn])
    cv2.imwrite("yins.jpg", ayiinxd)
    await memek.client.send_file(
        memek.chat_id,
        "yins.jpg",
        force_document=False,
        reply_to=memek.reply_to_msg_id,
    )
    await xd.delete()
    os.remove("yins.png")
    os.remove("yins.jpg")
    os.remove(yinsex)


@ayiin_cmd(pattern=r"toon(?: |$)(.*)")
async def yins(event):
    ureply = await event.get_reply_message()
    xd = await edit_or_reply(event, "`Sabar Ya Babi...`")
    if not (ureply and (ureply.media)):
        return await edit_delete(event, "`Balas Ke Foto Atau Sticker Bego...`")

    yinsex = await ureply.download_media()
    if yinsex.endswith(".tgs"):
        await xd.edit(get_string("sts_9"))
        cmd = ["lottie_convert.py", yinsex, "yins.png"]
        file = "yins.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await xd.edit("Sedang Memproses Tod...")
        img = cv2.VideoCapture(yinsex)
        kon, tol = img.read()
        cv2.imwrite("yins.png", tol)
        file = "yins.png"
    yins = cv2.imread(file)
    height, width, channels = yins.shape
    samples = np.zeros([height * width, 3], dtype=np.float32)
    count = 0
    for x in range(height):
        for y in range(width):
            samples[count] = yins[x][y]
            count += 1
    compactness, labels, centers = cv2.kmeans(
        samples,
        12,
        None,
        (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10000, 0.0001),
        5,
        cv2.KMEANS_PP_CENTERS,
    )
    centers = np.uint8(centers)
    asu = centers[labels.flatten()]
    ayiinxd = asu.reshape(yins.shape)
    cv2.imwrite("yins.jpg", ayiinxd)
    await event.client.send_file(
        event.chat_id,
        "yins.jpg",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    await xd.delete()
    os.remove("yins.png")
    os.remove("yins.jpg")
    os.remove(yinsex)


@ayiin_cmd(pattern=r"danger(?: |$)(.*)")
async def ayiin(event):
    ureply = await event.get_reply_message()
    ayiin = await edit_or_reply(event, "`Sabar Ya Kentod...`")
    if not (ureply and (ureply.media)):
        return await edit_delete(event, "Balas Ke Foto Atau Sticker Bego...")

    ayiinxd = await ureply.download_media()
    if ayiinxd.endswith(".tgs"):
        await ayiin.edit("`Sedang Memproses Tod...`")
        cmd = ["lottie_convert.py", ayiinxd, "yins.png"]
        file = "yins.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await ayiin.edit("Sedang Menggenjot Lebih Kenceng...")
        img = cv2.VideoCapture(ayiinxd)
        kon, tol = img.read()
        cv2.imwrite("yins.png", tol)
        file = "yins.png"
    yins = cv2.imread(file)
    dan = cv2.cvtColor(yins, cv2.COLOR_BGR2RGB)
    kontol = cv2.cvtColor(dan, cv2.COLOR_HSV2BGR)
    cv2.imwrite("yins.jpg", kontol)
    await event.client.send_file(
        event.chat_id,
        "yins.jpg",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    await ayiin.delete()
    os.remove("yins.png")
    os.remove("yins.jpg")
    os.remove(ayiinxd)


@ayiin_cmd(pattern=r"csample(?: |$)(.*)")
async def sampl(ayiin):
    color = ayiin.pattern_match.group(1).strip()
    if color:
        img = Image.new("RGB", (200, 100), f"{color}")
        img.save("csample.png")
        try:
            try:
                await ayiin.delete()
                await ayiin.client.send_message(
                    ayiin.chat_id, f"Contoh Warna untuk `{color}` !", file="csample.png"
                )
            except MessageDeleteForbiddenError:
                await ayiin.reply(f"Contoh Warna untuk `{color}` !", file="csample.png")
        except ChatSendMediaForbiddenError:
            await edit_delete(ayiin, "`Hmm! Mengirim Media Dinonaktifkan Di Sini Anj!!!`")

    else:
        await edit_or_reply(ayiin, "Ketik Yang Bener Anj, Nama Warna/Kode Salah Tod !")


@ayiin_cmd(pattern=r"blue(?: |$)(.*)")
async def ayiin(event):
    ureply = await event.get_reply_message()
    xd = await edit_or_reply(event, "`Sabar Kentod`")
    if not (ureply and (ureply.media)):
        await edit_delete(event, "`Balas Ke Foto Atau Sticker Bego...`")
        return
    xdxd = await ureply.download_media()
    if xdxd.endswith(".tgs"):
        await xd.edit("`Gua Proses Sekarang Babi...`")
        cmd = ["lottie_convert.py", xdxd, "yins.png"]
        file = "yins.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await event.edit("`Sabar Babi Gua Proses Dulu...`")
        img = cv2.VideoCapture(xdxd)
        kon, tol = img.read()
        cv2.imwrite("yins.png", tol)
        file = "yins.png"
    got = upf(file)
    lnk = f"https://telegra.ph{got[0]}"
    r = await async_search(
        f"https://nekobot.xyz/api/imagegen?type=blurpify&image={lnk}", re_json=True
    )
    ms = r.get("message")
    if not r["success"]:
        return await xd.edit(ms)
    await download_file(ms, "yins.png")
    img = Image.open("yins.png").convert("RGB")
    img.save("yins.webp", "webp")
    await event.client.send_file(
        event.chat_id,
        "yins.webp",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    await xd.delete()
    os.remove("yins.png")
    os.remove("yins.webp")
    os.remove(xdxd)


@ayiin_cmd(pattern=r"border(?: |$)(.*)")
async def ayiixd(event):
    mmk = await event.get_reply_message()
    if not (mmk and (mmk.photo or mmk.sticker)):
        return await edit_delete(event, "`Balas Ke Sticker Atau Foto Bego...`")
    kntl = event.pattern_match.group(1).strip()
    wh = 20
    if not kntl:
        kntl = [255, 255, 255]
    else:
        try:
            if ";" in kntl:
                col_ = kntl.split(";", maxsplit=1)
                wh = int(col_[1])
                kntl = col_[0]
            kntl = [int(kntl) for kntl in kntl.split(",")[:2]]
        except ValueError:
            return await edit_delete(event, "`Not a Valid Input...`")
    yups = await mmk.download_media()
    img1 = cv2.imread(yups)
    constant = cv2.copyMakeBorder(
        img1, wh, wh, wh, wh, cv2.BORDER_CONSTANT, value=kntl)
    cv2.imwrite("output.png", constant)
    await event.client.send_file(event.chat.id, "output.png")
    os.remove("output.png")
    os.remove(yups)
    await event.delete()


@ayiin_cmd(pattern=r"pixelator(?: |$)(.*)")
async def pixelator(event):
    reply_message = await event.get_reply_message()
    if not (reply_message and reply_message.photo):
        return await edit_delete(event, "`Balas Ke Fotonya Bego...`")
    hw = 50
    try:
        hw = int(event.pattern_match.group(1).strip())
    except (ValueError, TypeError):
        pass
    yins = await edit_or_reply(event, "`Sabar Ya Tod...`")
    imayiin = await reply_message.download_media()
    input_ = cv2.imread(imayiin)
    height, width = input_.shape[:2]
    w, h = (hw, hw)
    temp = cv2.resize(input_, (w, h), interpolation=cv2.INTER_LINEAR)
    output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
    cv2.imwrite("output.jpg", output)
    await yins.respond("⍟ 𝙋𝙞𝙭𝙚𝙡𝙖𝙩𝙚𝙙 𝙗𝙮 𝘼𝙮𝙞𝙞𝙣-𝙐𝙨𝙚𝙧𝙗𝙤𝙩 ⍟", file="output.jpg")
    await yins.delete()
    os.remove("output.jpg")
    os.remove(imayiin)


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


CMD_HELP.update(
    {
        "yinsimg": f"**Plugin : **`yinsimg`\
        \n\n  •  **Syntax :** `{cmd}sketch` <reply ke Foto/Sticker>\
        \n  •  **Function :** Coba Dulu Tod.\
        \n\n  •  **Syntax :** `{cmd}grey` <reply ke Foto/Sticker>\
        \n  •  **Function :** Coba Dulu Tod.\
        \n\n  •  **Syntax :** `{cmd}blur` <reply ke Foto/Sticker>\
        \n  •  **Function :** Coba Dulu Tod.\
        \n\n  •  **Syntax :** `{cmd}negative` <reply ke Foto/Sticker>\
        \n  •  **Function :** Coba Dulu Tod.\
        \n\n  •  **Syntax :** `{cmd}mirror` <reply ke Foto/Sticker>\
        \n  •  **Function :** Coba Dulu Tod.\
        \n\n  •  **Syntax :** `{cmd}flip` <reply ke Foto/Sticker>\
        \n  •  **Function :** Coba Dulu Tod.\
        \n\n  •  **Syntax :** `{cmd}quad` <reply ke Foto/Sticker>\
        \n  •  **Function :** Coba Dulu Tod.\
        \n\n  •  **Syntax :** `{cmd}toon` <reply ke Foto/Sticker>\
        \n  •  **Function :** Coba Dulu Tod.\
        \n\n  •  **Syntax :** `{cmd}danger` <reply ke Foto/Sticker>\
        \n  •  **Function :** Coba Dulu Tod.\
        \n\n  •  **Syntax :** `{cmd}csample` <reply ke Foto/Sticker>\
        \n  •  **Function :** Coba Dulu Tod.\
        \n\n  •  **Syntax :** `{cmd}blue` <reply ke Foto/Sticker>\
        \n  •  **Function :** Coba Dulu Tod.\
        \n\n  •  **Syntax :** `{cmd}border` <reply ke Foto/Sticker>\
        \n  •  **Function :** Coba Dulu Tod.\
        \n\n  •  **Syntax :** `{cmd}pixelator` <reply ke Foto/Sticker>\
        \n  •  **Function :** Coba Dulu Tod.\
    "
    }
)
