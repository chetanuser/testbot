from lunaBot import telethn as sree
from telethon import events, Button
from lunaBot import JOIN_LOGGER, EVENT_LOGS


@sree.on(events.NewMessage(incoming=True, func=lambda d: not d.is_group))
async def sreehyper(e):
    usrid = e.sender.id
    name = e.sender.first_name
    buttons = [Button.url(f"{name}", f"https://t.me/{e.sender.username}")]
    chtid = int(EVENT_LOGS)
    msg = """New user message!!
SenderINFO--
Name: `{}`

User id: `{}`
  
Sender: [{}](tg://user?id={})"""
    await e.forward_to(chtid)
    await sree.send_message(
        chtid, msg.format(name, usrid, name, usrid), buttons=buttons
    )
