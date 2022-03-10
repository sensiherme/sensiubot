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


from userbot import CMD_HELP
from userbot import CMD_HANDLER as cmd
from userbot.utils import ayiin_cmd, edit_delete, edit_or_reply


arguments = [
    "small caps",
    "monospace",
    "double stroke",
    "script royal"
    "points",
    "strike through",
    "black bubbles",
    "bubbles",
    "bold",
    "bold italic",
    "black squares",
    "squares"]

fonts = [
    "small caps",
    "monospace",
    "double stroke",
    "script royal",
    "points",
    "strike through",
    "black bubbles",
    "bubbles",
    "bold",
    "bold italic",
    "black squares",
    "squares"]

_default = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
_small_caps = "ᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘϙʀsᴛᴜᴠᴡxʏᴢABCDEFGHIJKLMNOPQRSTUVWXYZ"
_monospace = "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉"
_double_stroke = "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ"
_script_royal = "𝒶𝒷𝒸𝒹𝑒𝒻𝑔𝒽𝒾𝒿𝓀𝓁𝓂𝓃𝑜𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵"
_points = "a ̤b ̤c ̤d ̤e ̤f ̤g ̤h ̤i ̤j ̤k ̤l ̤m ̤n ̤o ̤p ̤q ̤r ̤s ̤t ̤u ̤v ̤w ̤x ̤y ̤z ̤A ̤B ̤C ̤D ̤E ̤F ̤G ̤H ̤I ̤J ̤K ̤L ̤M ̤N ̤O ̤P ̤Q ̤R ̤S ̤T ̤U ̤V ̤W ̤X ̤Y ̤Z ̤"
_strike_through = "a ̶b ̶c ̶d ̶e ̶f ̶g ̶h ̶i ̶j ̶k ̶l ̶m ̶n ̶o ̶p ̶q ̶r ̶s ̶t ̶u ̶v ̶w ̶x ̶y ̶z ̶A ̶B ̶C ̶D ̶E ̶F ̶G ̶H ̶I ̶J ̶K ̶L ̶M ̶N ̶O ̶P ̶Q ̶R ̶S ̶T ̶U ̶V ̶W ̶X ̶Y ̶̶Z"
_black_bubbles = "🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩"
_bubbles = "ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ"
_bold = "𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭"
_bold_italic = "𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕"
_black_squares = "🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉"
_squares = "🅰︎🅱︎🅲︎🅳︎🅴︎🅵︎🅶︎🅷︎🅸︎🅹︎🅺︎🅻︎🅼︎🅽︎🅾︎🅿︎🆀︎🆁︎🆂︎🆃︎🆄︎🆅︎🆆︎🆇︎🆈︎🆉︎"


async def fonts(text):
    r = requests.get(
        f"{fonts}?type=fonts&text={text}"
    ).json()
    geng = r.get("message")
    kapak = url(geng)
    if not kapak:
        return "check syntax once more"
    with open("chat_id", "msg") as f:
        f.write(requests.get(geng).content)
    text = await event.send_message("fonts").convert("text")
    event.get_message("fonts", "text")
    return "fonts"


@ayiin_cmd(pattern="font(.*)(|$)")
async def _(event):
    input = event.pattern_match.group(1).strip()
    reply = await event.get_reply_message()
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()

    if not reply:
        try:
            _ = input.split(":", maxsplit=1)
            font = _[0][:-1]
            text = _[0]
        except IndexError:
            return await edit_delete(event, reply_to_id)
    elif not input:
        return await edit_delete(event, "`Give font dude :/`")

    else:
        font = input
        text = reply.message
    if not fonts:
        return await edit_or_reply(event, f"`{font} not in font list`.", time=13)
    if font == "small caps":
        yins = gen_font(text, _small_caps)
    elif font == "monospace":
        yins = gen_font(text, _monospace)
    elif font == "double stroke":
        yins = gen_font(text, _double_stroke)
    elif font == "script royal":
        yins = gen_font(text, _script_royal)
    elif font == "points":
        yins = gen_font(text, _points)
    elif font == "strike through":
        yins = gen_font(text, _strike_through)
    elif font == "black bubbles":
        yins = gen_font(text, _black_bubbles)
    elif font == "bubbles":
        yins = gen_font(text, _bubbles)
    elif font == "bold":
        yins = gen_font(text, _bold)
    elif font == "bold italic":
        yins = gen_font(text, _bold_italic)
    elif font == "black squares":
        yins = gen_font(text, _black_squares)
    elif font == "squares":
        yins = gen_font(text, _squares)
    await edit_or_reply(event, yins)
    await event.reply("**𝙂𝙚𝙣𝙚𝙧𝙖𝙩𝙚𝙙 𝘽𝙮 :** ✧ 𝙰𝚈𝙸𝙸𝙽-𝚄𝚂𝙴𝚁𝙱𝙾𝚃 ✧")


def gen_font(text, new_font):
    new_font = " ".join(new_font).split()
    for q in text:
        if q in _default:
            new = new_font[_default.index(q)]
            text = text.replace(q, new)
    return text


@ayiin_cmd(pattern="fonts(.*)(|$)")
async def font(event):
    ayiin = await edit_or_reply(event,
                                "**𝘿𝙖𝙛𝙩𝙖𝙧 𝙁𝙤𝙣𝙩𝙨**\n"
                                "**    ☟︎︎︎☟︎︎︎☟︎︎︎☟︎︎︎☟︎︎︎☟︎︎**")
    await event.reply("**• small caps » ᴀʏɪɪɴ**\n"
                      "**• monospace » 𝙰𝚈𝙸𝙸𝙽**\n"
                      "**• double stroke » 𝔸𝕐𝕀𝕀ℕ**\n"
                      "**• script royal » 𝒜𝒴ℐℐ𝒩**\n"
                      "**• points » A ̤Y ̤I ̤I ̤N ̤**\n"
                      "**• strike through » A̶Y̶I̶I̶N̶**\n"
                      "**• black bubbles » 🅐︎🅨︎🅘︎🅘︎🅝︎**\n"
                      "**• bubbles » Ⓐ︎Ⓨ︎Ⓘ︎Ⓘ︎Ⓝ︎**\n"
                      "**• bold » 𝗔𝗬𝗜𝗜𝗡**\n"
                      "**• bold italic » 𝘼𝙔𝙄𝙄𝙉**\n"
                      "**• black squares » 🅰︎🆈︎🅸︎🅸︎🅽︎**\n"
                      "**• squares  » 🄰🅈🄸🄸🄽**\n\n"
                      "**   ✧ 𝙰𝚈𝙸𝙸𝙽-𝚄𝚂𝙴𝚁𝙱𝙾𝚃 ✧**")


CMD_HELP.update(
    {
        "yinsgen": f"**Plugin : **`yinsgen`\
        \n\n  •  **Syntax :** `{cmd}font <nama font> <Balas Ke Pesan>`\
        \n  •  **Function : **Menghasilkan font yang berbeda untuk teks.\
        \n\n  •  **Syntax :** `{cmd}fonts`\
        \n  •  **Function : **Untuk Melihat Daftar Font Lainnya.\
    "
    }
)
