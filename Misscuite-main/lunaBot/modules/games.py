from telethon.tl.types import InputMediaDice

from lunaBot.events import register


@register(pattern="^/dice(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    r = await event.reply(file=InputMediaDice(""))
    input_int = int(input_str)
    if input_int > 6:
        await event.reply("ʜᴇʏ ɴɪɢɢᴀ ᴜsᴇ ɴᴜᴍʙᴇʀ 1 ᴛᴏ 6 ᴏɴʟʏ")

    else:
        try:
            required_number = input_int
            while r.media.value != required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice(""))
        except BaseException:
            pass


@register(pattern="^/dart(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    r = await event.reply(file=InputMediaDice("🎯"))
    input_int = int(input_str)
    if input_int > 6:
        await event.reply("ʜᴇʏ ɴɪɢɢᴀ ᴜsᴇ ɴᴜᴍʙᴇʀ 1 ᴛᴏ 6 ᴏɴʟʏ")

    else:
        try:
            required_number = input_int
            while r.media.value != required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice("🎯"))
        except BaseException:
            pass


@register(pattern="^/ball(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    r = await event.reply(file=InputMediaDice("🏀"))
    input_int = int(input_str)
    if input_int > 5:
        await event.reply("ʜᴇʏ ɴɪɢɢᴀ ᴜsᴇ ɴᴜᴍʙᴇʀ 1 ᴛᴏ 6 ᴏɴʟʏ")

    else:
        try:
            required_number = input_int
            while r.media.value != required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice("🏀"))
        except BaseException:
            pass


__mod_name__ = "ɢᴀᴍᴇ 🔥"

__help__ = """
✦ `ʜᴇʀᴇ ɪs ᴛʜᴇ ᴅᴇᴛᴀɪʟs ғᴏʀ sᴏᴍᴇ ɴᴏʀᴍᴀʟ ɢᴀᴍᴇ ᴄᴍᴅs ʟɪᴋᴇ ᴅɪᴄᴇ,sʟᴀᴘ,ᴅᴀʀᴛ ᴇᴛᴄ.`

✿ /dice : `ᴛʜʀᴏᴡɪɴɢ ʀᴀɴᴅᴏᴍ ᴅɪᴄᴇ. `
✿ /dart : `ᴛʜʀᴏᴡɪɴɢ ʀᴀɴᴅᴏᴍ sᴍᴀʟʟ ᴀʀʀᴏᴡ ᴛᴏ ᴀ ᴘᴏɪɴᴛ. `
✿ /ball : `ᴘʟᴀʏɪɴɢ ʙᴀsᴇʙᴀʟʟ. `
✿ /slap `(ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ)` : `sʟᴀᴘᴘɪɴɢ ʀᴇᴘʟʏɪᴇᴅ ᴜsᴇʀ. `
✿ /decide : `ᴘʀᴇᴅɪᴄᴛɪɴɢ ᴀʙᴏᴜᴛ ᴇɪᴛʜᴇʀ ᴛʜᴇ sᴛᴀᴛᴇᴍᴇɴᴛ ɪs ᴛʀᴜᴇ ᴏғ ғᴀʟsᴇ. `
✿ /run : `ᴜsᴇ ɴᴅ sᴇᴇ.`
✿ /roll : `ᴜsᴇ ɴᴅ sᴇᴇ ғᴏʀ ғᴜɴ.`
✿ /toss : `ᴛᴏss ᴠɪʀᴛᴜᴀʟ ᴄᴏɪɴ.`
✿ /shh : `ᴜsᴇ ɴᴅ sᴇᴇ.`
✿ /tball : `ᴜsᴇ ɪᴛ ғᴏʀ ғᴜɴ.`
✿ /truth : `ɢɪᴠɪɴɢ ᴄʜᴀʟʟᴀɴɢᴇ ᴛᴏ sᴀʏ ᴛʀᴜᴛʜ ᴀʙᴏᴜᴛ ᴛʜᴇ ǫᴜᴇsᴛɪᴏɴ ᴛʜᴀᴛ ʙᴏᴛ ᴡɪʟʟ ᴀsᴋ ᴛᴏ ʏᴏᴜ. 🥲`
✿ /dare : `ɢɪᴠɪɴɢ ᴅᴀʀᴇ ᴛᴏ ᴜsᴇʀ ᴛᴏ ᴅᴏ ᴡʜɪᴄʜ ʙᴏᴛ ᴡɪʟʟ sᴀʏ ᴀғᴛᴇʀ ᴜsɪɴɢ ᴛʜɪs ᴄᴍᴅ. `
"""
