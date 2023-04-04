from lunaBot.modules.helper_funcs.chat_status import user_admin
from lunaBot.modules.disable import DisableAbleCommandHandler
from lunaBot import dispatcher

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ParseMode, Update
from telegram.ext.dispatcher import run_async
from telegram.ext import CallbackContext, Filters, CommandHandler

MARKDOWN_HELP = f"""
ᴍᴀʀᴋᴅᴏᴡɴ ɪs ᴀ ᴠᴇʀʏ ᴘᴏᴡᴇʀꜰᴜʟ ꜰᴏʀᴍᴀᴛᴛɪɴɢ ᴛᴏᴏʟ sᴜᴘᴘᴏʀᴛᴇᴅ ʙʏ ᴛᴇʟᴇɢʀᴀᴍ. {dispatcher.bot.first_name} ʜᴀs sᴏᴍᴇ ᴇɴʜᴀɴᴄᴇᴍᴇɴᴛs, ᴛᴏ ᴍᴀᴋᴇ sᴜʀᴇ ᴛʜᴀᴛ \
sᴀᴠᴇᴅ ᴍᴇssᴀɢᴇs ᴀʀᴇ ᴄᴏʀʀᴇᴄᴛʟʏ ᴘᴀʀsᴇᴅ, ᴀɴᴅ ᴛᴏ ᴀʟʟᴏᴡ ʏᴏᴜ ᴛᴏ ᴄʀᴇᴀᴛᴇ ʙᴜᴛᴛᴏɴs.

• <code>_italic_</code> : ᴡʀᴀᴘᴘɪɴɢ ᴛᴇxᴛ ᴡɪᴛʜ '_' ᴡɪʟʟ ᴘʀᴏᴅᴜᴄᴇ ɪᴛᴀʟɪᴄ ᴛᴇxᴛ
• <code>*bold*</code> : ᴡʀᴀᴘᴘɪɴɢ ᴛᴇxᴛ ᴡɪᴛʜ '*' ᴡɪʟʟ ᴘʀᴏᴅᴜᴄᴇ ʙᴏʟᴅ ᴛᴇxᴛ
• <code>`code`</code> : ᴡʀᴀᴘᴘɪɴɢ ᴛᴇxᴛ ᴡɪᴛʜ '`' ᴡɪʟʟ ᴘʀᴏᴅᴜᴄᴇ ᴍᴏɴᴏsᴘᴀᴄᴇᴅ ᴛᴇxᴛ, ᴀʟsᴏ ᴋɴᴏᴡɴ ᴀs 'ᴄᴏᴅᴇ'
• <code>[sometext](someURL)</code> : ᴛʜɪs ᴡɪʟʟ ᴄʀᴇᴀᴛᴇ ᴀ ʟɪɴᴋ - ᴛʜᴇ ᴍᴇssᴀɢᴇ ᴡɪʟʟ ᴊᴜsᴛ sʜᴏᴡ <code>sometext</code>, \
ᴀɴᴅ ᴛᴀᴘᴘɪɴɢ ᴏɴ ɪᴛ ᴡɪʟʟ ᴏᴘᴇɴ ᴛʜᴇ ᴘᴀɢᴇ ᴀᴛ <code>someURL</code>
<b>Example:</b><code>[test](example.com)</code>

• <code>[buttontext](buttonurl:someURL)</code> : ᴛʜɪs ɪs ᴀ sᴘᴇᴄɪᴀʟ ᴇɴʜᴀɴᴄᴇᴍᴇɴᴛ ᴛᴏ ᴀʟʟᴏᴡ ᴜsᴇʀs ᴛᴏ ʜᴀᴠᴇ ᴛᴇʟᴇɢʀᴀᴍ \
ʙᴜᴛᴛᴏɴs ɪɴ ᴛʜᴇɪʀ ᴍᴀʀᴋᴅᴏᴡɴ. <code>buttontext</code> ᴡɪʟʟ ʙᴇ ᴡʜᴀᴛ ɪs ᴅɪsᴘʟᴀʏᴇᴅ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴ, ᴀɴᴅ <code>someurl</code> \
ᴡɪʟʟ ʙᴇ ᴛʜᴇ ᴜʀʟ ᴡʜɪᴄʜ ɪs ᴏᴘᴇɴᴇᴅ.
<b>Example:</b> <code>[This is a button](buttonurl:example.com)</code>

ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴍᴜʟᴛɪᴘʟᴇ ʙᴜᴛᴛᴏɴs ᴏɴ ᴛʜᴇ sᴀᴍᴇ ʟɪɴᴇ, ᴜsᴇ :sᴀᴍᴇ, ᴀs sᴜᴄʜ:
<code>[one](buttonurl://example.com)
[two](buttonurl://google.com:same)</code>
ᴛʜɪs ᴡɪʟʟ ᴄʀᴇᴀᴛᴇ ᴛᴡᴏ ʙᴜᴛᴛᴏɴs ᴏɴ ᴀ sɪɴɢʟᴇ ʟɪɴᴇ, ɪɴsᴛᴇᴀᴅ ᴏꜰ ᴏɴᴇ ʙᴜᴛᴛᴏɴ ᴘᴇʀ ʟɪɴᴇ.

ᴋᴇᴇᴘ ɪɴ ᴍɪɴᴅ ᴛʜᴀᴛ ʏᴏᴜʀ ᴍᴇssᴀɢᴇ <b>MUST</b> ᴄᴏɴᴛᴀɪɴ sᴏᴍᴇ ᴛᴇxᴛ ᴏᴛʜᴇʀ ᴛʜᴀɴ ᴊᴜsᴛ ᴀ ʙᴜᴛᴛᴏɴ!
"""


@run_async
@user_admin
def echo(update: Update, context: CallbackContext):
    args = update.effective_message.text.split(None, 1)
    message = update.effective_message

    if message.reply_to_message:
        message.reply_to_message.reply_text(
            args[1], parse_mode="MARKDOWN", disable_web_page_preview=True
        )
    else:
        message.reply_text(
            args[1], quote=False, parse_mode="MARKDOWN", disable_web_page_preview=True
        )
    message.delete()


def markdown_help_sender(update: Update):
    update.effective_message.reply_text(MARKDOWN_HELP, parse_mode=ParseMode.HTML)
    update.effective_message.reply_text(
        "Try forwarding the following message to me, and you'll see, and Use #test!"
    )
    update.effective_message.reply_text(
        "/save test This is a markdown test. _italics_, *bold*, code, "
        "[URL](example.com) [button](buttonurl:github.com) "
        "[button2](buttonurl://google.com:same)"
    )


@run_async
def markdown_help(update: Update, context: CallbackContext):
    if update.effective_chat.type != "private":
        update.effective_message.reply_text(
            "Contact me in pm",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Markdown help",
                            url=f"t.me/{context.bot.username}?start=markdownhelp",
                        )
                    ]
                ]
            ),
        )
        return
    markdown_help_sender(update)


__help__ = """
*ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:*
*ᴍᴀʀᴋᴅᴏᴡɴ:*
 ✿ /markdownhelp*:* ǫᴜɪᴄᴋ sᴜᴍᴍᴀʀʏ ᴏꜰ ʜᴏᴡ ᴍᴀʀᴋᴅᴏᴡɴ ᴡᴏʀᴋs ɪɴ ᴛᴇʟᴇɢʀᴀᴍ - ᴄᴀɴ ᴏɴʟʏ ʙᴇ ᴄᴀʟʟᴇᴅ ɪɴ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛs
*ᴘᴀsᴛᴇ:*
 ✿ /paste*:* sᴀᴠᴇs ʀᴇᴘʟɪᴇᴅ ᴄᴏɴᴛᴇɴᴛ ᴛᴏ nekobin.com ᴀɴᴅ ʀᴇᴘʟɪᴇs ᴡɪᴛʜ ᴀ ᴜʀʟ
*ʀᴇᴀᴄᴛ:*
 ✿ /react*:* ʀᴇᴀᴄᴛs ᴡɪᴛʜ ᴀ ʀᴀɴᴅᴏᴍ ʀᴇᴀᴄᴛɪᴏɴ 
*ᴜʀʙᴀɴ ᴅɪᴄᴛᴏɴᴀʀʏ:*
 ✿ /ud <ᴡᴏʀᴅ>*:* ᴛʏᴘᴇ ᴛʜᴇ ᴡᴏʀᴅ ᴏʀ ᴇxᴘʀᴇssɪᴏɴ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴇᴀʀᴄʜ ᴜsᴇ
*ᴡɪᴋɪᴘᴇᴅɪᴀ:*
 ✿ /wiki <ǫᴜᴇʀʏ>*:* ᴡɪᴋɪᴘᴇᴅɪᴀ ʏᴏᴜʀ ǫᴜᴇʀʏ
*ᴡᴀʟʟᴘᴀᴘᴇʀs:*
 ✿ /wall <ǫᴜᴇʀʏ>*:* ɢᴇᴛ ᴀ ᴡᴀʟʟᴘᴀᴘᴇʀ ꜰʀᴏᴍ wall.alphacoders.com
*ʟɪᴠᴇ ᴄʀɪᴄᴋᴇᴛ sᴄᴏʀᴇ*
 ✿ /cs*:* ʟᴀᴛᴇsᴛ ʟɪᴠᴇ sᴄᴏʀᴇs ꜰʀᴏᴍ ᴄʀɪᴄɪɴꜰᴏ
*ᴄᴜʀʀᴇɴᴄʏ ᴄᴏɴᴠᴇʀᴛᴇʀ:* 
 ✿ /cash*:* ᴄᴜʀʀᴇɴᴄʏ ᴄᴏɴᴠᴇʀᴛᴇʀ
ᴇxᴀᴍᴘʟᴇ:
` /cash 1 USD INR`
      _ᴏʀ_
`/cash 1 USD INR`
ᴏᴜᴛᴘᴜᴛ: `1.0 USD = 75.505 INR`

*ᴍᴀᴛʜs*
sᴏʟᴠᴇs ᴄᴏᴍᴘʟᴇx ᴍᴀᴛʜ ᴘʀᴏʙʟᴇᴍs ᴜsɪɴɢ https://newton.now.sh
✿ /math *:* ᴍᴀᴛʜ `/math 2^2+2(2)`
✿ /factor *:* ꜰᴀᴄᴛᴏʀ `/factor x^2 + 2x`
✿ /derive *:* ᴅᴇʀɪᴠᴇ `/derive x^2+2x`
✿ /integrate *:* ɪɴᴛᴇɢʀᴀᴛᴇ `/integrate x^2+2x`
✿ /zeroes *:* ꜰɪɴᴅ 0's `/zeroes x^2+2x`
✿ /tangent *:* ꜰɪɴᴅ ᴛᴀɴɢᴇɴᴛ `/tangent 2lx^3`
✿ /area *:* ᴀʀᴇᴀ ᴜɴᴅᴇʀ ᴄᴜʀᴠᴇ `/area 2:4lx^3`
✿ /cos *:* ᴄᴏsɪɴᴇ `/cos pi`
✿ /sin *:* sɪɴᴇ `/sin 0`
✿ /tan *:* ᴛᴀɴɢᴇɴᴛ `/tan 0`
✿ /arccos *:* ɪɴᴠᴇʀsᴇ ᴄᴏsɪɴᴇ `/arccos 1`
✿ /arcsin *:* ɪɴᴠᴇʀsᴇ sɪɴᴇ `/arcsin 0`
✿ /arctan *:* ɪɴᴠᴇʀsᴇ ᴛᴀɴɢᴇɴᴛ `/arctan 0`
✿ /abs *:* ᴀʙsᴏʟᴜᴛᴇ ᴠᴀʟᴜᴇ `/abs -1`
✿ /log *:* ʟᴏɢᴀʀɪᴛʜᴍ `/log 2l8`

**ᴋᴇᴇᴘ ɪɴ ᴍɪɴᴅ**: ᴛᴏ ꜰɪɴᴅ ᴛʜᴇ ᴛᴀɴɢᴇɴᴛ ʟɪɴᴇ ᴏꜰ ᴀ ꜰᴜɴᴄᴛɪᴏɴ ᴀᴛ ᴀ ᴄᴇʀᴛᴀɪɴ x ᴠᴀʟᴜᴇ, sᴇɴᴅ ᴛʜᴇ ʀᴇǫᴜᴇsᴛ ᴀs ᴄ|ꜰ(x) ᴡʜᴇʀᴇ ᴄ ɪs ᴛʜᴇ ɢɪᴠᴇɴ x ᴠᴀʟᴜᴇ ᴀɴᴅ ꜰ(x) ɪs ᴛʜᴇ ꜰᴜɴᴄᴛɪᴏɴ ᴇxᴘʀᴇssɪᴏɴ, ᴛʜᴇ sᴇᴘᴀʀᴀᴛᴏʀ ɪs ᴀ ᴠᴇʀᴛɪᴄᴀʟ ʙᴀʀ '|'. sᴇᴇ ᴛʜᴇ ᴛᴀʙʟᴇ ᴀʙᴏᴠᴇ ꜰᴏʀ ᴀɴ ᴇxᴀᴍᴘʟᴇ ʀᴇǫᴜᴇsᴛ.
ᴛᴏ ꜰɪɴᴅ ᴛʜᴇ ᴀʀᴇᴀ ᴜɴᴅᴇʀ ᴀ ꜰᴜɴᴄᴛɪᴏɴ, sᴇɴᴅ ᴛʜᴇ ʀᴇǫᴜᴇsᴛ ᴀs ᴄ:ᴅ|ꜰ(x) ᴡʜᴇʀᴇ ᴄ ɪs ᴛʜᴇ sᴛᴀʀᴛɪɴɢ x ᴠᴀʟᴜᴇ, ᴅ ɪs ᴛʜᴇ ᴇɴᴅɪɴɢ x ᴠᴀʟᴜᴇ, ᴀɴᴅ ꜰ(x) ɪs ᴛʜᴇ ꜰᴜɴᴄᴛɪᴏɴ ᴜɴᴅᴇʀ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴᴛ ᴛʜᴇ ᴄᴜʀᴠᴇ ʙᴇᴛᴡᴇᴇɴ ᴛʜᴇ ᴛᴡᴏ x ᴠᴀʟᴜᴇs.
ᴛᴏ ᴄᴏᴍᴘᴜᴛᴇ ꜰʀᴀᴄᴛɪᴏɴs, ᴇɴᴛᴇʀ ᴇxᴘʀᴇssɪᴏɴs ᴀs ɴᴜᴍᴇʀᴀᴛᴏʀ(ᴏᴠᴇʀ)ᴅᴇɴᴏᴍɪɴᴀᴛᴏʀ. ꜰᴏʀ ᴇxᴀᴍᴘʟᴇ, ᴛᴏ ᴘʀᴏᴄᴇss 2/4 ʏᴏᴜ ᴍᴜsᴛ sᴇɴᴅ ɪɴ ʏᴏᴜʀ ᴇxᴘʀᴇssɪᴏɴ ᴀs 2(ᴏᴠᴇʀ)4. ᴛʜᴇ ʀᴇsᴜʟᴛ ᴇxᴘʀᴇssɪᴏɴ ᴡɪʟʟ ʙᴇ ɪɴ sᴛᴀɴᴅᴀʀᴅ ᴍᴀᴛʜ ɴᴏᴛᴀᴛɪᴏɴ (1/2, 3/4).

💡`ʀᴇᴀᴅ ꜰʀᴏᴍ ᴛᴏᴘ`

"""

ECHO_HANDLER = DisableAbleCommandHandler("echo", echo, filters=Filters.group)
MD_HELP_HANDLER = CommandHandler("markdownhelp", markdown_help)

dispatcher.add_handler(ECHO_HANDLER)
dispatcher.add_handler(MD_HELP_HANDLER)

__mod_name__ = "ᴇxᴛʀᴀs ⭐"
__command_list__ = ["id", "echo"]
__handlers__ = [
    ECHO_HANDLER,
    MD_HELP_HANDLER,
]
