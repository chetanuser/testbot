import html
import random
import time

import lunaBot.modules.fun_strings as fun_strings
from lunaBot import dispatcher
from lunaBot.modules.disable import DisableAbleCommandHandler, DisableAbleMessageHandler
from lunaBot.modules.helper_funcs.chat_status import is_user_admin
from lunaBot.modules.helper_funcs.alternate import typing_action
from lunaBot.modules.helper_funcs.filters import CustomFilters
from lunaBot.modules.helper_funcs.extraction import extract_user
from telegram import ChatPermissions, ParseMode, Update
from telegram.error import BadRequest
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.ext import CallbackContext, run_async, CommandHandler, Filters


normiefont = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
weebyfont = [
    "卂",
    "乃",
    "匚",
    "刀",
    "乇",
    "下",
    "厶",
    "卄",
    "工",
    "丁",
    "长",
    "乚",
    "从",
    "𠘨",
    "口",
    "尸",
    "㔿",
    "尺",
    "丂",
    "丅",
    "凵",
    "リ",
    "山",
    "乂",
    "丫",
    "乙",
]
bubblefont = [
    "Ⓐ︎",
    "Ⓑ︎",
    "Ⓒ︎",
    "Ⓓ︎",
    "Ⓔ︎",
    "Ⓕ︎",
    "Ⓖ︎",
    "Ⓗ︎",
    "Ⓘ︎",
    "Ⓙ︎",
    "Ⓚ︎",
    "Ⓛ︎",
    "Ⓜ︎",
    "Ⓝ︎",
    "Ⓞ︎",
    "Ⓟ︎",
    "Ⓠ︎",
    "Ⓡ︎",
    "Ⓢ︎",
    "Ⓣ︎",
    "Ⓤ︎",
    "Ⓥ︎",
    "Ⓦ︎",
    "Ⓧ︎",
    "Ⓨ︎",
    "Ⓩ︎",
]
fbubblefont = [
    "🅐︎",
    "🅑︎",
    "🅒︎",
    "🅓︎",
    "🅔︎",
    "🅕︎",
    "🅖︎",
    "🅗︎",
    "🅘︎",
    "🅙︎",
    "🅚︎",
    "🅛︎",
    "🅜︎",
    "🅝︎",
    "🅞︎",
    "🅟︎",
    "🅠︎",
    "🅡︎",
    "🅢︎",
    "🅣︎",
    "🅤︎",
    "🅥︎",
    "🅦︎",
    "🅧︎",
    "🅨︎",
    "🅩︎",
]
tinyfont = [
    "ᵃ",
    "ᵇ",
    "ᶜ",
    "ᵈ",
    "ᵉ",
    "ᶠ",
    "ᵍ",
    "ʰ",
    "ⁱ",
    "ʲ",
    "ᵏ",
    "ˡ",
    "ᵐ",
    "ⁿ",
    "ᵒ",
    "ᵖ",
    "ᵠ",
    "ʳ",
    "ˢ",
    "ᵗ",
    "ᵘ",
    "ᵛ",
    "ʷ",
    "ˣ",
    "ʸ",
    "ᶻ",
]
cuitefont = [
    "ᴀ",
    "ʙ",
    "ᴄ",
    "ᴅ",
    "ᴇ",
    "ғ",
    "ɢ",
    "ʜ",
    "ɪ",
    "ᴊ",
    "ᴋ",
    "ʟ",
    "ᴍ",
    "ɴ",
    "ᴏ",
    "ᴘ",
    "ǫ",
    "s",
    "ᴛ",
    "ᴜ",
    "ᴠ",
    "ᴡ",
    "x",
    "ʏ",
    "ᴢ",
]
nontinyfont = [
    "𝚊",
    "𝚋",
    "𝚌",
    "𝚍",
    "𝚎",
    "𝚏",
    "𝚐",
    "𝚑",
    "𝚒",
    "𝚓",
    "𝚔",
    "𝚕",
    "𝚖",
    "𝚗",
    "𝚘",
    "𝚙",
    "𝚚",
    "𝚛",
    "𝚜",
    "𝚝",
    "𝚞",
    "𝚟",
    "𝚠",
    "𝚡",
    "𝚢",
    "𝚣",
]
squarefont = [
    "🄰",
    "🄱",
    "🄲",
    "🄳",
    "🄴",
    "🄵",
    "🄶",
    "🄷",
    "🄸",
    "🄹",
    "🄺",
    "🄻",
    "🄼",
    "🄽",
    "🄾",
    "🄿",
    "🅀",
    "🅁",
    "🅂",
    "🅃",
    "🅄",
    "🅅",
    "🅆",
    "🅇",
    "🅈",
    "🅉",
]
fsquarefont = [
    "🅰︎",
    "🅱︎",
    "🅲︎",
    "🅳︎",
    "🅴︎",
    "🅵︎",
    "🅶︎",
    "🅷︎",
    "🅸︎",
    "🅹︎",
    "🅺︎",
    "🅻︎",
    "🅼︎",
    "🅽︎",
    "🅾︎",
    "🅿︎",
    "🆀︎",
    "🆁︎",
    "🆂︎",
    "🆃︎",
    "🆄︎",
    "🆅︎",
    "🆆︎",
    "🆇︎",
    "🆈︎",
    "🆉︎",
]
glowfont = [
    "🇦 ",
    "🇧 ",
    "🇨 ",
    "🇩 ",
    "🇪 ",
    "🇫 ",
    "🇬 ",
    "🇭 ",
    "🇮 ",
    "🇯 ",
    "🇰 ",
    "🇱 ",
    "🇲 ",
    "🇳 ",
    "🇴 ",
    "🇵 ",
    "🇶 ",
    "🇷 ",
    "🇸 ",
    "🇹 ",
    "🇺 ",
    "🇻 ",
    "🇼 ",
    "🇽 ",
    "🇾 ",
    "🇿 ",
]
outlinefont = [
    "𝕒",
    "𝕓",
    "𝕔",
    "𝕕",
    "𝕖",
    "𝕗",
    "𝕘",
    "𝕙",
    "𝕚",
    "𝕛",
    "𝕜",
    "𝕝",
    "𝕞",
    "𝕟",
    "𝕠",
    "𝕡",
    "𝕢",
    "𝕣",
    "𝕤",
    "𝕥",
    "𝕦",
    "𝕧",
    "𝕨",
    "𝕩",
    "𝕪",
    "𝕫",
]
boldfont = [
    "𝗮",
    "𝗯",
    "𝗰",
    "𝗱",
    "𝗲",
    "𝗳",
    "𝗴",
    "𝗵",
    "𝗶",
    "𝗷",
    "𝗸",
    "𝗹",
    "𝗺",
    "𝗻",
    "𝗼",
    "𝗽",
    "𝗾",
    "𝗿",
    "𝘀",
    "𝘁",
    "𝘂",
    "𝘃",
    "𝘄",
    "𝘅",
    "𝘆",
    "𝘇",
]
iboldfont = [
    "𝙖",
    "𝙗",
    "𝙘",
    "𝙙",
    "𝙚",
    "𝙛",
    "𝙜",
    "𝙝",
    "𝙞",
    "𝙟",
    "𝙠",
    "𝙡",
    "𝙢",
    "𝙣",
    "𝙤",
    "𝙥",
    "𝙦",
    "𝙧",
    "𝙨",
    "𝙩",
    "𝙪",
    "𝙫",
    "𝙬",
    "𝙭",
    "𝙮",
    "𝙯",
]
sonicfont = [
    "𝖆",
    "𝖇",
    "𝖈",
    "𝖉",
    "𝖊",
    "𝖋",
    "𝖌",
    "𝖍",
    "𝖎",
    "𝖏",
    "𝖐",
    "𝖑",
    "𝖒",
    "𝖓",
    "𝖔",
    "𝖕",
    "𝖖",
    "𝖗",
    "𝖘",
    "𝖙",
    "𝖚",
    "𝖛",
    "𝖜",
    "𝖝",
    "𝖞",
    "𝖟",
]
blockfont = [
    "a⃠",
    "b⃠",
    "c⃠",
    "d⃠",
    "e⃠",
    "f⃠",
    "g⃠",
    "h⃠",
    "i⃠",
    "j⃠",
    "k⃠",
    "l⃠",
    "m⃠",
    "n⃠",
    "o⃠",
    "p⃠",
    "q⃠",
    "r⃠",
    "s⃠",
    "t⃠",
    "u⃠",
    "v⃠",
    "w⃠",
    "x⃠",
    "y⃠",
    "z⃠",
]
cursivfont = [
    "𝓪",
    "𝓫",
    "𝓬",
    "𝓭",
    "𝓮",
    "𝓯",
    "𝓰",
    "𝓱",
    "𝓲",
    "𝓳",
    "𝓴",
    "𝓵",
    "𝓶",
    "𝓷",
    "𝓸",
    "𝓹",
    "𝓺",
    "𝓻",
    "𝓼",
    "𝓽",
    "𝓾",
    "𝓿",
    "𝔀",
    "𝔁",
    "𝔂",
    "𝔃",
]
comic = [
    "ᗩ",
    "ᗷ",
    "ᑕ",
    "ᗪ",
    "ᗴ",
    "ᖴ",
    "ᘜ",
    "ᕼ",
    "I",
    "ᒍ",
    "K",
    "ᒪ",
    "ᗰ",
    "ᑎ",
    "O",
    "ᑭ",
    "ᑫ",
    "ᖇ",
    "Տ",
    "T",
    "ᑌ",
    "ᐯ",
    "ᗯ",
    "᙭",
    "Y",
    "ᘔ",
]
typefont = [
    "ꪖ",
    "᥇",
    "ᥴ",
    "ᦔ",
    "ꫀ",
    "ᠻ",
    "ᧁ",
    "ꫝ",
    "𝓲",
    "𝓳",
    "𝘬",
    "ꪶ",
    "ꪑ",
    "ꪀ",
    "ꪮ",
    "ρ",
    "𝘲",
    "𝘳",
    "𝘴",
    "𝓽",
    "ꪊ",
    "ꪜ",
    "᭙",
    "᥊",
    "ꪗ",
    "ɀ",
]


@run_async
def weebify(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("ᴜsᴀɢᴇ :  `/weeb <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(
            f"`{string}`", parse_mode=ParseMode.MARKDOWN
        )
    else:
        message.reply_text(f"`{string}`", parse_mode=ParseMode.MARKDOWN)


@run_async
def bubbolefont(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("ᴜsᴀɢᴇ :  `/bubble <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            bubblecharacter = bubblefont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, bubblecharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(
            f"`{string}`", parse_mode=ParseMode.MARKDOWN
        )
    else:
        message.reply_text(f"`{string}`", parse_mode=ParseMode.MARKDOWN)


@run_async
def fbubble(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("ᴜsᴀɢᴇ :  `/fbubble <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            fbubblecharacter = fbubblefont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, fbubblecharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(
            f"`{string}`", parse_mode=ParseMode.MARKDOWN
        )
    else:
        message.reply_text(f"`{string}`", parse_mode=ParseMode.MARKDOWN)


@run_async
def tinytext(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("ᴜsᴀɢᴇ :  `/tini <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            tinycharacter = tinyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, tinycharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(
            f"`{string}`", parse_mode=ParseMode.MARKDOWN
        )
    else:
        message.reply_text(f"`{string}`", parse_mode=ParseMode.MARKDOWN)


@run_async
def devutext(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("ᴜsᴀɢᴇ :  `/cuite <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            devucharacter = devufont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, devucharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(
            f"`{string}`", parse_mode=ParseMode.MARKDOWN
        )
    else:
        message.reply_text(f"`{string}`", parse_mode=ParseMode.MARKDOWN)


@run_async
def nontinytext(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("ᴜsᴀɢᴇ :  `/ntini <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            nontinycharacter = nontinyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, nontinycharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(
            f"`{string}`", parse_mode=ParseMode.MARKDOWN
        )
    else:
        message.reply_text(f"`{string}`", parse_mode=ParseMode.MARKDOWN)


@run_async
def squaretext(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("ᴜsᴀɢᴇ :  `/square <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            squarecharacter = squarefont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, squarecharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(
            f"`{string}`", parse_mode=ParseMode.MARKDOWN
        )
    else:
        message.reply_text(f"`{string}`", parse_mode=ParseMode.MARKDOWN)


@run_async
def fsquaretext(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("ᴜsᴀɢᴇ :  `/fsquare <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            fsquarecharacter = fsquarefont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, fsquarecharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(
            f"`{string}`", parse_mode=ParseMode.MARKDOWN
        )
    else:
        message.reply_text(f"`{string}`", parse_mode=ParseMode.MARKDOWN)


@run_async
def glowtext(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("ᴜsᴀɢᴇ :  `/glow <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            glowcharacter = glowfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, glowcharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(
            f"`{string}`", parse_mode=ParseMode.MARKDOWN
        )
    else:
        message.reply_text(f"`{string}`", parse_mode=ParseMode.MARKDOWN)


@run_async
def boldtext(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("ᴜsᴀɢᴇ :  `/bold <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            boldcharacter = boldfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, boldcharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(
            f"`{string}`", parse_mode=ParseMode.MARKDOWN
        )
    else:
        message.reply_text(f"`{string}`", parse_mode=ParseMode.MARKDOWN)


@run_async
def outlinetext(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("ᴜsᴀɢᴇ :  `/outline <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            outlinecharacter = outlinefont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, outlinecharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(
            f"`{string}`", parse_mode=ParseMode.MARKDOWN
        )
    else:
        message.reply_text(f"`{string}`", parse_mode=ParseMode.MARKDOWN)


@run_async
def iboldtext(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("ᴜsᴀɢᴇ :  `/ibold <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            iboldcharacter = iboldfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, iboldcharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(
            f"`{string}`", parse_mode=ParseMode.MARKDOWN
        )
    else:
        message.reply_text(f"`{string}`", parse_mode=ParseMode.MARKDOWN)


@run_async
def blocktext(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("ᴜsᴀɢᴇ :  `/blok <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            blockcharacter = blockfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, blockcharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(
            f"`{string}`", parse_mode=ParseMode.MARKDOWN
        )
    else:
        message.reply_text(f"`{string}`", parse_mode=ParseMode.MARKDOWN)


@run_async
def sonictext(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("ᴜsᴀɢᴇ :  `/sonic <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            soniccharacter = sonicfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, soniccharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(
            f"`{string}`", parse_mode=ParseMode.MARKDOWN
        )
    else:
        message.reply_text(f"`{string}`", parse_mode=ParseMode.MARKDOWN)


@run_async
def comictext(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("ᴜsᴀɢᴇ :  `/comics <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            comicfcharacter = comic[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, comicfcharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(
            f"`{string}`", parse_mode=ParseMode.MARKDOWN
        )
    else:
        message.reply_text(f"`{string}`", parse_mode=ParseMode.MARKDOWN)


@run_async
def cursivtext(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("ᴜsᴀɢᴇ :  `/cursiv <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            cursivcharacter = cursivfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, cursivcharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(
            f"`{string}`", parse_mode=ParseMode.MARKDOWN
        )
    else:
        message.reply_text(f"`{string}`", parse_mode=ParseMode.MARKDOWN)


@run_async
def typetext(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("ᴜsᴀɢᴇ :  `/miss <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            typecharacter = typefont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, typecharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(
            f"`{string}`", parse_mode=ParseMode.MARKDOWN
        )
    else:
        message.reply_text(f"`{string}`", parse_mode=ParseMode.MARKDOWN)


WEEBIFY_HANDLER = DisableAbleCommandHandler("weeb", weebify)
BUBBLE_FONT = DisableAbleCommandHandler("bubble", bubbolefont)
FBUBBLE_FONT = DisableAbleCommandHandler("fbubble", fbubble)
TINI_FONT = DisableAbleCommandHandler("tini", tinytext)
DEVU_FONT = DisableAbleCommandHandler("cuite", devutext)
NONTINI_FONT = DisableAbleCommandHandler("ntini", nontinytext)
SQUARE_FONT = DisableAbleCommandHandler("square", squaretext)
FSQUARE_FONT = DisableAbleCommandHandler("fsquare", fsquaretext)
GLOW_FONT = DisableAbleCommandHandler("glow", glowtext)
BOLD_FONT = DisableAbleCommandHandler("bold", boldtext)
OUTLINE_FONT = DisableAbleCommandHandler("outline", outlinetext)
IBOLD_FONT = DisableAbleCommandHandler("ibold", iboldtext)
BLOK_FONT = DisableAbleCommandHandler("blok", blocktext)
SONIC_FONT = DisableAbleCommandHandler("sonic", sonictext)
COMIC_FONT = DisableAbleCommandHandler("comics", comictext)
CURSIV_FONT = DisableAbleCommandHandler("cursiv", cursivtext)
TYPE_FONT = DisableAbleCommandHandler("miss", typetext)


dispatcher.add_handler(WEEBIFY_HANDLER)
dispatcher.add_handler(BUBBLE_FONT)
dispatcher.add_handler(FBUBBLE_FONT)
dispatcher.add_handler(TINI_FONT)
dispatcher.add_handler(DEVU_FONT)
dispatcher.add_handler(NONTINI_FONT)
dispatcher.add_handler(SQUARE_FONT)
dispatcher.add_handler(FSQUARE_FONT)
dispatcher.add_handler(GLOW_FONT)
dispatcher.add_handler(BOLD_FONT)
dispatcher.add_handler(OUTLINE_FONT)
dispatcher.add_handler(IBOLD_FONT)
dispatcher.add_handler(BLOK_FONT)
dispatcher.add_handler(SONIC_FONT)
dispatcher.add_handler(COMIC_FONT)
dispatcher.add_handler(CURSIV_FONT)
dispatcher.add_handler(TYPE_FONT)


__mod_name__ = "ғᴏɴᴛ-ғᴜɴ 😙"


__help__ = """
✦ ғᴏɴᴛ-ᴛᴇxᴛ ғᴜɴs ✨\n
✿ /weeb <text> : `ᴄᴏɴᴠᴇʀᴛ ᴛᴏ ᴡᴇᴇᴘ ᴛᴇxᴛ.`\n
✿ /bubble <text> : `ᴄᴏɴᴠᴇʀᴛ ᴛᴏ ʙᴜʙʙʟᴇ ᴛᴇxᴛ.`\n
✿ /fbubble <text> : `ᴄᴏɴᴠᴇʀᴛ ᴛᴏ ғʙᴜʙʙʟᴇ ᴛᴇxᴛ.`\n
✿ /square <text> : `ᴄᴏɴᴠᴇʀᴛ ᴛᴏ sǫᴜᴀʀᴇ ᴛᴇxᴛ.`\n
✿ /fsquare <text> : `ᴄᴏɴᴠᴇʀᴛ ᴛᴏ ғsǫᴜᴀʀᴇ ᴛᴇxᴛ.`\n
✿ /glow <text> : `ᴄᴏɴᴠᴇʀᴛ ᴛᴏ ɢʟᴏᴡ ᴛᴇxᴛ.`\n
✿ /bold <text> : `ᴄᴏɴᴠᴇʀᴛ ᴛᴏ ʙᴏʟᴅ ᴛᴇxᴛ.`\n
✿ /outline <text> : `ᴄᴏɴᴠᴇʀᴛ ᴛᴏ ᴏᴜᴛʟɪɴᴇ ᴛᴇxᴛ.`\n
✿ /ibold <text> : `ᴄᴏɴᴠᴇʀᴛ ᴛᴏ ɪʙᴏʟᴅ ᴛᴇxᴛ.`\n
✿ /blok <text> : `ᴄᴏɴᴠᴇʀᴛ ᴛᴏ ʙʟᴏᴄᴋ ᴛᴇxᴛ.`\n
✿ /sonic <text> : `ᴄᴏɴᴠᴇʀᴛ ᴛᴏ sᴏɴɪᴄ ᴛᴇxᴛ.`\n
✿ /comics <text> : `ᴄᴏɴᴠᴇʀᴛ ᴛᴏ ᴄᴏᴍɪᴄ ᴛᴇxᴛ.`\n
✿ /cursiv <text> : `ᴄᴏɴᴠᴇʀᴛ ᴛᴏ ᴄᴜʀsɪᴠ ᴛᴇxᴛ.`\n
"""
