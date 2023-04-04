import random
import time
from typing import List

import requests
from telegram import (
    ChatPermissions,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ParseMode,
    Update,
)
from telegram.ext import CallbackContext, run_async

from lunaBot import StartTime, dispatcher
from lunaBot.modules.helper_funcs.chat_status import sudo_plus
from lunaBot.modules.disable import DisableAbleCommandHandler

sites_list = {
    "Telegram": "https://api.telegram.org",
    "Kaizoku": "https://animekaizoku.com",
    "Kayo": "https://animekayo.com",
    "Jikan": "https://api.jikan.moe/v3",
}


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


def ping_func(to_ping: List[str]) -> List[str]:
    ping_result = []

    for each_ping in to_ping:

        start_time = time.time()
        site_to_ping = sites_list[each_ping]
        r = requests.get(site_to_ping)
        end_time = time.time()
        ping_time = str(round((end_time - start_time), 2)) + "s"

        pinged_site = f"<b>{each_ping}</b>"

        if each_ping == "Kaizoku" or each_ping == "Kayo":
            pinged_site = f'<a href="{sites_list[each_ping]}">{each_ping}</a>'
            ping_time = f"<code>{ping_time} (Status: {r.status_code})</code>"

        ping_text = f"{pinged_site}: <code>{ping_time}</code>"
        ping_result.append(ping_text)

    return ping_result


LETS_GO_OYO = [
    "https://telegra.ph/file/49fb57c05a33474ab8c39.mp4",
    "https://telegra.ph/file/857d80a08b50009a42d54.mp4",
    "https://telegra.ph/file/e862a09d07c01dbd0d862.mp4",
    "https://telegra.ph/file/bf7994a3562682792e8e4.mp4",
    "https://telegra.ph/file/94750969db96d944356df.mp4",
]


@run_async
@sudo_plus
def ping(update: Update, context: CallbackContext):
    # msg = update.effective_message

    start_time = time.time()
    # message = msg.reply_video(LETS_GO_OYO, caption= "⚡",)
    end_time = time.time()
    telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ms"
    uptime = get_readable_time((time.time() - StartTime))
    pingpong = random.choice(LETS_GO_OYO)

    update.effective_message.reply_video(
        pingpong,
        caption="""✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯\n\n𝗢𝗠𝗙𝗢 <a href="https://t.me/HYPER_AD17">𝗚𝗢𝗗-𝗛𝗬𝗣𝗘𝗥</a> 𝗔𝗥𝗜𝗩𝗘𝗗🔥!!\n<b>ᴛɪᴍᴇ ᴛᴀᴋᴇɴ:</b> <code>{}</code>\n<b>sᴇʀᴠɪᴄᴇ ᴜᴘᴛɪᴍᴇ:</b> <code>{}</code>""".format(
            telegram_ping, uptime
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                {
                    InlineKeyboardButton(
                        text="🔥Gᴏᴅ Kɪɴɢ!🔥", url="https://t.me/HYPER_AD13"
                    ),
                }
            ]
        ),
        parse_mode=ParseMode.HTML,
    )


LOL_PINGG = [
    "https://telegra.ph/file/0acbf58d966ac935380ef.mp4",
    "https://telegra.ph/file/840564d8c2ffb77a22247.mp4",
    "https://telegra.ph/file/43153d7d094a4e65462d5.mp4",
    "https://telegra.ph/file/c710a42668981afee2ac5.mp4",
    "https://telegra.ph/file/39350f815ec8411597dff.mp4",
    "https://telegra.ph/file/c5500c10d5c82c7b56e0a.mp4",
]


@run_async
@sudo_plus
def king(update: Update, context: CallbackContext):
    # msg = update.effective_message

    start_time = time.time()
    # message = msg.reply_video(LETS_GO_OYO, caption= "⚡",)
    end_time = time.time()
    telegram_king = str(round((end_time - start_time) * 1000, 3)) + " ms"
    uptime = get_readable_time((time.time() - StartTime))
    kingkong = random.choice(LOL_PINGG)

    update.effective_message.reply_video(
        kingkong,
        caption="✰✰✰✰✰✰✰✰✰✰✰✰\n𝗢𝗠𝗙𝗢🔥!!\n<b>ᴛɪᴍᴇ ᴛᴀᴋᴇɴ:</b> <code>{}</code>\n<b>sᴇʀᴠɪᴄᴇ ᴜᴘᴛɪᴍᴇ:</b> <code>{}</code>".format(
            telegram_king, uptime
        ),
        parse_mode=ParseMode.HTML,
    )


@run_async
@sudo_plus
def pingall(update: Update, context: CallbackContext):
    to_ping = ["Kaizoku", "Kayo", "Telegram", "Jikan"]
    pinged_list = ping_func(to_ping)
    pinged_list.insert(2, "")
    uptime = get_readable_time((time.time() - StartTime))

    reply_msg = "⏱Ping results are lol:\n"
    reply_msg += "\n".join(pinged_list)
    reply_msg += "\n<b>Service uptime:</b> <code>{}</code>".format(uptime)

    update.effective_message.reply_text(
        reply_msg, parse_mode=ParseMode.HTML, disable_web_page_preview=True
    )


PING_HANDLER = DisableAbleCommandHandler("king", ping)
SASTAPING_HANDLER = DisableAbleCommandHandler("ping2", king)
PINGALL_HANDLER = DisableAbleCommandHandler("kkingall", pingall)

dispatcher.add_handler(PING_HANDLER)
dispatcher.add_handler(SASTAPING_HANDLER)
dispatcher.add_handler(PINGALL_HANDLER)

__command_list__ = ["king", "ping", "kkingall"]
__handlers__ = [PING_HANDLER, SASTAPING_HANDLER, PINGALL_HANDLER]
