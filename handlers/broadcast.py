# Copyright (C) 2021 By StrayCoder
# Originally written by levina on github
# Broadcast function


import asyncio

from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant

from callsmusic.callsmusic import client as aditya
from config import SUDO_USERS

@Client.on_message(filters.command(["gcast"]))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("Broadcast Starting 🔄")
        if not message.reply_to_message:
            await wtf.edit("**Please reply to a message to broadcast❗**")
            return
        lmao = message.reply_to_message.text
        async for dialog in aditya.iter_dialogs():
            try:
                await aditya.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"`BroadCasting❗` \n\n**Sent To:** `{sent}` Chats\n**Failed In :** {failed} chats")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await message.reply_text(f"`BroadCast succesfully` \n\n**Sent To :** `{sent}` chats\n**Failed In :** {failed} Chats")
