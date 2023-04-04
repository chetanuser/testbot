import html
import re

from telegram import (
    ParseMode,
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from telegram import ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Filters,
    run_async,
    CallbackQueryHandler,
)
from telegram.utils.helpers import mention_html

from lunaBot import DRAGONS, dispatcher
from lunaBot.modules.disable import DisableAbleCommandHandler
from lunaBot.modules.helper_funcs.chat_status import (
    bot_admin,
    can_pin,
    can_promote,
    connection_status,
    user_admin,
    ADMIN_CACHE,
)
from lunaBot.helper_extra.admin_rights import (
    user_can_pin,
    user_can_promote,
    user_can_changeinfo,
)

from lunaBot.modules.helper_funcs.extraction import (
    extract_user,
    extract_user_and_text,
)
from lunaBot.modules.log_channel import loggable
from lunaBot.modules.helper_funcs.alternate import send_message
from lunaBot.modules.helper_funcs.alternate import typing_action


WRONG_IG = "https://telegra.ph/file/debbb4b9f7f1a12c1f034.png"


@run_async
@connection_status
@bot_admin
@can_promote
@user_admin
@loggable
def promote(update: Update, context: CallbackContext) -> str:
    bot = context.bot
    args = context.args

    message = update.effective_message
    chat = update.effective_chat
    user = update.effective_user

    promoter = chat.get_member(user.id)

    if (
        not (promoter.can_promote_members or promoter.status == "creator")
        and user.id not in DRAGONS
    ):
        message.reply_photo(
            WRONG_IG, caption="You don't have the necessary rights to do that!"
        )
        return

    user_id = extract_user(message, args)

    if not user_id:
        message.reply_text(
            "You don't seem to be referring to a user or the ID specified is incorrect.."
        )
        return

    try:
        user_member = chat.get_member(user_id)
    except:
        return

    if user_member.status == "administrator" or user_member.status == "creator":
        message.reply_photo(
            WRONG_IG,
            caption="How am I meant to promote someone that's already an admin?",
        )
        return

    if user_id == bot.id:
        message.reply_photo(
            WRONG_IG, caption="I can't promote myself! Get an admin to do it for me."
        )
        return

    # set same perms as bot - bot can't assign higher perms than itself!
    bot_member = chat.get_member(bot.id)

    try:
        bot.promoteChatMember(
            chat.id,
            user_id,
            # can_change_info=bot_member.can_change_info,
            can_post_messages=bot_member.can_post_messages,
            can_edit_messages=bot_member.can_edit_messages,
            can_delete_messages=bot_member.can_delete_messages,
            can_invite_users=bot_member.can_invite_users,
            # can_promote_members=bot_member.can_promote_members,
            # can_restrict_members=bot_member.can_restrict_members,
            can_pin_messages=bot_member.can_pin_messages,
        )
    except BadRequest as err:
        if err.message == "User_not_mutual_contact":
            message.reply_photo(
                WRONG_IG, caption="I can't promote someone who isn't in the group."
            )
        else:
            message.reply_photo(WRONG_IG, caption="An error occured while promoting.")
        return

    keyboard = [
        [
            InlineKeyboardButton(
                "", callback_data="demote_({})".format(user_member.user.id)
            )
        ]
    ]

    bot.sendMessage(
        chat.id,
        f"💖 sᴜᴄᴄᴇsғᴜʟʟʏ ᴘʀᴏᴍᴏᴛᴇᴅ ɪɴ <b>{chat.title}</b>\n\n࿂ ᴜsᴇʀ: {mention_html(user_member.user.id, user_member.user.first_name)}\n\n࿂ ᴘʀᴏᴍᴏᴛᴇʀ: {mention_html(user.id, user.first_name)}",
        parse_mode=ParseMode.HTML,
    )

    log_message = (
        f"<b>{html.escape(chat.title)}:</b>\n"
        f"USER PROMOTED SUCCESSFULLY\n"
        f"<b>Admin:</b> {mention_html(user.id, user.first_name)}\n"
        f"<b>User:</b> {mention_html(user_member.user.id, user_member.user.first_name)}"
    )

    return log_message


@run_async
@connection_status
@bot_admin
@can_promote
@user_admin
@loggable
def spromote(update: Update, context: CallbackContext) -> str:
    bot = context.bot
    args = context.args

    message = update.effective_message
    chat = update.effective_chat
    user = update.effective_user

    promoter = chat.get_member(user.id)

    if (
        not (promoter.can_promote_members or promoter.status == "creator")
        and user.id not in DRAGONS
    ):
        message.reply_photo(
            WRONG_IG, caption="You don't have the necessary rights to do that!"
        )
        return

    user_id = extract_user(message, args)

    if not user_id:
        message.reply_text(
            "You don't seem to be referring to a user or the ID specified is incorrect.."
        )
        return

    try:
        user_member = chat.get_member(user_id)
    except:
        return

    if user_member.status == "administrator" or user_member.status == "creator":
        message.reply_photo(
            WRONG_IG,
            caption="How am I meant to promote someone that's already an admin?",
        )
        return

    if user_id == bot.id:
        message.reply_photo(
            WRONG_IG, caption="I can't promote myself! Get an admin to do it for me."
        )
        return

    # set same perms as bot - bot can't assign higher perms than itself!
    bot_member = chat.get_member(bot.id)

    try:
        bot.promoteChatMember(
            chat.id,
            user_id,
            # can_change_info=bot_member.can_change_info,
            # can_post_messages=bot_member.can_post_messages,
            can_edit_messages=bot_member.can_edit_messages,
            # can_delete_messages=bot_member.can_delete_messages,
            can_invite_users=bot_member.can_invite_users,
            # can_promote_members=bot_member.can_promote_members,
            # can_restrict_members=bot_member.can_restrict_members,
            # can_pin_messages=bot_member.can_pin_messages,
        )
    except BadRequest as err:
        if err.message == "User_not_mutual_contact":
            message.reply_photo(
                WRONG_IG, caption="I can't promote someone who isn't in the group."
            )
        else:
            message.reply_photo(WRONG_IG, caption="An error occured while promoting.")
        return

    bot.sendMessage(
        chat.id,
        f"💖 sᴜᴄᴄᴇsғᴜʟʟʏ sᴀsᴛᴀ ᴘʀᴏᴍᴏᴛᴇᴅ ɪɴ <b>{chat.title}</b>\n\n࿂ sᴀsᴛᴀ ᴜsᴇʀ: {mention_html(user_member.user.id, user_member.user.first_name)}\n\n࿂ ᴘʀᴏᴍᴏᴛᴇʀ: {mention_html(user.id, user.first_name)}",
        parse_mode=ParseMode.HTML,
    )

    log_message = (
        f"<b>{html.escape(chat.title)}:</b>\n"
        f"USER PROMOTED SUCCESSFULLY\n"
        f"<b>Admin:</b> {mention_html(user.id, user.first_name)}\n"
        f"<b>User:</b> {mention_html(user_member.user.id, user_member.user.first_name)}"
    )

    return log_message


@run_async
@connection_status
@bot_admin
@can_promote
@user_admin
@loggable
def fullpromote(update: Update, context: CallbackContext) -> str:
    bot = context.bot
    args = context.args

    message = update.effective_message
    chat = update.effective_chat
    user = update.effective_user

    promoter = chat.get_member(user.id)

    if (
        not (promoter.can_promote_members or promoter.status == "creator")
        and user.id not in DRAGONS
    ):
        message.reply_photo(
            WRONG_IG, caption="You don't have the necessary rights to do that!"
        )
        return

    user_id = extract_user(message, args)

    if not user_id:
        message.reply_text(
            "You don't seem to be referring to a user or the ID specified is incorrect.."
        )
        return

    try:
        user_member = chat.get_member(user_id)
    except:
        return

    if user_member.status == "administrator" or user_member.status == "creator":
        message.reply_photo(
            WRONG_IG,
            caption="How am I meant to promote someone that's already an admin?",
        )
        return

    if user_id == bot.id:
        message.reply_photo(
            WRONG_IG, caption="I can't promote myself! Get an admin to do it for me."
        )
        return

    # set same perms as bot - bot can't assign higher perms than itself!
    bot_member = chat.get_member(bot.id)

    try:
        bot.promoteChatMember(
            chat.id,
            user_id,
            can_change_info=bot_member.can_change_info,
            can_post_messages=bot_member.can_post_messages,
            can_edit_messages=bot_member.can_edit_messages,
            can_delete_messages=bot_member.can_delete_messages,
            can_invite_users=bot_member.can_invite_users,
            can_promote_members=bot_member.can_promote_members,
            can_restrict_members=bot_member.can_restrict_members,
            can_pin_messages=bot_member.can_pin_messages,
        )
    except BadRequest as err:
        if err.message == "User_not_mutual_contact":
            message.reply_photo(
                WRONG_IG, caption="I can't promote someone who isn't in the group."
            )
        else:
            message.reply_photo(WRONG_IG, caption="An error occured while promoting.")
        return

    bot.sendMessage(
        chat.id,
        f"💖 sᴜᴄᴄᴇsғᴜʟʟʏ ғᴜʟʟᴘʀᴏᴍᴏᴛᴇᴅ ɪɴ <b>{chat.title}</b>\n\n࿂ ᴜsᴇʀ: {mention_html(user_member.user.id, user_member.user.first_name)}\n\n࿂ ᴘʀᴏᴍᴏᴛᴇʀ: {mention_html(user.id, user.first_name)}",
        parse_mode=ParseMode.HTML,
    )

    log_message = (
        f"<b>{html.escape(chat.title)}:</b>\n"
        f"USER FULLPROMOTED SUCCESSFULLY\n"
        f"<b>Admin:</b> {mention_html(user.id, user.first_name)}\n"
        f"<b>User:</b> {mention_html(user_member.user.id, user_member.user.first_name)}"
    )

    return log_message


@run_async
@connection_status
@bot_admin
@can_promote
@user_admin
@loggable
def demote(update: Update, context: CallbackContext) -> str:
    bot = context.bot
    args = context.args

    chat = update.effective_chat
    message = update.effective_message
    user = update.effective_user

    user_id = extract_user(message, args)

    if user_can_promote(chat, user, context.bot.id) is False:
        message.reply_text("You don't have enough rights to demote someone!")
        return ""

    if not user_id:
        message.reply_text(
            "You don't seem to be referring to a user or the ID specified is incorrect.."
        )
        return

    try:
        user_member = chat.get_member(user_id)
    except:
        return

    if user_member.status == "creator":
        message.reply_text("This person CREATED the chat, how would I demote them?")
        return

    if not user_member.status == "administrator":
        message.reply_text("Can't demote what wasn't promoted!")
        return

    if user_id == bot.id:
        message.reply_text("I can't demote myself! Get an admin to do it for me.")
        return

    try:
        bot.promoteChatMember(
            chat.id,
            user_id,
            can_change_info=False,
            can_post_messages=False,
            can_edit_messages=False,
            can_delete_messages=False,
            can_invite_users=False,
            can_restrict_members=False,
            can_pin_messages=False,
            can_promote_members=False,
        )

        bot.sendMessage(
            chat.id,
            f"💖 sᴜᴄᴄᴇsғᴜʟʟʏ ᴅᴇᴍᴏᴛᴇᴅ ɪɴ <b>{chat.title}</b>\n\n࿂ ᴜsᴇʀ: {mention_html(user_member.user.id, user_member.user.first_name)}\n\n࿂ ᴘʀᴏᴍᴏᴛᴇʀ: {mention_html(user.id, user.first_name)}",
            parse_mode=ParseMode.HTML,
        )

        log_message = (
            f"<b>{html.escape(chat.title)}:</b>\n"
            f"USER DEMOTED SUCCESSFULLY\n"
            f"<b>Admin:</b> {mention_html(user.id, user.first_name)}\n"
            f"<b>User:</b> {mention_html(user_member.user.id, user_member.user.first_name)}"
        )

        return log_message
    except BadRequest:
        message.reply_text(
            "Could not demote. I might not be admin, or the admin status was appointed by another"
            " user, so I can't act upon them!"
        )
        return


@run_async
@user_admin
def refresh_admin(update, _):
    try:
        ADMIN_CACHE.pop(update.effective_chat.id)
    except KeyError:
        pass

    update.effective_message.reply_text("ʏᴏʏᴏ ᴀᴅᴍɪɴ ᴄᴀᴄʜᴇ ʀᴇғʀᴇsʜᴇᴅ ฅ^•ﻌ•^ฅ!!")


@run_async
@connection_status
@bot_admin
@can_promote
@user_admin
def set_title(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args

    chat = update.effective_chat
    message = update.effective_message

    user_id, title = extract_user_and_text(message, args)
    try:
        user_member = chat.get_member(user_id)
    except:
        return

    if not user_id:
        message.reply_text(
            "You don't seem to be referring to a user or the ID specified is incorrect.."
        )
        return

    if user_member.status == "creator":
        message.reply_text(
            "This person CREATED the chat, how can i set custom title for him?"
        )
        return

    if user_member.status != "administrator":
        message.reply_text(
            "Can't set title for non-admins!\nPromote them first to set custom title!"
        )
        return

    if user_id == bot.id:
        message.reply_text(
            "I can't set my own title myself! Get the one who made me admin to do it for me."
        )
        return

    if not title:
        message.reply_text("Setting blank title doesn't do anything!")
        return

    if len(title) > 16:
        message.reply_text(
            "The title length is longer than 16 characters.\nTruncating it to 16 characters."
        )

    try:
        bot.setChatAdministratorCustomTitle(chat.id, user_id, title)
    except BadRequest:
        message.reply_text("I can't set custom title for admins that I didn't promote!")
        return

    bot.sendMessage(
        chat.id,
        f"Sucessfully set title for <code>{user_member.user.first_name or user_id}</code> "
        f"to <code>{html.escape(title[:16])}</code>!",
        parse_mode=ParseMode.HTML,
    )


@run_async
@bot_admin
@user_admin
@typing_action
def setchatpic(update, context):
    chat = update.effective_chat
    msg = update.effective_message
    user = update.effective_user

    if user_can_changeinfo(chat, user, context.bot.id) is False:
        msg.reply_text("You are missing right to change group info!")
        return

    if msg.reply_to_message:
        if msg.reply_to_message.photo:
            pic_id = msg.reply_to_message.photo[-1].file_id
        elif msg.reply_to_message.document:
            pic_id = msg.reply_to_message.document.file_id
        else:
            msg.reply_text("You can only set some photo as chat pic!")
            return
        dlmsg = msg.reply_text("Just a sec...")
        tpic = context.bot.get_file(pic_id)
        tpic.download("gpic.png")
        try:
            with open("gpic.png", "rb") as chatp:
                context.bot.set_chat_photo(int(chat.id), photo=chatp)
                msg.reply_text("Successfully set new chatpic!")
        except BadRequest as excp:
            msg.reply_text(f"Error! {excp.message}")
        finally:
            dlmsg.delete()
            if os.path.isfile("gpic.png"):
                os.remove("gpic.png")
    else:
        msg.reply_text("Reply to some photo or file to set new chat pic!")


@run_async
@bot_admin
@user_admin
@typing_action
def rmchatpic(update, context):
    chat = update.effective_chat
    msg = update.effective_message
    user = update.effective_user

    if user_can_changeinfo(chat, user, context.bot.id) is False:
        msg.reply_text("You don't have enough rights to delete group photo")
        return
    try:
        context.bot.delete_chat_photo(int(chat.id))
        msg.reply_text("Successfully deleted chat's profile photo!")
    except BadRequest as excp:
        msg.reply_text(f"Error! {excp.message}.")
        return


@run_async
@bot_admin
@user_admin
@typing_action
def setchat_title(update, context):
    chat = update.effective_chat
    msg = update.effective_message
    user = update.effective_user
    args = context.args

    if user_can_changeinfo(chat, user, context.bot.id) is False:
        msg.reply_text("You don't have enough rights to change chat info!")
        return

    title = " ".join(args)
    if not title:
        msg.reply_text("Enter some text to set new title in your chat!")
        return

    try:
        context.bot.set_chat_title(int(chat.id), str(title))
        msg.reply_text(
            f"Successfully set <b>{title}</b> as new chat title!",
            parse_mode=ParseMode.HTML,
        )
    except BadRequest as excp:
        msg.reply_text(f"Error! {excp.message}.")
        return


@run_async
@bot_admin
@user_admin
@typing_action
def set_sticker(update, context):
    msg = update.effective_message
    chat = update.effective_chat
    user = update.effective_user

    if user_can_changeinfo(chat, user, context.bot.id) is False:
        return msg.reply_text("You're missing rights to change chat info!")

    if msg.reply_to_message:
        if not msg.reply_to_message.sticker:
            return msg.reply_text(
                "You need to reply to some sticker to set chat sticker set!"
            )
        stkr = msg.reply_to_message.sticker.set_name
        try:
            context.bot.set_chat_sticker_set(chat.id, stkr)
            msg.reply_text(f"Successfully set new group stickers in {chat.title}!")
        except BadRequest as excp:
            if excp.message == "Participants_too_few":
                return msg.reply_text(
                    "Sorry, due to telegram restrictions chat needs to have minimum 100 members before they can have group stickers!"
                )
            msg.reply_text(f"Error! {excp.message}.")
    else:
        msg.reply_text("You need to reply to some sticker to set chat sticker set!")


@run_async
@bot_admin
@user_admin
@typing_action
def set_desc(update, context):
    msg = update.effective_message
    chat = update.effective_chat
    user = update.effective_user

    if user_can_changeinfo(chat, user, context.bot.id) is False:
        return msg.reply_text("You're missing rights to change chat info!")

    tesc = msg.text.split(None, 1)
    if len(tesc) >= 2:
        desc = tesc[1]
    else:
        return msg.reply_text("Setting empty description won't do anything!")
    try:
        if len(desc) > 255:
            return msg.reply_text("Description must needs to be under 255 characters!")
        context.bot.set_chat_description(chat.id, desc)
        msg.reply_text(f"Successfully updated chat description in {chat.title}!")
    except BadRequest as excp:
        msg.reply_text(f"Error! {excp.message}.")


def __chat_settings__(chat_id, user_id):
    return "You are *admin*: `{}`".format(
        dispatcher.bot.get_chat_member(chat_id, user_id).status
        in ("administrator", "creator")
    )


@run_async
@bot_admin
@can_pin
@user_admin
@loggable
def pin(update: Update, context: CallbackContext) -> str:
    bot = context.bot
    args = context.args

    user = update.effective_user
    chat = update.effective_chat

    is_group = chat.type != "private" and chat.type != "channel"
    prev_message = update.effective_message.reply_to_message

    if user_can_pin(chat, user, context.bot.id) is False:
        message.reply_text("You are missing rights to pin a message!")
        return ""

    is_silent = True
    if len(args) >= 1:
        is_silent = not (
            args[0].lower() == "notify"
            or args[0].lower() == "loud"
            or args[0].lower() == "violent"
        )

    if prev_message and is_group:
        try:
            bot.pinChatMessage(
                chat.id, prev_message.message_id, disable_notification=is_silent
            )
        except BadRequest as excp:
            if excp.message == "Chat_not_modified":
                pass
            else:
                raise
        log_message = (
            f"<b>{html.escape(chat.title)}:</b>\n"
            f"MESSAGE PINNED SUCCESSFULLY\n"
            f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}"
        )

        return log_message


@run_async
@bot_admin
@can_pin
@user_admin
@loggable
def unpin(update: Update, context: CallbackContext) -> str:
    bot = context.bot
    chat = update.effective_chat
    user = update.effective_user

    try:
        bot.unpinChatMessage(chat.id)
    except BadRequest as excp:
        if excp.message == "Chat_not_modified":
            pass
        else:
            raise

    log_message = (
        f"<b>{html.escape(chat.title)}:</b>\n"
        f"MESSAGE UNPINNED SUCCESSFULLY\n"
        f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}"
    )

    return log_message


@run_async
@bot_admin
@user_admin
@connection_status
def invite(update: Update, context: CallbackContext):
    bot = context.bot
    chat = update.effective_chat

    if chat.username:
        update.effective_message.reply_text(f"https://t.me/{chat.username}")
    elif chat.type in [chat.SUPERGROUP, chat.CHANNEL]:
        bot_member = chat.get_member(bot.id)
        if bot_member.can_invite_users:
            invitelink = bot.exportChatInviteLink(chat.id)
            update.effective_message.reply_text(invitelink)
        else:
            update.effective_message.reply_text(
                "I don't have access to the invite link, try changing my permissions!"
            )
    else:
        update.effective_message.reply_text(
            "I can only give you invite links for supergroups and channels, sorry!"
        )


@run_async
@connection_status
def adminlist(update, context):
    chat = update.effective_chat  # type: Optional[Chat]
    user = update.effective_user  # type: Optional[User]
    args = context.args
    bot = context.bot

    if update.effective_message.chat.type == "private":
        send_message(update.effective_message, "This command only works in Groups.")
        return

    chat = update.effective_chat
    chat_id = update.effective_chat.id
    chat_name = update.effective_message.chat.title

    try:
        msg = update.effective_message.reply_text(
            "Fetching group admins...", parse_mode=ParseMode.HTML
        )
    except BadRequest:
        msg = update.effective_message.reply_text(
            "Fetching group admins...", quote=False, parse_mode=ParseMode.HTML
        )

    administrators = bot.getChatAdministrators(chat_id)
    text = "Admins in <b>{}</b>:".format(html.escape(update.effective_chat.title))

    bot_admin_list = []

    for admin in administrators:
        user = admin.user
        status = admin.status
        custom_title = admin.custom_title

        if user.first_name == "":
            name = "☠ Deleted Account"
        else:
            name = "{}".format(
                mention_html(
                    user.id, html.escape(user.first_name + " " + (user.last_name or ""))
                )
            )

        if user.is_bot:
            bot_admin_list.append(name)
            administrators.remove(admin)
            continue

        # if user.username:
        #    name = escape_markdown("@" + user.username)
        if status == "creator":
            text += "\n 👑 Creator:"
            text += "\n<code> • </code>{}\n".format(name)

            if custom_title:
                text += f"<code> ┗━ {html.escape(custom_title)}</code>\n"

    text += "\n🔱 Admins:"

    custom_admin_list = {}
    normal_admin_list = []

    for admin in administrators:
        user = admin.user
        status = admin.status
        custom_title = admin.custom_title

        if user.first_name == "":
            name = "☠ Deleted Account"
        else:
            name = "{}".format(
                mention_html(
                    user.id, html.escape(user.first_name + " " + (user.last_name or ""))
                )
            )
        # if user.username:
        #    name = escape_markdown("@" + user.username)
        if status == "administrator":
            if custom_title:
                try:
                    custom_admin_list[custom_title].append(name)
                except KeyError:
                    custom_admin_list.update({custom_title: [name]})
            else:
                normal_admin_list.append(name)

    for admin in normal_admin_list:
        text += "\n<code> • </code>{}".format(admin)

    for admin_group in custom_admin_list.copy():
        if len(custom_admin_list[admin_group]) == 1:
            text += "\n<code> • </code>{} | <code>{}</code>".format(
                custom_admin_list[admin_group][0], html.escape(admin_group)
            )
            custom_admin_list.pop(admin_group)

    text += "\n"
    for admin_group, value in custom_admin_list.items():
        text += "\n🚨 <code>{}</code>".format(admin_group)
        for admin in value:
            text += "\n<code> • </code>{}".format(admin)
        text += "\n"

    text += "\n🤖 Bots:"
    for each_bot in bot_admin_list:
        text += "\n<code> • </code>{}".format(each_bot)

    try:
        msg.edit_text(text, parse_mode=ParseMode.HTML)
    except BadRequest:  # if original message is deleted
        return


# ❍ /antispam <on/off/yes/no>*:* Will toggle our antispam tech or return your current settings.

__help__ = """
 ✿ /adminlist *:* ʟɪsᴛ ᴏꜰ ᴀᴅᴍɪɴs ɪɴ ᴛʜᴇ ᴄʜᴀᴛ

*ᴀᴅᴍɪɴs ᴏɴʟʏ:*
 ✿ /pin *:* sɪʟᴇɴᴛʟʏ ᴘɪɴs ᴛʜᴇ ᴍᴇssᴀɢᴇ ʀᴇᴘʟɪᴇᴅ ᴛᴏ - ᴀᴅᴅ 'ʟᴏᴜᴅ' ᴏʀ 'ɴᴏᴛɪꜰʏ' ᴛᴏ ɢɪᴠᴇ ɴᴏᴛɪꜰs ᴛᴏ ᴜsᴇʀs
 ✿ /unpin *:* ᴜɴᴘɪɴs ᴛʜᴇ ᴄᴜʀʀᴇɴᴛʟʏ ᴘɪɴɴᴇᴅ ᴍᴇssᴀɢᴇ
 ✿ /getlink *:* ɢᴇᴛs ɪɴᴠɪᴛᴇʟɪɴᴋ
 ✿ /promote *:* ᴘʀᴏᴍᴏᴛᴇs ᴛʜᴇ ᴜsᴇʀ
 ✿ /demote *:* ᴅᴇᴍᴏᴛᴇs ᴛʜᴇ ᴜsᴇʀ
 ✿ /title <ᴛɪᴛʟᴇ ʜᴇʀᴇ>*:* sᴇᴛs ᴀ ᴄᴜsᴛᴏᴍ ᴛɪᴛʟᴇ ꜰᴏʀ ᴀɴ ᴀᴅᴍɪɴ ᴛʜᴀᴛ ᴛʜᴇ ʙᴏᴛ ᴘʀᴏᴍᴏᴛᴇᴅ
 ✿ /setgtitle <ɴᴇᴡᴛɪᴛʟᴇ>*:* sᴇᴛs ɴᴇᴡ ᴄʜᴀᴛ ᴛɪᴛʟᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
 ✿ /setgpic *:* ᴀs ᴀ ʀᴇᴘʟʏ ᴛᴏ ꜰɪʟᴇ ᴏʀ ᴘʜᴏᴛᴏ ᴛᴏ sᴇᴛ ɢʀᴏᴜᴘ ᴘʀᴏꜰɪʟᴇ ᴘɪᴄ!
 ✿ /rmgpic *:* sᴀᴍᴇ ᴀs ᴀʙᴏᴠᴇ ʙᴜᴛ ᴛᴏ ʀᴇᴍᴏᴠᴇ ɢʀᴏᴜᴘ ᴘʀᴏꜰɪʟᴇ ᴘɪᴄ.
 ✿ /setsticker *:* ᴀs ᴀ ʀᴇᴘʟʏ ᴛᴏ sᴏᴍᴇ sᴛɪᴄᴋᴇʀ ᴛᴏ sᴇᴛ ɪᴛ ᴀs ɢʀᴏᴜᴘ sᴛɪᴄᴋᴇʀ sᴇᴛ!
 ✿ /setdescription <ᴅᴇsᴄʀɪᴘᴛɪᴏɴ>*:* sᴇᴛs ɴᴇᴡ ᴄʜᴀᴛ ᴅᴇsᴄʀɪᴘᴛɪᴏɴ ɪɴ ɢʀᴏᴜᴘ.
 ✿ /refresh *:* ꜰᴏʀᴄᴇ ʀᴇꜰʀᴇsʜ ᴛʜᴇ ᴀᴅᴍɪɴs ʟɪsᴛ.
 ✿ /del *:* ᴅᴇʟᴇᴛᴇs ᴛʜᴇ ᴍᴇssᴀɢᴇ ʏᴏᴜ ʀᴇᴘʟɪᴇᴅ ᴛᴏ
 ✿ /purge *:* ᴅᴇʟᴇᴛᴇs ᴀʟʟ ᴍᴇssᴀɢᴇs ʙᴇᴛᴡᴇᴇɴ ᴛʜɪs ᴀɴᴅ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴍᴇssᴀɢᴇ.
 ✿ /purge  <ɪɴᴛᴇɢᴇʀ x>*:* ᴅᴇʟᴇᴛᴇs ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ, ᴀɴᴅ x ᴍᴇssᴀɢᴇs ꜰᴏʟʟᴏᴡɪɴɢ ɪᴛ ɪꜰ ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ.
 ✿ /zombies : ᴄᴏᴜɴᴛs ᴛʜᴇ ɴᴜᴍʙᴇʀ ᴏꜰ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ
 ✿ `/zombies clean` : ʀᴇᴍᴏᴠᴇ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs ꜰʀᴏᴍ ɢʀᴏᴜᴘ..

*ɴᴏᴛᴇ:* ɴɪɢʜᴛ ᴍᴏᴅᴇ ᴄʜᴀᴛs ɢᴇᴛ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴄʟᴏsᴇᴅ ᴀᴛ 12 ᴀᴍ(ɪsᴛ)
ᴀɴᴅ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴏᴘᴇɴɴᴇᴅ ᴀᴛ 6 ᴀᴍ(ɪsᴛ) ᴛᴏ ᴘʀᴇᴠᴇɴᴛ ɴɪɢʜᴛ sᴘᴀᴍs.

`⚠️ ʀᴇᴀᴅ ꜰʀᴏᴍ ᴛᴏᴘ`
"""

ADMINLIST_HANDLER = DisableAbleCommandHandler("adminlist", adminlist)

PIN_HANDLER = CommandHandler("pin", pin, filters=Filters.group)
UNPIN_HANDLER = CommandHandler("unpin", unpin, filters=Filters.group)

INVITE_HANDLER = DisableAbleCommandHandler("getlink", invite)

PROMOTE_HANDLER = DisableAbleCommandHandler("promote", promote)
DEMOTE_HANDLER = DisableAbleCommandHandler("demote", demote)
FULLPROMOTE_HANDLER = DisableAbleCommandHandler("fullpromote", fullpromote)
SPROMOTE_HANDLER = DisableAbleCommandHandler("spromote", spromote)

SET_TITLE_HANDLER = CommandHandler("title", set_title)
ADMIN_REFRESH_HANDLER = CommandHandler("refresh", refresh_admin, filters=Filters.group)

CHAT_PIC_HANDLER = CommandHandler("setgpic", setchatpic, filters=Filters.group)
DEL_CHAT_PIC_HANDLER = CommandHandler("rmgpic", rmchatpic, filters=Filters.group)
SETCHAT_TITLE_HANDLER = CommandHandler(
    "setgtitle", setchat_title, filters=Filters.group
)
SETSTICKET_HANDLER = CommandHandler("setsticker", set_sticker, filters=Filters.group)
SETDESC_HANDLER = CommandHandler("setdescription", set_desc, filters=Filters.group)

dispatcher.add_handler(ADMINLIST_HANDLER)
dispatcher.add_handler(PIN_HANDLER)
dispatcher.add_handler(UNPIN_HANDLER)
dispatcher.add_handler(INVITE_HANDLER)
dispatcher.add_handler(PROMOTE_HANDLER)
dispatcher.add_handler(DEMOTE_HANDLER)
dispatcher.add_handler(SET_TITLE_HANDLER)
dispatcher.add_handler(ADMIN_REFRESH_HANDLER)
dispatcher.add_handler(CHAT_PIC_HANDLER)
dispatcher.add_handler(DEL_CHAT_PIC_HANDLER)
dispatcher.add_handler(SETCHAT_TITLE_HANDLER)
dispatcher.add_handler(SETSTICKET_HANDLER)
dispatcher.add_handler(SETDESC_HANDLER)
dispatcher.add_handler(FULLPROMOTE_HANDLER)
dispatcher.add_handler(SPROMOTE_HANDLER)

__mod_name__ = "ᴀᴅᴍɪɴs ✅"
__command_list__ = [
    "adminlist",
    "admins",
    "invitelink",
    "promote",
    "demote",
    "admincache",
]
__handlers__ = [
    ADMINLIST_HANDLER,
    PIN_HANDLER,
    UNPIN_HANDLER,
    INVITE_HANDLER,
    PROMOTE_HANDLER,
    DEMOTE_HANDLER,
    SPROMOTE_HANDLER,
    FULLPROMOTE_HANDLER,
    SET_TITLE_HANDLER,
    ADMIN_REFRESH_HANDLER,
]
