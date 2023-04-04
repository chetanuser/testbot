# Kang With Credit @HYPER_AD13
import os
import math
import requests
import cloudscraper
import urllib.request as urllib
from PIL import Image
from html import escape
from bs4 import BeautifulSoup as bs

from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from telegram import TelegramError, Update
from telegram.ext import run_async, CallbackContext
from telegram.utils.helpers import mention_html

from lunaBot import dispatcher
from lunaBot.modules.disable import DisableAbleCommandHandler

combot_stickers_url = "https://combot.org/telegram/stickers?q="

"""sticker_button = [
    InlineKeyboardButton(text="ᴘᴀᴄᴋ", url=f"t.me/addstickers/{packname}")
]"""


@run_async
def stickerid(update: Update, context: CallbackContext):
    msg = update.effective_message
    if msg.reply_to_message and msg.reply_to_message.sticker:
        update.effective_message.reply_text(
            "ʜᴏɪɪ, "
            + f"{mention_html(msg.from_user.id, msg.from_user.first_name)}"
            + ", ᴛʜᴇ sᴛɪᴄᴋᴇʀ ɪᴅ ʏᴏᴜ ᴀʀᴇ ʀᴇᴘʟʏɪɴɢ ɪs :\n <code>"
            + escape(msg.reply_to_message.sticker.file_id)
            + "</code>",
            parse_mode=ParseMode.HTML,
        )
    else:
        update.effective_message.reply_text(
            "ʜᴏɪɪ, "
            + f"{mention_html(msg.from_user.id, msg.from_user.first_name)}"
            + ", ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ sᴛɪᴄᴋᴇʀ ᴍᴇssᴀɢᴇ ᴛᴏ ɢᴇᴛ ɪᴅ sᴛɪᴄᴋᴇʀ",
            parse_mode=ParseMode.HTML,
        )


@run_async
def cb_sticker(update: Update, context: CallbackContext):
    msg = update.effective_message
    split = msg.text.split(" ", 1)
    if len(split) == 1:
        msg.reply_text("ᴘʀᴏᴠɪᴅᴇ sᴏᴍᴇ ɴᴀᴍᴇ ᴛᴏ sᴇᴀʀᴄʜ ꜰᴏʀ ᴘᴀᴄᴋ.")
        return

    scraper = cloudscraper.create_scraper()
    text = scraper.get(combot_stickers_url + split[1]).text
    soup = bs(text, "lxml")
    results = soup.find_all("a", {"class": "sticker-pack__btn"})
    titles = soup.find_all("div", "sticker-pack__title")
    if not results:
        msg.reply_text("No results found :(.")
        return
    reply = f"sᴛɪᴄᴋᴇʀs ꜰᴏʀ *{split[1]}*:"
    for result, title in zip(results, titles):
        link = result["href"]
        reply += f"\n• [{title.get_text()}]({link})"
    msg.reply_text(reply, parse_mode=ParseMode.MARKDOWN)


def getsticker(update: Update, context: CallbackContext):
    bot = context.bot
    msg = update.effective_message
    chat_id = update.effective_chat.id
    if msg.reply_to_message and msg.reply_to_message.sticker:
        file_id = msg.reply_to_message.sticker.file_id
        new_file = bot.get_file(file_id)
        new_file.download("sticker.png")
        bot.send_document(chat_id, document=open("sticker.png", "rb"))
        os.remove("sticker.png")
    else:
        update.effective_message.reply_text(
            "ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ sᴛɪᴄᴋᴇʀ ꜰᴏʀ ᴍᴇ ᴛᴏ ᴜᴘʟᴏᴀᴅ ɪᴛs ᴘɴɢ."
        )


def imgconvert(update: Update, context: CallbackContext):
    bot = context.bot
    msg = update.effective_message
    chat_id = update.effective_chat.id
    if msg.reply_to_message and msg.reply_to_message.sticker:
        file_id = msg.reply_to_message.sticker.file_id
        new_file = bot.get_file(file_id)
        new_file.download("sticker.jpg")
        update.effective_message.reply_photo(
            photo=open("sticker.jpg", "rb"),
            caption=" ʏᴏᴜʀ ɪᴍᴀɢᴇ ɪs ʀᴇᴀᴅʏ\n✦ᴄʀᴇᴀᴛᴏʀ [ᴍɪss ᴄᴜɪᴛᴇ](t.me/MISSCUITEBOT)",
            parse_mode=ParseMode.MARKDOWN,
        )
        os.remove("sticker.jpg")
    else:
        update.effective_message.reply_text(
            "ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ sᴛɪᴄᴋᴇʀ ꜰᴏʀ ᴍᴇ ᴛᴏ ᴜᴘʟᴏᴀᴅ ɪᴛs ᴊᴘɢ."
        )


def videoconvert(update: Update, context: CallbackContext):
    bot = context.bot
    msg = update.effective_message
    chat_id = update.effective_chat.id
    if msg.reply_to_message and msg.reply_to_message.sticker:
        file_id = msg.reply_to_message.sticker.file_id
        new_file = bot.get_file(file_id)
        new_file.download("sticker.mp4")
        update.effective_message.reply_video(
            video=open("sticker.mp4", "rb"),
            caption="✦ᴜʜ ʏᴏᴜʀ ғɪʟᴇ ɪᴢ ʀᴇᴀᴅʏ🧚‍♀\n✦ᴄʀᴇᴀᴛᴏʀ [ᴍɪss ᴄᴜɪᴛᴇ](t.me/MISSCUITEBOT)",
            parse_mode=ParseMode.MARKDOWN,
        )
        os.remove("sticker.mp4")
    else:
        update.effective_message.reply_text(
            "ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ sᴛɪᴄᴋᴇʀ ꜰᴏʀ ᴍᴇ ᴛᴏ ᴜᴘʟᴏᴀᴅ ɪᴛs `mp4`."
        )


@run_async
def kang(update: Update, context: CallbackContext):
    msg = update.effective_message
    user = update.effective_user
    args = context.args
    packnum = 0
    packname = "a" + str(user.id) + "_by_" + context.bot.username
    packname_found = 0
    max_stickers = 120
    while packname_found == 0:
        try:
            stickerset = context.bot.get_sticker_set(packname)
            if len(stickerset.stickers) >= max_stickers:
                packnum += 1
                packname = (
                    "a"
                    + str(packnum)
                    + "_"
                    + str(user.id)
                    + "_by_"
                    + context.bot.username
                )
            else:
                packname_found = 1
        except TelegramError as e:
            if e.message == "Stickerset_invalid":
                packname_found = 1
    kangsticker = "kangsticker.png"
    is_animated = False
    file_id = ""

    if msg.reply_to_message:
        if msg.reply_to_message.sticker:
            if msg.reply_to_message.sticker.is_animated:
                is_animated = True
            file_id = msg.reply_to_message.sticker.file_id

        elif msg.reply_to_message.photo:
            file_id = msg.reply_to_message.photo[-1].file_id
        elif msg.reply_to_message.document:
            file_id = msg.reply_to_message.document.file_id
        else:
            msg.reply_text("Yea, I can't kang that.")

        kang_file = context.bot.get_file(file_id)
        if not is_animated:
            kang_file.download("kangsticker.png")
        else:
            kang_file.download("kangsticker.tgs")

        if args:
            sticker_emoji = str(args[0])
        elif msg.reply_to_message.sticker and msg.reply_to_message.sticker.emoji:
            sticker_emoji = msg.reply_to_message.sticker.emoji
        else:
            sticker_emoji = "✨"

        if not is_animated:
            try:
                im = Image.open(kangsticker)
                maxsize = (512, 512)
                if (im.width and im.height) < 512:
                    size1 = im.width
                    size2 = im.height
                    if im.width > im.height:
                        scale = 512 / size1
                        size1new = 512
                        size2new = size2 * scale
                    else:
                        scale = 512 / size2
                        size1new = size1 * scale
                        size2new = 512
                    size1new = math.floor(size1new)
                    size2new = math.floor(size2new)
                    sizenew = (size1new, size2new)
                    im = im.resize(sizenew)
                else:
                    im.thumbnail(maxsize)
                if not msg.reply_to_message.sticker:
                    im.save(kangsticker, "PNG")
                context.bot.add_sticker_to_set(
                    user_id=user.id,
                    name=packname,
                    png_sticker=open("kangsticker.png", "rb"),
                    emojis=sticker_emoji,
                )

                msg.reply_text(
                    f"sᴛɪᴄᴋᴇʀ sᴜᴄᴄᴇssꜰᴜʟʟʏ ᴀᴅᴅᴇᴅ ᴛᴏ ʏᴏᴜʀ ᴘᴀᴄᴋ!"
                    + f"\n\n `ᴇᴍᴏᴊɪ ɪs`: {sticker_emoji}",
                    parse_mode=ParseMode.MARKDOWN,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text="ʏᴏᴜʀ-ᴘᴀᴄᴋ❁",
                                    url=f"t.me/addstickers/{packname}",
                                )
                            ],
                        ]
                    ),
                )

            except OSError as e:
                msg.reply_text("I can only kang images m8.")
                print(e)
                return

            except TelegramError as e:
                if e.message == "Stickerset_invalid":
                    makepack_internal(
                        update,
                        context,
                        msg,
                        user,
                        sticker_emoji,
                        packname,
                        packnum,
                        png_sticker=open("kangsticker.png", "rb"),
                    )
                elif e.message == "Sticker_png_dimensions":
                    im.save(kangsticker, "PNG")
                    context.bot.add_sticker_to_set(
                        user_id=user.id,
                        name=packname,
                        png_sticker=open("kangsticker.png", "rb"),
                        emojis=sticker_emoji,
                    )
                    msg.reply_text(
                        f"sᴛɪᴄᴋᴇʀ sᴜᴄᴄᴇssꜰᴜʟʟʏ ᴀᴅᴅᴇᴅ ᴛᴏ ʏᴏᴜʀ ᴘᴀᴄᴋ!"
                        + f"\n\n `ᴇᴍᴏᴊɪ ɪs`: {sticker_emoji}",
                        parse_mode=ParseMode.MARKDOWN,
                        reply_markup=InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton(
                                        text="ʏᴏᴜʀ-ᴘᴀᴄᴋ❁",
                                        url=f"t.me/addstickers/{packname}",
                                    )
                                ],
                            ]
                        ),
                    )
                elif e.message == "Invalid sticker emojis":
                    msg.reply_text("Invalid emoji(s).")
                elif e.message == "Stickers_too_much":
                    msg.reply_text("Max packsize reached. Press F to pay respecc.")
                elif e.message == "Internal Server Error: sticker set not found (500)":
                    msg.reply_text(
                        "sᴛɪᴄᴋᴇʀ sᴜᴄᴄᴇssꜰᴜʟʟʏ ᴀᴅᴅᴇᴅ ᴛᴏ ʏᴏᴜʀ ᴘᴀᴄᴋ!" + "\n\n"
                        "`ᴇᴍᴏᴊɪ ɪs`:" + " " + sticker_emoji,
                        parse_mode=ParseMode.MARKDOWN,
                        reply_markup=InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton(
                                        text="ʏᴏᴜʀ-ᴘᴀᴄᴋ❁",
                                        url=f"t.me/addstickers/{packname}",
                                    )
                                ],
                            ]
                        ),
                    )
                print(e)

        else:
            packname = "animated" + str(user.id) + "_by_" + context.bot.username
            packname_found = 0
            max_stickers = 50
            while packname_found == 0:
                try:
                    stickerset = context.bot.get_sticker_set(packname)
                    if len(stickerset.stickers) >= max_stickers:
                        packnum += 1
                        packname = (
                            "animated"
                            + str(packnum)
                            + "_"
                            + str(user.id)
                            + "_by_"
                            + context.bot.username
                        )
                    else:
                        packname_found = 1
                except TelegramError as e:
                    if e.message == "Stickerset_invalid":
                        packname_found = 1
            try:
                context.bot.add_sticker_to_set(
                    user_id=user.id,
                    name=packname,
                    tgs_sticker=open("kangsticker.tgs", "rb"),
                    emojis=sticker_emoji,
                )
                msg.reply_text(
                    f"sᴛɪᴄᴋᴇʀ sᴜᴄᴄᴇssꜰᴜʟʟʏ ᴀᴅᴅᴇᴅ ᴛᴏ ʏᴏᴜʀ ᴘᴀᴄᴋ!"
                    + f"\n\n`ᴇᴍᴏᴊɪ ɪs`: {sticker_emoji}",
                    parse_mode=ParseMode.MARKDOWN,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text="ʏᴏᴜʀ-ᴘᴀᴄᴋ❁",
                                    url=f"t.me/addstickers/{packname}",
                                )
                            ],
                        ]
                    ),
                )
            except TelegramError as e:
                if e.message == "Stickerset_invalid":
                    makepack_internal(
                        update,
                        context,
                        msg,
                        user,
                        sticker_emoji,
                        packname,
                        packnum,
                        tgs_sticker=open("kangsticker.tgs", "rb"),
                    )
                elif e.message == "Invalid sticker emojis":
                    msg.reply_text("Invalid emoji(s).")
                elif e.message == "Internal Server Error: sticker set not found (500)":
                    msg.reply_text(
                        "sᴛɪᴄᴋᴇʀ sᴜᴄᴄᴇssꜰᴜʟʟʏ ᴀᴅᴅᴇᴅ ᴛᴏ ʏᴏᴜʀ ᴘᴀᴄᴋ!" + "\n\n"
                        "`ᴇᴍᴏᴊɪ ɪs`:" + " " + sticker_emoji,
                        parse_mode=ParseMode.MARKDOWN,
                        reply_markup=InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton(
                                        text="ʏᴏᴜʀ-ᴘᴀᴄᴋ❁",
                                        url=f"t.me/addstickers/{packname}",
                                    )
                                ],
                            ]
                        ),
                    )
                print(e)

    elif args:
        try:
            try:
                urlemoji = msg.text.split(" ")
                png_sticker = urlemoji[1]
                sticker_emoji = urlemoji[2]
            except IndexError:
                sticker_emoji = "✨"
            urllib.urlretrieve(png_sticker, kangsticker)
            im = Image.open(kangsticker)
            maxsize = (512, 512)
            if (im.width and im.height) < 512:
                size1 = im.width
                size2 = im.height
                if im.width > im.height:
                    scale = 512 / size1
                    size1new = 512
                    size2new = size2 * scale
                else:
                    scale = 512 / size2
                    size1new = size1 * scale
                    size2new = 512
                size1new = math.floor(size1new)
                size2new = math.floor(size2new)
                sizenew = (size1new, size2new)
                im = im.resize(sizenew)
            else:
                im.thumbnail(maxsize)
            im.save(kangsticker, "PNG")
            msg.reply_photo(photo=open("kangsticker.png", "rb"))
            context.bot.add_sticker_to_set(
                user_id=user.id,
                name=packname,
                png_sticker=open("kangsticker.png", "rb"),
                emojis=sticker_emoji,
            )
            msg.reply_text(
                f"sᴛɪᴄᴋᴇʀ sᴜᴄᴄᴇssꜰᴜʟʟʏ ᴀᴅᴅᴇᴅ ᴛᴏ ʏᴏᴜʀ ᴘᴀᴄᴋ!"
                + f"\n\n`ᴇᴍᴏᴊɪ ɪs`: {sticker_emoji}",
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="ʏᴏᴜʀ-ᴘᴀᴄᴋ❁", url=f"t.me/addstickers/{packname}"
                            )
                        ],
                    ]
                ),
            )
        except OSError as e:
            msg.reply_text("I can only kang images m8.")
            print(e)
            return
        except TelegramError as e:
            if e.message == "Stickerset_invalid":
                makepack_internal(
                    update,
                    context,
                    msg,
                    user,
                    sticker_emoji,
                    packname,
                    packnum,
                    png_sticker=open("kangsticker.png", "rb"),
                )
            elif e.message == "Sticker_png_dimensions":
                im.save(kangsticker, "PNG")
                context.bot.add_sticker_to_set(
                    user_id=user.id,
                    name=packname,
                    png_sticker=open("kangsticker.png", "rb"),
                    emojis=sticker_emoji,
                )
                msg.reply_text(
                    "sᴛɪᴄᴋᴇʀ sᴜᴄᴄᴇssꜰᴜʟʟʏ ᴀᴅᴅᴇᴅ ᴛᴏ ʏᴏᴜʀ ᴘᴀᴄᴋ!"
                    + "\n"
                    + "`ᴇᴍᴏᴊɪ ɪs`:"
                    + " "
                    + sticker_emoji,
                    parse_mode=ParseMode.MARKDOWN,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text="ʏᴏᴜʀ-ᴘᴀᴄᴋ❁",
                                    url=f"t.me/addstickers/{packname}",
                                )
                            ],
                        ]
                    ),
                )
            elif e.message == "Invalid sticker emojis":
                msg.reply_text("Invalid emoji(s).")
            elif e.message == "Stickers_too_much":
                msg.reply_text("Max packsize reached. Press F to pay respecc.")
            elif e.message == "Internal Server Error: sticker set not found (500)":
                msg.reply_text(
                    "sᴛɪᴄᴋᴇʀ sᴜᴄᴄᴇssꜰᴜʟʟʏ ᴀᴅᴅᴇᴅ ᴛᴏ ʏᴏᴜʀ ᴘᴀᴄᴋ🧚‍♀!" + "\n\n"
                    "`ᴇᴍᴏᴊɪ ɪs`:" + " " + sticker_emoji,
                    parse_mode=ParseMode.MARKDOWN,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text="ʏᴏᴜʀ-ᴘᴀᴄᴋ❁",
                                    url=f"t.me/addstickers/{packname}",
                                )
                            ],
                        ]
                    ),
                )
            print(e)
    else:
        packss = "ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ sᴛɪᴄᴋᴇʀ, ᴏʀ ɪᴍᴀɢᴇ ᴛᴏ ᴋᴀɴɢ ɪᴛ!\nᴏʜ, ʙʏ ᴛʜᴇ ᴡᴀʏ. ʜᴇʀᴇ ᴀʀᴇ ʏᴏᴜʀ ᴘᴀᴄᴋs ⇩\n"
        if packnum > 0:
            firstpackname = "a" + str(user.id) + "_by_" + context.bot.username
            for i in range(0, packnum + 1):
                if i == 0:
                    buttun = [
                        [
                            InlineKeyboardButton(
                                text="ʏᴏᴜʀ-ᴘᴀᴄᴋ❁",
                                url=f"t.me/addstickers/{firstpackname}",
                            )
                        ],
                    ]
                else:
                    buttun = [
                        [
                            InlineKeyboardButton(
                                text="ʏᴏᴜʀ-ᴘᴀᴄᴋ❁", url=f"t.me/addstickers/{packname}"
                            )
                        ],
                    ]
        else:
            buttun = [
                [
                    InlineKeyboardButton(
                        text="ʏᴏᴜʀ-ᴘᴀᴄᴋ❁", url=f"t.me/addstickers/{packname}"
                    )
                ],
            ]
        msg.reply_text(
            packss,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(buttun),
        )
    try:
        if os.path.isfile("kangsticker.png"):
            os.remove("kangsticker.png")
        elif os.path.isfile("kangsticker.tgs"):
            os.remove("kangsticker.tgs")
    except:
        pass


"""
if i == 0:
                    packs += f"[pack](t.me/addstickers/{firstpackname})\n"
                else:
                    packs += f"[pack{i}](t.me/addstickers/{packname})\n"
        else:
            packs += f"[pack](t.me/addstickers/{packname})"
"""


def makepack_internal(
    update,
    context,
    msg,
    user,
    emoji,
    packname,
    packnum,
    png_sticker=None,
    tgs_sticker=None,
):
    name = user.first_name
    name = name[:50]
    try:
        extra_version = ""
        if packnum > 0:
            extra_version = " " + str(packnum)
        if png_sticker:
            success = context.bot.create_new_sticker_set(
                user.id,
                packname,
                f"{name}s kang pack" + extra_version,
                png_sticker=png_sticker,
                emojis=emoji,
            )
        if tgs_sticker:
            success = context.bot.create_new_sticker_set(
                user.id,
                packname,
                f"{name}s animated kang pack" + extra_version,
                tgs_sticker=tgs_sticker,
                emojis=emoji,
            )

    except TelegramError as e:
        print(e)
        if e.message == "sᴛɪᴄᴋᴇʀ sᴇᴛ ɴᴀᴍᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴏᴄᴄᴜᴘɪᴇᴅ":
            msg.reply_text(
                "sᴛɪᴄᴋᴇʀ sᴜᴄᴄᴇssꜰᴜʟʟʏ ᴀᴅᴅᴇᴅ ᴛᴏ ʏᴏᴜʀ ᴘᴀᴄᴋ🧚‍♀!",
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="ʏᴏᴜʀ-ᴘᴀᴄᴋ❁", url=f"t.me/addstickers/{packname}"
                            )
                        ],
                    ]
                ),
            )
        elif e.message in ("Peer_id_invalid", "bot was blocked by the user"):
            msg.reply_text(
                "ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ ɪɴ ᴘᴍ ꜰɪʀsᴛ.",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="sᴛᴀʀᴛꪝ", url=f"t.me/{context.bot.username}"
                            )
                        ]
                    ]
                ),
            )
        elif e.message == "ɪɴᴛᴇʀɴᴀʟ sᴇʀᴠᴇʀ ᴇʀʀᴏʀ: ᴄʀᴇᴀᴛᴇᴅ sᴛɪᴄᴋᴇʀ sᴇᴛ ɴᴏᴛ ꜰᴏᴜɴᴅ (500)":
            msg.reply_text(
                "sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋ sᴜᴄᴄᴇssꜰᴜʟʟʏ ᴄʀᴇᴀᴛᴇᴅ. ɢᴇᴛ ɪᴛ",
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="ʏᴏᴜʀ-ᴘᴀᴄᴋ❁", url=f"t.me/addstickers/{packname}"
                            )
                        ],
                    ]
                ),
            )
        return

    if success:
        msg.reply_text(
            "sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋ sᴜᴄᴄᴇssꜰᴜʟʟʏ ᴄʀᴇᴀᴛᴇᴅ. ɢᴇᴛ ɪᴛ 🤍 ",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="ʏᴏᴜʀ-ᴘᴀᴄᴋ❁", url=f"t.me/addstickers/{packname}"
                        )
                    ],
                ]
            ),
        )
    else:
        msg.reply_text("ꜰᴀɪʟᴇᴅ ᴛᴏ ᴄʀᴇᴀᴛᴇ sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋ. ᴘᴏssɪʙʟʏ ᴅᴜᴇ ᴛᴏ ʙɪʟᴇᴋ ᴍᴇɢɪᴋ 😕.")


__mod_name__ = "sᴛɪᴄᴋᴇʀ 🤠"

__help__ = """*ʜᴇʟᴘ ᴍᴇɴᴜ ꜰᴏʀ sᴛɪᴄᴋᴇʀs ᴛᴏᴏʟs*
✦ /stickerid *:* ʀᴇᴘʟʏ ᴛᴏ ᴀ sᴛɪᴄᴋᴇʀ ᴛᴏ ᴍᴇ ᴛᴏ ᴛᴇʟʟ ʏᴏᴜ ɪᴛs ꜰɪʟᴇ ɪᴅ.\n\n✦ /getsticker *:* ʀᴇᴘʟʏ ᴛᴏ ᴀ sᴛɪᴄᴋᴇʀ ᴛᴏ ᴍᴇ ᴛᴏ ᴜᴘʟᴏᴀᴅ ɪᴛs ʀᴀᴡ ᴘɴɢ ꜰɪʟᴇ.\n\n✦ /kang *:* ʀᴇᴘʟʏ ᴛᴏ ᴀ sᴛɪᴄᴋᴇʀ ᴛᴏ ᴀᴅᴅ ɪᴛ ᴛᴏ ʏᴏᴜʀ ᴘᴀᴄᴋ.\n\n✦ /stickers *:* ꜰɪɴᴅ sᴛɪᴄᴋᴇʀs ꜰᴏʀ ɢɪᴠᴇɴ ᴛᴇʀᴍ ᴏɴ ᴄᴏᴍʙᴏᴛ sᴛɪᴄᴋᴇʀ ᴄᴀᴛᴀʟᴏɢᴜᴇ.\n\n✦ /image : ᴛᴏ ᴄᴏɴᴠᴇʀᴛ sᴛɪᴄᴋᴇʀ ɪɴᴛᴏ ɪᴍᴀɢᴇ ɪɴ ᴊᴘɢ ꜰᴏʀᴍᴀᴛᴇ.\n\n✦ /getvideo : ᴛᴏ ᴄᴏɴᴠᴇʀᴛ ᴠɪᴅᴇᴏ's sᴛɪᴄᴋᴇʀ ɪɴᴛᴏ ɪᴍᴀɢᴇ ɪɴ `mp4` ꜰᴏʀᴍᴀᴛᴇ.\n\n"""

STICKERID_HANDLER = DisableAbleCommandHandler("stickerid", stickerid)
GETSTICKER_HANDLER = DisableAbleCommandHandler("getsticker", getsticker)
IMG_CONVERTOR = DisableAbleCommandHandler("image", imgconvert)
VIDEO_CONVERTORR = DisableAbleCommandHandler("getvideo", videoconvert)
KANG_HANDLER = DisableAbleCommandHandler("kang", kang, admin_ok=True)
STICKERS_HANDLER = DisableAbleCommandHandler("stickers", cb_sticker)

dispatcher.add_handler(STICKERS_HANDLER)
dispatcher.add_handler(STICKERID_HANDLER)
dispatcher.add_handler(GETSTICKER_HANDLER)
dispatcher.add_handler(IMG_CONVERTOR)
dispatcher.add_handler(VIDEO_CONVERTORR)
dispatcher.add_handler(KANG_HANDLER)
