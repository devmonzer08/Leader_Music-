from YukkiMusic.utils.database import is_music_playing, music_off
from strings import get_command
import asyncio
from strings.filters import command
from YukkiMusic import app
from YukkiMusic.core.call import Yukki
from YukkiMusic.utils.database import set_loop
from YukkiMusic.utils.decorators import AdminRightsCheck
from YukkiMusic.utils.database import is_muted, mute_on
from YukkiMusic.utils.database import is_muted, mute_off
from YukkiMusic.utils.database import is_music_playing, music_on
from datetime import datetime
from config import BANNED_USERS, MUSIC_BOT_NAME, PING_IMG_URL, lyrical, START_IMG_URL, MONGO_DB_URI, OWNER_ID
from YukkiMusic.utils import bot_sys_stats
from YukkiMusic.utils.decorators.language import language
import random
import config
import re
from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
import string
import lyricsgenius as lg
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from pyrogram import Client, filters
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
import sys
from os import getenv
from dotenv import load_dotenv

load_dotenv()

BOT_USERNAME = getenv("BOT_USERNAME")

START_IMG_URL = getenv("START_IMG_URL")

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME")

# Commands
STOP_COMMAND = get_command("STOP_COMMAND")
PAUSE_COMMAND = get_command("PAUSE_COMMAND")
MUTE_COMMAND = get_command("MUTE_COMMAND")
UNMUTE_COMMAND = get_command("UNMUTE_COMMAND")
RESUME_COMMAND = get_command("RESUME_COMMAND")
PING_COMMAND = get_command("PING_COMMAND")
LYRICS_COMMAND = get_command("LYRICS_COMMAND")

api_key = "Vd9FvPMOKWfsKJNG9RbZnItaTNIRFzVyyXFdrGHONVsGqHcHBoj3AI3sIlNuqzuf0ZNG8uLcF9wAd5DXBBnUzA"
y = lg.Genius(
    api_key,
    skip_non_songs=True,
    excluded_terms=["(Remix)", "(Live)"],
    remove_section_headers=True,
)
y.verbose = False


    
@app.on_message(
    command(["قول"])
    & filters.group
    & ~filters.edited
)
@app.on_message(
    command(["قول"])
    & filters.private
    & ~filters.edited
)
@app.on_message(
    command(["قول"])
    & filters.channel
    & ~filters.edited
)
def echo(client, msg):
    text = msg.text.split(None, 1)[1]
    msg.reply(text)

@app.on_message(
    command(["انا مين"])
    & filters.group
    & ~filters.edited
)
@app.on_message(
    command(["انا مين"])
    & filters.private
    & ~filters.edited
)
@app.on_message(
    command(["انا مين"])
    & filters.channel
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""انت {message.from_user.mention} روح قلبي .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ ᥉᥆υᖇᥴᥱ ᥲ️ᖇꪀ᥆ρ . 🐰 ›", url=f"https://t.me/N_G_12"),
                ],
            ]
        ),
    )

@app.on_message(
     command(["شغل","تشغيل","سوره","سورة","اغنيه","اغنية","/skip","/settings","/play","/vplay","/stop"])
    & filters.private
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/30c40c9b5d5aa28102c7a.jpg",
        caption=f""" • عذرا  !. لا يمكنك التشغيل في الخاص\n\n• قم بأنشاء جروب ثم ضفني لكي اعمل\n\n• معلومات التشغيل انضم @Ng_334\n\n• البوت الميوزك  @A_Rn_obot\n\n• تقدر تشغل كل ما تحتاجه """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("‹ اضف البوت مجموعتك ›", url=f"https://t.me/A_Rn_obot?startgroup=true"),
                ],[
                InlineKeyboardButton(
                        "‹ ᥉᥆υᖇᥴᥱ ᥲ️ᖇꪀ᥆ρ . 🐰 ›", url=f"https://t.me/N_G_12"), 
                ]
            ]
        ),
    )

@app.on_message(
     command(["اسمي"])
    & filters.private
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/d1f75386af9cf775c0c52.jpg",
        caption=f""" 🐉 | اسـمـڪ  : [ `{name}` ]\n✓ """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("‹ اضف البوت مجموعتك ›", url=f"https://t.me/A_Rn_obot?startgroup=true"),
                ],[
                InlineKeyboardButton(
                        "‹ ᥉᥆υᖇᥴᥱ ᥲ️ᖇꪀ᥆ρ . 🐰 ›", url=f"https://t.me/N_G_12"), 
                ]
            ]
        ),
    )

@app.on_message(
     command(["يوزري","معرفي"])
    & filters.private
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/d1f75386af9cf775c0c52.jpg",
        caption=f""" 🐉 | يـوزرڪ : [ @{user} ] \n✓ """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("‹ اضف البوت مجموعتك ›", url=f"https://t.me/A_Rn_obot?startgroup=true"),
                ],[
                InlineKeyboardButton(
                        "‹ ᥉᥆υᖇᥴᥱ ᥲ️ᖇꪀ᥆ρ . 🐰 ›", url=f"https://t.me/N_G_12"), 
                ]
            ]
        ),
    )

@app.on_message(
     command(["بايو","البايو"])
    & filters.private
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/d1f75386af9cf775c0c52.jpg",
        caption=f""" 🐉 | البـايـو : [ `{kbio}` ] \n✓""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("‹ اضف البوت مجموعتك ›", url=f"https://t.me/A_Rn_obot?startgroup=true"),
                ],[
                InlineKeyboardButton(
                        "‹ ᥉᥆υᖇᥴᥱ ᥲ️ᖇꪀ᥆ρ . 🐰 ›", url=f"https://t.me/N_G_12"), 
                ]
            ]
        ),
    )
                    
@app.on_message(
     command(["مبرمج السورس","نادر"])
    & filters.group
    & ~filters.edited
)
@app.on_message(
     command(["مبرمج السورس","نادر"])
    & filters.channel
    & ~filters.edited
)
@app.on_message(
     command(["مبرمج السورس","نادر"])
    & filters.private
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/37e224b04dfedf222f8d2.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪ [𓏺 ժᥱ᥎ ꪀᥲ️ժᥱᖇ . 🕷 ˼](https://t.me/Ng_103)  ❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @Ng_103 ❫
◉ 𝙸𝙳   : ❪ 5054546767 ❫
◉ 𝙱𝙸𝙾  : ❪ انا كبير في عين نفسي. انما عينك انتا تع احطلك فيها قطره. @Ng_104 ❫ """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("‹ ժᥱ᥎ ꪀᥲ️ժᥱᖇ ›", url=f"https://t.me/Ng_103"),
                ],[
                InlineKeyboardButton(
                        "‹ ᥉᥆υᖇᥴᥱ ᥲ️ᖇꪀ᥆ρ . 🐰 › ", url=f"https://t.me/N_G_12"), 
                ]
            ]
        ),
    )

@app.on_message(
     command(["مبرمج البوت","المبرمج"])
    & filters.group
    & ~filters.edited
)
@app.on_message(
     command(["مبرمج البوت","المبرمج"])
    & filters.private
    & ~filters.edited
)
@app.on_message(
     command(["مبرمج البوت","المبرمج"])
    & filters.channel
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/37e224b04dfedf222f8d2.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪ [𓏺 ժᥱ᥎ ꪀᥲ️ժᥱᖇ . 🕷 ˼](https://t.me/Ng_103)  ❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @Ng_103 ❫
◉ 𝙸𝙳   : ❪ 5054546767 ❫
◉ 𝙱𝙸𝙾  : ❪ انا كبير في عين نفسي. انما عينك انتا تع احطلك فيها قطره. @Ng_104 ❫ """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("‹ ժᥱ᥎ ꪀᥲ️ժᥱᖇ ›", url=f"https://t.me/Ng_103"),
                ],[
                InlineKeyboardButton(
                        "‹ ᥉᥆υᖇᥴᥱ ᥲ️ᖇꪀ᥆ρ . 🐰 ›", url=f"https://t.me/N_G_12"), 
                ]
            ]
        ),
    )

@app.on_message(
     command(["صاحب السورس","صاحب العظمه","نادور","نادر"])
    & filters.group
    & ~filters.edited
)
@app.on_message(
     command(["صاحب السورس","صاحب العظمه","نادير","نادر"])
    & filters.channel
    & ~filters.edited
)
@app.on_message(
     command(["صاحب السورس","صاحب العظمه","نادير","نادر"])
    & filters.private
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/37e224b04dfedf222f8d2.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪ [𓏺 ժᥱ᥎ ꪀᥲ️ժᥱᖇ . 🕷 ˼](https://t.me/Ng_103)  ❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @Ng_103 ❫
◉ 𝙸𝙳   : ❪ 5054546767 ❫
◉ 𝙱𝙸𝙾  : ❪ انا كبير في عين نفسي. انما عينك انتا تع احطلك فيها قطره. @Ng_104 ❫ """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("‹ ժᥱ᥎ ꪀᥲ️ժᥱᖇ ›", url=f"https://t.me/Ng_103"),
                ],[
                InlineKeyboardButton(
                        "‹ ᥉᥆υᖇᥴᥱ ᥲ️ᖇꪀ᥆ρ . 🐰 ›", url=f"https://t.me/N_G_12"), 
                ]
            ]
        ),
    )

@app.on_message(
     command(["المطور نادر","المبرمج نادر"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/37e224b04dfedf222f8d2.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪ [𓏺 ժᥱ᥎ ꪀᥲ️ժᥱᖇ . 🕷 ˼](https://t.me/Ng_103)  ❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @Ng_103 ❫
◉ 𝙸𝙳   : ❪ 5054546767 ❫
◉ 𝙱𝙸𝙾  : ❪ انا كبير في عين نفسي. انما عينك انتا تع احطلك فيها قطره. @Ng_104 ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("‹ ժᥱ᥎ ꪀᥲ️ժᥱᖇ ›", url=f"https://t.me/Ng_103"),
                ],[
                InlineKeyboardButton(
                        "‹ ᥉᥆υᖇᥴᥱ ᥲ️ᖇꪀ᥆ρ . 🐰 ›", url=f"https://t.me/N_G_12"), 
                ]
            ]
        ),
    )

@app.on_message(
    command(["سورس","السورس","يا سورس"])
    & filters.group
    & ~filters.edited
)
@app.on_message(
    command(["سورس","السورس","يا سورس"])
    & filters.channel
    & ~filters.edited
)
@app.on_message(
    command(["سورس","السورس","يا سورس","قناة","قناه"])
    & filters.private
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/09e50c75b48945d209829.jpg",
        caption=f"""╭──── • ◈ • ────╮
么 [َ ᥉᥆υᖇᥴᥱ ᥲ️ᖇꪀ᥆ρ](t.me/N_G_12)
么 [َժᥱ᥎ ꪀᥲ️ժᥱᖇ](t.me/Ng_103)
么 [َ ᥉υρρ᥆ᖇƚ ](t.me/Ng_333)
╰──── • ◈ • ────╯
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "‹ ժᥱ᥎ ꪀᥲ️ժᥱᖇ . 🕷 › ", url=f"https://t.me/Ng_103"),
                ],[
                    InlineKeyboardButton(
                        "‹ ᥴ𝗁ᥲ️ꪀꪀᥱᥣ›", url=f"https://t.me/N_G_12"), 
                    InlineKeyboardButton(
                        "‹ ᥉υρρ᥆ᖇƚ›", url=f"https://t.me/Ng_333"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف البوت لمجموعتك ›", url=f"https://t.me/A_Rn_obot?startgroup=true"),
            ]
        ]
         ),
     )
  
