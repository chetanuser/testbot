import os
import asyncio
import random
from platform import python_version as kontol
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from lunaBot.resources.stuff.useless1 import ALIV, DEVUAD, atxt
from lunaBot import pbot as sree
from pyrogram import filters


@sree.on_message(filters.command("alive"))
async def awake(bot, l: Message):
    userid = l.from_user.id
    name = l.from_user.first_name
    semx = random.choice(ALIV)
    ok = await l.reply_text(f"ʜᴇʏ {name} 💞,\nᴡᴀɪᴛ ʙᴏᴛ ɪs ᴘʀᴇᴘᴀʀɪɴɢ ꜰᴏʀ ᴀʟɪᴠᴇ!! ✨")
    await asyncio.sleep(2)
    await ok.delete()
    t1 = await l.reply_text("⚡️")
    await asyncio.sleep(2)
    t2 = await t1.edit_text("__ᴀʟɪᴠɪɴɢ...__")
    await asyncio.sleep(0)
    t3 = await t2.edit_text("__ᴀʟɪᴠɪɴɢ.....__")
    await asyncio.sleep(0)
    t4 = await t3.edit_text("__ᴀʟɪᴠɪɴɢ...__")
    await asyncio.sleep(0)
    t5 = await t4.edit_text("__ᴀʟɪᴠɪɴɢ.....__")
    await asyncio.sleep(0)
    t6 = await t5.edit_text("__ᴀʟɪᴠɪɴɢ...__")
    await asyncio.sleep(0)
    await t6.delete()
    str = await l.reply_sticker(
        "CAACAgUAAx0CXL6UewACCgti3UiJPAteIAAB5-VVmwN-Q4Ow_QMAAm4GAAJeyulW5ITkAd_53zMpBA"
    )
    await asyncio.sleep(3)
    await str.delete()
    await l.reply_video(
        semx,
        caption=atxt.format(name, userid, tlhver, pyrover),
        reply_markup=InlineKeyboardMarkup(DEVUAD),
    )
    await l.delete()
