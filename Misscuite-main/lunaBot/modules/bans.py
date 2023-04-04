import html
import re

from telegram import (
    ParseMode,
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    CallbackContext,
    Filters,
    CommandHandler,
    run_async,
    CallbackQueryHandler,
)
from telegram.error import BadRequest
from telegram.ext import CallbackContext, CommandHandler, Filters, run_async
from telegram.utils.helpers import mention_html

from lunaBot import (
    DEV_USERS,
    LOGGER,
    OWNER_ID,
    DRAGONS,
    DEMONS,
    TIGERS,
    WOLVES,
    dispatcher,
)
from lunaBot.modules.disable import DisableAbleCommandHandler
from lunaBot.modules.helper_funcs.chat_status import (
    user_admin_no_reply,
    bot_admin,
    can_restrict,
    connection_status,
    is_user_admin,
    is_user_ban_protected,
    is_user_in_chat,
    user_admin,
    user_can_ban,
    can_delete,
)
from lunaBot.modules.helper_funcs.extraction import extract_user_and_text
from lunaBot.modules.helper_funcs.string_handling import extract_time
from lunaBot.modules.log_channel import gloggable, loggable

# XXD = "https://telegra.ph/file/6139d3fd30a44c705143f.jpg"


@run_async
@connection_status
@bot_admin
@can_restrict
@user_admin
@user_can_ban
@loggable
def ban(update: Update, context: CallbackContext) -> str:
    chat = update.effective_chat
    user = update.effective_user
    message = update.effective_message
    log_message = ""
    bot = context.bot
    args = context.args
    user_id, reason = extract_user_and_text(message, args)

    if not user_id:
        message.reply_text("I doubt that's a user.")
        return log_message
    try:
        member = chat.get_member(user_id)
    except BadRequest as excp:
        if excp.message != "User not found":
            raise
        message.reply_text("Can't seem to find this person.")
        return log_message
    if user_id == bot.id:
        message.reply_text("Oh yeah, ban myself, noob!")
        return log_message

    if is_user_ban_protected(chat, user_id, member) and user not in DEV_USERS:
        if user_id == OWNER_ID:
            message.reply_text("Trying to put me against a God level disaster huh?")
        elif user_id in DEV_USERS:
            message.reply_text("I can't act against our own.")
        elif user_id in DRAGONS:
            message.reply_text(
                "Fighting this Dragon here will put civilian lives at risk."
            )
        elif user_id in DEMONS:
            message.reply_text(
                "Bring an order from Heroes association to fight a Demon disaster."
            )
        elif user_id in TIGERS:
            message.reply_text(
                "Bring an order from Heroes association to fight a Tiger disaster."
            )
        elif user_id in WOLVES:
            message.reply_text("Wolf abilities make them ban immune!")
        else:
            message.reply_text("This user has immunity and cannot be banned.")
        return log_message
    if message.text.startswith("/s"):
        silent = True
        if not can_delete(chat, context.bot.id):
            return ""
    else:
        silent = False
    log = (
        f"<b>{html.escape(chat.title)}:</b>\n"
        f"#{'S' if silent else ''}BANNED\n"
        f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
        f"<b>User:</b> {mention_html(member.user.id, html.escape(member.user.first_name))}"
    )
    if reason:
        log += "\n<b>✤ ʀᴇᴀsᴏɴ:</b> {}".format(reason)

    try:
        chat.kick_member(user_id)

        if silent:
            if message.reply_to_message:
                message.reply_to_message.delete()
            message.delete()
            return log

        # bot.send_sticker(chat.id, BAN_STICKER)  # banhammer marie sticker
        reply = (
            f"<code>♦</code><b>ᴜsᴇʀ ʙᴀɴɴᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ!!</b>\n"
            f"<b>✤  ᴜsᴇʀ:</b> {mention_html(member.user.id, html.escape(member.user.first_name))}\n    ➥ [ <code>{member.user.id}</code> ]\n✤ ʙᴀɴɴᴇᴅ ʙʏ: {mention_html(user.id, user.first_name)}"
        )
        if reason:
            reply += f"\n<b>✤ ʀᴇᴀsᴏɴ:</b> <code>{html.escape(reason)}</code>"
        if message.reply_to_message:
            bot.sendMessage(
                chat.id,
                reply,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="❕ᴜɴʙᴀɴ",
                                callback_data="un_ban({})".format(user_id),
                            ),
                            InlineKeyboardButton(
                                text="🗑️ᴄʟᴏsᴇ", callback_data="close_"
                            ),
                        ]
                    ]
                ),
                parse_mode=ParseMode.HTML,
            )
            message.reply_to_message.delete()
        else:
            bot.sendMessage(
                chat.id,
                reply,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="❕ᴜɴʙᴀɴ",
                                callback_data="un_ban({})".format(user_id),
                            ),
                            InlineKeyboardButton(
                                text="🗑️ᴄʟᴏsᴇ", callback_data="close_"
                            ),
                        ]
                    ]
                ),
                parse_mode=ParseMode.HTML,
            )
        return log

    except BadRequest as excp:
        if excp.message == "Reply message not found":
            # Do not reply
            if silent:
                return log
            message.reply_text("Banned!", quote=False)
            return log
        else:
            LOGGER.warning(update)
            LOGGER.exception(
                "ERROR banning user %s in chat %s (%s) due to %s",
                user_id,
                chat.title,
                chat.id,
                excp.message,
            )
            message.reply_text("Uhm...that didn't work...")

    return log_message


@run_async
@connection_status
@bot_admin
@can_restrict
@user_admin
@user_can_ban
@loggable
def temp_ban(update: Update, context: CallbackContext) -> str:
    chat = update.effective_chat
    user = update.effective_user
    message = update.effective_message
    log_message = ""
    bot, args = context.bot, context.args
    user_id, reason = extract_user_and_text(message, args)

    if not user_id:
        message.reply_text("I doubt that's a user.")
        return log_message

    try:
        member = chat.get_member(user_id)
    except BadRequest as excp:
        if excp.message != "User not found":
            raise
        message.reply_text("I can't seem to find this user.")
        return log_message
    if user_id == bot.id:
        message.reply_text("I'm not gonna BAN myself, are you crazy?")
        return log_message

    if is_user_ban_protected(chat, user_id, member):
        message.reply_text("I don't feel like it.")
        return log_message

    if not reason:
        message.reply_text("You haven't specified a time to ban this user for!")
        return log_message

    split_reason = reason.split(None, 1)

    time_val = split_reason[0].lower()
    reason = split_reason[1] if len(split_reason) > 1 else ""
    bantime = extract_time(message, time_val)

    if not bantime:
        return log_message

    log = (
        f"<b>{html.escape(chat.title)}:</b>\n"
        "#TEMP BANNED\n"
        f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
        f"<b>User:</b> {mention_html(member.user.id, html.escape(member.user.first_name))}\n"
        f"<b>Time:</b> {time_val}"
    )
    if reason:
        log += "\n<b>✤ ʀᴇᴀsᴏɴ:</b> {}".format(reason)

    try:
        chat.kick_member(user_id, until_date=bantime)
        # bot.send_sticker(chat.id, BAN_STICKER)  # banhammer marie sticker
        bot.sendMessage(
            chat.id,
            reply_msg,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="❕ᴜɴʙᴀɴ", callback_data="un_ban({})".format(user_id)
                        ),
                        InlineKeyboardButton(text="🗑️ᴄʟᴏsᴇ", callback_data="close_"),
                    ]
                ]
            ),
            parse_mode=ParseMode.HTML,
        )
        return log

    except BadRequest as excp:
        if excp.message == "Reply message not found":
            # Do not reply
            message.reply_text(
                f"Banned! User will be banned for {time_val}.", quote=False
            )
            return log
        else:
            LOGGER.warning(update)
            LOGGER.exception(
                "ERROR banning user %s in chat %s (%s) due to %s",
                user_id,
                chat.title,
                chat.id,
                excp.message,
            )
            message.reply_text("Well damn, I can't ban that user.")

    return log_message


@user_admin_no_reply
@user_can_ban
@bot_admin
@loggable
def button_unbn(update: Update, context: CallbackContext) -> str:
    query: Optional[CallbackQuery] = update.callback_query
    user: Optional[User] = update.effective_user
    match = re.match(r"un_ban\((.+?)\)", query.data)

    if match:
        user_id = match.group(1)
        chat: Optional[Chat] = update.effective_chat
        user_member = chat.get_member(user_id)
        unabnned = chat.unban_member(user_id)
        if unabnned:
            update.effective_message.edit_text(
                f"✅ {mention_html(user_member.user.id, user_member.user.first_name)} ᴜɴʙᴀɴɴᴇᴅ ʙʏ {mention_html(user.id, user.first_name)} sᴜᴄᴄᴇsғᴜʟʟʏ !!.",
                parse_mode=ParseMode.HTML,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="🗑️ᴄʟᴏsᴇ", callback_data="close_"
                            ),
                        ]
                    ]
                ),
            )

            return (
                f"<b>{html.escape(chat.title)}:</b>\n"
                f"#UNBANNED\n"
                f"<b>Admin:</b> {mention_html(user.id, user.first_name)}\n"
                f"<b>User:</b> {mention_html(user_member.user.id, user_member.user.first_name)}"
            )
        else:
            update.effective_message.edit_text(
                f"ʜᴇʏ {mention_html(user.id, user.first_name)} ᴛʜᴀᴛ ᴜsᴇʀ ᴜɴʙᴀɴɴᴇᴅ ᴀʟʀᴇᴀᴅʏ.",
                parse_mode=ParseMode.HTML,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="🗑️ᴄʟᴏsᴇ", callback_data="close_"
                            ),
                        ]
                    ]
                ),
            )

    return ""


@run_async
@connection_status
@bot_admin
@can_restrict
@user_admin
@user_can_ban
@loggable
def punch(update: Update, context: CallbackContext) -> str:
    chat = update.effective_chat
    user = update.effective_user
    message = update.effective_message
    log_message = ""
    bot, args = context.bot, context.args
    user_id, reason = extract_user_and_text(message, args)

    if not user_id:
        message.reply_text("I doubt that's a user, Is it right🙄.")
        return log_message

    try:
        member = chat.get_member(user_id)
    except BadRequest as excp:
        if excp.message != "User not found":
            raise

        message.reply_text("I can't seem to find this user.")
        return log_message
    if user_id == bot.id:
        message.reply_text("Yeahhh I'm not gonna do that.")
        return log_message

    if is_user_ban_protected(chat, user_id):
        message.reply_text("I really wish I could punch this user....")
        return log_message

    res = chat.unban_member(user_id)  # unban on current user = kick
    if res:
        # bot.send_sticker(chat.id, BAN_STICKER)  # banhammer marie sticker
        bot.sendMessage(
            chat.id,
            f"Yeah!, Okki Sir I kicked!😌 {mention_html(member.user.id, html.escape(member.user.first_name))}.",
            parse_mode=ParseMode.HTML,
        )
        log = (
            f"<b>{html.escape(chat.title)}:</b>\n"
            f"#KICKED\n"
            f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            f"<b>User:</b> {mention_html(member.user.id, html.escape(member.user.first_name))}"
        )
        if reason:
            log += f"\n<b>✤ ʀᴇᴀsᴏɴ:</b> {reason}"

        return log

    else:
        message.reply_text("Well damn, I can't punch that user.")

    return log_message


@run_async
@bot_admin
@can_restrict
def punchme(update: Update, context: CallbackContext):
    user_id = update.effective_message.from_user.id
    if is_user_admin(update.effective_chat, user_id):
        update.effective_message.reply_text("I wish I could... but you're an admin.")
        return

    res = update.effective_chat.unban_member(user_id)  # unban on current user = kick
    if res:
        update.effective_message.reply_text("*punches you out of the group*")
    else:
        update.effective_message.reply_text("Huh? I can't :/")


@run_async
@connection_status
@bot_admin
@can_restrict
@user_admin
@user_can_ban
@loggable
def unban(update: Update, context: CallbackContext) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    log_message = ""
    bot, args = context.bot, context.args
    user_id, reason = extract_user_and_text(message, args)

    if not user_id:
        message.reply_text("I doubt that's a user.")
        return log_message

    try:
        member = chat.get_member(user_id)
    except BadRequest as excp:
        if excp.message != "User not found":
            raise
        message.reply_text("I can't seem to find this user.")
        return log_message
    if user_id == bot.id:
        message.reply_text("How would I unban myself if I wasn't here...?")
        return log_message

    if is_user_in_chat(chat, user_id):
        message.reply_text("Isn't this person already here??")
        return log_message

    ghnta = (
        f"<code>✅</code><b>ᴜsᴇʀ ᴜɴʙᴀɴɴᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ!!</b>\n"
        f"<b>✤  ᴜsᴇʀ:</b> {mention_html(member.user.id, html.escape(member.user.first_name))}\n    ➥ [ <code>{member.user.id}</code> ]\n✤ ᴜɴʙᴀɴɴᴇᴅ ʙʏ: {mention_html(user.id, user.first_name)}"
    )
    chat.unban_member(user_id)
    # message.reply_text("Yep, this user can join!")
    bot.sendMessage(
        chat.id,
        ghnta,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="🗑️ᴄʟᴏsᴇ", callback_data="close_"),
                ]
            ]
        ),
        parse_mode=ParseMode.HTML,
    )
    message.delete()

    log = (
        f"<b>{html.escape(chat.title)}:</b>\n"
        f"#UNBANNED\n"
        f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
        f"<b>User:</b> {mention_html(member.user.id, html.escape(member.user.first_name))}"
    )
    if reason:
        log += f"\n<b>✤ ʀᴇᴀsᴏɴ:</b> {reason}"

    return log


__help__ = """
 ✿ /kickme *:* ᴘᴜɴᴄʜs ᴛʜᴇ ᴜsᴇʀ ᴡʜᴏ ɪssᴜᴇᴅ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ

*ᴀᴅᴍɪɴs ᴏɴʟʏ:*
 ✿ /ban <ᴜsᴇʀʜᴀɴᴅʟᴇ>*:* ʙᴀɴs ᴀ ᴜsᴇʀ. (ᴠɪᴀ ʜᴀɴᴅʟᴇ, ᴏʀ ʀᴇᴘʟʏ)
 ✿ /sban <ᴜsᴇʀʜᴀɴᴅʟᴇ>*:* sɪʟᴇɴᴛʟʏ ʙᴀɴ ᴀ ᴜsᴇʀ. ᴅᴇʟᴇᴛᴇs ᴄᴏᴍᴍᴀɴᴅ, ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ ᴀɴᴅ ᴅᴏᴇsɴ'ᴛ ʀᴇᴘʟʏ. (ᴠɪᴀ ʜᴀɴᴅʟᴇ, ᴏʀ ʀᴇᴘʟʏ)
 ✿ /tban <ᴜsᴇʀʜᴀɴᴅʟᴇ> x(ᴍ/ʜ/ᴅ)*:* ʙᴀɴs ᴀ ᴜsᴇʀ ꜰᴏʀ x ᴛɪᴍᴇ. (ᴠɪᴀ ʜᴀɴᴅʟᴇ, ᴏʀ ʀᴇᴘʟʏ). ᴍ = ᴍɪɴᴜᴛᴇs, ʜ = ʜᴏᴜʀs, ᴅ = ᴅᴀʏs.
 ✿ /unban <ᴜsᴇʀʜᴀɴᴅʟᴇ>*:* ᴜɴʙᴀɴs ᴀ ᴜsᴇʀ. (ᴠɪᴀ ʜᴀɴᴅʟᴇ, ᴏʀ ʀᴇᴘʟʏ)
 ✿ /kick <ᴜsᴇʀʜᴀɴᴅʟᴇ>*:* ᴘᴜɴᴄʜᴇs ᴀ ᴜsᴇʀ ᴏᴜᴛ ᴏꜰ ᴛʜᴇ ɢʀᴏᴜᴘ, (ᴠɪᴀ ʜᴀɴᴅʟᴇ, ᴏʀ ʀᴇᴘʟʏ)

 *ᴀᴅᴍɪɴs ᴏɴʟʏ:*
 ✿ /mute <ᴜsᴇʀʜᴀɴᴅʟᴇ>*:* sɪʟᴇɴᴄᴇs ᴀ ᴜsᴇʀ. ᴄᴀɴ ᴀʟsᴏ ʙᴇ ᴜsᴇᴅ ᴀs ᴀ ʀᴇᴘʟʏ, ᴍᴜᴛɪɴɢ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴜsᴇʀ.
 ✿ /tmute <ᴜsᴇʀʜᴀɴᴅʟᴇ> x(ᴍ/ʜ/ᴅ)*:* ᴍᴜᴛᴇs ᴀ ᴜsᴇʀ ꜰᴏʀ x ᴛɪᴍᴇ. (ᴠɪᴀ ʜᴀɴᴅʟᴇ, ᴏʀ ʀᴇᴘʟʏ). ᴍ = ᴍɪɴᴜᴛᴇs, ʜ = ʜᴏᴜʀs, ᴅ = ᴅᴀʏs.
 ✿ /unmute <ᴜsᴇʀʜᴀɴᴅʟᴇ>*:* ᴜɴᴍᴜᴛᴇs ᴀ ᴜsᴇʀ. ᴄᴀɴ ᴀʟsᴏ ʙᴇ ᴜsᴇᴅ ᴀs ᴀ ʀᴇᴘʟʏ, ᴍᴜᴛɪɴɢ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴜsᴇʀ.
"""

BAN_HANDLER = CommandHandler(["ban", "sban"], ban)
TEMPBAN_HANDLER = CommandHandler(["tban"], temp_ban)
PUNCH_HANDLER = CommandHandler("kick", punch)
UNBAN_HANDLER = CommandHandler("unban", unban)
UNBAN_BUTTON_HANDLER = CallbackQueryHandler(button_unbn, pattern=r"un_ban")
PUNCHME_HANDLER = DisableAbleCommandHandler("kickme", punchme, filters=Filters.group)

dispatcher.add_handler(BAN_HANDLER)
dispatcher.add_handler(TEMPBAN_HANDLER)
dispatcher.add_handler(PUNCH_HANDLER)
dispatcher.add_handler(UNBAN_HANDLER)
dispatcher.add_handler(UNBAN_BUTTON_HANDLER)
dispatcher.add_handler(PUNCHME_HANDLER)

__mod_name__ = "ʙᴀɴs & ᴍᴜᴛᴇ ⭕"
__handlers__ = [
    BAN_HANDLER,
    TEMPBAN_HANDLER,
    PUNCH_HANDLER,
    UNBAN_HANDLER,
    UNBAN_BUTTON_HANDLER,
    PUNCHME_HANDLER,
]
