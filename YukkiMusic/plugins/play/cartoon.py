###############################################
##  CopyRight & Creator File And Programing  ##
##                                           ##
##     #######  ######  #####*     *##*      ##
##     #  #  #  ###     #     *   *    *     ##
##     #     #  ##      #     *   *    *     ##
##     #     #  #####   #####*     *##*      ##
##                                           ##
###############################################

import asyncio

from strings import get_command
from strings.filters import command
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from YukkiMusic import app

################################
####
################################

@app.on_message(
    command(["كرتون"])
    & ~filters.edited
)
async def cartoon(c: Client, m: Message):
    global mid
    mid = m.message_id
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("انمي 🧚‍♀️", callback_data="anmie2 " + str(m.from_user.id))],
        [InlineKeyboardButton("مسلسلات كارتون 👼", callback_data="fmoslsl " + str(m.from_user.id))],
        [InlineKeyboardButton("افلام كارتون 🍿", callback_data="fcartoon " + str(m.from_user.id))],

        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.reply_text("◍ أهلا بيك بقائمه افلام ومسلسلات الكارتون والانمي\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^cartoon2 (\\d+)$"))
async def cartoon2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("انمي 🧚‍♀️", callback_data="anmie2 " + str(m.from_user.id))],
        [InlineKeyboardButton("مسلسلات كارتون 👼", callback_data="fmoslsl " + str(m.from_user.id))],
        [InlineKeyboardButton("افلام كارتون 🍿", callback_data="fcartoon " + str(m.from_user.id))],

        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ أهلا بيك بقائمه افلام ومسلسلات الكارتون والانمي\n√", reply_markup=keyboard)


#####################################################################################################
######################################################################################################
#####################################################################################################
@app.on_callback_query(filters.regex("^anmie (\\d+)$"))
async def anmie(c: Client, m: Message):
    global mid
    mid = m.message_id
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("هنتر اكس هنتر 🌝", callback_data="hinterx " + str(m.from_user.id))],
        [InlineKeyboardButton("طوكيو غول 😎", callback_data="tokyo " + str(m.from_user.id))],
        [InlineKeyboardButton("هجوم العمالقه 🎉", callback_data="hgoom " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="cartoon2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.reply_text("◍ اهلا بيك في قايمة الانمي\n√", reply_markup=keyboard)


# anime
@app.on_callback_query(filters.regex("^anmie2 (\\d+)$"))
async def anmie2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("هنتر اكس هنتر 🌝", callback_data="hinterx " + str(m.from_user.id))],
        [InlineKeyboardButton("طوكيو غول 😎", callback_data="tokyo " + str(m.from_user.id))],
        [InlineKeyboardButton("هجوم العمالقه 🎉", callback_data="hgoom " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="cartoon2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك في قايمة الانمي\n√", reply_markup=keyboard)


########################################################################################
#########################################################################################
##############   hinter x hinter  #########
@app.on_callback_query(filters.regex("^hinterx (\\d+)$"))
async def hinterx(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("الجزء الاول 1⃣", callback_data="hinterx1 " + str(m.from_user.id))],
        [InlineKeyboardButton("الجزء التاني 2⃣", callback_data="hinterx2 " + str(m.from_user.id))],
        [InlineKeyboardButton("الجزء التالت 3⃣", callback_data="hinterx3 " + str(m.from_user.id))],
        [InlineKeyboardButton("الجزء الرابع 4⃣", callback_data="hinterx4 " + str(m.from_user.id))],
        [InlineKeyboardButton("الجزء الخامس 5⃣", callback_data="hinterx5 " + str(m.from_user.id))],
        [InlineKeyboardButton("الجزء السادس 6⃣", callback_data="hinterx6 " + str(m.from_user.id))],
        [InlineKeyboardButton("الجزء السابع 7⃣", callback_data="hinterx7 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="anmie2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ أهلا بيك في قايمة اجزاء هنتر اكس هنتر\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^hinterx1 (\\d+)$"))
async def hinterx1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ الحلقه 1", callback_data="Xhint1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 2", callback_data="Xhint2 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 3", callback_data="Xhint3 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 4", callback_data="Xhint4 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 5", callback_data="Xhint5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 6", callback_data="Xhint6 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 7", callback_data="Xhint7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 8", callback_data="Xhint8 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 9", callback_data="Xhint9 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 10", callback_data="Xhint10 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 11", callback_data="Xhint11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 12", callback_data="Xhint12 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 13", callback_data="Xhint13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 14", callback_data="Xhint14 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 15", callback_data="Xhint15 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 16", callback_data="Xhint16 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 17", callback_data="Xhint17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 18", callback_data="Xhint18 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 19", callback_data="Xhint19 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 20", callback_data="Xhint20 " + str(m.from_user.id))],

        [InlineKeyboardButton("➡️ التالي", callback_data="hinterx2 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="anmie2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك في القايمة الاولي من #القناص هنتر اكس هنتر\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^hinterx2 (\\d+)$"))
async def hinterx2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقه 21", callback_data="Xhint21 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 22", callback_data="Xhint22 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 23", callback_data="Xhint23 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 24", callback_data="Xhint24 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 25", callback_data="Xhint25 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 26", callback_data="Xhint26 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 27", callback_data="Xhint27 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 28", callback_data="Xhint28 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 29", callback_data="Xhint29 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 30", callback_data="Xhint30 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 31", callback_data="Xhint31 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 32", callback_data="Xhint32 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 33", callback_data="Xhint33 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 34", callback_data="Xhint34 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 35", callback_data="Xhint35 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 36", callback_data="Xhint36 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 37", callback_data="Xhint37 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 38", callback_data="Xhint38 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 39", callback_data="Xhint39 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 40", callback_data="Xhint40 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="hinterx1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("➡️ التالي", callback_data="hinterx3 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="anmie2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك في القايمة التانيه من #القناص هنتر اكس هنتر\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^hinterx3 (\\d+)$"))
async def hinterx3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقه 41", callback_data="Xhint41 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 42", callback_data="Xhint42 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 43", callback_data="Xhint43 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 44", callback_data="Xhint44 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 45", callback_data="Xhint45 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 46", callback_data="Xhint46 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 47", callback_data="Xhint47 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 48", callback_data="Xhint48 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 49", callback_data="Xhint49 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 50", callback_data="Xhint50 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 51", callback_data="Xhint51 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 52", callback_data="Xhint52 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 53", callback_data="Xhint53 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 54", callback_data="Xhint54 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 55", callback_data="Xhint55 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 56", callback_data="Xhint56 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 57", callback_data="Xhint57 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 58", callback_data="Xhint58 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 59", callback_data="Xhint59 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 60", callback_data="Xhint60 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="hinterx2 " + str(m.from_user.id))] +
        [InlineKeyboardButton("➡️ التالي", callback_data="hinterx4 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="anmie2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك في القايمة التالته من #القناص هنتر اكس هنتر\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^hinterx4 (\\d+)$"))
async def hinterx4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقه 61", callback_data="Xhint61 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 62", callback_data="Xhint62 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 63", callback_data="Xhint63 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 64", callback_data="Xhint64 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 65", callback_data="Xhint65 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 66", callback_data="Xhint66 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 67", callback_data="Xhint67 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 68", callback_data="Xhint68 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 69", callback_data="Xhint69 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 70", callback_data="Xhint70 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 71", callback_data="Xhint71 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 72", callback_data="Xhint72 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 73", callback_data="Xhint73 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 74", callback_data="Xhint74 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 75", callback_data="Xhint75 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 76", callback_data="Xhint76 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 77", callback_data="Xhint77 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 78", callback_data="Xhint78 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 79", callback_data="Xhint79 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 80", callback_data="Xhint80 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="hinterx3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("➡️ التالي", callback_data="hinterx5 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="anmie2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك في القايمة الرابعه من #القناص هنتر اكس هنتر\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^hinterx5 (\\d+)$"))
async def hinterx5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقه 81", callback_data="Xhint81 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 82", callback_data="Xhint82 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 83", callback_data="Xhint83 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 84", callback_data="Xhint84 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 85", callback_data="Xhint85 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 86", callback_data="Xhint86 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 87", callback_data="Xhint87 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 88", callback_data="Xhint88 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 89", callback_data="Xhint89 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 90", callback_data="Xhint90 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 91", callback_data="Xhint91 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 92", callback_data="Xhint92 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 93", callback_data="Xhint93 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 94", callback_data="Xhint94 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 95", callback_data="Xhint95 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 96", callback_data="Xhint96 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 97", callback_data="Xhint97 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 98", callback_data="Xhint98 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 99", callback_data="Xhint99 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 100", callback_data="Xhint100 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="hinterx4 " + str(m.from_user.id))] +
        [InlineKeyboardButton("➡️ التالي", callback_data="hinterx6 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="anmie2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك في القايمة الخامسه من #القناص هنتر اكس هنتر\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^hinterx6 (\\d+)$"))
async def hinterx6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقه 101", callback_data="Xhint101 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 102", callback_data="Xhint102 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 103", callback_data="Xhint103 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 104", callback_data="Xhint104 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 105", callback_data="Xhint105 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 106", callback_data="Xhint106 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 107", callback_data="Xhint107 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 108", callback_data="Xhint108 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 109", callback_data="Xhint109 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 110", callback_data="Xhint110 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ 111 الحلقه ", callback_data="Xhint111 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 112", callback_data="Xhint112 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 113", callback_data="Xhint113 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 114", callback_data="Xhint114 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 115", callback_data="Xhint115 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 116", callback_data="Xhint116 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 117", callback_data="Xhint117 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 118", callback_data="Xhint118 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 119", callback_data="Xhint119 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 120", callback_data="Xhint120 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="hinterx5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("➡️ التالي", callback_data="hinterx7 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="anmie2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك في القايمة السادسه من #القناص هنتر اكس هنتر\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^hinterx7 (\\d+)$"))
async def hinterx7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقه 121", callback_data="Xhint121 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 122", callback_data="Xhint122 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 123", callback_data="Xhint123 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 124", callback_data="Xhint124 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 125", callback_data="Xhint125 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 126", callback_data="Xhint126 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 127", callback_data="Xhint127 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 128", callback_data="Xhint128 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 129", callback_data="Xhint129 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 130", callback_data="Xhint130 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 131", callback_data="Xhint131 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 132", callback_data="Xhint132 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 133", callback_data="Xhint133 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 134", callback_data="Xhint134 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 135", callback_data="Xhint135 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 136", callback_data="Xhint136 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 137", callback_data="Xhint137 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 138", callback_data="Xhint138 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 139", callback_data="Xhint139 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 140", callback_data="Xhint140 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 141", callback_data="Xhint141 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 142", callback_data="Xhint142 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 143", callback_data="Xhint143 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 144", callback_data="Xhint144 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 145", callback_data="Xhint145 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 146", callback_data="Xhint146 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 147", callback_data="Xhint147 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 148", callback_data="Xhint148 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="hinterx6 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="anmie2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك في القايمة السابعه من #القناص هنتر اكس هنتر\n√", reply_markup=keyboard)


########################################################################################################################
########################################################################################################################
#######################################################################################################################

@app.on_callback_query(filters.regex("^Xhint1 (\\d+)$"))
async def Xhint1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/807", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint2 (\\d+)$"))
async def Xhint2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/808", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint3 (\\d+)$"))
async def Xhint3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/809", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint4 (\\d+)$"))
async def Xhint4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/810", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint5 (\\d+)$"))
async def Xhint5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/811", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint6 (\\d+)$"))
async def Xhint6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/812", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint7 (\\d+)$"))
async def Xhint7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/813", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint8 (\\d+)$"))
async def Xhint8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/814", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint9 (\\d+)$"))
async def Xhint9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/815", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint10 (\\d+)$"))
async def Xhint10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/816", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint11 (\\d+)$"))
async def Xhint11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/817", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint12 (\\d+)$"))
async def Xhint12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/818", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint13 (\\d+)$"))
async def Xhint13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/819", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint14 (\\d+)$"))
async def Xhint14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/820", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint15 (\\d+)$"))
async def Xhint15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/821", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint16 (\\d+)$"))
async def Xhint16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/822", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint17 (\\d+)$"))
async def Xhint17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/823", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint18 (\\d+)$"))
async def Xhint18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/824", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint19 (\\d+)$"))
async def Xhint19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/825", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint20 (\\d+)$"))
async def Xhint20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/826", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint21 (\\d+)$"))
async def Xhint21(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/847", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint22 (\\d+)$"))
async def Xhint22(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/848", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint23 (\\d+)$"))
async def Xhint23(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/849", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint24 (\\d+)$"))
async def Xhint24(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/850", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint25 (\\d+)$"))
async def Xhint25(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/851", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint26 (\\d+)$"))
async def Xhint26(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/852", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint27 (\\d+)$"))
async def Xhint27(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/853", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint28 (\\d+)$"))
async def Xhint28(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/854", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint29 (\\d+)$"))
async def Xhint29(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/855", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint30 (\\d+)$"))
async def Xhint30(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/856", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint31 (\\d+)$"))
async def Xhint31(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/857", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint32 (\\d+)$"))
async def Xhint32(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/858", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint33 (\\d+)$"))
async def Xhint33(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/859", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint34 (\\d+)$"))
async def Xhint34(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/860", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint35 (\\d+)$"))
async def Xhint35(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/861", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint36 (\\d+)$"))
async def Xhint36(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/862", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint37 (\\d+)$"))
async def Xhint37(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/863", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint38 (\\d+)$"))
async def Xhint38(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/864", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint39 (\\d+)$"))
async def Xhint39(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/865", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint40 (\\d+)$"))
async def Xhint40(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/866", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint41 (\\d+)$"))
async def Xhint41(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/867", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint42 (\\d+)$"))
async def Xhint42(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/868", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint43 (\\d+)$"))
async def Xhint43(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/869", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint44 (\\d+)$"))
async def Xhint44(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/870", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint45 (\\d+)$"))
async def Xhint45(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/871", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint46 (\\d+)$"))
async def Xhint46(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/872", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint47 (\\d+)$"))
async def Xhint47(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/877", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint48 (\\d+)$"))
async def Xhint48(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/878", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint49 (\\d+)$"))
async def Xhint49(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/879", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint50 (\\d+)$"))
async def Xhint50(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/880", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint51 (\\d+)$"))
async def Xhint51(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/881", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint52 (\\d+)$"))
async def Xhint52(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/882", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint53 (\\d+)$"))
async def Xhint53(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/883", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint54 (\\d+)$"))
async def Xhint54(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/884", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint55 (\\d+)$"))
async def Xhint55(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/885", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint56 (\\d+)$"))
async def Xhint56(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/886", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint57 (\\d+)$"))
async def Xhint57(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/887", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint58 (\\d+)$"))
async def Xhint58(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/888", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint59 (\\d+)$"))
async def Xhint59(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/889", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint60 (\\d+)$"))
async def Xhint60(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/890", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint61 (\\d+)$"))
async def Xhint61(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/891", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint62 (\\d+)$"))
async def Xhint62(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/892", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint63 (\\d+)$"))
async def Xhint63(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/893", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint64 (\\d+)$"))
async def Xhint64(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/894", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint65 (\\d+)$"))
async def Xhint65(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/895", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint66 (\\d+)$"))
async def Xhint66(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/896", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint67 (\\d+)$"))
async def Xhint67(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/897", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint68 (\\d+)$"))
async def Xhint68(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/898", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint69 (\\d+)$"))
async def Xhint69(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/899", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint70 (\\d+)$"))
async def Xhint70(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/900", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint71 (\\d+)$"))
async def Xhint71(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/901", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint72 (\\d+)$"))
async def Xhint72(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/902", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint73 (\\d+)$"))
async def Xhint73(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/903", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint74 (\\d+)$"))
async def Xhint74(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/904", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint75 (\\d+)$"))
async def Xhint75(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/905", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint76 (\\d+)$"))
async def Xhint76(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/906", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint77 (\\d+)$"))
async def Xhint77(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/907", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint78 (\\d+)$"))
async def Xhint78(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/908", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint79 (\\d+)$"))
async def Xhint79(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/909", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint80 (\\d+)$"))
async def Xhint80(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/910", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint81 (\\d+)$"))
async def Xhint81(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/911", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint82 (\\d+)$"))
async def Xhint82(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/912", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint83 (\\d+)$"))
async def Xhint83(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/913", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint84 (\\d+)$"))
async def Xhint84(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/914", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint85 (\\d+)$"))
async def Xhint85(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/915", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint86 (\\d+)$"))
async def Xhint86(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/916", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint87 (\\d+)$"))
async def Xhint87(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/917", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint88 (\\d+)$"))
async def Xhint88(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/918", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint89 (\\d+)$"))
async def Xhint89(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/919", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint90 (\\d+)$"))
async def Xhint90(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/920", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint91 (\\d+)$"))
async def Xhint91(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/921", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint92 (\\d+)$"))
async def Xhint92(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/922", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint93 (\\d+)$"))
async def Xhint93(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/923", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint94 (\\d+)$"))
async def Xhint94(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon924/", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint95 (\\d+)$"))
async def Xhint95(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/925", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint96 (\\d+)$"))
async def Xhint96(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/926", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint97 (\\d+)$"))
async def Xhint97(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/927", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint98 (\\d+)$"))
async def Xhint98(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/928", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint99 (\\d+)$"))
async def Xhint99(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/929", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint100 (\\d+)$"))
async def Xhint100(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/930", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint101 (\\d+)$"))
async def Xhint101(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/931", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint102 (\\d+)$"))
async def Xhint102(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/932", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint103 (\\d+)$"))
async def Xhint103(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/933", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint104 (\\d+)$"))
async def Xhint104(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/934", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint105 (\\d+)$"))
async def Xhint105(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/935", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint106 (\\d+)$"))
async def Xhint106(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/936", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint107 (\\d+)$"))
async def Xhint107(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/937", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint108 (\\d+)$"))
async def Xhint108(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/938", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint109 (\\d+)$"))
async def Xhint109(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/939", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint110 (\\d+)$"))
async def Xhint110(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/940", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint111 (\\d+)$"))
async def Xhint111(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/941", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint112 (\\d+)$"))
async def Xhint112(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/942", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint113 (\\d+)$"))
async def Xhint113(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/943", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint114 (\\d+)$"))
async def Xhint114(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/944", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint115 (\\d+)$"))
async def Xhint115(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/945", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint116 (\\d+)$"))
async def Xhint116(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/946", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint117 (\\d+)$"))
async def Xhint117(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/947", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint118 (\\d+)$"))
async def Xhint118(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/948", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint119 (\\d+)$"))
async def Xhint119(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/949", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint120 (\\d+)$"))
async def Xhint120(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/950", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint121 (\\d+)$"))
async def Xhint121(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/951", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint122 (\\d+)$"))
async def Xhint122(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/952", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint123 (\\d+)$"))
async def Xhint123(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/953", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint124 (\\d+)$"))
async def Xhint124(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/954", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint125 (\\d+)$"))
async def Xhint125(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/955", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint126 (\\d+)$"))
async def Xhint126(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/956", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint127 (\\d+)$"))
async def Xhint127(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/957", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint128 (\\d+)$"))
async def Xhint128(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/958", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint129 (\\d+)$"))
async def Xhint129(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/959", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint130 (\\d+)$"))
async def Xhint1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/960", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint131 (\\d+)$"))
async def Xhint2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/961", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint132 (\\d+)$"))
async def Xhint3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/962", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint133 (\\d+)$"))
async def Xhint4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/963", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint134 (\\d+)$"))
async def Xhint5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/964", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint135 (\\d+)$"))
async def Xhint6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/965", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint136 (\\d+)$"))
async def Xhint7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/966", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint137 (\\d+)$"))
async def Xhint8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/967", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint138 (\\d+)$"))
async def Xhint9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/968", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint139 (\\d+)$"))
async def Xhint10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/969", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint140 (\\d+)$"))
async def Xhint11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/970", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint141 (\\d+)$"))
async def Xhint12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/971", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint142 (\\d+)$"))
async def Xhint13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/972", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint143 (\\d+)$"))
async def Xhint14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/973", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint144 (\\d+)$"))
async def Xhint15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/974", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint145 (\\d+)$"))
async def Xhint16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/975", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint146 (\\d+)$"))
async def Xhint17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/976", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint147 (\\d+)$"))
async def Xhint18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/977", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhint148 (\\d+)$"))
async def Xhint19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/978", reply_to_message_id=mid)


########################################################################################################################
########################################################################################################################
#######################################################################################################################
####### tokyo ##################

@app.on_callback_query(filters.regex("^tokyo (\\d+)$"))
async def tokyo(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ الموسم الاول 1⃣", callback_data="tokyo1 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الموسم التاني 2⃣", callback_data="tokyo2 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الموسم التالت 3⃣", callback_data="tokyo3 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الموسم الرابع 4⃣", callback_data="tokyo4 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="hinterx " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك في قايمة الانمي ل طوكيو غول\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^tokyo1 (\\d+)$"))
async def tokyo1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ الحلقه 1", callback_data="Xtok1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 2", callback_data="Xtok2 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 3", callback_data="Xtok3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 4", callback_data="Xtok4 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 5", callback_data="Xtok5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 6", callback_data="Xtok6 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 7", callback_data="Xtok7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 8", callback_data="Xtok8 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 9", callback_data="Xtok9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 10", callback_data="Xtok10 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 11", callback_data="Xtok11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 12", callback_data="Xtok12 " + str(m.from_user.id))],

        [InlineKeyboardButton("➡️ التالي", callback_data="tokyo2 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="anmie2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك في الموسم الاول ل طوكيو غول\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^tokyo2 (\\d+)$"))
async def tokyo2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ الحلقه 1", callback_data="Xtok13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 2", callback_data="Xtok14 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 3", callback_data="Xtok15 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 4", callback_data="Xtok16 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 5", callback_data="Xtok17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 6", callback_data="Xtok18 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 7", callback_data="Xtok19 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 8", callback_data="Xtok20 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 9", callback_data="Xtok21 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 10", callback_data="Xtok22 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 11", callback_data="Xtok23 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 12", callback_data="Xtok24 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="tokyo1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("➡️ التالي", callback_data="tokyo3 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="anmie2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك في الموسم التاني ل طوكيو غول\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^tokyo3 (\\d+)$"))
async def tokyo3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ الحلقه 1", callback_data="Xtok25 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 2", callback_data="Xtok26 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 3", callback_data="Xtok27 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 4", callback_data="Xtok28 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 5", callback_data="Xtok29 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 6", callback_data="Xtok30 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 7", callback_data="Xtok31 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 8", callback_data="Xtok32 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 9", callback_data="Xtok33 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 10", callback_data="Xtok34 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 11", callback_data="Xtok35 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 12", callback_data="Xtok36 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="tokyo2 " + str(m.from_user.id))] +
        [InlineKeyboardButton("➡️ التالي", callback_data="tokyo4 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="anmie2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك في الموسم التالت ل طوكيو غول\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^tokyo4 (\\d+)$"))
async def tokyo4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ الحلقه 1", callback_data="Xtok37 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 2", callback_data="Xtok38 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 3", callback_data="Xtok39 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 4", callback_data="Xtok40 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 5", callback_data="Xtok41 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ 6 الحلقه", callback_data="Xtok42 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 7", callback_data="Xtok43 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 8", callback_data="Xtok44 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 9", callback_data="Xtok45 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 10", callback_data="Xtok46 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 11", callback_data="Xtok47 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 12", callback_data="Xtok48 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="tokyo3 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="anmie2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك في الموسم الرابع ل طوكيو غول\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xtok1 (\\d+)$"))
async def Xtok1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/622", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok2 (\\d+)$"))
async def Xtok2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/623", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok3 (\\d+)$"))
async def Xtok3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/624", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok4 (\\d+)$"))
async def Xtok4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/625", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok5 (\\d+)$"))
async def Xtok5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/626", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok6 (\\d+)$"))
async def Xtok6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/627", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok7 (\\d+)$"))
async def Xtok7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/628", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok8 (\\d+)$"))
async def Xtok8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/629", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok9 (\\d+)$"))
async def Xtok9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/630", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok10 (\\d+)$"))
async def Xtok10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/631", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok11 (\\d+)$"))
async def Xtok11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/632", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok12 (\\d+)$"))
async def Xtok12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/633", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok13 (\\d+)$"))
async def Xtok13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/638", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok14 (\\d+)$"))
async def Xtok14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/639", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok15 (\\d+)$"))
async def Xtok15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/640", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok16 (\\d+)$"))
async def Xtok16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/641", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok17 (\\d+)$"))
async def Xtok17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/642", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok18 (\\d+)$"))
async def Xtok18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/643", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok19 (\\d+)$"))
async def Xtok19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/644", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok20 (\\d+)$"))
async def Xtok20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/645", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok21 (\\d+)$"))
async def Xtok21(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/646", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok22 (\\d+)$"))
async def Xtok22(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/647", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok23 (\\d+)$"))
async def Xtok23(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/648", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok24 (\\d+)$"))
async def Xtok24(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/649", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok25 (\\d+)$"))
async def Xtok25(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/655", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok26 (\\d+)$"))
async def Xtok26(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/656", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok27 (\\d+)$"))
async def Xtok27(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/657", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok28 (\\d+)$"))
async def Xtok28(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/658", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok29 (\\d+)$"))
async def Xtok29(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/659", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok30 (\\d+)$"))
async def Xtok30(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/660", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok31 (\\d+)$"))
async def Xtok31(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/661", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok32 (\\d+)$"))
async def Xtok32(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/662", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok33 (\\d+)$"))
async def Xtok33(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/663", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok34 (\\d+)$"))
async def Xtok34(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/664", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok35 (\\d+)$"))
async def Xtok35(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/665", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok36 (\\d+)$"))
async def Xtok36(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/666", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok37 (\\d+)$"))
async def Xtok37(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/669", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok38 (\\d+)$"))
async def Xtok38(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/670", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok39 (\\d+)$"))
async def Xtok39(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/671", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok40 (\\d+)$"))
async def Xtok40(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/672", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok41 (\\d+)$"))
async def Xtok41(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/673", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok42 (\\d+)$"))
async def Xtok42(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/674", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok43 (\\d+)$"))
async def Xtok43(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/675", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok44 (\\d+)$"))
async def Xtok44(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/676", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok45 (\\d+)$"))
async def Xtok45(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/681", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok46 (\\d+)$"))
async def Xtok46(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/682", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok47 (\\d+)$"))
async def Xtok47(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/683", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtok48 (\\d+)$"))
async def Xtok48(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/684", reply_to_message_id=mid)


#####################################################################################################
######################################################################################################
#####################################################################################################
############  hgoom 3malika  ################

@app.on_callback_query(filters.regex("^hgoom (\\d+)$"))
async def hgoom(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ الموسم الاول", callback_data="hgoom1 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الموسم التاني", callback_data="hgoom2 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الموسم التالت بارت 1", callback_data="hgoom3 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الموسم التالت بارت 2", callback_data="hgoom4 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الموسم الرابع", callback_data="hgoom5 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="hinterx " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ أهلا بيك في قايمة الانمي ل هجوم العمالقه\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^hgoom1 (\\d+)$"))
async def hgoom1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ الحلقه 1", callback_data="Xhgoo1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 2", callback_data="Xhgoo2 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 3", callback_data="Xhgoo3 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 4", callback_data="Xhgoo4 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 5", callback_data="Xhgoo5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 6", callback_data="Xhgoo6 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 7", callback_data="Xhgoo7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 8", callback_data="Xhgoo8 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 9", callback_data="Xhgoo9 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 10", callback_data="Xhgoo10 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 11", callback_data="Xhgoo11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 12", callback_data="Xhgoo12 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 13", callback_data="Xhgoo13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 14", callback_data="Xhgoo14 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 15", callback_data="Xhgoo15 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 16", callback_data="Xhgoo16 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 17", callback_data="Xhgoo17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 18", callback_data="Xhgoo18 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 19", callback_data="Xhgoo19 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 20", callback_data="Xhgoo20 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 21", callback_data="Xhgoo21 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 22", callback_data="Xhgoo22 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 23", callback_data="Xhgoo23 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 24", callback_data="Xhgoo24 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 25", callback_data="Xhgoo25 " + str(m.from_user.id))],

        [InlineKeyboardButton("➡️ التالي", callback_data="hgoom2 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="anmie2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك في الموسم الاول ل هجوم العمالقه\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^hgoom2 (\\d+)$"))
async def hgoom2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقه 1", callback_data="Xhgoo26 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 2", callback_data="Xhgoo27 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 3", callback_data="Xhgoo28 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 4", callback_data="Xhgoo29 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 5", callback_data="Xhgoo30 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 6", callback_data="Xhgoo31 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 7", callback_data="Xhgoo32 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 8", callback_data="Xhgoo33 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 9", callback_data="Xhgoo34 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 10", callback_data="Xhgoo35 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 11", callback_data="Xhgoo36 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 12", callback_data="Xhgoo37 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="hgoom1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("➡️ التالي", callback_data="hgoom3 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="anmie2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك في الموسم التاني ل هجوم العمالقه\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^hgoom3 (\\d+)$"))
async def hgoom3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقه 1", callback_data="Xhgoo38 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 2", callback_data="Xhgoo39 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 3", callback_data="Xhgoo40 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 4", callback_data="Xhgoo41 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ 5 الحلقه ", callback_data="Xhgoo42 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 6", callback_data="Xhgoo43 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 7", callback_data="Xhgoo44 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 8", callback_data="Xhgoo45 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 9", callback_data="Xhgoo46 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 10", callback_data="Xhgoo47 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 11", callback_data="Xhgoo48 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 12", callback_data="Xhgoo49 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="hgoom2 " + str(m.from_user.id))] +
        [InlineKeyboardButton("➡️ التالي", callback_data="hgoom4 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="anmie2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك في الموسم التالت بارت 1 ل هجوم العمالقه\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^hgoom4 (\\d+)$"))
async def hgoom4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقه 1", callback_data="Xhgoo50 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 2", callback_data="Xhgoo51 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 3", callback_data="Xhgoo52 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 4", callback_data="Xhgoo53 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 5", callback_data="Xhgoo54 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 6", callback_data="Xhgoo55 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 7", callback_data="Xhgoo56 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 8", callback_data="Xhgoo57 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 9", callback_data="Xhgoo58 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 10", callback_data="Xhgoo59 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="hgoom3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("➡️ التالي", callback_data="hgoom5 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="anmie2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك في الموسم التالت بارت 2 ل هجوم العمالقه\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^hgoom5 (\\d+)$"))
async def hgoom5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقه 1", callback_data="Xhgoo60 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 2", callback_data="Xhgoo61 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 3", callback_data="Xhgoo62 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 4", callback_data="Xhgoo63 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 5", callback_data="Xhgoo64 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 6", callback_data="Xhgoo65 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 7", callback_data="Xhgoo66 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 8", callback_data="Xhgoo67 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 9", callback_data="Xhgoo68 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 10", callback_data="Xhgoo69 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 11", callback_data="Xhgoo70 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 12", callback_data="Xhgoo71 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 13", callback_data="Xhgoo72 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="hgoom4 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="anmie2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك في الموسم الرابع ل هجوم العمالقه\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xhgoo1 (\\d+)$"))
async def Xhgoo1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/687", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo2 (\\d+)$"))
async def Xhgoo2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/688", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo3 (\\d+)$"))
async def Xhgoo3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/689", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo4 (\\d+)$"))
async def Xhgoo4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/690", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo5 (\\d+)$"))
async def Xhgoo5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/691", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo6 (\\d+)$"))
async def Xhgoo6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/692", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo7 (\\d+)$"))
async def Xhgoo7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/693", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo8 (\\d+)$"))
async def Xhgoo8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/694", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo9 (\\d+)$"))
async def Xhgoo9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/695", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo10 (\\d+)$"))
async def Xhgoo10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/696", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo11 (\\d+)$"))
async def Xhgoo11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/697", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo12 (\\d+)$"))
async def Xhgoo12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/698", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo13 (\\d+)$"))
async def Xhgoo13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/699", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo14 (\\d+)$"))
async def Xhgoo14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/700", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo15 (\\d+)$"))
async def Xhgoo15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/701", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo16 (\\d+)$"))
async def Xhgoo16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/702", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo17 (\\d+)$"))
async def Xhgoo17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/703", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo18 (\\d+)$"))
async def Xhgoo18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/704", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo19 (\\d+)$"))
async def Xhgoo19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/705", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo20 (\\d+)$"))
async def Xhgoo20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/706", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo21 (\\d+)$"))
async def Xhgoo21(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/707", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo22 (\\d+)$"))
async def Xhgoo22(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/708", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo23 (\\d+)$"))
async def Xhgoo23(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/709", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo24 (\\d+)$"))
async def Xhgoo24(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/710", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo25 (\\d+)$"))
async def Xhgoo25(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/711", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo26 (\\d+)$"))
async def Xhgoo26(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/713", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo27 (\\d+)$"))
async def Xhgoo27(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/714", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo28 (\\d+)$"))
async def Xhgoo28(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/715", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo29 (\\d+)$"))
async def Xhgoo29(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/716", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo30 (\\d+)$"))
async def Xhgoo30(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/717", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo31 (\\d+)$"))
async def Xhgoo31(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/718", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo32 (\\d+)$"))
async def Xhgoo32(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/719", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo33 (\\d+)$"))
async def Xhgoo33(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/720", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo34 (\\d+)$"))
async def Xhgoo34(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/721", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo35 (\\d+)$"))
async def Xhgoo35(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/722", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo36 (\\d+)$"))
async def Xhgoo36(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/723", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo37 (\\d+)$"))
async def Xhgoo37(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/724", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo38 (\\d+)$"))
async def Xhgoo38(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/728", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo39 (\\d+)$"))
async def Xhgoo39(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/729", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo40 (\\d+)$"))
async def Xhgoo40(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/730", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo41 (\\d+)$"))
async def Xhgoo41(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/731", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo42 (\\d+)$"))
async def Xhgoo42(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/732", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo43 (\\d+)$"))
async def Xhgoo43(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/733", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo44 (\\d+)$"))
async def Xhgoo44(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/734", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo45 (\\d+)$"))
async def Xhgoo45(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/735", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo46 (\\d+)$"))
async def Xhgoo46(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/736", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo47 (\\d+)$"))
async def Xhgoo47(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/737", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo48 (\\d+)$"))
async def Xhgoo48(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/738", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo49 (\\d+)$"))
async def Xhgoo49(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/739", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo50 (\\d+)$"))
async def Xhgoo50(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/742", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo51 (\\d+)$"))
async def Xhgoo51(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/743", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo52 (\\d+)$"))
async def Xhgoo52(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/744", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo53 (\\d+)$"))
async def Xhgoo53(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/745", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo54 (\\d+)$"))
async def Xhgoo54(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/746", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo55 (\\d+)$"))
async def Xhgoo55(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/747", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo56 (\\d+)$"))
async def Xhgoo56(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/748", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo57 (\\d+)$"))
async def Xhgoo57(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/749", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo58 (\\d+)$"))
async def Xhgoo58(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/750", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo59 (\\d+)$"))
async def Xhgoo59(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/751", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo60 (\\d+)$"))
async def Xhgoo60(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/754", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo61 (\\d+)$"))
async def Xhgoo61(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/755", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo62 (\\d+)$"))
async def Xhgoo62(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/756", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo63 (\\d+)$"))
async def Xhgoo63(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/757", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo64 (\\d+)$"))
async def Xhgoo64(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/758", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo65 (\\d+)$"))
async def Xhgoo65(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/759", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo66 (\\d+)$"))
async def Xhgoo66(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/760", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo67 (\\d+)$"))
async def Xhgoo67(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/761", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo68 (\\d+)$"))
async def Xhgoo68(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/762", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo69 (\\d+)$"))
async def Xhgoo69(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/763", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo70 (\\d+)$"))
async def Xhgoo70(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/764", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo71 (\\d+)$"))
async def Xhgoo71(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/765", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhgoo72 (\\d+)$"))
async def Xhgoo72(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/766", reply_to_message_id=mid)


#####################################################################################################
######################################################################################################
#####################################################################################################

# moslsl
@app.on_callback_query(filters.regex("^fmoslsl (\\d+)$"))
async def fmoslsl(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("توم و جيري 🐈", callback_data="tom " + str(m.from_user.id))] +
        [InlineKeyboardButton("سبونج بوب 🧽", callback_data="spong " + str(m.from_user.id))],
        [InlineKeyboardButton("داني الشبح 👻", callback_data="dany " + str(m.from_user.id))] +
        [InlineKeyboardButton("غامبول المدهش 😯", callback_data="ghmbol " + str(m.from_user.id))],
        [InlineKeyboardButton("اوسكار الشجاع 🦸", callback_data="oskar " + str(m.from_user.id))] +
        [InlineKeyboardButton("تيمون وبومبا 🐗", callback_data="temon " + str(m.from_user.id))],
        [InlineKeyboardButton("السنافر 💙", callback_data="snafer " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="cartoon2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ أهلا بيك في قايمة مسلسلات الكارتون\n√", reply_markup=keyboard)


########################################################################################
#########################################################################################
#######     TOM & G     ########
@app.on_callback_query(filters.regex("^tom (\\d+)$"))
async def tom(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ الحلقه 1", callback_data="Xto1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 2", callback_data="Xto2 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 3", callback_data="Xto3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 4", callback_data="Xto4 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 5", callback_data="Xto5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 6", callback_data="Xto6 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 7", callback_data="Xto7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 8", callback_data="Xto8 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 9", callback_data="Xto9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 10", callback_data="Xto10 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 11", callback_data="Xto11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 12", callback_data="Xto12 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 13", callback_data="Xto13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 14", callback_data="Xto14 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 15", callback_data="Xto15 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 16", callback_data="Xto16 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 17", callback_data="Xto17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 18", callback_data="Xto18 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 19", callback_data="Xto19 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 20", callback_data="Xto20 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="cartoon2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ أهلا بيك في قايمة حلقات توم و جيري\n√", reply_markup=keyboard)


############################################################

@app.on_callback_query(filters.regex("^Xto1 (\\d+)$"))
async def Xto1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/9", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xto2 (\\d+)$"))
async def Xto2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/10", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xto3 (\\d+)$"))
async def Xto3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/11", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xto4 (\\d+)$"))
async def Xto4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/12", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xto5 (\\d+)$"))
async def Xto5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/13", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xto6 (\\d+)$"))
async def Xto6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/14", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xto7 (\\d+)$"))
async def Xto7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/15", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xto8 (\\d+)$"))
async def Xto8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/16", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xto9 (\\d+)$"))
async def Xto9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/17", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xto10 (\\d+)$"))
async def Xto10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/18", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xto11 (\\d+)$"))
async def Xto11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/19", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xto12 (\\d+)$"))
async def Xto12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/20", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xto13 (\\d+)$"))
async def Xto13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/21", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xto14 (\\d+)$"))
async def Xto14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/22", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xto15 (\\d+)$"))
async def Xto15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/23", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xto16 (\\d+)$"))
async def Xto16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/24", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xto17 (\\d+)$"))
async def Xto17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/25", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xto18 (\\d+)$"))
async def Xto18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/26", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xto19 (\\d+)$"))
async def Xto19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/27", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xto20 (\\d+)$"))
async def Xto20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/28", reply_to_message_id=mid)


#######################################
@app.on_callback_query(filters.regex("^spong (\\d+)$"))
async def spong(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ الموسم الاول", callback_data="spong1 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الموسم التاني", callback_data="spong2 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الموسم التالت", callback_data="spong3 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الموسم الرابع", callback_data="spong4 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الموسم الخامس", callback_data="spong5 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الموسم السادس", callback_data="spong6 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="cartoon2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ أهلا بيك في قايمة مسلسلات سبونج بوب\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^spong1 (\\d+)$"))
async def spong1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ الحلقه 1", callback_data="Xs1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 2", callback_data="Xs2 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 3", callback_data="Xs3 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 4", callback_data="Xs4 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 5", callback_data="Xs5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 6", callback_data="Xs6 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 7", callback_data="Xs7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 8", callback_data="Xs8 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 9", callback_data="Xs9 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 10", callback_data="Xs10 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 11", callback_data="Xs11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 12", callback_data="Xs12 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 13", callback_data="Xs13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 14", callback_data="Xs14 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 15", callback_data="Xs15 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 16", callback_data="Xs16 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 17", callback_data="Xs17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 18", callback_data="Xs18 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 19", callback_data="Xs19 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 20", callback_data="Xs20 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 21", callback_data="Xs21 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 22", callback_data="Xs22 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 23", callback_data="Xs23 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 24", callback_data="Xs24 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 25", callback_data="Xs25 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 26", callback_data="Xs26 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 27", callback_data="Xs27 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 28", callback_data="Xs28 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 29", callback_data="Xs29 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 30", callback_data="Xs30 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 31", callback_data="Xs31 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 32", callback_data="Xs32 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 33", callback_data="Xs33 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 34", callback_data="Xs34 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 35", callback_data="Xs35 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 36", callback_data="Xs36 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 37", callback_data="Xs37 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 38", callback_data="Xs38 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 39", callback_data="Xs39 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="spong " + str(m.from_user.id))] +
        [InlineKeyboardButton("➡️ التالي", callback_data="spong2 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="cartoon2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ أهلا بيك في قايمة مسلسلات سبونج بوب الموسم الاول\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^spong2 (\\d+)$"))
async def spong2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ الحلقه 1", callback_data="Xs40 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 2", callback_data="Xs41 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ 3الحلقه ", callback_data="Xs42 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 4", callback_data="Xs43 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 5", callback_data="Xs44 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 6", callback_data="Xs45 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 7", callback_data="Xs46 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 8", callback_data="Xs47 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 9", callback_data="Xs48 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 10", callback_data="Xs49 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="spong1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("➡️ التالي", callback_data="spong3 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="cartoon2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ أهلا بيك في قايمة مسلسلات سبونج بوب الموسم التاني\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^spong3 (\\d+)$"))
async def spong3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ الحلقه 1", callback_data="Xs50 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 2", callback_data="Xs51 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 3", callback_data="Xs52 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 4", callback_data="Xs53 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 5", callback_data="Xs54 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 6", callback_data="Xs55 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 7", callback_data="Xs56 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 8", callback_data="Xs57 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 9", callback_data="Xs58 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 10", callback_data="Xs59 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 11", callback_data="Xs60 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 12", callback_data="Xs61 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 13", callback_data="Xs62 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 14", callback_data="Xs63 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 15", callback_data="Xs64 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 16", callback_data="Xs65 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 17", callback_data="Xs66 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 18", callback_data="Xs67 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="spong2 " + str(m.from_user.id))] +
        [InlineKeyboardButton("➡️ التالي", callback_data="spong4 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="cartoon2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ أهلا بيك في قايمة مسلسلات سبونج بوب الموسم التالت\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^spong4 (\\d+)$"))
async def spong4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ الحلقه 1", callback_data="Xs68 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 2", callback_data="Xs69 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 3", callback_data="Xs70 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 4", callback_data="Xs71 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 5", callback_data="Xs72 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 6", callback_data="Xs73 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 7", callback_data="Xs74 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 8", callback_data="Xs75 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 9", callback_data="Xs76 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 10", callback_data="Xs77 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 11", callback_data="Xs78 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 12", callback_data="Xs79 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 13", callback_data="Xs80 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 14", callback_data="Xs81 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 15", callback_data="Xs82 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 16", callback_data="Xs83 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 17", callback_data="Xs84 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 18", callback_data="Xs85 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 19", callback_data="Xs86 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 20", callback_data="Xs87 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 21", callback_data="Xs88 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 22", callback_data="Xs89 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 23", callback_data="Xs90 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 24", callback_data="Xs91 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 25", callback_data="Xs92 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 26", callback_data="Xs93 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 27", callback_data="Xs94 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="spong3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("➡️ التالي", callback_data="spong5 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="cartoon2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ أهلا بيك في قايمة مسلسلات سبونج بوب الموسم الرابع\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^spong5 (\\d+)$"))
async def spong5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ الحلقه 1", callback_data="Xs95 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 2", callback_data="Xs96 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 3", callback_data="Xs97 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 4", callback_data="Xs98 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 5", callback_data="Xs99 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 6", callback_data="Xs100 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 7", callback_data="Xs101 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 8", callback_data="Xs102 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 9", callback_data="Xs103 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 10", callback_data="Xs104 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 11", callback_data="Xs105 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 12", callback_data="Xs106 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 13", callback_data="Xs107 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 14", callback_data="Xs108 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 15", callback_data="Xs109 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="spong4 " + str(m.from_user.id))] +
        [InlineKeyboardButton("➡️ التالي", callback_data="spong6 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="cartoon2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ أهلا بيك في قايمة مسلسلات سبونج بوب الموسم الخامس\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^spong6 (\\d+)$"))
async def spong6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ الحلقه 1", callback_data="Xs110 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ 2الحلقه ", callback_data="Xs111 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 3", callback_data="Xs112 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 4", callback_data="Xs113 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 5", callback_data="Xs114 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 6", callback_data="Xs115 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 7", callback_data="Xs116 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 8", callback_data="Xs117 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 9", callback_data="Xs118 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 10", callback_data="Xs119 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 11", callback_data="Xs120 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 12", callback_data="Xs121 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 13", callback_data="Xs122 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 14", callback_data="Xs123 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 15", callback_data="Xs124 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 16", callback_data="Xs125 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 17", callback_data="Xs126 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 18", callback_data="Xs127 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 19", callback_data="Xs128 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 20", callback_data="Xs129 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="spong5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="cartoon2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ أهلا بيك في قايمة مسلسلات سبونج بوب الموسم السادس\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xs1 (\\d+)$"))
async def Xs1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/30", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs2 (\\d+)$"))
async def Xs2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/31", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs3 (\\d+)$"))
async def Xs3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/32", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs4 (\\d+)$"))
async def Xs4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/33", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs5 (\\d+)$"))
async def Xs5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/34", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs6 (\\d+)$"))
async def Xs6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/35", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs7 (\\d+)$"))
async def Xs7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/36", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs8 (\\d+)$"))
async def Xs8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/37", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs9 (\\d+)$"))
async def Xs9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/38", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs10 (\\d+)$"))
async def Xs10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/39", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs11 (\\d+)$"))
async def Xs11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/40", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs12 (\\d+)$"))
async def Xs12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/41", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs13 (\\d+)$"))
async def Xs13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/42", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs14 (\\d+)$"))
async def Xs14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/43", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs15 (\\d+)$"))
async def Xs15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/44", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs16 (\\d+)$"))
async def Xs16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/45", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs17 (\\d+)$"))
async def Xs17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/46", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs18 (\\d+)$"))
async def Xs18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/47", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs19 (\\d+)$"))
async def Xs19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/48", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs20 (\\d+)$"))
async def Xs20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/49", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs21 (\\d+)$"))
async def Xs21(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/50", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs22 (\\d+)$"))
async def Xs22(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/51", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs23 (\\d+)$"))
async def Xs23(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/52", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs24 (\\d+)$"))
async def Xs24(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/53", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs25 (\\d+)$"))
async def Xs25(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/54", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs26 (\\d+)$"))
async def Xs26(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/55", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs27 (\\d+)$"))
async def Xs27(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/56", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs28 (\\d+)$"))
async def Xs28(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/57", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs29 (\\d+)$"))
async def Xs29(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/58", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs30 (\\d+)$"))
async def Xs30(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/59", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs31 (\\d+)$"))
async def Xs31(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/60", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs32 (\\d+)$"))
async def Xs32(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/61", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs33 (\\d+)$"))
async def Xs33(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/62", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs34 (\\d+)$"))
async def Xs34(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/63", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs35 (\\d+)$"))
async def Xs35(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/64", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs36 (\\d+)$"))
async def Xs36(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/65", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs37 (\\d+)$"))
async def Xs37(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/66", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs38 (\\d+)$"))
async def Xs38(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/67", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs39 (\\d+)$"))
async def Xs39(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/68", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs40 (\\d+)$"))
async def Xs40(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/70", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs41 (\\d+)$"))
async def Xs41(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/71", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs42 (\\d+)$"))
async def Xs42(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/72", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs43 (\\d+)$"))
async def Xs43(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/73", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs44 (\\d+)$"))
async def Xs44(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/74", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs45 (\\d+)$"))
async def Xs45(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/75", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs46 (\\d+)$"))
async def Xs46(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/76", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs47 (\\d+)$"))
async def Xs47(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/77", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs48 (\\d+)$"))
async def Xs48(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/78", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs49 (\\d+)$"))
async def Xs49(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/79", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs50 (\\d+)$"))
async def Xs50(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/81", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs51 (\\d+)$"))
async def Xs51(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/82", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs52 (\\d+)$"))
async def Xs52(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/83", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs53 (\\d+)$"))
async def Xs53(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/84", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs54 (\\d+)$"))
async def Xs54(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/85", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs55 (\\d+)$"))
async def Xs55(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/86", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs56 (\\d+)$"))
async def Xs56(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/87", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs57 (\\d+)$"))
async def Xs57(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/88", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs58 (\\d+)$"))
async def Xs58(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/89", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs59 (\\d+)$"))
async def Xs59(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/90", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs60 (\\d+)$"))
async def Xs60(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/91", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs61 (\\d+)$"))
async def Xs61(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/92", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs62 (\\d+)$"))
async def Xs62(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/93", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs63 (\\d+)$"))
async def Xs63(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/94", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs64 (\\d+)$"))
async def Xs64(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/95", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs65 (\\d+)$"))
async def Xs65(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/96", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs66 (\\d+)$"))
async def Xs66(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/97", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs67 (\\d+)$"))
async def Xs67(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/98", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs68 (\\d+)$"))
async def Xs68(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/100", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs69 (\\d+)$"))
async def Xs69(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/101", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs70 (\\d+)$"))
async def Xs70(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/102", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs71 (\\d+)$"))
async def Xs71(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/103", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs72 (\\d+)$"))
async def Xs72(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/104", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs73 (\\d+)$"))
async def Xs73(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/105", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs74 (\\d+)$"))
async def Xs74(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/106", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs75 (\\d+)$"))
async def Xs75(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/107", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs76 (\\d+)$"))
async def Xs76(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/108", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs77 (\\d+)$"))
async def Xs77(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/109", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs78 (\\d+)$"))
async def Xs78(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/110", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs79 (\\d+)$"))
async def Xs79(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/111", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs80 (\\d+)$"))
async def Xs80(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/112", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs81 (\\d+)$"))
async def Xs81(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/113", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs82 (\\d+)$"))
async def Xs82(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/114", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs83 (\\d+)$"))
async def Xs83(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/115", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs84 (\\d+)$"))
async def Xs84(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/116", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs85 (\\d+)$"))
async def Xs85(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/117", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs86 (\\d+)$"))
async def Xs86(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/118", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs87 (\\d+)$"))
async def Xs87(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/119", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs88 (\\d+)$"))
async def Xs88(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/120", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs89 (\\d+)$"))
async def Xs89(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/121", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs90 (\\d+)$"))
async def Xs90(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/122", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs91 (\\d+)$"))
async def Xs91(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/123", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs92 (\\d+)$"))
async def Xs92(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/124", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs93 (\\d+)$"))
async def Xs93(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/125", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs94 (\\d+)$"))
async def Xs94(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/126", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs95 (\\d+)$"))
async def Xs95(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/129", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs96 (\\d+)$"))
async def Xs96(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/130", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs97 (\\d+)$"))
async def Xs97(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/131", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs98 (\\d+)$"))
async def Xs98(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/132", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs99 (\\d+)$"))
async def Xs99(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/133", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs100 (\\d+)$"))
async def Xs100(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/134", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs101 (\\d+)$"))
async def Xs101(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/135", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs102 (\\d+)$"))
async def Xs102(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/136", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs103 (\\d+)$"))
async def Xs103(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/137", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs104 (\\d+)$"))
async def Xs104(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/138", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs105 (\\d+)$"))
async def Xs105(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/139", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs106 (\\d+)$"))
async def Xs106(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/140", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs107 (\\d+)$"))
async def Xs107(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/141", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs108 (\\d+)$"))
async def Xs108(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/142", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs109 (\\d+)$"))
async def Xs109(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/143", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs110 (\\d+)$"))
async def Xs110(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/145", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs111 (\\d+)$"))
async def Xs111(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/146", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs112 (\\d+)$"))
async def Xs112(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/147", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs113 (\\d+)$"))
async def Xs113(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/148", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs114 (\\d+)$"))
async def Xs114(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/149", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs115 (\\d+)$"))
async def Xs115(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/150", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs116 (\\d+)$"))
async def Xs116(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/151", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs117 (\\d+)$"))
async def Xs117(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/152", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs118 (\\d+)$"))
async def Xs118(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/153", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs119 (\\d+)$"))
async def Xs119(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/154", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs120 (\\d+)$"))
async def Xs120(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/155", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs121 (\\d+)$"))
async def Xs121(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/156", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs122 (\\d+)$"))
async def Xs122(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/157", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs123 (\\d+)$"))
async def Xs123(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/158", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs124 (\\d+)$"))
async def Xs124(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/159", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs125 (\\d+)$"))
async def Xs125(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/160", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs126 (\\d+)$"))
async def Xs126(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/161", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs127 (\\d+)$"))
async def Xs127(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/162", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs128 (\\d+)$"))
async def Xs128(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/163", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xs129 (\\d+)$"))
async def Xs129(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/164", reply_to_message_id=mid)


########################################################################################################################
########################################################################################################################
#######################################################################################################################
########### Dany #######

@app.on_callback_query(filters.regex("^dany (\\d+)$"))
async def dany(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ الموسم الاول", callback_data="dany1 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الموسم التاني", callback_data="dany2 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الموسم التالت", callback_data="dany3 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="cartoon2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ أهلا بيك في قايمة مسلسلات داني الشبح\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^dany1 (\\d+)$"))
async def dany1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ الحلقه 1", callback_data="Xda1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 2", callback_data="Xda2 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 3", callback_data="Xda3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 4", callback_data="Xda4 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 5", callback_data="Xda5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 6", callback_data="Xda6 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 7", callback_data="Xda7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 8", callback_data="Xda8 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 9", callback_data="Xda9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 10", callback_data="Xda10 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 11", callback_data="Xda11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 12", callback_data="Xda12 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 13", callback_data="Xda13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 14", callback_data="Xda14 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 15", callback_data="Xda15 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="dany " + str(m.from_user.id))] +
        [InlineKeyboardButton("➡️ التالي", callback_data="dany2 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="cartoon2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ أهلا بيك في قايمة مسلسلات داني الشبح الموسم الاول\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^dany2 (\\d+)$"))
async def dany2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ الحلقه 1", callback_data="Xda16 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 2", callback_data="Xda17 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 3", callback_data="Xda18 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 4", callback_data="Xda19 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 5", callback_data="Xda20 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 6", callback_data="Xda21 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 7", callback_data="Xda22 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 8", callback_data="Xda23 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 9", callback_data="Xda24 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 10", callback_data="Xda25 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 1", callback_data="Xda26 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 12", callback_data="Xda27 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 13", callback_data="Xda28 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 14", callback_data="Xda29 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 15", callback_data="Xda30 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="dany1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("➡️ التالي", callback_data="dany3 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="cartoon2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ أهلا بيك في قايمة مسلسلات داني الشبح الموسم التاني\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^dany3 (\\d+)$"))
async def dany3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ الحلقه 1", callback_data="Xda31 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 2", callback_data="Xda32 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 3", callback_data="Xda33 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 4", callback_data="Xda34 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 5", callback_data="Xda35 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 6", callback_data="Xda36 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 7", callback_data="Xda37 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 8", callback_data="Xda38 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 9", callback_data="Xda39 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="dany2 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="cartoon2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ أهلا بيك في قايمة مسلسلات داني الشبح الموسم التالت\n√", reply_markup=keyboard)


############################################################

@app.on_callback_query(filters.regex("^Xda1 (\\d+)$"))
async def Xda1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/187", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xda2 (\\d+)$"))
async def Xda2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/188", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xda3 (\\d+)$"))
async def Xda3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/189", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xda4 (\\d+)$"))
async def Xda4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/190", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xda5 (\\d+)$"))
async def Xda5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/191", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xda6 (\\d+)$"))
async def Xda6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/192", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xda7 (\\d+)$"))
async def Xda7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/193", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xda8 (\\d+)$"))
async def Xda8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/194", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xda9 (\\d+)$"))
async def Xda9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/195", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xda10 (\\d+)$"))
async def Xda10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/196", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xda11 (\\d+)$"))
async def Xda11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/197", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xda12 (\\d+)$"))
async def Xda12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/198", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xda13 (\\d+)$"))
async def Xda13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/199", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xda14 (\\d+)$"))
async def Xda14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/200", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xda15 (\\d+)$"))
async def Xda15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/201", reply_to_message_id=mid)


##################################################################################### 222222

@app.on_callback_query(filters.regex("^Xda16 (\\d+)$"))
async def Xda16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/203", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xda17 (\\d+)$"))
async def Xda17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/204", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xda18 (\\d+)$"))
async def Xda18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/205", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xda19 (\\d+)$"))
async def Xda19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/206", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xda20 (\\d+)$"))
async def Xda20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/207", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xda21 (\\d+)$"))
async def Xda21(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/208", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xda22 (\\d+)$"))
async def Xda22(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/209", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xda23 (\\d+)$"))
async def Xda23(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/210", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xda24 (\\d+)$"))
async def Xda24(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/211", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xda25 (\\d+)$"))
async def Xda25(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/212", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xda26 (\\d+)$"))
async def Xda26(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/213", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xda27 (\\d+)$"))
async def Xda27(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/214", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xda28 (\\d+)$"))
async def Xda28(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/215", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xda29 (\\d+)$"))
async def Xda29(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/216", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xda30 (\\d+)$"))
async def Xda30(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/217", reply_to_message_id=mid)


###################################################################################  3333

@app.on_callback_query(filters.regex("^Xda31 (\\d+)$"))
async def Xda31(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/219", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xda32 (\\d+)$"))
async def Xda32(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/220", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xda33 (\\d+)$"))
async def Xda33(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/221", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xda34 (\\d+)$"))
async def Xda34(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/222", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xda35 (\\d+)$"))
async def Xda35(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/223", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xda36 (\\d+)$"))
async def Xda36(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/224", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xda37 (\\d+)$"))
async def Xda37(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/225", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xda38 (\\d+)$"))
async def Xda38(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/226", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xda39 (\\d+)$"))
async def Xda39(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/227", reply_to_message_id=mid)


########################################################################################################################
########################################################################################################################
#######################################################################################################################
########################################################################################################################
########### Ghmbol #######
@app.on_callback_query(filters.regex("^ghmbol (\\d+)$"))
async def ghmbol(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ الحلقه 1", callback_data="Xgh1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 2", callback_data="Xgh2 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 3", callback_data="Xgh3 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 4", callback_data="Xgh4 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 5", callback_data="Xgh5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 6", callback_data="Xgh6 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 7", callback_data="Xgh7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 8", callback_data="Xgh8 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 9", callback_data="Xgh9 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 10", callback_data="Xgh10 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 11", callback_data="Xgh11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 12", callback_data="Xgh12 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 13", callback_data="Xgh13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 14", callback_data="Xgh14 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 15", callback_data="Xgh15 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 16", callback_data="Xgh16 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 17", callback_data="Xgh17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 18", callback_data="Xgh18 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 19", callback_data="Xgh19 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 20", callback_data="Xgh20 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 21", callback_data="Xgh21 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 22", callback_data="Xgh22 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 23", callback_data="Xgh23 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 24", callback_data="Xgh24 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 25", callback_data="Xgh25 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 26", callback_data="Xgh26 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 27", callback_data="Xgh27 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 28", callback_data="Xgh28 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 29", callback_data="Xgh29 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 30", callback_data="Xgh30 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 31", callback_data="Xgh31 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 32", callback_data="Xgh32 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 33", callback_data="Xgh33 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 34", callback_data="Xgh34 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 35", callback_data="Xgh35 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 36", callback_data="Xgh36 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 37", callback_data="Xgh37 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 38", callback_data="Xgh38 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 39", callback_data="Xgh39 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="cartoon2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ أهلا بيك في قايمة حلقات غامبول المدهش\n√", reply_markup=keyboard)


############################################################  111111111111

@app.on_callback_query(filters.regex("^Xgh1 (\\d+)$"))
async def Xgh1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/229", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xgh2 (\\d+)$"))
async def Xgh2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/230", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xgh3 (\\d+)$"))
async def Xgh3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/231", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xgh4 (\\d+)$"))
async def Xgh4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/232", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xgh5 (\\d+)$"))
async def Xgh5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/233", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xgh6 (\\d+)$"))
async def Xgh6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/234", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xgh7 (\\d+)$"))
async def Xgh7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/235", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xgh8 (\\d+)$"))
async def Xgh8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/236", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xgh9 (\\d+)$"))
async def Xgh9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/237", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xgh10 (\\d+)$"))
async def Xgh10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/238", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xgh11 (\\d+)$"))
async def Xgh11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/239", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xgh12 (\\d+)$"))
async def Xgh12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/240", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xgh13 (\\d+)$"))
async def Xgh13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/241", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xgh14 (\\d+)$"))
async def Xgh14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/242", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xgh15 (\\d+)$"))
async def Xgh15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/243", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xgh16 (\\d+)$"))
async def Xgh16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/244", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xgh17 (\\d+)$"))
async def Xgh17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/245", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xgh18 (\\d+)$"))
async def Xgh18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/246", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xgh19 (\\d+)$"))
async def Xgh19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/247", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xgh20 (\\d+)$"))
async def Xgh20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/248", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xgh21 (\\d+)$"))
async def Xgh21(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/249", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xgh22 (\\d+)$"))
async def Xgh22(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/250", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xgh23 (\\d+)$"))
async def Xgh23(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/251", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xgh24 (\\d+)$"))
async def Xgh24(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/252", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xgh25 (\\d+)$"))
async def Xgh25(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/253", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xgh26 (\\d+)$"))
async def Xgh26(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/254", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xgh27 (\\d+)$"))
async def Xgh27(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/255", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xgh28 (\\d+)$"))
async def Xgh28(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/256", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xgh29 (\\d+)$"))
async def Xgh29(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/257", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xgh30 (\\d+)$"))
async def Xgh30(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/258", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xgh31 (\\d+)$"))
async def Xgh31(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/259", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xgh32 (\\d+)$"))
async def Xgh32(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/260", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xgh33 (\\d+)$"))
async def Xgh33(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/261", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xgh34 (\\d+)$"))
async def Xgh34(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/262", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xgh35 (\\d+)$"))
async def Xgh35(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/263", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xgh36 (\\d+)$"))
async def Xgh36(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/264", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xgh37 (\\d+)$"))
async def Xgh37(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/265", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xgh38 (\\d+)$"))
async def Xgh38(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/266", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xgh39 (\\d+)$"))
async def Xgh39(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/267", reply_to_message_id=mid)


########################################################################################
#########################################################################################
#########  oskar     ############
@app.on_callback_query(filters.regex("^oskar (\\d+)$"))
async def oskar(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ الحلقه 1", callback_data="Xosk1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 2", callback_data="Xosk2 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 3", callback_data="Xosk3 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 4", callback_data="Xosk4 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 5", callback_data="Xosk5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 6", callback_data="Xosk6 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 7", callback_data="Xosk7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 8", callback_data="Xosk8 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 9", callback_data="Xosk9 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 10", callback_data="Xosk10 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 11", callback_data="Xosk11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 12", callback_data="Xosk12 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 13", callback_data="Xosk13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 14", callback_data="Xosk14 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 15", callback_data="Xosk15 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 16", callback_data="Xosk16 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 17", callback_data="Xosk17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 18", callback_data="Xosk18 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 19", callback_data="Xosk19 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 20", callback_data="Xosk20 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 21", callback_data="Xosk21 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 22", callback_data="Xosk22 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 23", callback_data="Xosk23 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 24", callback_data="Xosk24 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 25", callback_data="Xosk25 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 26", callback_data="Xosk26 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 27", callback_data="Xosk27 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 28", callback_data="Xosk28 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 29", callback_data="Xosk29 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 30", callback_data="Xosk30 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="cartoon2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ أهلا بيك في قايمة حلقات اوسكار االشجاع\n√", reply_markup=keyboard)


############################################################  111111111111

@app.on_callback_query(filters.regex("^Xosk1 (\\d+)$"))
async def Xosk1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/271", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xosk2 (\\d+)$"))
async def Xosk2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/272", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xosk3 (\\d+)$"))
async def Xosk3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/273", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xosk4 (\\d+)$"))
async def Xosk4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/274", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xosk5 (\\d+)$"))
async def Xosk5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/275", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xosk6 (\\d+)$"))
async def Xosk6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/276", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xosk7 (\\d+)$"))
async def Xosk7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/277", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xosk8 (\\d+)$"))
async def Xosk8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/278", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xosk9 (\\d+)$"))
async def Xosk9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/279", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xosk10 (\\d+)$"))
async def Xosk10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/280", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xosk11 (\\d+)$"))
async def Xosk11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/281", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xosk12 (\\d+)$"))
async def Xosk12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/282", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xosk13 (\\d+)$"))
async def Xosk13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/283", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xosk14 (\\d+)$"))
async def Xosk14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/284", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xosk15 (\\d+)$"))
async def Xosk15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/285", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xosk16 (\\d+)$"))
async def Xosk16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/286", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xosk17 (\\d+)$"))
async def Xosk17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/287", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xosk18 (\\d+)$"))
async def Xosk18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/288", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xosk19 (\\d+)$"))
async def Xosk19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/289", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xosk20 (\\d+)$"))
async def Xosk20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/290", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xosk21 (\\d+)$"))
async def Xosk21(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/291", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xosk22 (\\d+)$"))
async def Xosk22(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/292", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xosk23 (\\d+)$"))
async def Xosk23(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/293", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xosk24 (\\d+)$"))
async def Xosk24(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/294", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xosk25 (\\d+)$"))
async def Xosk25(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/295", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xosk26 (\\d+)$"))
async def Xosk26(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/296", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xosk27 (\\d+)$"))
async def Xosk27(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/297", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xosk28 (\\d+)$"))
async def Xosk28(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/298", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xosk29 (\\d+)$"))
async def Xosk29(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/300", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xosk30 (\\d+)$"))
async def Xosk30(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/299", reply_to_message_id=mid)


########################################################################################
#########################################################################################
##############   Temon & Bomba  #########

@app.on_callback_query(filters.regex("^temon (\\d+)$"))
async def temon(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ الموسم الاول", callback_data="temon1 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الموسم التاني", callback_data="temon2 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="cartoon2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ أهلا بيك في قايمة حلقات تيمون وبمومبا\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^temon1 (\\d+)$"))
async def temon1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقه 1", callback_data="Xtem1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 2", callback_data="Xtem2 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 3", callback_data="Xtem3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 4", callback_data="Xtem4 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 5", callback_data="Xtem5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 6", callback_data="Xtem6 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 7", callback_data="Xtem7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 8", callback_data="Xtem8 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 9", callback_data="Xtem9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 10", callback_data="Xtem10 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 11", callback_data="Xtem11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 12", callback_data="Xtem12 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 13", callback_data="Xtem13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 14", callback_data="Xtem14 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 15", callback_data="Xtem15 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 16", callback_data="Xtem16 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 17", callback_data="Xtem17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 18", callback_data="Xtem18 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 19", callback_data="Xtem19 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 20", callback_data="Xtem20 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="temon " + str(m.from_user.id))] +
        [InlineKeyboardButton("➡️ التالي", callback_data="temon2 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="cartoon2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ أهلا بيك في قايمة حلقات تيمون وبمومبا الموسم الاول\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^temon2 (\\d+)$"))
async def temon2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقه 1", callback_data="Xtem21 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 2", callback_data="Xtem22 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 3", callback_data="Xtem23 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 4", callback_data="Xtem24 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 5", callback_data="Xtem25 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 6", callback_data="Xtem26 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 7", callback_data="Xtem27 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 8", callback_data="Xtem28 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 9", callback_data="Xtem29 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 10", callback_data="Xtem30 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 11", callback_data="Xtem31 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 12", callback_data="Xtem32 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 13", callback_data="Xtem33 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 14", callback_data="Xtem34 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 15", callback_data="Xtem35 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 16", callback_data="Xtem36 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 17", callback_data="Xtem37 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 18", callback_data="Xtem38 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 19", callback_data="Xtem39 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 20", callback_data="Xtem40 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="temon1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="cartoon2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ أهلا بيك في قايمة حلقات تيمون وبمومبا الموسم التاني\n√", reply_markup=keyboard)


#################################################################################  1111

@app.on_callback_query(filters.regex("^Xtem1 (\\d+)$"))
async def Xtem1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/302", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtem2 (\\d+)$"))
async def Xtem2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/303", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtem3 (\\d+)$"))
async def Xtem3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/304", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtem4 (\\d+)$"))
async def Xtem4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/305", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtem5 (\\d+)$"))
async def Xtem5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/306", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtem6 (\\d+)$"))
async def Xtem6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/307", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtem7 (\\d+)$"))
async def Xtem7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/308", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtem8 (\\d+)$"))
async def Xtem8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/309", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtem9 (\\d+)$"))
async def Xtem9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/310", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtem10 (\\d+)$"))
async def Xtem10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/311", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtem11 (\\d+)$"))
async def Xtem11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/312", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtem12 (\\d+)$"))
async def Xtem12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/313", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtem13 (\\d+)$"))
async def Xtem13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/314", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtem14 (\\d+)$"))
async def Xtem14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/315", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtem15 (\\d+)$"))
async def Xtem15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/316", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtem16 (\\d+)$"))
async def Xtem16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/317", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtem17 (\\d+)$"))
async def Xtem17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/318", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtem18 (\\d+)$"))
async def Xtem18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/319", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtem19 (\\d+)$"))
async def Xtem19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/320", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtem20 (\\d+)$"))
async def Xtem20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/321", reply_to_message_id=mid)


#################################################################################  2222222

@app.on_callback_query(filters.regex("^Xtem21 (\\d+)$"))
async def Xtem21(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/322", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtem22 (\\d+)$"))
async def Xtem22(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/323", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtem23 (\\d+)$"))
async def Xtem23(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/324", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtem24 (\\d+)$"))
async def Xtem24(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/325", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtem25 (\\d+)$"))
async def Xtem25(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/326", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtem26 (\\d+)$"))
async def Xtem26(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/327", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtem27 (\\d+)$"))
async def Xtem27(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/328", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtem28 (\\d+)$"))
async def Xtem28(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/329", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtem29 (\\d+)$"))
async def Xtem29(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/330", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtem30 (\\d+)$"))
async def Xtem30(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/331", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtem31 (\\d+)$"))
async def Xtem31(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/332", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtem32 (\\d+)$"))
async def Xtem32(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/333", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtem33 (\\d+)$"))
async def Xtem33(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/334", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtem34 (\\d+)$"))
async def Xtem34(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/335", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtem35 (\\d+)$"))
async def Xtem35(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/336", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtem36 (\\d+)$"))
async def Xtem36(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/337", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtem37 (\\d+)$"))
async def Xtem37(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/338", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtem38 (\\d+)$"))
async def Xtem38(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/339", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtem39 (\\d+)$"))
async def Xtem39(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/340", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtem40 (\\d+)$"))
async def Xtem40(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/341", reply_to_message_id=mid)


########################################################################################
#########################################################################################
############## Snafer  #########
@app.on_callback_query(filters.regex("^snafer (\\d+)$"))
async def snafer(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الموسم الاول", callback_data="snafer1 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الموسم التاني", callback_data="snafer2 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الموسم الرابع", callback_data="snafer4 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="cartoon2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ أهلا بيك في قايمة حلقات السنافر\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^snafer1 (\\d+)$"))
async def snafer1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقه 1", callback_data="Xsna1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 2", callback_data="Xsna2 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 3", callback_data="Xsna3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 4", callback_data="Xsna4 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 5", callback_data="Xsna5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 6", callback_data="Xsna6 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 7", callback_data="Xsna7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 8", callback_data="Xsna8 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 9", callback_data="Xsna9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 10", callback_data="Xsna10 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 11", callback_data="Xsna11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 12", callback_data="Xsna12 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 13", callback_data="Xsna13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 14", callback_data="Xsna14 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 15", callback_data="Xsna15 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 16", callback_data="Xsna16 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 17", callback_data="Xsna17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 18", callback_data="Xsna18 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 19", callback_data="Xsna19 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 20", callback_data="Xsna20 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="snafer " + str(m.from_user.id))] +
        [InlineKeyboardButton("➡️ التالي", callback_data="snafer2 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="cartoon2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ أهلا بيك في قايمة حلقات السنافر الموسم الاول\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^snafer2 (\\d+)$"))
async def snafer2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقه 1", callback_data="Xsna21 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 2", callback_data="Xsna22 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 3", callback_data="Xsna23 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 4", callback_data="Xsna24 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 5", callback_data="Xsna25 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 6", callback_data="Xsna26 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 7", callback_data="Xsna27 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 8", callback_data="Xsna28 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 9", callback_data="Xsna29 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 10", callback_data="Xsna30 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 11", callback_data="Xsna31 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 12", callback_data="Xsna32 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 13", callback_data="Xsna33 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 14", callback_data="Xsna34 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 15", callback_data="Xsna35 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 16", callback_data="Xsna36 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 17", callback_data="Xsna37 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 18", callback_data="Xsna38 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 19", callback_data="Xsna39 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 20", callback_data="Xsna40 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="snafer1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("➡️ التالي", callback_data="snafer3 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="cartoon2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ أهلا بيك في قايمة حلقات السنافر الموسم التاني\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^snafer4 (\\d+)$"))
async def snafer3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقه 1", callback_data="Xsna41 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ 2الحلقه ", callback_data="Xsna42 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 3", callback_data="Xsna43 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 4", callback_data="Xsna44 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 5", callback_data="Xsna45 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 6", callback_data="Xsna46 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 7", callback_data="Xsna47 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 8", callback_data="Xsna48 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 9", callback_data="Xsna49 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 10", callback_data="Xsna50 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 11", callback_data="Xsna51 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 12", callback_data="Xsna52 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 13", callback_data="Xsna53 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 14", callback_data="Xsna54 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 15", callback_data="Xsna55 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="snafer2 " + str(m.from_user.id))] +
        [InlineKeyboardButton("➡️ التالي", callback_data="snafer4 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="cartoon2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ أهلا بيك في قايمة حلقات السنافر الموسم الرابع\n√", reply_markup=keyboard)


############################################################

@app.on_callback_query(filters.regex("^Xsna1 (\\d+)$"))
async def Xsna1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/343", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna2 (\\d+)$"))
async def Xsna2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/344", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna3 (\\d+)$"))
async def Xsna3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/345", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna4 (\\d+)$"))
async def Xsna4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/346", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna5 (\\d+)$"))
async def Xsna5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/347", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna6 (\\d+)$"))
async def Xsna6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/348", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna7 (\\d+)$"))
async def Xsna7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/349", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna8 (\\d+)$"))
async def Xsna8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/350", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna9 (\\d+)$"))
async def Xsna9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/351", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna10 (\\d+)$"))
async def Xsna10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/352", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna11 (\\d+)$"))
async def Xsna11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/353", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna12 (\\d+)$"))
async def Xsna12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/354", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna13 (\\d+)$"))
async def Xsna13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/355", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna14 (\\d+)$"))
async def Xsna14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/356", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna15 (\\d+)$"))
async def Xsna15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/357", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna16 (\\d+)$"))
async def Xsna16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/358", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna17 (\\d+)$"))
async def Xsna17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/359", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna18 (\\d+)$"))
async def Xsna18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/360", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna19 (\\d+)$"))
async def Xsna19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/361", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna20 (\\d+)$"))
async def Xsna20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/362", reply_to_message_id=mid)


#################################################################################  2222222

@app.on_callback_query(filters.regex("^Xsna21 (\\d+)$"))
async def Xsna21(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/364", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna22 (\\d+)$"))
async def Xsna22(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/365", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna23 (\\d+)$"))
async def Xsna23(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/366", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna24 (\\d+)$"))
async def Xsna24(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/367", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna25 (\\d+)$"))
async def Xsna25(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/368", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna26 (\\d+)$"))
async def Xsna26(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/369", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna27 (\\d+)$"))
async def Xsna27(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/370", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna28 (\\d+)$"))
async def Xsna28(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/371", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna29 (\\d+)$"))
async def Xsna29(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/372", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna30 (\\d+)$"))
async def Xsna30(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/373", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna31 (\\d+)$"))
async def Xsna31(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/374", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna32 (\\d+)$"))
async def Xsna32(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/375", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna33 (\\d+)$"))
async def Xsna33(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/376", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna34 (\\d+)$"))
async def Xsna34(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/377", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna35 (\\d+)$"))
async def Xsna35(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/378", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna36 (\\d+)$"))
async def Xsna36(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/379", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna37 (\\d+)$"))
async def Xsna37(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/380", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna38 (\\d+)$"))
async def Xsna38(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/381", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna39 (\\d+)$"))
async def Xsna39(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/382", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna40 (\\d+)$"))
async def Xsna40(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/383", reply_to_message_id=mid)


################################################################################## 33333333

@app.on_callback_query(filters.regex("^Xsna41 (\\d+)$"))
async def Xsna41(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/385", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna42 (\\d+)$"))
async def Xsna42(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/386", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna43 (\\d+)$"))
async def Xsna43(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/387", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna44 (\\d+)$"))
async def Xsna44(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/388", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna45 (\\d+)$"))
async def Xsna45(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/389", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna46 (\\d+)$"))
async def Xsna46(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/390", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna47 (\\d+)$"))
async def Xsna47(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/391", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna48 (\\d+)$"))
async def Xsna48(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/392", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna49 (\\d+)$"))
async def Xsna49(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/393", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna50 (\\d+)$"))
async def Xsna50(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/394", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna51 (\\d+)$"))
async def Xsna51(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/395", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna52 (\\d+)$"))
async def Xsna52(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/399", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna53 (\\d+)$"))
async def Xsna53(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/398", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna54 (\\d+)$"))
async def Xsna54(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/396", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsna55 (\\d+)$"))
async def Xsna55(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/397", reply_to_message_id=mid)


## AFLAM ##
########################################################################################
#########################################################################################

# AFLAM CARTOON #
@app.on_callback_query(filters.regex("^fcartoon (\\d+)$"))
async def fcartoon(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ القائمة رقم 1", callback_data="Xfcartoon1 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ القائمة رقم 2", callback_data="Xfcartoon2 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="cartoon2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ أهلا بيك في قايمة افلام الكارتون\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xfcartoon1 (\\d+)$"))
async def Xfcartoon1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ بارفي مدبلج", callback_data="barvy " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الفار الطباخ مدبلج", callback_data="far " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ السيارات 1 مدبلج", callback_data="car1 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ السيارات 2 مدبلج", callback_data="car2 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ السيارات 3 مدبلج", callback_data="car3 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ فروج القلة مدبلج", callback_data="froj " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ حكاية لعبه 4 مدبلج", callback_data="toy " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ جامعه المرعبين المحدوده مدبلج", callback_data="uni " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ 101 كلب منقط مدبلج", callback_data="dog " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الديناصور مترجم", callback_data="dinasor " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ بن تن مدبلج", callback_data="ben10 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ بن تن هيروز يونايتد مدبلج", callback_data="benhero10 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الكلب بولت مدبلج", callback_data="bolt " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="fcartoon " + str(m.from_user.id))] +
        [InlineKeyboardButton("➡️ التالي", callback_data="Xfcartoon2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ أهلا بيك في قايمة افلام الكارتون رقم 1\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xfcartoon2 (\\d+)$"))
async def Xfcartoon2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ رالف المدمر مدبلج", callback_data="ralph " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ ليلو 2 مدبلج", callback_data="lilo " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الطفل الزعيم مدبلج", callback_data="bossbaby " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الفيل هورتن مدبلج", callback_data="horten " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ Coco مدبلج", callback_data="coco " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ سبايدر مان 2018 مدبلج", callback_data="spider " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ Ice Age1 مترجم", callback_data="ice1 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ Ice Age2 مترجم", callback_data="ice2 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ Ice Age3 مترجم", callback_data="ice3 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ Ice Age4 مترجم", callback_data="ice4 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ Ice Age5 مترجم", callback_data="ice5 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ انا الحقير 1 مدبلج", callback_data="haker1 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ انا الحقير 2 مدبلج", callback_data="haker2 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ انا الحقير 3 مدبلج", callback_data="haker3 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="Xfcartoon1 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="cartoon2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ أهلا بيك في قايمة افلام الكارتون رقم 2\n√", reply_markup=keyboard)


########################################################################################
#########################################################################################

@app.on_callback_query(filters.regex("^barvy (\\d+)$"))
async def barvy(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/400", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^far (\\d+)$"))
async def far(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/401", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^car1 (\\d+)$"))
async def car1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/440", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^car2 (\\d+)$"))
async def car2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/441", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^car3 (\\d+)$"))
async def car3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/450", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^froj (\\d+)$"))
async def froj(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/406", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^toy (\\d+)$"))
async def toy(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/408", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^uni (\\d+)$"))
async def uni(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/410", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^dog (\\d+)$"))
async def dog(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/412", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^dinasor (\\d+)$"))
async def dinasor(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/414", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^ben10 (\\d+)$"))
async def ben10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/416", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^benhero10 (\\d+)$"))
async def benhero10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/422", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^bolt (\\d+)$"))
async def bolt(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/418", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^ralph (\\d+)$"))
async def ralph(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/420", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^lilo (\\d+)$"))
async def lilo(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/427", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^bossbaby (\\d+)$"))
async def Xsbossbaby16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/434", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^horten (\\d+)$"))
async def horten(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/436", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^coco (\\d+)$"))
async def coco(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/438", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^spider (\\d+)$"))
async def spider(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/443", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^ice1 (\\d+)$"))
async def ice1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/445", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^ice2 (\\d+)$"))
async def ice2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/446", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^ice3 (\\d+)$"))
async def ice3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/447", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^ice4 (\\d+)$"))
async def ice4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/448", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^ice5 (\\d+)$"))
async def ice5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/449", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^haker1 (\\d+)$"))
async def haker1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/453", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^haker2 (\\d+)$"))
async def haker2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/454", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^haker3 (\\d+)$"))
async def haker3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UCartoon/455", reply_to_message_id=mid)
#########################################################################################
#########################################################################################
#########################         # END masrahia AR #          ##########################
#########################################################################################
#########################################################################################
