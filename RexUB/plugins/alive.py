# RexUB
import asyncio
from pyrogram import *
from pyrogram.types import *
from RexUB.modules.helpers.basics import edit_or_reply
from RexUB.modules.helpers.filters import command
from RexUB.utilities.misc import SUDOERS


@Client.on_message(command(["alive"]) & SUDOERS)
async def mother_chod(client: Client, message: Message):
    await edit_or_reply(message, "**🥀 I Aᴍ Aʟɪᴠᴇ Mʏ Dᴇᴀʀ Rᴇxᴜʙ Mᴀsᴛᴇʀ ✨ ...**")



__MODULE__ = "Aʟɪᴠᴇ"
__HELP__ = f"""
**🥀 Tᴇsᴛ Yᴏᴜʀ Bᴏᴛ Wᴏʀᴋɪɴɢ Oʀ Nᴏᴛ.**

`.alive` - **Usᴇ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Cʜᴇᴄᴋ**
"""
