import os

import requests
from faker import Faker
from faker.providers import internet
from telethon import events

from lunaBot.pyrogramee.telethonbasics import is_admin
from lunaBot import telethn as tbot


@tbot.on(events.NewMessage(pattern="/fakeinfo$"))
async def hi(event):
    if event.fwd_from:
        return
    if event.is_group:
        if not await is_admin(event, event.message.sender_id):
            await event.reply("`ʏᴏᴜ sʜᴏᴜʟᴅ ʙᴇ ᴀᴅᴍɪɴ ᴛᴏ ᴅᴏ ᴛʜɪs!`")
            return
    fake = Faker()
    print("ꜰᴀᴋᴇ ᴅᴇᴛᴀɪʟs ɢᴇɴᴇʀᴀᴛᴇᴅ\n")
    name = str(fake.name())
    fake.add_provider(internet)
    address = str(fake.address())
    ip = fake.ipv4_private()
    cc = fake.credit_card_full()
    email = fake.ascii_free_email()
    job = fake.job()
    android = fake.android_platform_token()
    pc = fake.chrome()
    await event.reply(
        f"<b><u> ꜰᴀᴋᴇ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ɢᴇɴᴇʀᴀᴛᴇᴅ</b></u>\n<b>ɴᴀᴍᴇ :-</b><code>{name}</code>\n\n<b>ᴀᴅᴅʀᴇss:-</b><code>{address}</code>\n\n<b>ʏᴏᴜʀ ɪᴘ-ᴀᴅᴅʀᴇss:-</b><code>{ip}</code>\n\n<b>ʏᴏᴜʀ ᴄᴄ-ᴅᴇᴛᴀɪʟs:-</b><code>{cc}</code>\n\n<b>ʏᴏᴜʀ ᴍᴀɪʟ-ɪᴅ:-</b><code>{email}</code>\n\n<b>ᴊᴏʙ-ᴅᴇᴛᴀɪʟs:-</b><code>{job}</code>\n\n<b>ᴀɴᴅʀᴏɪᴅ ᴜsᴇʀ ᴀɢᴇɴᴛ:-</b><code>{android}</code>\n\n<b>ᴘᴄ ᴜsᴇʀ ᴀɢᴇɴᴛ:-</b><code>{pc}</code>\n\n<code>",
        parse_mode="HTML",
    )


@tbot.on(events.NewMessage(pattern="/fakepic$"))
async def _(event):
    if event.fwd_from:
        return
    if await is_admin(event, event.message.sender_id):
        url = "https://thispersondoesnotexist.com/image"
        response = requests.get(url)
        if response.status_code == 200:
            with open("luna.jpg", "wb") as f:
                f.write(response.content)

        captin = f"ʏᴏᴜʀ ғᴀᴋᴇ ɪᴍɢ ɢᴇɴᴇʀᴀᴛᴇᴅ ʏᴜᴘ!🥀\n\n`➬➬ Pᴏᴡᴇʀᴇᴅ Bʏ Cᴏɴᴛʀᴏʟʟᴇʀ` [Tᴇᴀᴍ-Sɪʟᴇɴᴛ💞](t.me/SILENT_DEVS) ✨."
        fole = "luna.jpg"
        await tbot.send_file(event.chat_id, fole, caption=captin, parse_mode="MARKDOWN")
        await event.delete()
        os.system("rm ./luna.jpg ")
