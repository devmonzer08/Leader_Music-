import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
     command(["/help", "الاوامر"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/c6c72a67afca445b3175a.jpg",
caption=f"""**[᥉ᥱᥣᥣᥴƚ ᥣᥲ️ꪀᘜυᥲ️ᘜᥱ ƚ᥆ ᥣᥱᥲ️ᖇꪀ ꪔ᥆ᖇᥱ](https://t.me/N_G_12)**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(
                    "عربي 🇪🇬", callback_data="arbic"
                ),
                ],
                [
                    InlineKeyboardButton(
                        "English 🇺🇲", callback_data="english"),
                ],
            ]
        ),
    )


