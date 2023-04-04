# credits @AD_1317, @Mr_dark_⚡⚡

import logging
import time

from pyrogram import filters
from pyrogram.errors.exceptions.bad_request_400 import (
    ChatAdminRequired,
    PeerIdInvalid,
    UsernameNotOccupied,
    UserNotParticipant,
)
from pyrogram.types import ChatPermissions, InlineKeyboardButton, InlineKeyboardMarkup

from lunaBot import DRAGONS as SUDO_USERS
from lunaBot import pbot
from lunaBot.modules.sql_extended import forceSubscribe_sql as sql

logging.basicConfig(level=logging.INFO)

static_data_filter = filters.create(
    lambda _, __, query: query.data == "onUnMuteRequest"
)


@pbot.on_callback_query(static_data_filter)
def _onUnMuteRequest(client, cb):
    user_id = cb.from_user.id
    chat_id = cb.message.chat.id
    chat_db = sql.fs_settings(chat_id)
    if chat_db:
        channel = chat_db.channel
        chat_member = client.get_chat_member(chat_id, user_id)
        if chat_member.restricted_by:
            if chat_member.restricted_by.id == (client.get_me()).id:
                try:
                    client.get_chat_member(channel, user_id)
                    client.unban_chat_member(chat_id, user_id)
                    cb.message.delete()
                    # if cb.message.reply_to_message.from_user.id == user_id:
                    # cb.message.delete()
                except UserNotParticipant:
                    client.answer_callback_query(
                        cb.id,
                        text=f"❗ Jᴏɪɴ Oᴜʀ @{channel} Cʜᴀɴɴᴇʟ Aɴᴅ Pʀᴇss 'Uɴᴍᴜᴛᴇ Mᴇ' Bᴜᴛᴛᴏɴ🌚.",
                        show_alert=True,
                    )
            else:
                client.answer_callback_query(
                    cb.id,
                    text="❗ Yᴏᴜ Hᴀᴠᴇ Bᴇᴇɴ Bᴜᴛᴇᴅ Bʏ Aᴅᴍɪɴs Dᴜᴇ Tᴏ Sᴏᴍᴇ Oᴛʜᴇʀ Rᴇᴀsᴏɴ, Mᴀᴋᴇ Sᴜʀᴇ Tʜᴀᴛ Qᴜᴇsᴛɪᴏɴ💔!!.",
                    show_alert=True,
                )
        else:
            if (
                not client.get_chat_member(chat_id, (client.get_me()).id).status
                == "administrator"
            ):
                client.send_message(
                    chat_id,
                    f"❗ **{cb.from_user.mention} ɪs ᴛʀʏɪɴɢ ᴛᴏ ᴜɴᴍᴜᴛᴇ ʜɪᴍsᴇʟꜰ ʙᴜᴛ ɪ ᴄᴀɴ'ᴛ ᴜɴᴍᴜᴛᴇ ʜɪᴍ ʙᴇᴄᴀᴜsᴇ ɪ ᴀᴍ ɴᴏᴛ ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜɪs ᴄʜᴀᴛ ᴀᴅᴅ ᴍᴇ ᴀs ᴀᴅᴍɪɴ ᴀɢᴀɪɴ! ʜᴇᴀʀᴛ ʙʀᴇᴀᴋ ᴋʀ ᴅɪʏᴀ ᴠʀᴏ🥺💔!.**\n__#Lᴇᴀᴠɪɴɢ_Tʜɪs_Cʜᴀᴛ💔...__",
                )

            else:
                client.answer_callback_query(
                    cb.id,
                    text="❗ Wᴀʀɴɪɴɢ! Dᴏɴ'ᴛ Pʀᴇss Tʜᴇ Bᴜᴛᴛᴏɴ Wʜᴇɴ Yᴏᴜ Cᴀɴ Tᴀʟᴋ Fʀᴇᴇʟʏ Fᴏᴏʟ🙄🙄!!.",
                    show_alert=True,
                )


@pbot.on_message(filters.text & ~filters.private & ~filters.edited, group=1)
def _check_member(client, message):
    chat_id = message.chat.id
    chat_db = sql.fs_settings(chat_id)
    if chat_db:
        user_id = message.from_user.id
        if (
            not client.get_chat_member(chat_id, user_id).status
            in ("administrator", "creator")
            and not user_id in SUDO_USERS
        ):
            channel = chat_db.channel
            try:
                client.get_chat_member(channel, user_id)
            except UserNotParticipant:
                try:
                    sent_message = message.reply_text(
                        "Wᴇʟᴄᴏᴍᴇ {} 🙏 \n **Yᴏᴜ Hᴀᴠᴇɴᴛ Jᴏɪɴᴇᴅ Oᴜʀ @{} Cʜᴀɴɴᴇʟ Yᴇᴛ🥺💔!** 😭 \n \nPʟᴇᴀsᴇ Jᴏɪɴ😞🙏 [Oᴜʀ Jʜᴀɴɴᴇʟ - Cʟɪᴄᴋ Hᴇʀᴇ🙃](https://t.me/{}) Aɴᴅ Tʜᴇɴ Pʀᴇss Oʀ Tᴀᴘ Oɴ **𝗨𝗡𝗠𝗨𝗧𝗘 𝗠𝗘😇** Bᴜᴛᴛᴏɴ🙃🙃. \n \n ".format(
                            message.from_user.mention, channel, channel
                        ),
                        disable_web_page_preview=True,
                        reply_markup=InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton(
                                        "Jᴏɪɴ Cʜᴀɴɴᴇʟ👀",
                                        url="https://t.me/{}".format(channel),
                                    ),
                                    InlineKeyboardButton(
                                        "Uɴᴍᴜᴛᴇ Mᴇ🌚", callback_data="onUnMuteRequest"
                                    ),
                                ],
                            ]
                        ),
                    )
                    client.restrict_chat_member(
                        chat_id, user_id, ChatPermissions(can_send_messages=False)
                    )
                except ChatAdminRequired:
                    sent_message.edit(
                        "❗ **ɪ'ᴍ ɴᴏᴛ ᴀᴅᴍɪɴ ʜᴇʀᴇ..**\n__ɢɪᴠᴇ ᴍᴇ ʙᴀɴ ᴘᴇʀᴍɪssɪᴏɴs ᴀɴᴅ ʀᴇᴛʀʏ.. \n#ᴇɴᴅɪɴɢ ꜰsᴜʙ...__"
                    )

            except ChatAdminRequired:
                client.send_message(
                    chat_id,
                    text=f"❗ **ɪ ɴᴏᴛ ᴀɴ ᴀᴅᴍɪɴ ᴏꜰ @{channel} ᴄʜᴀɴɴᴇʟ.**\n__ɢɪᴠᴇ ᴍᴇ ᴀᴅᴍɪɴ ᴏꜰ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ʀᴇᴛʀʏ.\n#ᴇɴᴅɪɴɢ ꜰsᴜʙ...__",
                )


# BOOM_BOOM = "https://telegra.ph/file/8789440a82e75eeb89eb3.mp4"
# DOOM_DOOM = "https://telegra.ph/file/3dc058bcfd3e824bfbd34.mp4"


@pbot.on_message(filters.command(["forcesubscribe", "fsub"]) & ~filters.private)
def config(client, message):
    user = client.get_chat_member(message.chat.id, message.from_user.id)
    if user.status is "creator" or user.user.id in SUDO_USERS:
        chat_id = message.chat.id
        if len(message.command) > 1:
            input_str = message.command[1]
            input_str = input_str.replace("@", "")
            if input_str.lower() in ("off", "no", "disable"):
                sql.disapprove(chat_id)
                message.reply_text("✘ **ꜰᴏʀᴄᴇ sᴜʙsᴄʀɪʙᴇ ɪs ᴅɪsᴀʙʟᴇᴅ sᴜᴄᴄᴇssꜰᴜʟʟʏ.**")
            elif input_str.lower() in ("clear"):
                sent_message = message.reply_text(
                    "**ᴜɴᴍᴜᴛɪɴɢ ᴀʟʟ ᴍᴇᴍʙᴇʀs ᴡʜᴏ ᴀʀᴇ ᴍᴜᴛᴇᴅ ʙʏ ᴍᴇ...**"
                )
                try:
                    for chat_member in client.get_chat_members(
                        message.chat.id, filter="restricted"
                    ):
                        if chat_member.restricted_by.id == (client.get_me()).id:
                            client.unban_chat_member(chat_id, chat_member.user.id)
                            time.sleep(1)
                    sent_message.edit("✅ **ᴜɴᴍᴜᴛᴇᴅ ᴀʟʟ ᴍᴇᴍʙᴇʀs ᴡʜᴏ ᴀʀᴇ ᴍᴜᴛᴇᴅ ʙʏ ᴍᴇ.**")
                except ChatAdminRequired:
                    sent_message.edit(
                        "❗ **ɪ ᴀᴍ ɴᴏᴛ ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜɪs ᴄʜᴀᴛ.**\n__ɪ ᴄᴀɴ'ᴛ ᴜɴᴍᴜᴛᴇ ᴍᴇᴍʙᴇʀs ʙᴇᴄᴀᴜsᴇ ɪ ᴀᴍ ɴᴏᴛ ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜɪs ᴄʜᴀᴛ ᴍᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ ᴡɪᴛʜ ʙᴀɴ ᴜsᴇʀ ᴘᴇʀᴍɪssɪᴏɴ.__"
                    )
            else:
                try:
                    client.get_chat_member(input_str, "me")
                    sql.add_channel(chat_id, input_str)
                    message.reply_text(
                        f"●───────────\n✅ **ꜰᴏʀᴄᴇ sᴜʙsᴄʀɪʙᴇ ɪs ᴇɴᴀʙʟᴇᴅ**\n__ꜰᴏʀᴄᴇ sᴜʙsᴄʀɪʙᴇ ɪs ᴇɴᴀʙʟᴇᴅ, ᴀʟʟ ᴛʜᴇ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs ʜᴀᴠᴇ ᴛᴏ sᴜʙsᴄʀɪʙᴇ ᴛʜɪs [Cʜᴀɴɴᴇʟ](https://t.me/{input_str}) ɪɴ ᴏʀᴅᴇʀ ᴛᴏ sᴇɴᴅ ᴍᴇssᴀɢᴇs ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ.__───────────●",
                        disable_web_page_preview=True,
                    )
                except UserNotParticipant:
                    message.reply_text(
                        f"❗ **ɴᴏᴛ ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ**\n__ɪ ᴀᴍ ɴᴏᴛ ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇ [Cʜᴀɴɴᴇʟ](https://t.me/{input_str}). ᴀᴅᴅ ᴍᴇ ᴀs ᴀ ᴀᴅᴍɪɴ ɪɴ ᴏʀᴅᴇʀ ᴛᴏ ᴇɴᴀʙʟᴇ ꜰᴏʀᴄᴇsᴜʙsᴄʀɪʙᴇ.__",
                        disable_web_page_preview=True,
                    )
                except (UsernameNotOccupied, PeerIdInvalid):
                    message.reply_text(f"❗ **ɪɴᴠᴀʟɪᴅ ᴄʜᴀɴɴᴇʟ ᴜsᴇʀɴᴀᴍᴇ.**")
                except Exception as err:
                    message.reply_text(f"❗ **Eʀʀᴏʀ 404:** ```{err}```")
        else:
            if sql.fs_settings(chat_id):
                message.reply_text(
                    f"●───────────\n✅ **ꜰᴏʀᴄᴇ sᴜʙsᴄʀɪʙᴇ ɪs ᴇɴᴀʙʟᴇᴅ ɪɴ ᴛʜɪs ᴄʜᴀᴛ.**\n__ꜰᴏʀ ᴛʜɪs [Cʜᴀɴɴᴇʟ](https://t.me/{sql.fs_settings(chat_id).channel})__\n───────────●",
                    disable_web_page_preview=True,
                )
            else:
                message.reply_text("✘ **Fᴏʀᴄᴇ sᴜʙsᴄʀɪʙᴇ ɪs ᴅɪsᴀʙʟᴇᴅ ɪɴ ᴛʜɪs ᴄʜᴀᴛ.**")
    else:
        message.reply_text(
            "❗ **ɢʀᴏᴜᴘ ᴄʀᴇᴀᴛᴏʀ ʀᴇǫᴜɪʀᴇᴅ**\n__ʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ ʙᴇ ᴛʜᴇ ɢʀᴏᴜᴘ ᴄʀᴇᴀᴛᴏʀ ᴛᴏ ᴅᴏ ᴛʜᴀᴛ.__"
        )


__help__ = """
*🥷ꜰᴏʀᴄᴇ sᴜʙsᴄʀɪʙᴇ🥷:*
✿ ᴍɪss ᴄᴜɪᴛᴇ ᴄᴀɴ ᴍᴜᴛᴇ ᴍᴇᴍʙᴇʀs ᴡʜᴏ ᴀʀᴇ ɴᴏᴛ sᴜʙsᴄʀɪʙᴇᴅ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴜɴᴛɪʟ ᴛʜᴇʏ sᴜʙsᴄʀɪʙᴇ
✿ ᴡʜᴇɴ ᴇɴᴀʙʟᴇᴅ ɪ ᴡɪʟʟ ᴍᴜᴛᴇ ᴜɴsᴜʙsᴄʀɪʙᴇᴅ ᴍᴇᴍʙᴇʀs ᴀɴᴅ sʜᴏᴡ ᴛʜᴇᴍ ᴀ ᴜɴᴍᴜᴛᴇ ʙᴜᴛᴛᴏɴ. ᴡʜᴇɴ ᴛʜᴇʏ ᴘʀᴇssᴇᴅ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ɪ ᴡɪʟʟ ᴜɴᴍᴜᴛᴇ ᴛʜᴇᴍ
*sᴇᴛᴜᴘ*
*ᴏɴʟʏ ᴄʀᴇᴀᴛᴏʀ*
✿ [ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀs ᴀᴅᴍɪɴ](http://t.me/MISSCUITEBOT?startgroup=true)
✿ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴀs ᴀᴅᴍɪɴ 
 
*ᴄᴏᴍᴍᴍᴀɴᴅs*
 ✿ /fsub {ᴄʜᴀɴɴᴇʟ ᴜsᴇʀɴᴀᴍᴇ} - ᴛᴏ ᴛᴜʀɴ ᴏɴ ᴀɴᴅ sᴇᴛᴜᴘ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ.
  💡ᴅᴏ ᴛʜɪs ꜰɪʀsᴛ...
 ✿ /fsub - ᴛᴏ ɢᴇᴛ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ sᴇᴛᴛɪɴɢs.
 ✿ /fsub  `Disable`  or  `off`  - ᴛᴏ ᴛᴜʀɴ ᴏꜰ ꜰᴏʀᴄᴇsᴜʙsᴄʀɪʙᴇ..
  💡ɪꜰ ʏᴏᴜ ᴅɪsᴀʙʟᴇ ꜰsᴜʙ, ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ sᴇᴛ ᴀɢᴀɪɴ ꜰᴏʀ ᴡᴏʀᴋɪɴɢ.. /fsub {ᴄʜᴀɴɴᴇʟ ᴜsᴇʀɴᴀᴍᴇ} 
 ✿ /fsub Clear - ᴛᴏ ᴜɴᴍᴜᴛᴇ ᴀʟʟ ᴍᴇᴍʙᴇʀs ᴡʜᴏ ᴍᴜᴛᴇᴅ ʙʏ ᴍᴇ.

"""
__mod_name__ = "ꜰ-sᴜʙ 〽️"
