import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import *
from random import choice
from DAXXMUSIC import app
from config import API_ID, API_HASH, ASSUSERNAME

IMG = ["https://graph.org/file/1aaff3780b5ba59cb1f63.jpg", "https://graph.org/file/1aaff3780b5ba59cb1f63.jpg", "https://graph.org/file/1aaff3780b5ba59cb1f63.jpg", "https://graph.org/file/1aaff3780b5ba59cb1f63.jpg"]
MESSAGE = "Heya! I'm a music bot hoster/Cloner\n\nI can Host Your Bot On My Server within seconds\n\nTry /clone Token from @botfather"

@app.on_message(filters.private & filters.command("copy"))
async def copy(client, message: Message):
    buttons = [
           [
                InlineKeyboardButton("✘ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ", url="t.me/"),
            ],
            [
                InlineKeyboardButton("✘ ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url="t.me/"),
            ],
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_photo(message.chat.id, f"{choice(IMG)}", caption=MESSAGE, reply_markup=reply_markup)

