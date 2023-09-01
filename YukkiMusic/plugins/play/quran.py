from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from config import get_bot_information
###############################################
##  CopyRight & Creator File And Programing  ##
##                                           ##
##     #######  ######  #####*     *##*      ##
##     #  #  #  ###     #     *   *    *     ##
##     #     #  ##      #     *   *    *     ##
##     #     #  #####   #####*     *##*      ##
##                                           ##
###############################################

################################
## Dev By: @WWWL5 & @MRv7x  ##
################################

@Client.on_callback_query(filters.regex("^quran (\\d+)$"))
async def quran(c: Client, m: Message):
    global mid
    mid = m.message_id
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("فارس عباد 📖", callback_data="fares " + str(m.from_user.id))] +
        [InlineKeyboardButton("ناصر القطامى 📖", callback_data="naser " + str(m.from_user.id))],
        [InlineKeyboardButton("اسلام صبحى 📖", callback_data="eslam " + str(m.from_user.id))] +
        [InlineKeyboardButton("عبدالباسط عبد الصمد 📖", callback_data="abdelbaset " + str(m.from_user.id))],
        [InlineKeyboardButton("ياسر الدوسري 📖", callback_data="eldosary " + str(m.from_user.id))] +
        [InlineKeyboardButton("ادريس ابكر 📖", callback_data="abkar " + str(m.from_user.id))],
        [InlineKeyboardButton("مشارى العفاسى 📖", callback_data="afasy " + str(m.from_user.id))] +
        [InlineKeyboardButton("احمد بن على العجمي 📖", callback_data="agamy " + str(m.from_user.id))],
        [InlineKeyboardButton("ماهر المعيقلى 📖", callback_data="maher " + str(m.from_user.id))] +
        [InlineKeyboardButton("خالد الجليل 📖", callback_data="galel " + str(m.from_user.id))],

        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.reply_text("◍ اهلا بك فى القرءان الكريم اختر احدى المقرئين\n√", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^quran2 (\\d+)$"))
async def quran2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("فارس عباد 📖", callback_data="fares " + str(m.from_user.id))] +
        [InlineKeyboardButton("ناصر القطامى 📖", callback_data="naser " + str(m.from_user.id))],
        [InlineKeyboardButton("اسلام صبحى 📖", callback_data="eslam " + str(m.from_user.id))] +
        [InlineKeyboardButton("عبدالباسط عبد الصمد 📖", callback_data="abdelbaset " + str(m.from_user.id))],
        [InlineKeyboardButton("ياسر الدوسري 📖", callback_data="eldosary " + str(m.from_user.id))] +
        [InlineKeyboardButton("ادريس ابكر 📖", callback_data="abkar " + str(m.from_user.id))],
        [InlineKeyboardButton("مشارى العفاسى 📖", callback_data="afasy " + str(m.from_user.id))] +
        [InlineKeyboardButton("احمد بن على العجمي 📖", callback_data="agamy " + str(m.from_user.id))],
        [InlineKeyboardButton("ماهر المعيقلى 📖", callback_data="maher " + str(m.from_user.id))] +
        [InlineKeyboardButton("خالد الجليل 📖", callback_data="galel " + str(m.from_user.id))],

        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اختر السوره\n√", reply_markup=keyboard, disable_web_page_preview=True)


########################################################################################################################
########################################################################################################################

@Client.on_callback_query(filters.regex("^fares (\\d+)$"))
async def fares(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("الفاتحه 🕋", callback_data="xf1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البقرة 🕋", callback_data="xf2 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ال عمران 🕋", callback_data="xf3 " + str(m.from_user.id))],
        [InlineKeyboardButton("النساء 🕋", callback_data="xf4 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المائدة 🕋", callback_data="xf5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الانعام 🕋", callback_data="xf6 " + str(m.from_user.id))],
        [InlineKeyboardButton("الأعراف 🕋", callback_data="xf7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الأنفال 🕋", callback_data="xf8 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التوبة 🕋", callback_data="xf9 " + str(m.from_user.id))],
        [InlineKeyboardButton("يونس 🕋", callback_data="xf10 " + str(m.from_user.id))] +
        [InlineKeyboardButton("هود 🕋", callback_data="xf11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يوسف 🕋", callback_data="xf12 " + str(m.from_user.id))],
        [InlineKeyboardButton("الرعد 🕋", callback_data="xf13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("أبراهيم 🕋", callback_data="xf14 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحجر 🕋", callback_data="xf15 " + str(m.from_user.id))],
        [InlineKeyboardButton("النحل 🕋", callback_data="xf16 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاسراء 🕋", callback_data="xf17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الكهف 🕋", callback_data="xf18 " + str(m.from_user.id))],
        [InlineKeyboardButton("مريم 🕋", callback_data="xf19 " + str(m.from_user.id))] +
        [InlineKeyboardButton("طه 🕋", callback_data="xf20 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الأنبياء 🕋", callback_data="xf21 " + str(m.from_user.id))],
        [InlineKeyboardButton("الحج 🕋", callback_data="xf22 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المؤمنون 🕋", callback_data="xf23 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النور 🕋", callback_data="xf24 " + str(m.from_user.id))],
        [InlineKeyboardButton("الفرقان 🕋", callback_data="xf25 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الشعراء 🕋", callback_data="xf26 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النحل 🕋", callback_data="xf27 " + str(m.from_user.id))],
        [InlineKeyboardButton("القصص 🕋", callback_data="xf28 " + str(m.from_user.id))] +
        [InlineKeyboardButton("العنكبوت 🕋", callback_data="xf29 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الروم 🕋", callback_data="xf30 " + str(m.from_user.id))],
        [InlineKeyboardButton("لقمان 🕋", callback_data="xf31 " + str(m.from_user.id))] +
        [InlineKeyboardButton("السجدة 🕋", callback_data="xf32 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاحزاب 🕋", callback_data="xf33 " + str(m.from_user.id))],
        [InlineKeyboardButton("سبأ 🕋", callback_data="xf34 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فاطر 🕋", callback_data="xf35 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يس 🕋", callback_data="xf36 " + str(m.from_user.id))],
        [InlineKeyboardButton("الصافات 🕋", callback_data="xf37 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ص 🕋", callback_data="xf38 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الزمر 🕋", callback_data="xf39 " + str(m.from_user.id))],
        [InlineKeyboardButton("غافر 🕋", callback_data="xf40 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فصلت 🕋", callback_data="xf41 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الشورئ 🕋", callback_data="xf42 " + str(m.from_user.id))],
        [InlineKeyboardButton("الزخرف 🕋", callback_data="xf43 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الدخان 🕋", callback_data="xf44 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجاثيه 🕋", callback_data="xf45 " + str(m.from_user.id))],
        [InlineKeyboardButton("الاحقاف 🕋", callback_data="xf46 " + str(m.from_user.id))] +
        [InlineKeyboardButton("محمد 🕋", callback_data="xf47 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفتح 🕋", callback_data="xf48 " + str(m.from_user.id))],
        [InlineKeyboardButton("الحجرات 🕋", callback_data="xf49 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ق 🕋", callback_data="xf50 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الذاريات 🕋", callback_data="xf51 " + str(m.from_user.id))],

        [InlineKeyboardButton("➡️ التالي", callback_data="fares2 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اختر سوره للقارئ فارس عباد\n√", reply_markup=keyboard, disable_web_page_preview=True)


@Client.on_callback_query(filters.regex("^fares2 (\\d+)$"))
async def fares2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("الطور 🕋", callback_data="xf52 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النجم 🕋", callback_data="xf53 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القمر 🕋", callback_data="xf54 " + str(m.from_user.id))],
        [InlineKeyboardButton("الرحمن 🕋", callback_data="xf55 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الواقعه 🕋", callback_data="xf56 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحديد 🕋", callback_data="xf57 " + str(m.from_user.id))],
        [InlineKeyboardButton("المجادلة 🕋", callback_data="xf58 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحشر 🕋", callback_data="xf59 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الممتحنة 🕋", callback_data="xf60 " + str(m.from_user.id))],
        [InlineKeyboardButton("الصف 🕋", callback_data="xf61 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجمعة 🕋", callback_data="xf62 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المنافقون 🕋", callback_data="xf63 " + str(m.from_user.id))],
        [InlineKeyboardButton("التغابن 🕋", callback_data="xf64 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الطلاق 🕋", callback_data="xf65 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التحريم 🕋", callback_data="xf66 " + str(m.from_user.id))],
        [InlineKeyboardButton("الملك 🕋", callback_data="xf67 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القلم 🕋", callback_data="xf68 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحاقة 🕋", callback_data="xf69 " + str(m.from_user.id))],
        [InlineKeyboardButton("المعارج 🕋", callback_data="xf70 " + str(m.from_user.id))] +
        [InlineKeyboardButton("نوح 🕋", callback_data="xf71 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجن 🕋", callback_data="xf72 " + str(m.from_user.id))],
        [InlineKeyboardButton("المزمل 🕋", callback_data="xf73 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المدثر 🕋", callback_data="xf74 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القيامة 🕋", callback_data="xf75 " + str(m.from_user.id))],
        [InlineKeyboardButton("الانسان 🕋", callback_data="xf76 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المرسلات 🕋", callback_data="xf77 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النبأ 🕋", callback_data="xf78 " + str(m.from_user.id))],
        [InlineKeyboardButton("النازعات 🕋", callback_data="xf79 " + str(m.from_user.id))] +
        [InlineKeyboardButton("عبس 🕋", callback_data="xf80 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التكوير 🕋", callback_data="xf81 " + str(m.from_user.id))],
        [InlineKeyboardButton("الانفطار 🕋", callback_data="xf82 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المطففين 🕋", callback_data="xf83 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الانشقاق 🕋", callback_data="xf84 " + str(m.from_user.id))],
        [InlineKeyboardButton("البروج 🕋", callback_data="xf85 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الطارق 🕋", callback_data="xf86 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاعلي 🕋", callback_data="xf87 " + str(m.from_user.id))],
        [InlineKeyboardButton("الغاشية 🕋", callback_data="xf88 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفجر 🕋", callback_data="xf89 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البلد 🕋", callback_data="xf90 " + str(m.from_user.id))],
        [InlineKeyboardButton("الشمس 🕋", callback_data="xf91 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الليل 🕋", callback_data="xf92 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الضحئ 🕋", callback_data="xf93 " + str(m.from_user.id))],
        [InlineKeyboardButton("الشرح 🕋", callback_data="xf94 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التين 🕋", callback_data="xf95 " + str(m.from_user.id))] +
        [InlineKeyboardButton("العلق 🕋", callback_data="xf96 " + str(m.from_user.id))],
        [InlineKeyboardButton("القدر 🕋", callback_data="xf97 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البينة 🕋", callback_data="xf98 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الزلزلة 🕋", callback_data="xf99 " + str(m.from_user.id))],
        [InlineKeyboardButton("العاديات 🕋", callback_data="xf100 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القارعة 🕋", callback_data="xf101 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التكاثر 🕋", callback_data="xf102 " + str(m.from_user.id))],
        [InlineKeyboardButton("العصر 🕋", callback_data="xf103 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الهمزة 🕋", callback_data="xf104 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفيل 🕋", callback_data="xf105 " + str(m.from_user.id))],
        [InlineKeyboardButton("قريش 🕋", callback_data="xf106 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الماعون 🕋", callback_data="xf107 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الكوثر 🕋", callback_data="xf108 " + str(m.from_user.id))],
        [InlineKeyboardButton("الكافرون 🕋", callback_data="xf109 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النصر 🕋", callback_data="xf110 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المسد 🕋", callback_data="xf111 " + str(m.from_user.id))],
        [InlineKeyboardButton("الاخلاص 🕋", callback_data="xf112 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفلق 🕋", callback_data="xf113 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الناس 🕋", callback_data="xf114 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="fares " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اختر سوره للقارئ فارس عباد\n√", reply_markup=keyboard, disable_web_page_preview=True)


@Client.on_callback_query(filters.regex("^xf1 (\\d+)$"))
async def xf1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/285", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf2 (\\d+)$"))
async def xf2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/286", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf3 (\\d+)$"))
async def xf3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/287", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf4 (\\d+)$"))
async def xf4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/288", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf5 (\\d+)$"))
async def xf5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/289", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf6 (\\d+)$"))
async def xf6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/290", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf7 (\\d+)$"))
async def xf7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/291", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf8 (\\d+)$"))
async def xf8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/292", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf9 (\\d+)$"))
async def xf9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/293", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf10 (\\d+)$"))
async def xf10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/294", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf11 (\\d+)$"))
async def xf11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/295", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf12 (\\d+)$"))
async def xf12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/296", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf13 (\\d+)$"))
async def xf13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/297", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf14 (\\d+)$"))
async def xf14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/298", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf15 (\\d+)$"))
async def xf15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/299", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf16 (\\d+)$"))
async def xf16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/300", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf17 (\\d+)$"))
async def xf17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/301", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf18 (\\d+)$"))
async def xf18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/302", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf19 (\\d+)$"))
async def xf19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/303", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf20 (\\d+)$"))
async def xf20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/304", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf21 (\\d+)$"))
async def xf21(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/305", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf22 (\\d+)$"))
async def xf22(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/306", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf23 (\\d+)$"))
async def xf23(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/307", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf24 (\\d+)$"))
async def xf24(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/308", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf25 (\\d+)$"))
async def xf25(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/309", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf26 (\\d+)$"))
async def xf26(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/310", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf27 (\\d+)$"))
async def xf27(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/311", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf28 (\\d+)$"))
async def xf28(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/312", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf29 (\\d+)$"))
async def xf29(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/313", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf30 (\\d+)$"))
async def xf30(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/314", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf31 (\\d+)$"))
async def xf31(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/315", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf32 (\\d+)$"))
async def xf32(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/316", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf33 (\\d+)$"))
async def xf33(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/317", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf34 (\\d+)$"))
async def xf34(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/318", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf35 (\\d+)$"))
async def xf35(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/319", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf36 (\\d+)$"))
async def xf36(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/320", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf37 (\\d+)$"))
async def xf37(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/321", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf38 (\\d+)$"))
async def xf38(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/322", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf39 (\\d+)$"))
async def xf39(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/323", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf40 (\\d+)$"))
async def xf40(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/324", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf41 (\\d+)$"))
async def xf41(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/325", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf42 (\\d+)$"))
async def xf42(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/326", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf43 (\\d+)$"))
async def xf43(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/327", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf44 (\\d+)$"))
async def xf44(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/328", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf45 (\\d+)$"))
async def xf45(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/329", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf46 (\\d+)$"))
async def xf46(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/330", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf47 (\\d+)$"))
async def xf47(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/331", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf48 (\\d+)$"))
async def xf48(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/332", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf49 (\\d+)$"))
async def xf49(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/333", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf50 (\\d+)$"))
async def xf50(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/334", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf51 (\\d+)$"))
async def xf51(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/335", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf52 (\\d+)$"))
async def xf52(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/336", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf53 (\\d+)$"))
async def xf53(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/337", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf54 (\\d+)$"))
async def xf54(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/338", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf55 (\\d+)$"))
async def xf55(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/339", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf56 (\\d+)$"))
async def xf56(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/340", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf57 (\\d+)$"))
async def xf57(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/341", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf58 (\\d+)$"))
async def xf58(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/342", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf59 (\\d+)$"))
async def xf59(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/343", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf60 (\\d+)$"))
async def xf60(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/344", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf61 (\\d+)$"))
async def xf61(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/345", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf62 (\\d+)$"))
async def xf62(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/346", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf63 (\\d+)$"))
async def xf63(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/347", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf64 (\\d+)$"))
async def xf64(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/348", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf65 (\\d+)$"))
async def xf65(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/349", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf66 (\\d+)$"))
async def xf66(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/350", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf67 (\\d+)$"))
async def xf67(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/351", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf68 (\\d+)$"))
async def xf68(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/352", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf69 (\\d+)$"))
async def xf69(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/353", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf70 (\\d+)$"))
async def xf70(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/354", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf71 (\\d+)$"))
async def xf71(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/355", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf72 (\\d+)$"))
async def xf72(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/356", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf73 (\\d+)$"))
async def xf73(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/357", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf74 (\\d+)$"))
async def xf74(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/358", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf75 (\\d+)$"))
async def xf75(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/359", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf76 (\\d+)$"))
async def xf76(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/360", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf77 (\\d+)$"))
async def xf77(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/361", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf78 (\\d+)$"))
async def xf78(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/362", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf79 (\\d+)$"))
async def xf79(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/363", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf80 (\\d+)$"))
async def xf80(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/364", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf81 (\\d+)$"))
async def xf81(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/365", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf82 (\\d+)$"))
async def xf82(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/366", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf83 (\\d+)$"))
async def xf83(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/367", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf84 (\\d+)$"))
async def xf84(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/368", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf85 (\\d+)$"))
async def xf85(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/369", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf86 (\\d+)$"))
async def xf86(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/370", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf87 (\\d+)$"))
async def xf87(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/371", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf88 (\\d+)$"))
async def xf88(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/372", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf89 (\\d+)$"))
async def xf89(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/373", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf90 (\\d+)$"))
async def xf90(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/374", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf91 (\\d+)$"))
async def xf91(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/375", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf92 (\\d+)$"))
async def xf92(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/376", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf93 (\\d+)$"))
async def xf93(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/377", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf94 (\\d+)$"))
async def xf94(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/378", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf95 (\\d+)$"))
async def xf95(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/379", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf96 (\\d+)$"))
async def xf96(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/380", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf97 (\\d+)$"))
async def xf97(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/381", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf98 (\\d+)$"))
async def xf98(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/382", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf99 (\\d+)$"))
async def xf99(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/383", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf100 (\\d+)$"))
async def xf100(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/384", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf101 (\\d+)$"))
async def xf101(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/385", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf102 (\\d+)$"))
async def xf102(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/386", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf103 (\\d+)$"))
async def xf103(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/387", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf104 (\\d+)$"))
async def xf104(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/388", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf105 (\\d+)$"))
async def xf105(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/389", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf106 (\\d+)$"))
async def xf106(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/390", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf107 (\\d+)$"))
async def xf107(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/391", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf108 (\\d+)$"))
async def xf108(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/392", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf109 (\\d+)$"))
async def xf109(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/393", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf110 (\\d+)$"))
async def xf110(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/394", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf111 (\\d+)$"))
async def xf111(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/395", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf112 (\\d+)$"))
async def xf112(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/396", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf113 (\\d+)$"))
async def xf113(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/397", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf114 (\\d+)$"))
async def xf114(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/398", reply_to_message_id=mid)


########################################################################################################################
########################################################################################################################


@Client.on_callback_query(filters.regex("^naser (\\d+)$"))
async def naser(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("الفاتحه 🕋", callback_data="xn1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البقرة 🕋", callback_data="xn2 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ال عمران 🕋", callback_data="xn3 " + str(m.from_user.id))],
        [InlineKeyboardButton("النساء 🕋", callback_data="xn4 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المائدة 🕋", callback_data="xn5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الانعام 🕋", callback_data="xn6 " + str(m.from_user.id))],
        [InlineKeyboardButton("الأعراف 🕋", callback_data="xn7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الأنفال 🕋", callback_data="xn8 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التوبة 🕋", callback_data="xn9 " + str(m.from_user.id))],
        [InlineKeyboardButton("يونس 🕋", callback_data="xn10 " + str(m.from_user.id))] +
        [InlineKeyboardButton("هود 🕋", callback_data="xn11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يوسف 🕋", callback_data="xn12 " + str(m.from_user.id))],
        [InlineKeyboardButton("الرعد 🕋", callback_data="xn13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("أبراهيم 🕋", callback_data="xn14 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحجر 🕋", callback_data="xn15 " + str(m.from_user.id))],
        [InlineKeyboardButton("النحل 🕋", callback_data="xn16 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاسراء 🕋", callback_data="xn17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الكهف 🕋", callback_data="xn18 " + str(m.from_user.id))],
        [InlineKeyboardButton("مريم 🕋", callback_data="xn19 " + str(m.from_user.id))] +
        [InlineKeyboardButton("طه 🕋", callback_data="xn20 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الأنبياء 🕋", callback_data="xn21 " + str(m.from_user.id))],
        [InlineKeyboardButton("الحج 🕋", callback_data="xn22 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المؤمنون 🕋", callback_data="xn23 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النور 🕋", callback_data="xn24 " + str(m.from_user.id))],
        [InlineKeyboardButton("الفرقان 🕋", callback_data="xn25 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الشعراء 🕋", callback_data="xn26 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النحل 🕋", callback_data="xn27 " + str(m.from_user.id))],
        [InlineKeyboardButton("القصص 🕋", callback_data="xn28 " + str(m.from_user.id))] +
        [InlineKeyboardButton("العنكبوت 🕋", callback_data="xn29 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الروم 🕋", callback_data="xn30 " + str(m.from_user.id))],
        [InlineKeyboardButton("لقمان 🕋", callback_data="xn31 " + str(m.from_user.id))] +
        [InlineKeyboardButton("السجدة 🕋", callback_data="xn32 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاحزاب 🕋", callback_data="xn33 " + str(m.from_user.id))],
        [InlineKeyboardButton("سبأ 🕋", callback_data="xn34 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فاطر 🕋", callback_data="xn35 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يس 🕋", callback_data="xn36 " + str(m.from_user.id))],
        [InlineKeyboardButton("الصافات 🕋", callback_data="xn37 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ص 🕋", callback_data="xn38 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الزمر 🕋", callback_data="xn39 " + str(m.from_user.id))],
        [InlineKeyboardButton("غافر 🕋", callback_data="xn40 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فصلت 🕋", callback_data="xn41 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الشورئ 🕋", callback_data="xn42 " + str(m.from_user.id))],
        [InlineKeyboardButton("الزخرف 🕋", callback_data="xn43 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الدخان 🕋", callback_data="xn44 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجاثيه 🕋", callback_data="xn45 " + str(m.from_user.id))],
        [InlineKeyboardButton("الاحقاف 🕋", callback_data="xn46 " + str(m.from_user.id))] +
        [InlineKeyboardButton("محمد 🕋", callback_data="xn47 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفتح 🕋", callback_data="xn48 " + str(m.from_user.id))],
        [InlineKeyboardButton("الحجرات 🕋", callback_data="xn49 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ق 🕋", callback_data="xn50 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الذاريات 🕋", callback_data="xn51 " + str(m.from_user.id))],

        [InlineKeyboardButton("➡️ التالي", callback_data="naser2 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اختر سوره للقارئ ناصر القطامي\n√", reply_markup=keyboard, disable_web_page_preview=True)


@Client.on_callback_query(filters.regex("^naser2 (\\d+)$"))
async def naser2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("الطور 🕋", callback_data="xn52 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النجم 🕋", callback_data="xn53 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القمر 🕋", callback_data="xn54 " + str(m.from_user.id))],
        [InlineKeyboardButton("الرحمن 🕋", callback_data="xn55 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الواقعه 🕋", callback_data="xn56 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحديد 🕋", callback_data="xn57 " + str(m.from_user.id))],
        [InlineKeyboardButton("المجادلة 🕋", callback_data="xn58 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحشر 🕋", callback_data="xn59 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الممتحنة 🕋", callback_data="xn60 " + str(m.from_user.id))],
        [InlineKeyboardButton("الصف 🕋", callback_data="xn61 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجمعة 🕋", callback_data="xn62 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المنافقون 🕋", callback_data="xn63 " + str(m.from_user.id))],
        [InlineKeyboardButton("التغابن 🕋", callback_data="xn64 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الطلاق 🕋", callback_data="xn65 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التحريم 🕋", callback_data="xn66 " + str(m.from_user.id))],
        [InlineKeyboardButton("الملك 🕋", callback_data="xn67 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القلم 🕋", callback_data="xn68 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحاقة 🕋", callback_data="xn69 " + str(m.from_user.id))],
        [InlineKeyboardButton("المعارج 🕋", callback_data="xn70 " + str(m.from_user.id))] +
        [InlineKeyboardButton("نوح 🕋", callback_data="xn71 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجن 🕋", callback_data="xn72 " + str(m.from_user.id))],
        [InlineKeyboardButton("المزمل 🕋", callback_data="xn73 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المدثر 🕋", callback_data="xn74 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القيامة 🕋", callback_data="xn75 " + str(m.from_user.id))],
        [InlineKeyboardButton("الانسان 🕋", callback_data="xn76 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المرسلات 🕋", callback_data="xn77 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النبأ 🕋", callback_data="xn78 " + str(m.from_user.id))],
        [InlineKeyboardButton("النازعات 🕋", callback_data="xn79 " + str(m.from_user.id))] +
        [InlineKeyboardButton("عبس 🕋", callback_data="xn80 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التكوير 🕋", callback_data="xn81 " + str(m.from_user.id))],
        [InlineKeyboardButton("الانفطار 🕋", callback_data="xn82 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المطففين 🕋", callback_data="xn83 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الانشقاق 🕋", callback_data="xn84 " + str(m.from_user.id))],
        [InlineKeyboardButton("البروج 🕋", callback_data="xn85 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الطارق 🕋", callback_data="xn86 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاعلي 🕋", callback_data="xn87 " + str(m.from_user.id))],
        [InlineKeyboardButton("الغاشية 🕋", callback_data="xn88 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفجر 🕋", callback_data="xn89 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البلد 🕋", callback_data="xn90 " + str(m.from_user.id))],
        [InlineKeyboardButton("الشمس 🕋", callback_data="xn91 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الليل 🕋", callback_data="xn92 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الضحئ 🕋", callback_data="xn93 " + str(m.from_user.id))],
        [InlineKeyboardButton("الشرح 🕋", callback_data="xn94 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التين 🕋", callback_data="xn95 " + str(m.from_user.id))] +
        [InlineKeyboardButton("العلق 🕋", callback_data="xn96 " + str(m.from_user.id))],
        [InlineKeyboardButton("القدر 🕋", callback_data="xn97 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البينة 🕋", callback_data="xn98 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الزلزلة 🕋", callback_data="xn99 " + str(m.from_user.id))],
        [InlineKeyboardButton("العاديات 🕋", callback_data="xn100 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القارعة 🕋", callback_data="xn101 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التكاثر 🕋", callback_data="xn102 " + str(m.from_user.id))],
        [InlineKeyboardButton("العصر 🕋", callback_data="xn103 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الهمزة 🕋", callback_data="xn104 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفيل 🕋", callback_data="xn105 " + str(m.from_user.id))],
        [InlineKeyboardButton("قريش 🕋", callback_data="xn106 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الماعون 🕋", callback_data="xn107 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الكوثر 🕋", callback_data="xn108 " + str(m.from_user.id))],
        [InlineKeyboardButton("الكافرون 🕋", callback_data="xn109 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النصر 🕋", callback_data="xn110 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المسد 🕋", callback_data="xn111 " + str(m.from_user.id))],
        [InlineKeyboardButton("الاخلاص 🕋", callback_data="xn112 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفلق 🕋", callback_data="xn113 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الناس 🕋", callback_data="xn114 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="naser " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اختر سوره للقارئ ناصر القطامي\n√", reply_markup=keyboard, disable_web_page_preview=True)


@Client.on_callback_query(filters.regex("^xn1 (\\d+)$"))
async def xn1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/762", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn2 (\\d+)$"))
async def xn2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/763", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn3 (\\d+)$"))
async def xn3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/764", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn4 (\\d+)$"))
async def xn4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/765", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn5 (\\d+)$"))
async def xn5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/766", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn6 (\\d+)$"))
async def xn6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/767", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn7 (\\d+)$"))
async def xn7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/768", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn8 (\\d+)$"))
async def xn8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/769", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn9 (\\d+)$"))
async def xn9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/770", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn10 (\\d+)$"))
async def xn10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/771", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn11 (\\d+)$"))
async def xn11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/772", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn12 (\\d+)$"))
async def xn12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/773", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn13 (\\d+)$"))
async def xn13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/774", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn14 (\\d+)$"))
async def xn14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/775", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn15 (\\d+)$"))
async def xn15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/776", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn16 (\\d+)$"))
async def xn16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/777", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn17 (\\d+)$"))
async def xn17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/778", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn18 (\\d+)$"))
async def xn18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/779", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn19 (\\d+)$"))
async def xn19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/780", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn20 (\\d+)$"))
async def xn20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/781", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn21 (\\d+)$"))
async def xn21(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/782", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn22 (\\d+)$"))
async def xn22(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/783", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn23 (\\d+)$"))
async def xn23(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/784", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn24 (\\d+)$"))
async def xn24(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/785", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn25 (\\d+)$"))
async def xn25(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/786", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn26 (\\d+)$"))
async def xn26(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/787", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn27 (\\d+)$"))
async def xn27(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/788", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn28 (\\d+)$"))
async def xn28(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/789", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn29 (\\d+)$"))
async def xn29(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/790", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn30 (\\d+)$"))
async def xn30(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/791", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn31 (\\d+)$"))
async def xn31(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/792", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn32 (\\d+)$"))
async def xn32(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/793", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn33 (\\d+)$"))
async def xn33(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/794", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn34 (\\d+)$"))
async def xn34(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/795", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn35 (\\d+)$"))
async def xn35(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/796", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn36 (\\d+)$"))
async def xn36(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/797", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn37 (\\d+)$"))
async def xn37(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/798", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn38 (\\d+)$"))
async def xn38(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/799", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn39 (\\d+)$"))
async def xn39(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/800", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn40 (\\d+)$"))
async def xn40(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/801", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn41 (\\d+)$"))
async def xn41(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/802", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn42 (\\d+)$"))
async def xn42(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/803", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn43 (\\d+)$"))
async def xn43(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/804", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn44 (\\d+)$"))
async def xn44(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/805", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn45 (\\d+)$"))
async def xn45(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/806", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn46 (\\d+)$"))
async def xn46(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/807", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn47 (\\d+)$"))
async def xn47(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/808", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn48 (\\d+)$"))
async def xn48(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/809", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn49 (\\d+)$"))
async def xn49(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/810", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn50 (\\d+)$"))
async def xn50(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/811", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn51 (\\d+)$"))
async def xn51(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/812", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn52 (\\d+)$"))
async def xn52(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/813", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn53 (\\d+)$"))
async def xn53(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/814", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn54 (\\d+)$"))
async def xn54(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/815", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn55 (\\d+)$"))
async def xn55(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/816", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn56 (\\d+)$"))
async def xn56(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/817", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn57 (\\d+)$"))
async def xn57(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/818", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn58 (\\d+)$"))
async def xn58(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/819", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn59 (\\d+)$"))
async def xn59(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/820", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn60 (\\d+)$"))
async def xn60(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/821", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn61 (\\d+)$"))
async def xn61(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/822", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn62 (\\d+)$"))
async def xn62(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/823", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn63 (\\d+)$"))
async def xn63(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/824", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn64 (\\d+)$"))
async def xn64(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/825", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn65 (\\d+)$"))
async def xn65(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/826", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn66 (\\d+)$"))
async def xn66(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/827", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn67 (\\d+)$"))
async def xn67(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/828", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn68 (\\d+)$"))
async def xn68(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/829", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn69 (\\d+)$"))
async def xn69(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/830", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn70 (\\d+)$"))
async def xn70(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/831", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn71 (\\d+)$"))
async def xn71(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/832", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn72 (\\d+)$"))
async def xn72(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/833", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn73 (\\d+)$"))
async def xn73(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/834", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn74 (\\d+)$"))
async def xn74(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/835", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn75 (\\d+)$"))
async def xn75(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/836", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn76 (\\d+)$"))
async def xn76(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/837", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn77 (\\d+)$"))
async def xn77(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/838", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn78 (\\d+)$"))
async def xn78(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/839", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn79 (\\d+)$"))
async def xn79(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/840", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn80 (\\d+)$"))
async def xn80(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/841", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn81 (\\d+)$"))
async def xn81(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/842", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn82 (\\d+)$"))
async def xn82(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/843", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn83 (\\d+)$"))
async def xn83(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/844", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn84 (\\d+)$"))
async def xn84(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/845", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn85 (\\d+)$"))
async def xn85(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/846", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn86 (\\d+)$"))
async def xn86(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/847", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn87 (\\d+)$"))
async def xn87(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/848", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn88 (\\d+)$"))
async def xn88(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/849", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn89 (\\d+)$"))
async def xn89(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/850", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn90 (\\d+)$"))
async def xn90(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/851", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn91 (\\d+)$"))
async def xn91(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/852", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn92 (\\d+)$"))
async def xn92(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/853", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn93 (\\d+)$"))
async def xn93(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/854", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn94 (\\d+)$"))
async def xn94(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/855", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn95 (\\d+)$"))
async def xn95(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/856", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn96 (\\d+)$"))
async def xn96(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/857", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn97 (\\d+)$"))
async def xn97(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/858", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn98 (\\d+)$"))
async def xn98(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/859", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn99 (\\d+)$"))
async def xn99(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/860", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn100 (\\d+)$"))
async def xn100(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/861", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn101 (\\d+)$"))
async def xn101(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/862", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn102 (\\d+)$"))
async def xn102(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/863", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn103 (\\d+)$"))
async def xn103(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/864", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn104 (\\d+)$"))
async def xn104(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/865", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn105 (\\d+)$"))
async def xn105(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/866", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn106 (\\d+)$"))
async def xn106(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/867", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn107 (\\d+)$"))
async def xn107(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/868", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn108 (\\d+)$"))
async def xn108(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/869", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn109 (\\d+)$"))
async def xn109(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/870", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn110 (\\d+)$"))
async def xn110(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/871", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn111 (\\d+)$"))
async def xn111(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/872", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn112 (\\d+)$"))
async def xn112(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/873", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn113 (\\d+)$"))
async def xn113(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/874", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn114 (\\d+)$"))
async def xn114(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/875", reply_to_message_id=mid)


########################################################################################################################
########################################################################################################################


@Client.on_callback_query(filters.regex("^eslam (\\d+)$"))
async def eslam(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("الرعد 🕋", callback_data="xes13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاسراء 🕋", callback_data="xes17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الكهف 🕋", callback_data="xes18 " + str(m.from_user.id))],
        [InlineKeyboardButton("الشعراء 🕋", callback_data="xes26 " + str(m.from_user.id))] +
        [InlineKeyboardButton("لقمان 🕋", callback_data="xes31 " + str(m.from_user.id))] +
        [InlineKeyboardButton("السجدة 🕋", callback_data="xes32 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فصلت 🕋", callback_data="xes41 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الشورئ 🕋", callback_data="xes42 " + str(m.from_user.id))],
        [InlineKeyboardButton("الدخان 🕋", callback_data="xes44 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ق 🕋", callback_data="xes50 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النجم 🕋", callback_data="xes53 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القمر 🕋", callback_data="xes54 " + str(m.from_user.id))],
        [InlineKeyboardButton("الرحمن 🕋", callback_data="xes55 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الواقعه 🕋", callback_data="xes56 " + str(m.from_user.id))] +

        [InlineKeyboardButton("➡️ التالي", callback_data="eslam2 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اختر سوره للقارئ اسلام صبحي\n√", reply_markup=keyboard, disable_web_page_preview=True)


@Client.on_callback_query(filters.regex("^eslam2 (\\d+)$"))
async def eslam2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("الحشر 🕋", callback_data="xes59 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التغابن 🕋", callback_data="xes64 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التحريم 🕋", callback_data="xes66 " + str(m.from_user.id))],
        [InlineKeyboardButton("الملك 🕋", callback_data="xes67 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القلم 🕋", callback_data="xes68 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المعارج 🕋", callback_data="xes70 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجن 🕋", callback_data="xes72 " + str(m.from_user.id))],
        [InlineKeyboardButton("الانسان 🕋", callback_data="xes76 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النازعات 🕋", callback_data="xes79 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البروج 🕋", callback_data="xes85 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الغاشية 🕋", callback_data="xes88 " + str(m.from_user.id))] +


        [InlineKeyboardButton("رجوع ⬅️", callback_data="eslam " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اختر سوره للقارئ اسلام صبحي\n√", reply_markup=keyboard, disable_web_page_preview=True)


@Client.on_callback_query(filters.regex("^xes13 (\\d+)$"))
async def xes13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/241", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes17 (\\d+)$"))
async def xes17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/243", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes18 (\\d+)$"))
async def xes18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/245", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes26 (\\d+)$"))
async def xes26(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/247", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes31 (\\d+)$"))
async def xes31(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/249", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes32 (\\d+)$"))
async def xes32(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/250", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes41 (\\d+)$"))
async def xes41(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/252", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes42 (\\d+)$"))
async def xes42(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/254", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes44 (\\d+)$"))
async def xes44(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/255", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes50 (\\d+)$"))
async def xes50(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/256", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes53 (\\d+)$"))
async def xes53(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/257", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes54 (\\d+)$"))
async def xes54(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/259", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes55 (\\d+)$"))
async def xes55(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/260", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes56 (\\d+)$"))
async def xes56(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/261", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes59 (\\d+)$"))
async def xes59(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/262", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes64 (\\d+)$"))
async def xes64(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/263", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes66 (\\d+)$"))
async def xes66(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/264", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes67 (\\d+)$"))
async def xes67(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/265", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes68 (\\d+)$"))
async def xes68(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/266", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes70 (\\d+)$"))
async def xes70(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/267", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes72 (\\d+)$"))
async def xes72(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/268", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes76 (\\d+)$"))
async def xes76(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/269", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes79 (\\d+)$"))
async def xes79(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/270", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes85 (\\d+)$"))
async def xes85(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/271", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes88 (\\d+)$"))
async def xes88(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/272", reply_to_message_id=mid)


############################################################################################
############################################################################################


@Client.on_callback_query(filters.regex("^abdelbaset (\\d+)$"))
async def abdelbaset(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("الفاتحه 🕋", callback_data="xabd1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البقرة 🕋", callback_data="xabd2 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ال عمران 🕋", callback_data="xabd3 " + str(m.from_user.id))],
        [InlineKeyboardButton("النساء 🕋", callback_data="xabd4 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المائدة 🕋", callback_data="xabd5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الانعام 🕋", callback_data="xabd6 " + str(m.from_user.id))],
        [InlineKeyboardButton("الأعراف 🕋", callback_data="xabd7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الأنفال 🕋", callback_data="xabd8 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التوبة 🕋", callback_data="xabd9 " + str(m.from_user.id))],
        [InlineKeyboardButton("يونس 🕋", callback_data="xabd10 " + str(m.from_user.id))] +
        [InlineKeyboardButton("هود 🕋", callback_data="xabd11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يوسف 🕋", callback_data="xabd12 " + str(m.from_user.id))],
        [InlineKeyboardButton("الرعد 🕋", callback_data="xabd13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("أبراهيم 🕋", callback_data="xabd14 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحجر 🕋", callback_data="xabd15 " + str(m.from_user.id))],
        [InlineKeyboardButton("النحل 🕋", callback_data="xabd16 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاسراء 🕋", callback_data="xabd17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الكهف 🕋", callback_data="xabd18 " + str(m.from_user.id))],
        [InlineKeyboardButton("مريم 🕋", callback_data="xabd19 " + str(m.from_user.id))] +
        [InlineKeyboardButton("طه 🕋", callback_data="xabd20 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الأنبياء 🕋", callback_data="xabd21 " + str(m.from_user.id))],
        [InlineKeyboardButton("الحج 🕋", callback_data="xabd22 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المؤمنون 🕋", callback_data="xabd23 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النور 🕋", callback_data="xabd24 " + str(m.from_user.id))],
        [InlineKeyboardButton("الفرقان 🕋", callback_data="xabd25 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الشعراء 🕋", callback_data="xabd26 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النحل 🕋", callback_data="xabd27 " + str(m.from_user.id))],
        [InlineKeyboardButton("القصص 🕋", callback_data="xabd28 " + str(m.from_user.id))] +
        [InlineKeyboardButton("العنكبوت 🕋", callback_data="xabd29 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الروم 🕋", callback_data="xabd30 " + str(m.from_user.id))],
        [InlineKeyboardButton("لقمان 🕋", callback_data="xabd31 " + str(m.from_user.id))] +
        [InlineKeyboardButton("السجدة 🕋", callback_data="xabd32 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاحزاب 🕋", callback_data="xabd33 " + str(m.from_user.id))],
        [InlineKeyboardButton("سبأ 🕋", callback_data="xabd34 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فاطر 🕋", callback_data="xabd35 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يس 🕋", callback_data="xabd36 " + str(m.from_user.id))],
        [InlineKeyboardButton("الصافات 🕋", callback_data="xabd37 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ص 🕋", callback_data="xabd38 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الزمر 🕋", callback_data="xabd39 " + str(m.from_user.id))],
        [InlineKeyboardButton("غافر 🕋", callback_data="xabd40 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فصلت 🕋", callback_data="xabd41 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الشورئ 🕋", callback_data="xabd42 " + str(m.from_user.id))],
        [InlineKeyboardButton("الزخرف 🕋", callback_data="xabd43 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الدخان 🕋", callback_data="xabd44 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجاثيه 🕋", callback_data="xabd45 " + str(m.from_user.id))],
        [InlineKeyboardButton("الاحقاف 🕋", callback_data="xabd46 " + str(m.from_user.id))] +
        [InlineKeyboardButton("محمد 🕋", callback_data="xabd47 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفتح 🕋", callback_data="xabd48 " + str(m.from_user.id))],
        [InlineKeyboardButton("الحجرات 🕋", callback_data="xabd49 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ق 🕋", callback_data="xabd50 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الذاريات 🕋", callback_data="xabd51 " + str(m.from_user.id))],

        [InlineKeyboardButton("➡️ التالي", callback_data="abdelbaset2 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اختر سوره للقارئ عبدالباسط عبدالصمد\n√", reply_markup=keyboard,
                              disable_web_page_preview=True)


@Client.on_callback_query(filters.regex("^abdelbaset2 (\\d+)$"))
async def abdelbaset2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("الطور 🕋", callback_data="xabd52 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النجم 🕋", callback_data="xabd53 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القمر 🕋", callback_data="xabd54 " + str(m.from_user.id))],
        [InlineKeyboardButton("الرحمن 🕋", callback_data="xabd55 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الواقعه 🕋", callback_data="xabd56 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحديد 🕋", callback_data="xabd57 " + str(m.from_user.id))],
        [InlineKeyboardButton("المجادلة 🕋", callback_data="xabd58 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحشر 🕋", callback_data="xabd59 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الممتحنة 🕋", callback_data="xabd60 " + str(m.from_user.id))],
        [InlineKeyboardButton("الصف 🕋", callback_data="xabd61 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجمعة 🕋", callback_data="xabd62 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المنافقون 🕋", callback_data="xabd63 " + str(m.from_user.id))],
        [InlineKeyboardButton("التغابن 🕋", callback_data="xabd64 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الطلاق 🕋", callback_data="xabd65 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التحريم 🕋", callback_data="xabd66 " + str(m.from_user.id))],
        [InlineKeyboardButton("الملك 🕋", callback_data="xabd67 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القلم 🕋", callback_data="xabd68 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحاقة 🕋", callback_data="xabd69 " + str(m.from_user.id))],
        [InlineKeyboardButton("المعارج 🕋", callback_data="xabd70 " + str(m.from_user.id))] +
        [InlineKeyboardButton("نوح 🕋", callback_data="xabd71 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجن 🕋", callback_data="xabd72 " + str(m.from_user.id))],
        [InlineKeyboardButton("المزمل 🕋", callback_data="xabd73 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المدثر 🕋", callback_data="xabd74 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القيامة 🕋", callback_data="xabd75 " + str(m.from_user.id))],
        [InlineKeyboardButton("الانسان 🕋", callback_data="xabd76 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المرسلات 🕋", callback_data="xabd77 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النبأ 🕋", callback_data="xabd78 " + str(m.from_user.id))],
        [InlineKeyboardButton("النازعات 🕋", callback_data="xabd79 " + str(m.from_user.id))] +
        [InlineKeyboardButton("عبس 🕋", callback_data="xabd80 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التكوير 🕋", callback_data="xabd81 " + str(m.from_user.id))],
        [InlineKeyboardButton("الانفطار 🕋", callback_data="xabd82 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المطففين 🕋", callback_data="xabd83 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الانشقاق 🕋", callback_data="xabd84 " + str(m.from_user.id))],
        [InlineKeyboardButton("البروج 🕋", callback_data="xabd85 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الطارق 🕋", callback_data="xabd86 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاعلي 🕋", callback_data="xabd87 " + str(m.from_user.id))],
        [InlineKeyboardButton("الغاشية 🕋", callback_data="xabd88 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفجر 🕋", callback_data="xabd89 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البلد 🕋", callback_data="xabd90 " + str(m.from_user.id))],
        [InlineKeyboardButton("الشمس 🕋", callback_data="xabd91 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الليل 🕋", callback_data="xabd92 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الضحئ 🕋", callback_data="xabd93 " + str(m.from_user.id))],
        [InlineKeyboardButton("الشرح 🕋", callback_data="xabd94 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التين 🕋", callback_data="xabd95 " + str(m.from_user.id))] +
        [InlineKeyboardButton("العلق 🕋", callback_data="xabd96 " + str(m.from_user.id))],
        [InlineKeyboardButton("القدر 🕋", callback_data="xabd97 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البينة 🕋", callback_data="xabd98 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الزلزلة 🕋", callback_data="xabd99 " + str(m.from_user.id))],
        [InlineKeyboardButton("العاديات 🕋", callback_data="xabd100 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القارعة 🕋", callback_data="xabd101 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التكاثر 🕋", callback_data="xabd102 " + str(m.from_user.id))],
        [InlineKeyboardButton("العصر 🕋", callback_data="xabd103 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الهمزة 🕋", callback_data="xabd104 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفيل 🕋", callback_data="xabd105 " + str(m.from_user.id))],
        [InlineKeyboardButton("قريش 🕋", callback_data="xabd106 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الماعون 🕋", callback_data="xabd107 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الكوثر 🕋", callback_data="xabd108 " + str(m.from_user.id))],
        [InlineKeyboardButton("الكافرون 🕋", callback_data="xabd109 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النصر 🕋", callback_data="xabd110 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المسد 🕋", callback_data="xabd111 " + str(m.from_user.id))],
        [InlineKeyboardButton("الاخلاص 🕋", callback_data="xabd112 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفلق 🕋", callback_data="xabd113 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الناس 🕋", callback_data="xabd114 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="abdelbaset " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اختر سوره للقارئ عبدالباسط عبدالصمد\n√", reply_markup=keyboard,
                              disable_web_page_preview=True)


@Client.on_callback_query(filters.regex("^xabd1 (\\d+)$"))
async def xabd1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/876", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd2 (\\d+)$"))
async def xabd2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/877", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd3 (\\d+)$"))
async def xabd3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/878", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd4 (\\d+)$"))
async def xabd4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/879", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd5 (\\d+)$"))
async def xabd5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/880", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd6 (\\d+)$"))
async def xabd6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/881", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd7 (\\d+)$"))
async def xabd7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/882", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd8 (\\d+)$"))
async def xabd8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/883", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd9 (\\d+)$"))
async def xabd9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/884", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd10 (\\d+)$"))
async def xabd10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/885", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd11 (\\d+)$"))
async def xabd11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/886", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd12 (\\d+)$"))
async def xabd12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/887", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd13 (\\d+)$"))
async def xabd13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/888", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd14 (\\d+)$"))
async def xabd14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/889", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd15 (\\d+)$"))
async def xabd15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/890", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd16 (\\d+)$"))
async def xabd16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/891", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd17 (\\d+)$"))
async def xabd17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/892", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd18 (\\d+)$"))
async def xabd18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/893", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd19 (\\d+)$"))
async def xabd19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/894", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd20 (\\d+)$"))
async def xabd20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/895", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd21 (\\d+)$"))
async def xabd21(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/896", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd22 (\\d+)$"))
async def xabd22(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/897", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd23 (\\d+)$"))
async def xabd23(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/898", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd24 (\\d+)$"))
async def xabd24(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/899", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd25 (\\d+)$"))
async def xabd25(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/900", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd26 (\\d+)$"))
async def xabd26(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/901", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd27 (\\d+)$"))
async def xabd27(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/902", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd28 (\\d+)$"))
async def xabd28(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/903", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd29 (\\d+)$"))
async def xabd29(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/904", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd30 (\\d+)$"))
async def xabd30(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/905", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd31 (\\d+)$"))
async def xabd31(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/906", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd32 (\\d+)$"))
async def xabd32(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/907", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd33 (\\d+)$"))
async def xabd33(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/908", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd34 (\\d+)$"))
async def xabd34(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/909", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd35 (\\d+)$"))
async def xabd35(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/910", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd36 (\\d+)$"))
async def xabd36(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/911", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd37 (\\d+)$"))
async def xabd37(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/912", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd38 (\\d+)$"))
async def xabd38(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/913", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd39 (\\d+)$"))
async def xabd39(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/914", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd40 (\\d+)$"))
async def xabd40(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/915", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd41 (\\d+)$"))
async def xabd41(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/916", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd42 (\\d+)$"))
async def xabd42(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/917", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd43 (\\d+)$"))
async def xabd43(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/918", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd44 (\\d+)$"))
async def xabd44(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/919", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd45 (\\d+)$"))
async def xabd45(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/920", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd46 (\\d+)$"))
async def xabd46(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/921", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd47 (\\d+)$"))
async def xabd47(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/922", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd48 (\\d+)$"))
async def xabd48(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/923", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd49 (\\d+)$"))
async def xabd49(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/924", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd50 (\\d+)$"))
async def xabd50(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/925", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd51 (\\d+)$"))
async def xabd51(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/926", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd52 (\\d+)$"))
async def xabd52(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/927", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd53 (\\d+)$"))
async def xabd53(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/928", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd54 (\\d+)$"))
async def xabd54(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/929", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd55 (\\d+)$"))
async def xabd55(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/930", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd56 (\\d+)$"))
async def xabd56(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/931", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd57 (\\d+)$"))
async def xabd57(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/932", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd58 (\\d+)$"))
async def xabd58(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/933", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd59 (\\d+)$"))
async def xabd59(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/934", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd60 (\\d+)$"))
async def xabd60(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/935", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd61 (\\d+)$"))
async def xabd61(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/936", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd62 (\\d+)$"))
async def xabd62(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/937", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd63 (\\d+)$"))
async def xabd63(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/938", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd64 (\\d+)$"))
async def xabd64(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/939", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd65 (\\d+)$"))
async def xabd65(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/940", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd66 (\\d+)$"))
async def xabd66(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/941", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd67 (\\d+)$"))
async def xabd67(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/942", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd68 (\\d+)$"))
async def xabd68(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/943", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd69 (\\d+)$"))
async def xabd69(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/944", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd70 (\\d+)$"))
async def xabd70(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/945", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd71 (\\d+)$"))
async def xabd71(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/946", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd72 (\\d+)$"))
async def xabd72(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/947", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd73 (\\d+)$"))
async def xabd73(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/948", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd74 (\\d+)$"))
async def xabd74(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/949", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd75 (\\d+)$"))
async def xabd75(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/950", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd76 (\\d+)$"))
async def xabd76(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/951", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd77 (\\d+)$"))
async def xabd77(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/952", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd78 (\\d+)$"))
async def xabd78(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/953", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd79 (\\d+)$"))
async def xabd79(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/954", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd80 (\\d+)$"))
async def xabd80(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/955", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd81 (\\d+)$"))
async def xabd81(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/956", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd82 (\\d+)$"))
async def xabd82(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/957", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd83 (\\d+)$"))
async def xabd83(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/958", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd84 (\\d+)$"))
async def xabd84(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/959", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd85 (\\d+)$"))
async def xabd85(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/560", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd86 (\\d+)$"))
async def xabd86(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/961", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd87 (\\d+)$"))
async def xabd87(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/962", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd88 (\\d+)$"))
async def xabd88(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/963", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd89 (\\d+)$"))
async def xabd89(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/964", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd90 (\\d+)$"))
async def xabd90(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/965", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd91 (\\d+)$"))
async def xabd91(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/966", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd92 (\\d+)$"))
async def xabd92(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/967", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd93 (\\d+)$"))
async def xabd93(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/968", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd94 (\\d+)$"))
async def xabd94(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/969", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd95 (\\d+)$"))
async def xabd95(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/970", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd96 (\\d+)$"))
async def xabd96(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/971", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd97 (\\d+)$"))
async def xabd97(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/972", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd98 (\\d+)$"))
async def xabd98(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/973", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd99 (\\d+)$"))
async def xabd99(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/974", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd100 (\\d+)$"))
async def xabd100(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/975", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd101 (\\d+)$"))
async def xabd101(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/976", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd102 (\\d+)$"))
async def xabd102(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/977", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd103 (\\d+)$"))
async def xabd103(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/978", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd104 (\\d+)$"))
async def xabd104(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/979", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd105 (\\d+)$"))
async def xabd105(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/980", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd106 (\\d+)$"))
async def xabd106(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/981", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd107 (\\d+)$"))
async def xabd107(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/982", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd108 (\\d+)$"))
async def xabd108(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/983", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd109 (\\d+)$"))
async def xabd109(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/984", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd110 (\\d+)$"))
async def xabd110(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/985", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd111 (\\d+)$"))
async def xabd111(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/986", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd112 (\\d+)$"))
async def xabd112(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/987", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd113 (\\d+)$"))
async def xabd113(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/988", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd114 (\\d+)$"))
async def xabd114(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/989", reply_to_message_id=mid)


########################################################################################################################
########################################################################################################################


@Client.on_callback_query(filters.regex("^eldosary (\\d+)$"))
async def eldosary(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("الفاتحه 🕋", callback_data="xdos1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البقرة 🕋", callback_data="xdos2 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ال عمران 🕋", callback_data="xdos3 " + str(m.from_user.id))],
        [InlineKeyboardButton("النساء 🕋", callback_data="xdos4 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المائدة 🕋", callback_data="xdos5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الانعام 🕋", callback_data="xdos6 " + str(m.from_user.id))],
        [InlineKeyboardButton("الأعراف 🕋", callback_data="xdos7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الأنفال 🕋", callback_data="xdos8 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التوبة 🕋", callback_data="xdos9 " + str(m.from_user.id))],
        [InlineKeyboardButton("يونس 🕋", callback_data="xdos10 " + str(m.from_user.id))] +
        [InlineKeyboardButton("هود 🕋", callback_data="xdos11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يوسف 🕋", callback_data="xdos12 " + str(m.from_user.id))],
        [InlineKeyboardButton("الرعد 🕋", callback_data="xdos13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("أبراهيم 🕋", callback_data="xdos14 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحجر 🕋", callback_data="xdos15 " + str(m.from_user.id))],
        [InlineKeyboardButton("النحل 🕋", callback_data="xdos16 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاسراء 🕋", callback_data="xdos17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الكهف 🕋", callback_data="xdos18 " + str(m.from_user.id))],
        [InlineKeyboardButton("مريم 🕋", callback_data="xdos19 " + str(m.from_user.id))] +
        [InlineKeyboardButton("طه 🕋", callback_data="xdos20 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الأنبياء 🕋", callback_data="xdos21 " + str(m.from_user.id))],
        [InlineKeyboardButton("الحج 🕋", callback_data="xdos22 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المؤمنون 🕋", callback_data="xdos23 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النور 🕋", callback_data="xdos24 " + str(m.from_user.id))],
        [InlineKeyboardButton("الفرقان 🕋", callback_data="xdos25 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الشعراء 🕋", callback_data="xdos26 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النحل 🕋", callback_data="xdos27 " + str(m.from_user.id))],
        [InlineKeyboardButton("القصص 🕋", callback_data="xdos28 " + str(m.from_user.id))] +
        [InlineKeyboardButton("العنكبوت 🕋", callback_data="xdos29 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الروم 🕋", callback_data="xdos30 " + str(m.from_user.id))],
        [InlineKeyboardButton("لقمان 🕋", callback_data="xdos31 " + str(m.from_user.id))] +
        [InlineKeyboardButton("السجدة 🕋", callback_data="xdos32 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاحزاب 🕋", callback_data="xdos33 " + str(m.from_user.id))],
        [InlineKeyboardButton("سبأ 🕋", callback_data="xdos34 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فاطر 🕋", callback_data="xdos35 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يس 🕋", callback_data="xdos36 " + str(m.from_user.id))],
        [InlineKeyboardButton("الصافات 🕋", callback_data="xdos37 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ص 🕋", callback_data="xdos38 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الزمر 🕋", callback_data="xdos39 " + str(m.from_user.id))],
        [InlineKeyboardButton("غافر 🕋", callback_data="xdos40 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فصلت 🕋", callback_data="xdos41 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الشورئ 🕋", callback_data="xdos42 " + str(m.from_user.id))],
        [InlineKeyboardButton("الزخرف 🕋", callback_data="xdos43 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الدخان 🕋", callback_data="xdos44 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجاثيه 🕋", callback_data="xdos45 " + str(m.from_user.id))],
        [InlineKeyboardButton("الاحقاف 🕋", callback_data="xdos46 " + str(m.from_user.id))] +
        [InlineKeyboardButton("محمد 🕋", callback_data="xdos47 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفتح 🕋", callback_data="xdos48 " + str(m.from_user.id))],
        [InlineKeyboardButton("الحجرات 🕋", callback_data="xdos49 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ق 🕋", callback_data="xdos50 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الذاريات 🕋", callback_data="xdos51 " + str(m.from_user.id))],

        [InlineKeyboardButton("➡️ التالي", callback_data="eldosary2 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اختر سوره للقارئ ياسر الدوسري\n√", reply_markup=keyboard, disable_web_page_preview=True)


@Client.on_callback_query(filters.regex("^eldosary2 (\\d+)$"))
async def eldosary2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("الطور 🕋", callback_data="xdos52 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النجم 🕋", callback_data="xdos53 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القمر 🕋", callback_data="xdos54 " + str(m.from_user.id))],
        [InlineKeyboardButton("الرحمن 🕋", callback_data="xdos55 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الواقعه 🕋", callback_data="xdos56 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحديد 🕋", callback_data="xdos57 " + str(m.from_user.id))],
        [InlineKeyboardButton("المجادلة 🕋", callback_data="xdos58 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحشر 🕋", callback_data="xdos59 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الممتحنة 🕋", callback_data="xdos60 " + str(m.from_user.id))],
        [InlineKeyboardButton("الصف 🕋", callback_data="xdos61 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجمعة 🕋", callback_data="xdos62 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المنافقون 🕋", callback_data="xdos63 " + str(m.from_user.id))],
        [InlineKeyboardButton("التغابن 🕋", callback_data="xdos64 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الطلاق 🕋", callback_data="xdos65 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التحريم 🕋", callback_data="xdos66 " + str(m.from_user.id))],
        [InlineKeyboardButton("الملك 🕋", callback_data="xdos67 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القلم 🕋", callback_data="xdos68 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحاقة 🕋", callback_data="xdos69 " + str(m.from_user.id))],
        [InlineKeyboardButton("المعارج 🕋", callback_data="xdos70 " + str(m.from_user.id))] +
        [InlineKeyboardButton("نوح 🕋", callback_data="xdos71 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجن 🕋", callback_data="xdos72 " + str(m.from_user.id))],
        [InlineKeyboardButton("المزمل 🕋", callback_data="xdos73 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المدثر 🕋", callback_data="xdos74 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القيامة 🕋", callback_data="xdos75 " + str(m.from_user.id))],
        [InlineKeyboardButton("الانسان 🕋", callback_data="xdos76 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المرسلات 🕋", callback_data="xdos77 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النبأ 🕋", callback_data="xdos78 " + str(m.from_user.id))],
        [InlineKeyboardButton("النازعات 🕋", callback_data="xdos79 " + str(m.from_user.id))] +
        [InlineKeyboardButton("عبس 🕋", callback_data="xdos80 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التكوير 🕋", callback_data="xdos81 " + str(m.from_user.id))],
        [InlineKeyboardButton("الانفطار 🕋", callback_data="xdos82 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المطففين 🕋", callback_data="xdos83 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الانشقاق 🕋", callback_data="xdos84 " + str(m.from_user.id))],
        [InlineKeyboardButton("البروج 🕋", callback_data="xdos85 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الطارق 🕋", callback_data="xdos86 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاعلي 🕋", callback_data="xdos87 " + str(m.from_user.id))],
        [InlineKeyboardButton("الغاشية 🕋", callback_data="xdos88 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفجر 🕋", callback_data="xdos89 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البلد 🕋", callback_data="xdos90 " + str(m.from_user.id))],
        [InlineKeyboardButton("الشمس 🕋", callback_data="xdos91 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الليل 🕋", callback_data="xdos92 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الضحئ 🕋", callback_data="xdos93 " + str(m.from_user.id))],
        [InlineKeyboardButton("الشرح 🕋", callback_data="xdos94 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التين 🕋", callback_data="xdos95 " + str(m.from_user.id))] +
        [InlineKeyboardButton("العلق 🕋", callback_data="xdos96 " + str(m.from_user.id))],
        [InlineKeyboardButton("القدر 🕋", callback_data="xdos97 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البينة 🕋", callback_data="xdos98 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الزلزلة 🕋", callback_data="xdos99 " + str(m.from_user.id))],
        [InlineKeyboardButton("العاديات 🕋", callback_data="xdos100 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القارعة 🕋", callback_data="xdos101 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التكاثر 🕋", callback_data="xdos102 " + str(m.from_user.id))],
        [InlineKeyboardButton("العصر 🕋", callback_data="xdos103 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الهمزة 🕋", callback_data="xdos104 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفيل 🕋", callback_data="xdos105 " + str(m.from_user.id))],
        [InlineKeyboardButton("قريش 🕋", callback_data="xdos106 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الماعون 🕋", callback_data="xdos107 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الكوثر 🕋", callback_data="xdos108 " + str(m.from_user.id))],
        [InlineKeyboardButton("الكافرون 🕋", callback_data="xdos109 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النصر 🕋", callback_data="xdos110 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المسد 🕋", callback_data="xdos111 " + str(m.from_user.id))],
        [InlineKeyboardButton("الاخلاص 🕋", callback_data="xdos112 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفلق 🕋", callback_data="xdos113 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الناس 🕋", callback_data="xdos114 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="eldosary " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اختر سوره للقارئ ياسر الدوسري\n√", reply_markup=keyboard, disable_web_page_preview=True)


@Client.on_callback_query(filters.regex("^xdos1 (\\d+)$"))
async def xdos1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/992", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos2 (\\d+)$"))
async def xdos2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/993", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos3 (\\d+)$"))
async def xdos3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/994", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos4 (\\d+)$"))
async def xdos4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/995", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos5 (\\d+)$"))
async def xdos5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/996", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos6 (\\d+)$"))
async def xdos6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/997", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos7 (\\d+)$"))
async def xdos7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/998", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos8 (\\d+)$"))
async def xdos8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/999", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos9 (\\d+)$"))
async def xdos9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1000", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos10 (\\d+)$"))
async def xdos10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1001", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos11 (\\d+)$"))
async def xdos11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1002", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos12 (\\d+)$"))
async def xdos12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1003", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos13 (\\d+)$"))
async def xdos13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1004", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos14 (\\d+)$"))
async def xdos14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1005", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos15 (\\d+)$"))
async def xdos15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1006", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos16 (\\d+)$"))
async def xdos16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1007", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos17 (\\d+)$"))
async def xdos17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1008", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos18 (\\d+)$"))
async def xdos18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1009", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos19 (\\d+)$"))
async def xdos19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1010", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos20 (\\d+)$"))
async def xdos20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1011", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos21 (\\d+)$"))
async def xdos21(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1012", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos22 (\\d+)$"))
async def xdos22(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1013", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos23 (\\d+)$"))
async def xdos23(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1014", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos24 (\\d+)$"))
async def xdos24(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1015", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos25 (\\d+)$"))
async def xdos25(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1016", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos26 (\\d+)$"))
async def xdos26(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1017", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos27 (\\d+)$"))
async def xdos27(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1018", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos28 (\\d+)$"))
async def xdos28(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1019", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos29 (\\d+)$"))
async def xdos30(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1020", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos30 (\\d+)$"))
async def xdos31(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1021", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos31 (\\d+)$"))
async def xdos32(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1022", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos32 (\\d+)$"))
async def xdos33(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1023", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos33 (\\d+)$"))
async def xdos34(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1024", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos34 (\\d+)$"))
async def xdos35(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1025", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos35 (\\d+)$"))
async def xdos36(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1026", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos36 (\\d+)$"))
async def xdos37(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1027", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos37 (\\d+)$"))
async def xdos38(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1028", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos38 (\\d+)$"))
async def xdos39(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1029", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos39 (\\d+)$"))
async def xdos40(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1030", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos40 (\\d+)$"))
async def xdos41(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1031", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos41 (\\d+)$"))
async def xdos42(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1032", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos42 (\\d+)$"))
async def xdos43(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1033", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos43 (\\d+)$"))
async def xdos44(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1034", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos44 (\\d+)$"))
async def xdos45(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1035", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos45 (\\d+)$"))
async def xdos46(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1036", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos46 (\\d+)$"))
async def xdos47(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1037", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos47 (\\d+)$"))
async def xdos48(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1038", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos48 (\\d+)$"))
async def xdos49(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1039", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos49 (\\d+)$"))
async def xdos50(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1040", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos50 (\\d+)$"))
async def xdos51(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1041", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos51 (\\d+)$"))
async def xdos52(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1042", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos52 (\\d+)$"))
async def xdos53(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1043", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos53 (\\d+)$"))
async def xdos54(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1044", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos54 (\\d+)$"))
async def xdos55(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1045", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos55 (\\d+)$"))
async def xdos56(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1046", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos56 (\\d+)$"))
async def xdos57(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1047", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos57 (\\d+)$"))
async def xdos58(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1084", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos58 (\\d+)$"))
async def xdos59(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1049", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos59 (\\d+)$"))
async def xdos60(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1050", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos60 (\\d+)$"))
async def xdos61(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1051", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos61 (\\d+)$"))
async def xdos62(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1052", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos62 (\\d+)$"))
async def xdos63(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1053", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos63 (\\d+)$"))
async def xdos64(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1054", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos64 (\\d+)$"))
async def xdos65(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1055", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos65 (\\d+)$"))
async def xdos66(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1056", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos66 (\\d+)$"))
async def xdos67(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1057", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos67 (\\d+)$"))
async def xdos68(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1058", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos68 (\\d+)$"))
async def xdos69(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1059", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos69 (\\d+)$"))
async def xdos70(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1060", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos70 (\\d+)$"))
async def xdos71(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1061", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos71 (\\d+)$"))
async def xdos72(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1062", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos72 (\\d+)$"))
async def xdos73(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1063", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos73 (\\d+)$"))
async def xdos74(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1064", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos74 (\\d+)$"))
async def xdos75(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1065", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos75 (\\d+)$"))
async def xdos76(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1066", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos76 (\\d+)$"))
async def xdos77(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1067", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos77 (\\d+)$"))
async def xdos78(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1068", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos78 (\\d+)$"))
async def xdos79(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1069", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos79 (\\d+)$"))
async def xdos80(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1070", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos80 (\\d+)$"))
async def xdos81(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1071", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos81 (\\d+)$"))
async def xdos82(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1072", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos82 (\\d+)$"))
async def xdos83(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1073", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos83 (\\d+)$"))
async def xdos84(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1074", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos84 (\\d+)$"))
async def xdos85(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1075", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos85 (\\d+)$"))
async def xdos86(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1076", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos86 (\\d+)$"))
async def xdos87(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1077", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos87 (\\d+)$"))
async def xdos88(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1078", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos88 (\\d+)$"))
async def xdos89(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1079", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos89 (\\d+)$"))
async def xdos90(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1080", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos90 (\\d+)$"))
async def xdos91(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1081", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos91 (\\d+)$"))
async def xdos92(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1082", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos92 (\\d+)$"))
async def xdos93(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1083", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos93 (\\d+)$"))
async def xdos94(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1084", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos94 (\\d+)$"))
async def xdos95(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1085", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos95 (\\d+)$"))
async def xdos96(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1086", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos96 (\\d+)$"))
async def xdos97(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1087", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos97 (\\d+)$"))
async def xdos98(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1088", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos98 (\\d+)$"))
async def xdos99(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1089", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos99 (\\d+)$"))
async def xdos100(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1090", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos100 (\\d+)$"))
async def xdos101(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1091", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos101 (\\d+)$"))
async def xdos102(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1092", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos102 (\\d+)$"))
async def xdos103(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1093", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos103 (\\d+)$"))
async def xdos104(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1094", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos104 (\\d+)$"))
async def xdos105(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1095", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos105 (\\d+)$"))
async def xdos106(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1096", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos106 (\\d+)$"))
async def xdos107(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1097", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos107 (\\d+)$"))
async def xdos108(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1098", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos108 (\\d+)$"))
async def xdos109(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/109", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos109 (\\d+)$"))
async def xdos110(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1100", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos110 (\\d+)$"))
async def xdos111(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1101", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos111 (\\d+)$"))
async def xdos112(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1102", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos112 (\\d+)$"))
async def xdos113(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1103", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos113 (\\d+)$"))
async def xdos114(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1104", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos114 (\\d+)$"))
async def xdos114(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/1105", reply_to_message_id=mid)


########################################################################################################################
########################################################################################################################


@Client.on_callback_query(filters.regex("^abkar (\\d+)$"))
async def abkar(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("الفاتحه 🕋", callback_data="xabk1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البقرة 🕋", callback_data="xabk2 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ال عمران 🕋", callback_data="xabk3 " + str(m.from_user.id))],
        [InlineKeyboardButton("النساء 🕋", callback_data="xabk4 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المائدة 🕋", callback_data="xabk5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الانعام 🕋", callback_data="xabk6 " + str(m.from_user.id))],
        [InlineKeyboardButton("الأعراف 🕋", callback_data="xabk7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الأنفال 🕋", callback_data="xabk8 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التوبة 🕋", callback_data="xabk9 " + str(m.from_user.id))],
        [InlineKeyboardButton("يونس 🕋", callback_data="xabk10 " + str(m.from_user.id))] +
        [InlineKeyboardButton("هود 🕋", callback_data="xabk11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يوسف 🕋", callback_data="xabk12 " + str(m.from_user.id))],
        [InlineKeyboardButton("الرعد 🕋", callback_data="xabk13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("أبراهيم 🕋", callback_data="xabk14 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحجر 🕋", callback_data="xabk15 " + str(m.from_user.id))],
        [InlineKeyboardButton("النحل 🕋", callback_data="xabk16 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاسراء 🕋", callback_data="xabk17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الكهف 🕋", callback_data="xabk18 " + str(m.from_user.id))],
        [InlineKeyboardButton("مريم 🕋", callback_data="xabk19 " + str(m.from_user.id))] +
        [InlineKeyboardButton("طه 🕋", callback_data="xabk20 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الأنبياء 🕋", callback_data="xabk21 " + str(m.from_user.id))],
        [InlineKeyboardButton("الحج 🕋", callback_data="xabk22 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المؤمنون 🕋", callback_data="xabk23 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النور 🕋", callback_data="xabk24 " + str(m.from_user.id))],
        [InlineKeyboardButton("الفرقان 🕋", callback_data="xabk25 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الشعراء 🕋", callback_data="xabk26 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النحل 🕋", callback_data="xabk27 " + str(m.from_user.id))],
        [InlineKeyboardButton("القصص 🕋", callback_data="xabk28 " + str(m.from_user.id))] +
        [InlineKeyboardButton("العنكبوت 🕋", callback_data="xabk29 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الروم 🕋", callback_data="xabk30 " + str(m.from_user.id))],
        [InlineKeyboardButton("لقمان 🕋", callback_data="xabk31 " + str(m.from_user.id))] +
        [InlineKeyboardButton("السجدة 🕋", callback_data="xabk32 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاحزاب 🕋", callback_data="xabk33 " + str(m.from_user.id))],
        [InlineKeyboardButton("سبأ 🕋", callback_data="xabk34 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فاطر 🕋", callback_data="xabk35 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يس 🕋", callback_data="xabk36 " + str(m.from_user.id))],
        [InlineKeyboardButton("الصافات 🕋", callback_data="xabk37 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ص 🕋", callback_data="xabk38 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الزمر 🕋", callback_data="xabk39 " + str(m.from_user.id))],
        [InlineKeyboardButton("غافر 🕋", callback_data="xabk40 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فصلت 🕋", callback_data="xabk41 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الشورئ 🕋", callback_data="xabk42 " + str(m.from_user.id))],
        [InlineKeyboardButton("الزخرف 🕋", callback_data="xabk43 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الدخان 🕋", callback_data="xabk44 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجاثيه 🕋", callback_data="xabk45 " + str(m.from_user.id))],
        [InlineKeyboardButton("الاحقاف 🕋", callback_data="xabk46 " + str(m.from_user.id))] +
        [InlineKeyboardButton("محمد 🕋", callback_data="xabk47 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفتح 🕋", callback_data="xabk48 " + str(m.from_user.id))],
        [InlineKeyboardButton("الحجرات 🕋", callback_data="xabk49 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ق 🕋", callback_data="xabk50 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الذاريات 🕋", callback_data="xabk51 " + str(m.from_user.id))],

        [InlineKeyboardButton("➡️ التالي", callback_data="abkar2 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اختر سوره للقارئ ادريس ابكر\n√", reply_markup=keyboard, disable_web_page_preview=True)


@Client.on_callback_query(filters.regex("^abkar2 (\\d+)$"))
async def abkar2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("الطور 🕋", callback_data="xabk52 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النجم 🕋", callback_data="xabk53 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القمر 🕋", callback_data="xabk54 " + str(m.from_user.id))],
        [InlineKeyboardButton("الرحمن 🕋", callback_data="xabk55 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الواقعه 🕋", callback_data="xabk56 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحديد 🕋", callback_data="xabk57 " + str(m.from_user.id))],
        [InlineKeyboardButton("المجادلة 🕋", callback_data="xabk58 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحشر 🕋", callback_data="xabk59 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الممتحنة 🕋", callback_data="xabk60 " + str(m.from_user.id))],
        [InlineKeyboardButton("الصف 🕋", callback_data="xabk61 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجمعة 🕋", callback_data="xabk62 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المنافقون 🕋", callback_data="xabk63 " + str(m.from_user.id))],
        [InlineKeyboardButton("التغابن 🕋", callback_data="xabk64 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الطلاق 🕋", callback_data="xabk65 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التحريم 🕋", callback_data="xabk66 " + str(m.from_user.id))],
        [InlineKeyboardButton("الملك 🕋", callback_data="xabk67 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القلم 🕋", callback_data="xabk68 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحاقة 🕋", callback_data="xabk69 " + str(m.from_user.id))],
        [InlineKeyboardButton("المعارج 🕋", callback_data="xabk70 " + str(m.from_user.id))] +
        [InlineKeyboardButton("نوح 🕋", callback_data="xabk71 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجن 🕋", callback_data="xabk72 " + str(m.from_user.id))],
        [InlineKeyboardButton("المزمل 🕋", callback_data="xabk73 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المدثر 🕋", callback_data="xabk74 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القيامة 🕋", callback_data="xabk75 " + str(m.from_user.id))],
        [InlineKeyboardButton("الانسان 🕋", callback_data="xabk76 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المرسلات 🕋", callback_data="xabk77 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النبأ 🕋", callback_data="xabk78 " + str(m.from_user.id))],
        [InlineKeyboardButton("النازعات 🕋", callback_data="xabk79 " + str(m.from_user.id))] +
        [InlineKeyboardButton("عبس 🕋", callback_data="xabk80 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التكوير 🕋", callback_data="xabk81 " + str(m.from_user.id))],
        [InlineKeyboardButton("الانفطار 🕋", callback_data="xabk82 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المطففين 🕋", callback_data="xabk83 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الانشقاق 🕋", callback_data="xabk84 " + str(m.from_user.id))],
        [InlineKeyboardButton("البروج 🕋", callback_data="xabk85 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الطارق 🕋", callback_data="xabk86 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاعلي 🕋", callback_data="xabk87 " + str(m.from_user.id))],
        [InlineKeyboardButton("الغاشية 🕋", callback_data="xabk88 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفجر 🕋", callback_data="xabk89 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البلد 🕋", callback_data="xabk90 " + str(m.from_user.id))],
        [InlineKeyboardButton("الشمس 🕋", callback_data="xabk91 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الليل 🕋", callback_data="xabk92 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الضحئ 🕋", callback_data="xabk93 " + str(m.from_user.id))],
        [InlineKeyboardButton("الشرح 🕋", callback_data="xabk94 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التين 🕋", callback_data="xabk95 " + str(m.from_user.id))] +
        [InlineKeyboardButton("العلق 🕋", callback_data="xabk96 " + str(m.from_user.id))],
        [InlineKeyboardButton("القدر 🕋", callback_data="xabk97 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البينة 🕋", callback_data="xabk98 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الزلزلة 🕋", callback_data="xabk99 " + str(m.from_user.id))],
        [InlineKeyboardButton("العاديات 🕋", callback_data="xabk100 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القارعة 🕋", callback_data="xabk101 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التكاثر 🕋", callback_data="xabk102 " + str(m.from_user.id))],
        [InlineKeyboardButton("العصر 🕋", callback_data="xabk103 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الهمزة 🕋", callback_data="xabk104 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفيل 🕋", callback_data="xabk105 " + str(m.from_user.id))],
        [InlineKeyboardButton("قريش 🕋", callback_data="xabk106 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الماعون 🕋", callback_data="xabk107 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الكوثر 🕋", callback_data="xabk108 " + str(m.from_user.id))],
        [InlineKeyboardButton("الكافرون 🕋", callback_data="xabk109 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النصر 🕋", callback_data="xabk110 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المسد 🕋", callback_data="xabk111 " + str(m.from_user.id))],
        [InlineKeyboardButton("الاخلاص 🕋", callback_data="xabk112 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفلق 🕋", callback_data="xabk113 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الناس 🕋", callback_data="xabk114 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="abkar " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اختر سوره للقارئ ادريس ابكر\n√", reply_markup=keyboard, disable_web_page_preview=True)


@Client.on_callback_query(filters.regex("^xabk1 (\\d+)$"))
async def xabk1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/577", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk2 (\\d+)$"))
async def xabk2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/578", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk3 (\\d+)$"))
async def xabk3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/579", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk4 (\\d+)$"))
async def xabk4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/580", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk5 (\\d+)$"))
async def xabk5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/581", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk6 (\\d+)$"))
async def xabk6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/582", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk7 (\\d+)$"))
async def xabk7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/583", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk8 (\\d+)$"))
async def xabk8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/584", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk9 (\\d+)$"))
async def xabk9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/585", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk10 (\\d+)$"))
async def xabk10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/586", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk11 (\\d+)$"))
async def xabk11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/587", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk12 (\\d+)$"))
async def xabk12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/588", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk13 (\\d+)$"))
async def xabk13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/589", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk14 (\\d+)$"))
async def xabk14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/590", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk15 (\\d+)$"))
async def xabk15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/591", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk16 (\\d+)$"))
async def xabk16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/592", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk17 (\\d+)$"))
async def xabk17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/593", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk18 (\\d+)$"))
async def xabk18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/594", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk19 (\\d+)$"))
async def xabk19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/595", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk20 (\\d+)$"))
async def xabk20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/596", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk21 (\\d+)$"))
async def xabk21(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/597", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk22 (\\d+)$"))
async def xabk22(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/598", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk23 (\\d+)$"))
async def xabk23(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/599", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk24 (\\d+)$"))
async def xabk24(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/600", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk25 (\\d+)$"))
async def xabk25(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/601", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk26 (\\d+)$"))
async def xabk26(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/602", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk27 (\\d+)$"))
async def xabk27(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/603", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk28 (\\d+)$"))
async def xabk28(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/603", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk29 (\\d+)$"))
async def xabk29(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/604", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk30 (\\d+)$"))
async def xabk30(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/605", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk31 (\\d+)$"))
async def xabk31(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/606", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk32 (\\d+)$"))
async def xabk32(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/607", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk33 (\\d+)$"))
async def xabk33(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/608", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk34 (\\d+)$"))
async def xabk34(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/609", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk35 (\\d+)$"))
async def xabk35(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/610", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk36 (\\d+)$"))
async def xabk36(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/611", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk37 (\\d+)$"))
async def xabk37(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/612", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk38 (\\d+)$"))
async def xabk38(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/613", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk39 (\\d+)$"))
async def xabk39(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/614", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk40 (\\d+)$"))
async def xabk40(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/615", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk41 (\\d+)$"))
async def xabk41(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/616", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk42 (\\d+)$"))
async def xabk42(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/617", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk43 (\\d+)$"))
async def xabk43(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/618", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk44 (\\d+)$"))
async def xabk44(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/619", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk45 (\\d+)$"))
async def xabk45(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/620", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk46 (\\d+)$"))
async def xabk46(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/621", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk47 (\\d+)$"))
async def xabk47(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/622", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk48 (\\d+)$"))
async def xabk48(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/623", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk49 (\\d+)$"))
async def xabk49(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/624", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk50 (\\d+)$"))
async def xabk50(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/625", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk51 (\\d+)$"))
async def xabk51(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/226", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk52 (\\d+)$"))
async def xabk52(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/627", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk53 (\\d+)$"))
async def xabk53(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/628", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk54 (\\d+)$"))
async def xabk54(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/629", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk55 (\\d+)$"))
async def xabk55(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/630", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk56 (\\d+)$"))
async def xabk56(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/631", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk57 (\\d+)$"))
async def xabk57(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/632", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk58 (\\d+)$"))
async def xabk58(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/633", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk59 (\\d+)$"))
async def xabk59(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/634", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk60 (\\d+)$"))
async def xabk60(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/635", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk61 (\\d+)$"))
async def xabk61(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/636", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk62 (\\d+)$"))
async def xabk62(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/637", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk63 (\\d+)$"))
async def xabk63(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/638", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk64 (\\d+)$"))
async def xabk64(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/639", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk65 (\\d+)$"))
async def xabk65(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/640", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk66 (\\d+)$"))
async def xabk66(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/641", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk67 (\\d+)$"))
async def xabk67(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/642", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk68 (\\d+)$"))
async def xabk68(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/643", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk69 (\\d+)$"))
async def xabk69(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/644", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk70 (\\d+)$"))
async def xabk70(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/645", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk71 (\\d+)$"))
async def xabk71(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/646", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk72 (\\d+)$"))
async def xabk72(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/647", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk73 (\\d+)$"))
async def xabk73(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/648", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk74 (\\d+)$"))
async def xabk74(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/649", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk75 (\\d+)$"))
async def xabk75(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/650", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk76 (\\d+)$"))
async def xabk76(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/651", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk77 (\\d+)$"))
async def xabk77(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/652", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk78 (\\d+)$"))
async def xabk78(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/653", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk79 (\\d+)$"))
async def xabk79(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/654", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk80 (\\d+)$"))
async def xabk80(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/655", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk81 (\\d+)$"))
async def xabk81(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/656", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk82 (\\d+)$"))
async def xabk82(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/657", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk83 (\\d+)$"))
async def xabk83(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/658", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk84 (\\d+)$"))
async def xabk84(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/659", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk85 (\\d+)$"))
async def xabk85(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/660", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk86 (\\d+)$"))
async def xabk86(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/661", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk87 (\\d+)$"))
async def xabk87(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/662", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk88 (\\d+)$"))
async def xabk88(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/663", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk89 (\\d+)$"))
async def xabk89(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/664", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk90 (\\d+)$"))
async def xabk90(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/665", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk91 (\\d+)$"))
async def xabk91(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/666", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk92 (\\d+)$"))
async def xabk92(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/667", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk93 (\\d+)$"))
async def xabk93(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/668", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk94 (\\d+)$"))
async def xabk94(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/669", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk95 (\\d+)$"))
async def xabk95(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/670", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk96 (\\d+)$"))
async def xabk96(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/671", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk97 (\\d+)$"))
async def xabk97(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/672", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk98 (\\d+)$"))
async def xabk98(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/673", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk99 (\\d+)$"))
async def xabk99(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/674", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk100 (\\d+)$"))
async def xabk100(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/675", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk101 (\\d+)$"))
async def xabk101(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/676", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk102 (\\d+)$"))
async def xabk102(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/677", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk103 (\\d+)$"))
async def xabk103(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/678", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk104 (\\d+)$"))
async def xabk104(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/679", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk105 (\\d+)$"))
async def xabk105(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/680", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk106 (\\d+)$"))
async def xabk106(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/681", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk107 (\\d+)$"))
async def xabk107(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/682", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk108 (\\d+)$"))
async def xabk108(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/683", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk109 (\\d+)$"))
async def xabk109(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/684", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk110 (\\d+)$"))
async def xabk110(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/685", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk111 (\\d+)$"))
async def xabk111(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/686", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk112 (\\d+)$"))
async def xabk112(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/687", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk113 (\\d+)$"))
async def xabk113(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/688", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabk114 (\\d+)$"))
async def xabk114(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iQuran/689", reply_to_message_id=mid)


########################################################################################################################
########################################################################################################################


@Client.on_callback_query(filters.regex("^afasy (\\d+)$"))
async def afasy(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("الفاتحه 🕋", callback_data="xafas1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البقرة 🕋", callback_data="xafas2 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ال عمران 🕋", callback_data="xafas3 " + str(m.from_user.id))],
        [InlineKeyboardButton("النساء 🕋", callback_data="xafas4 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المائدة 🕋", callback_data="xafas5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الانعام 🕋", callback_data="xafas6 " + str(m.from_user.id))],
        [InlineKeyboardButton("الأعراف 🕋", callback_data="xafas7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الأنفال 🕋", callback_data="xafas8 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التوبة 🕋", callback_data="xafas9 " + str(m.from_user.id))],
        [InlineKeyboardButton("يونس 🕋", callback_data="xafas10 " + str(m.from_user.id))] +
        [InlineKeyboardButton("هود 🕋", callback_data="xafas11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يوسف 🕋", callback_data="xafas12 " + str(m.from_user.id))],
        [InlineKeyboardButton("الرعد 🕋", callback_data="xafas13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("أبراهيم 🕋", callback_data="xafas14 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحجر 🕋", callback_data="xafas15 " + str(m.from_user.id))],
        [InlineKeyboardButton("النحل 🕋", callback_data="xafas16 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاسراء 🕋", callback_data="xafas17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الكهف 🕋", callback_data="xafas18 " + str(m.from_user.id))],
        [InlineKeyboardButton("مريم 🕋", callback_data="xafas19 " + str(m.from_user.id))] +
        [InlineKeyboardButton("طه 🕋", callback_data="xafas20 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الأنبياء 🕋", callback_data="xafas21 " + str(m.from_user.id))],
        [InlineKeyboardButton("الحج 🕋", callback_data="xafas22 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المؤمنون 🕋", callback_data="xafas23 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النور 🕋", callback_data="xafas24 " + str(m.from_user.id))],
        [InlineKeyboardButton("الفرقان 🕋", callback_data="xafas25 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الشعراء 🕋", callback_data="xafas26 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النحل 🕋", callback_data="xafas27 " + str(m.from_user.id))],
        [InlineKeyboardButton("القصص 🕋", callback_data="xafas28 " + str(m.from_user.id))] +
        [InlineKeyboardButton("العنكبوت 🕋", callback_data="xafas29 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الروم 🕋", callback_data="xafas30 " + str(m.from_user.id))],
        [InlineKeyboardButton("لقمان 🕋", callback_data="xafas31 " + str(m.from_user.id))] +
        [InlineKeyboardButton("السجدة 🕋", callback_data="xafas32 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاحزاب 🕋", callback_data="xafas33 " + str(m.from_user.id))],
        [InlineKeyboardButton("سبأ 🕋", callback_data="xafas34 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فاطر 🕋", callback_data="xafas35 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يس 🕋", callback_data="xafas36 " + str(m.from_user.id))],
        [InlineKeyboardButton("الصافات 🕋", callback_data="xafas37 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ص 🕋", callback_data="xafas38 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الزمر 🕋", callback_data="xafas39 " + str(m.from_user.id))],
        [InlineKeyboardButton("غافر 🕋", callback_data="xafas40 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فصلت 🕋", callback_data="xafas41 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الشورئ 🕋", callback_data="xafas42 " + str(m.from_user.id))],
        [InlineKeyboardButton("الزخرف 🕋", callback_data="xafas43 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الدخان 🕋", callback_data="xafas44 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجاثيه 🕋", callback_data="xafas45 " + str(m.from_user.id))],
        [InlineKeyboardButton("الاحقاف 🕋", callback_data="xafas46 " + str(m.from_user.id))] +
        [InlineKeyboardButton("محمد 🕋", callback_data="xafas47 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفتح 🕋", callback_data="xafas48 " + str(m.from_user.id))],
        [InlineKeyboardButton("الحجرات 🕋", callback_data="xafas49 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ق 🕋", callback_data="xafas50 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الذاريات 🕋", callback_data="xafas51 " + str(m.from_user.id))],

        [InlineKeyboardButton("➡️ التالي", callback_data="afasy2 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اختر سوره للقار ئمشاري العفاسي\n√", reply_markup=keyboard, disable_web_page_preview=True)


@Client.on_callback_query(filters.regex("^afasy2 (\\d+)$"))
async def afasy2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("الطور 🕋", callback_data="xafas52 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النجم 🕋", callback_data="xafas53 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القمر 🕋", callback_data="xafas54 " + str(m.from_user.id))],
        [InlineKeyboardButton("الرحمن 🕋", callback_data="xafas55 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الواقعه 🕋", callback_data="xafas56 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحديد 🕋", callback_data="xafas57 " + str(m.from_user.id))],
        [InlineKeyboardButton("المجادلة 🕋", callback_data="xafas58 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحشر 🕋", callback_data="xafas59 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الممتحنة 🕋", callback_data="xafas60 " + str(m.from_user.id))],
        [InlineKeyboardButton("الصف 🕋", callback_data="xafas61 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجمعة 🕋", callback_data="xafas62 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المنافقون 🕋", callback_data="xafas63 " + str(m.from_user.id))],
        [InlineKeyboardButton("التغابن 🕋", callback_data="xafas64 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الطلاق 🕋", callback_data="xafas65 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التحريم 🕋", callback_data="xafas66 " + str(m.from_user.id))],
        [InlineKeyboardButton("الملك 🕋", callback_data="xafas67 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القلم 🕋", callback_data="xafas68 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحاقة 🕋", callback_data="xafas69 " + str(m.from_user.id))],
        [InlineKeyboardButton("المعارج 🕋", callback_data="xafas70 " + str(m.from_user.id))] +
        [InlineKeyboardButton("نوح 🕋", callback_data="xafas71 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجن 🕋", callback_data="xafas72 " + str(m.from_user.id))],
        [InlineKeyboardButton("المزمل 🕋", callback_data="xafas73 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المدثر 🕋", callback_data="xafas74 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القيامة 🕋", callback_data="xafas75 " + str(m.from_user.id))],
        [InlineKeyboardButton("الانسان 🕋", callback_data="xafas76 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المرسلات 🕋", callback_data="xafas77 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النبأ 🕋", callback_data="xafas78 " + str(m.from_user.id))],
        [InlineKeyboardButton("النازعات 🕋", callback_data="xafas79 " + str(m.from_user.id))] +
        [InlineKeyboardButton("عبس 🕋", callback_data="xafas80 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التكوير 🕋", callback_data="xafas81 " + str(m.from_user.id))],
        [InlineKeyboardButton("الانفطار 🕋", callback_data="xafas82 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المطففين 🕋", callback_data="xafas83 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الانشقاق 🕋", callback_data="xafas84 " + str(m.from_user.id))],
        [InlineKeyboardButton("البروج 🕋", callback_data="xafas85 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الطارق 🕋", callback_data="xafas86 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاعلي 🕋", callback_data="xafas87 " + str(m.from_user.id))],
        [InlineKeyboardButton("الغاشية 🕋", callback_data="xafas88 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفجر 🕋", callback_data="xafas89 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البلد 🕋", callback_data="xafas90 " + str(m.from_user.id))],
        [InlineKeyboardButton("الشمس 🕋", callback_data="xafas91 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الليل 🕋", callback_data="xafas92 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الضحئ 🕋", callback_data="xafas93 " + str(m.from_user.id))],
        [InlineKeyboardButton("الشرح 🕋", callback_data="xafas94 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التين 🕋", callback_data="xafas95 " + str(m.from_user.id))] +
        [InlineKeyboardButton("العلق 🕋", callback_data="xafas96 " + str(m.from_user.id))],
        [InlineKeyboardButton("القدر 🕋", callback_data="xafas97 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البينة 🕋", callback_data="xafas98 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الزلزلة 🕋", callback_data="xafas99 " + str(m.from_user.id))],
        [InlineKeyboardButton("العاديات 🕋", callback_data="xafas100 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القارعة 🕋", callback_data="xafas101 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التكاثر 🕋", callback_data="xafas102 " + str(m.from_user.id))],
        [InlineKeyboardButton("العصر 🕋", callback_data="xafas103 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الهمزة 🕋", callback_data="xafas104 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفيل 🕋", callback_data="xafas105 " + str(m.from_user.id))],
        [InlineKeyboardButton("قريش 🕋", callback_data="xafas106 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الماعون 🕋", callback_data="xafas107 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الكوثر 🕋", callback_data="xafas108 " + str(m.from_user.id))],
        [InlineKeyboardButton("الكافرون 🕋", callback_data="xafas109 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النصر 🕋", callback_data="xafas110 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المسد 🕋", callback_data="xafas111 " + str(m.from_user.id))],
        [InlineKeyboardButton("الاخلاص 🕋", callback_data="xafas112 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفلق 🕋", callback_data="xafas113 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الناس 🕋", callback_data="xafas114 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="afasy " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اختر سوره للقار ئمشاري العفاسي\n√", reply_markup=keyboard, disable_web_page_preview=True)


@Client.on_callback_query(filters.regex("^xafas1 (\\d+)$"))
async def xafas1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/769", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas2 (\\d+)$"))
async def xafas2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/770", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas3 (\\d+)$"))
async def xafas3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/771", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas4 (\\d+)$"))
async def xafas4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/772", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas5 (\\d+)$"))
async def xafas5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/773", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas6 (\\d+)$"))
async def xafas6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/774", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas7 (\\d+)$"))
async def xafas7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/775", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas8 (\\d+)$"))
async def xafas8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/776", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas9 (\\d+)$"))
async def xafas9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/777", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas10 (\\d+)$"))
async def xafas10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/778", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas11 (\\d+)$"))
async def xafas11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/779", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas12 (\\d+)$"))
async def xafas12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/780", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas13 (\\d+)$"))
async def xafas13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/781", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas14 (\\d+)$"))
async def xafas14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/782", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas15 (\\d+)$"))
async def xafas15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/783", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas16 (\\d+)$"))
async def xafas16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/784", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas17 (\\d+)$"))
async def xafas17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/785", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas18 (\\d+)$"))
async def xafas18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/786", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas19 (\\d+)$"))
async def xafas19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/787", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas20 (\\d+)$"))
async def xafas20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/788", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas21 (\\d+)$"))
async def xafas21(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/789", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas22 (\\d+)$"))
async def xafas22(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/790", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas23 (\\d+)$"))
async def xafas23(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/791", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas24 (\\d+)$"))
async def xafas24(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/792", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas25 (\\d+)$"))
async def xafas25(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/793", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas26 (\\d+)$"))
async def xafas26(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/794", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas27 (\\d+)$"))
async def xafas27(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/795", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas28 (\\d+)$"))
async def xafas28(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/796", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas29 (\\d+)$"))
async def xafas29(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/797", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas30 (\\d+)$"))
async def xafas30(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/798", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas31 (\\d+)$"))
async def xafas31(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/799", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas32 (\\d+)$"))
async def xafas32(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/800", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas33 (\\d+)$"))
async def xafas33(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/801", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas34 (\\d+)$"))
async def xafas34(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/802", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas35 (\\d+)$"))
async def xafas35(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/803", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas36 (\\d+)$"))
async def xafas36(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/804", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas37 (\\d+)$"))
async def xafas37(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/805", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas38 (\\d+)$"))
async def xafas38(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/806", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas39 (\\d+)$"))
async def xafas39(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/807", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas40 (\\d+)$"))
async def xafas40(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/808", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas41 (\\d+)$"))
async def xafas41(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/809", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas42 (\\d+)$"))
async def xafas42(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/810", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas43 (\\d+)$"))
async def xafas43(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/811", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas44 (\\d+)$"))
async def xafas44(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/812", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas45 (\\d+)$"))
async def xafas45(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/813", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas46 (\\d+)$"))
async def xafas46(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/814", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas47 (\\d+)$"))
async def xafas47(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/815", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas48 (\\d+)$"))
async def xafas48(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/816", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas49 (\\d+)$"))
async def xafas49(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/817", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas50 (\\d+)$"))
async def xafas50(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/818", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas51 (\\d+)$"))
async def xafas51(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/819", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas52 (\\d+)$"))
async def xafas52(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/820", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas53 (\\d+)$"))
async def xafas53(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/821", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas54 (\\d+)$"))
async def xafas54(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/822", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas55 (\\d+)$"))
async def xafas55(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/823", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas56 (\\d+)$"))
async def xafas56(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/824", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas57 (\\d+)$"))
async def xafas57(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/825", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas58 (\\d+)$"))
async def xafas58(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/826", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas59 (\\d+)$"))
async def xafas59(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/827", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas60 (\\d+)$"))
async def xafas60(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/828", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas61 (\\d+)$"))
async def xafas61(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/829", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas62 (\\d+)$"))
async def xafas62(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/830", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas63 (\\d+)$"))
async def xafas63(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/831", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas64 (\\d+)$"))
async def xafas64(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/832", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas65 (\\d+)$"))
async def xafas65(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/833", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas66 (\\d+)$"))
async def xafas66(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/834", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas67 (\\d+)$"))
async def xafas67(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/835", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas68 (\\d+)$"))
async def xafas68(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/836", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas69 (\\d+)$"))
async def xafas69(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/837", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas70 (\\d+)$"))
async def xafas70(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/838", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas71 (\\d+)$"))
async def xafas71(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/839", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas72 (\\d+)$"))
async def xafas72(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/840", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas73 (\\d+)$"))
async def xafas73(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/841", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas74 (\\d+)$"))
async def xafas74(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/842", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas75 (\\d+)$"))
async def xafas75(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/843", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas76 (\\d+)$"))
async def xafas76(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/844", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas77 (\\d+)$"))
async def xafas77(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/845", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas78 (\\d+)$"))
async def xafas78(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/846", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas79 (\\d+)$"))
async def xafas79(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/847", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas80 (\\d+)$"))
async def xafas80(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/848", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas81 (\\d+)$"))
async def xafas81(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/849", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas82 (\\d+)$"))
async def xafas82(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/850", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas83 (\\d+)$"))
async def xafas83(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/851", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas84 (\\d+)$"))
async def xafas84(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/852", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas85 (\\d+)$"))
async def xafas85(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/853", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas86 (\\d+)$"))
async def xafas86(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/854", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas87 (\\d+)$"))
async def xafas87(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/855", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas88 (\\d+)$"))
async def xafas88(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/856", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas89 (\\d+)$"))
async def xafas89(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/857", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas90 (\\d+)$"))
async def xafas90(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/858", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas91 (\\d+)$"))
async def xafas91(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/859", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas92 (\\d+)$"))
async def xafas92(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/860", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas93 (\\d+)$"))
async def xafas93(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/861", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas94 (\\d+)$"))
async def xafas94(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/862", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas95 (\\d+)$"))
async def xafas95(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/863", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas96 (\\d+)$"))
async def xafas96(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/864", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas97 (\\d+)$"))
async def xafas97(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/865", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas98 (\\d+)$"))
async def xafas98(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/866", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas99 (\\d+)$"))
async def xafas99(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/867", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas100 (\\d+)$"))
async def xafas100(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/868", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas101 (\\d+)$"))
async def xafas101(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/869", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas102 (\\d+)$"))
async def xafas102(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/870", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas103 (\\d+)$"))
async def xafas103(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/871", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas104 (\\d+)$"))
async def xafas104(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/872", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas105 (\\d+)$"))
async def xafas105(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/873", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas106 (\\d+)$"))
async def xafas106(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/874", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas107 (\\d+)$"))
async def xafas107(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/875", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas108 (\\d+)$"))
async def xafas108(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/876", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas109 (\\d+)$"))
async def xafas109(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/877", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas110 (\\d+)$"))
async def xafas110(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/878", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas111 (\\d+)$"))
async def xafas111(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/879", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas112 (\\d+)$"))
async def xafas112(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/880", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas113 (\\d+)$"))
async def xafas113(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/881", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xafas114 (\\d+)$"))
async def xafas114(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/882", reply_to_message_id=mid)


########################################################################################################################
########################################################################################################################


@Client.on_callback_query(filters.regex("^agamy (\\d+)$"))
async def agamy(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("الفاتحه 🕋", callback_data="xagam1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البقرة 🕋", callback_data="xagam2 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ال عمران 🕋", callback_data="xagam3 " + str(m.from_user.id))],
        [InlineKeyboardButton("النساء 🕋", callback_data="xagam4 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المائدة 🕋", callback_data="xagam5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الانعام 🕋", callback_data="xagam6 " + str(m.from_user.id))],
        [InlineKeyboardButton("الأعراف 🕋", callback_data="xagam7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الأنفال 🕋", callback_data="xagam8 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التوبة 🕋", callback_data="xagam9 " + str(m.from_user.id))],
        [InlineKeyboardButton("يونس 🕋", callback_data="xagam10 " + str(m.from_user.id))] +
        [InlineKeyboardButton("هود 🕋", callback_data="xagam11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يوسف 🕋", callback_data="xagam12 " + str(m.from_user.id))],
        [InlineKeyboardButton("الرعد 🕋", callback_data="xagam13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("أبراهيم 🕋", callback_data="xagam14 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحجر 🕋", callback_data="xagam15 " + str(m.from_user.id))],
        [InlineKeyboardButton("النحل 🕋", callback_data="xagam16 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاسراء 🕋", callback_data="xagam17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الكهف 🕋", callback_data="xagam18 " + str(m.from_user.id))],
        [InlineKeyboardButton("مريم 🕋", callback_data="xagam19 " + str(m.from_user.id))] +
        [InlineKeyboardButton("طه 🕋", callback_data="xagam20 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الأنبياء 🕋", callback_data="xagam21 " + str(m.from_user.id))],
        [InlineKeyboardButton("الحج 🕋", callback_data="xagam22 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المؤمنون 🕋", callback_data="xagam23 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النور 🕋", callback_data="xagam24 " + str(m.from_user.id))],
        [InlineKeyboardButton("الفرقان 🕋", callback_data="xagam25 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الشعراء 🕋", callback_data="xagam26 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النحل 🕋", callback_data="xagam27 " + str(m.from_user.id))],
        [InlineKeyboardButton("القصص 🕋", callback_data="xagam28 " + str(m.from_user.id))] +
        [InlineKeyboardButton("العنكبوت 🕋", callback_data="xagam29 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الروم 🕋", callback_data="xagam30 " + str(m.from_user.id))],
        [InlineKeyboardButton("لقمان 🕋", callback_data="xagam31 " + str(m.from_user.id))] +
        [InlineKeyboardButton("السجدة 🕋", callback_data="xagam32 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاحزاب 🕋", callback_data="xagam33 " + str(m.from_user.id))],
        [InlineKeyboardButton("سبأ 🕋", callback_data="xagam34 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فاطر 🕋", callback_data="xagam35 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يس 🕋", callback_data="xagam36 " + str(m.from_user.id))],
        [InlineKeyboardButton("الصافات 🕋", callback_data="xagam37 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ص 🕋", callback_data="xagam38 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الزمر 🕋", callback_data="xagam39 " + str(m.from_user.id))],
        [InlineKeyboardButton("غافر 🕋", callback_data="xagam40 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فصلت 🕋", callback_data="xagam41 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الشورئ 🕋", callback_data="xagam42 " + str(m.from_user.id))],
        [InlineKeyboardButton("الزخرف 🕋", callback_data="xagam43 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الدخان 🕋", callback_data="xagam44 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجاثيه 🕋", callback_data="xagam45 " + str(m.from_user.id))],
        [InlineKeyboardButton("الاحقاف 🕋", callback_data="xagam46 " + str(m.from_user.id))] +
        [InlineKeyboardButton("محمد 🕋", callback_data="xagam47 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفتح 🕋", callback_data="xagam48 " + str(m.from_user.id))],
        [InlineKeyboardButton("الحجرات 🕋", callback_data="xagam49 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ق 🕋", callback_data="xagam50 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الذاريات 🕋", callback_data="xagam51 " + str(m.from_user.id))],

        [InlineKeyboardButton("➡️ التالي", callback_data="agamy2 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اختر سوره للقارئ احمد بن علي العجمي\n√", reply_markup=keyboard,
                              disable_web_page_preview=True)


@Client.on_callback_query(filters.regex("^agamy2 (\\d+)$"))
async def agamy2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("الطور 🕋", callback_data="xagam52 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النجم 🕋", callback_data="xagam53 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القمر 🕋", callback_data="xagam54 " + str(m.from_user.id))],
        [InlineKeyboardButton("الرحمن 🕋", callback_data="xagam55 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الواقعه 🕋", callback_data="xagam56 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحديد 🕋", callback_data="xagam57 " + str(m.from_user.id))],
        [InlineKeyboardButton("المجادلة 🕋", callback_data="xagam58 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحشر 🕋", callback_data="xagam59 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الممتحنة 🕋", callback_data="xagam60 " + str(m.from_user.id))],
        [InlineKeyboardButton("الصف 🕋", callback_data="xagam61 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجمعة 🕋", callback_data="xagam62 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المنافقون 🕋", callback_data="xagam63 " + str(m.from_user.id))],
        [InlineKeyboardButton("التغابن 🕋", callback_data="xagam64 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الطلاق 🕋", callback_data="xagam65 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التحريم 🕋", callback_data="xagam66 " + str(m.from_user.id))],
        [InlineKeyboardButton("الملك 🕋", callback_data="xagam67 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القلم 🕋", callback_data="xagam68 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحاقة 🕋", callback_data="xagam69 " + str(m.from_user.id))],
        [InlineKeyboardButton("المعارج 🕋", callback_data="xagam70 " + str(m.from_user.id))] +
        [InlineKeyboardButton("نوح 🕋", callback_data="xagam71 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجن 🕋", callback_data="xagam72 " + str(m.from_user.id))],
        [InlineKeyboardButton("المزمل 🕋", callback_data="xagam73 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المدثر 🕋", callback_data="xagam74 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القيامة 🕋", callback_data="xagam75 " + str(m.from_user.id))],
        [InlineKeyboardButton("الانسان 🕋", callback_data="xagam76 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المرسلات 🕋", callback_data="xagam77 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النبأ 🕋", callback_data="xagam78 " + str(m.from_user.id))],
        [InlineKeyboardButton("النازعات 🕋", callback_data="xagam79 " + str(m.from_user.id))] +
        [InlineKeyboardButton("عبس 🕋", callback_data="xagam80 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التكوير 🕋", callback_data="xagam81 " + str(m.from_user.id))],
        [InlineKeyboardButton("الانفطار 🕋", callback_data="xagam82 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المطففين 🕋", callback_data="xagam83 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الانشقاق 🕋", callback_data="xagam84 " + str(m.from_user.id))],
        [InlineKeyboardButton("البروج 🕋", callback_data="xagam85 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الطارق 🕋", callback_data="xagam86 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاعلي 🕋", callback_data="xagam87 " + str(m.from_user.id))],
        [InlineKeyboardButton("الغاشية 🕋", callback_data="xagam88 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفجر 🕋", callback_data="xagam89 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البلد 🕋", callback_data="xagam90 " + str(m.from_user.id))],
        [InlineKeyboardButton("الشمس 🕋", callback_data="xagam91 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الليل 🕋", callback_data="xagam92 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الضحئ 🕋", callback_data="xagam93 " + str(m.from_user.id))],
        [InlineKeyboardButton("الشرح 🕋", callback_data="xagam94 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التين 🕋", callback_data="xagam95 " + str(m.from_user.id))] +
        [InlineKeyboardButton("العلق 🕋", callback_data="xagam96 " + str(m.from_user.id))],
        [InlineKeyboardButton("القدر 🕋", callback_data="xagam97 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البينة 🕋", callback_data="xagam98 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الزلزلة 🕋", callback_data="xagam99 " + str(m.from_user.id))],
        [InlineKeyboardButton("العاديات 🕋", callback_data="xagam100 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القارعة 🕋", callback_data="xagam101 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التكاثر 🕋", callback_data="xagam102 " + str(m.from_user.id))],
        [InlineKeyboardButton("العصر 🕋", callback_data="xagam103 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الهمزة 🕋", callback_data="xagam104 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفيل 🕋", callback_data="xagam105 " + str(m.from_user.id))],
        [InlineKeyboardButton("قريش 🕋", callback_data="xagam106 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الماعون 🕋", callback_data="xagam107 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الكوثر 🕋", callback_data="xagam108 " + str(m.from_user.id))],
        [InlineKeyboardButton("الكافرون 🕋", callback_data="xagam109 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النصر 🕋", callback_data="xagam110 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المسد 🕋", callback_data="xagam111 " + str(m.from_user.id))],
        [InlineKeyboardButton("الاخلاص 🕋", callback_data="xagam112 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفلق 🕋", callback_data="xagam113 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الناس 🕋", callback_data="xagam114 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="agamy " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اختر سوره للقارئ احمد بن علي العجمي\n√", reply_markup=keyboard,
                              disable_web_page_preview=True)


@Client.on_callback_query(filters.regex("^xagam1 (\\d+)$"))
async def xagam1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/237", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam2 (\\d+)$"))
async def xagam2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/238", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam3 (\\d+)$"))
async def xagam3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/239", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam4 (\\d+)$"))
async def xagam4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/240", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam5 (\\d+)$"))
async def xagam5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/241", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam6 (\\d+)$"))
async def xagam6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/242", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam7 (\\d+)$"))
async def xagam7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/243", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam8 (\\d+)$"))
async def xagam8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/244", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam9 (\\d+)$"))
async def xagam9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/245", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam10 (\\d+)$"))
async def xagam10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/246", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam11 (\\d+)$"))
async def xagam11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/247", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam12 (\\d+)$"))
async def xagam12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/248", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam13 (\\d+)$"))
async def xagam13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/249", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam14 (\\d+)$"))
async def xagam14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/250", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam15 (\\d+)$"))
async def xagam15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/251", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam16 (\\d+)$"))
async def xagam16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/252", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam17 (\\d+)$"))
async def xagam17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/253", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam18 (\\d+)$"))
async def xagam18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/254", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam19 (\\d+)$"))
async def xagam19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/255", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam20 (\\d+)$"))
async def xagam20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/256", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam21 (\\d+)$"))
async def xagam21(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/257", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam22 (\\d+)$"))
async def xagam22(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/258", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam23 (\\d+)$"))
async def xagam23(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/259", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam24 (\\d+)$"))
async def xagam24(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/260", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam25 (\\d+)$"))
async def xagam25(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/261", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam26 (\\d+)$"))
async def xagam26(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/262", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam27 (\\d+)$"))
async def xagam27(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/263", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam28 (\\d+)$"))
async def xagam28(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/264", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam29 (\\d+)$"))
async def xagam29(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/265", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam30 (\\d+)$"))
async def xagam30(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/266", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam31 (\\d+)$"))
async def xagam31(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/267", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam32 (\\d+)$"))
async def xagam32(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/268", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam33 (\\d+)$"))
async def xagam33(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/269", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam34 (\\d+)$"))
async def xagam34(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/270", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam35 (\\d+)$"))
async def xagam35(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/271", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam36 (\\d+)$"))
async def xagam36(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/272", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam37 (\\d+)$"))
async def xagam37(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/273", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam38 (\\d+)$"))
async def xagam38(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/274", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam39 (\\d+)$"))
async def xagam39(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/275", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam40 (\\d+)$"))
async def xagam40(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/276", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam41 (\\d+)$"))
async def xagam41(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/277", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam42 (\\d+)$"))
async def xagam42(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/278", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam43 (\\d+)$"))
async def xagam43(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/279", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam44 (\\d+)$"))
async def xagam44(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/280", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam45 (\\d+)$"))
async def xagam45(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/281", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam46 (\\d+)$"))
async def xagam46(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/282", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam47 (\\d+)$"))
async def xagam47(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/283", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam48 (\\d+)$"))
async def xagam48(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/284", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam49 (\\d+)$"))
async def xagam49(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/285", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam50 (\\d+)$"))
async def xagam50(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/286", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam51 (\\d+)$"))
async def xagam51(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/287", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam52 (\\d+)$"))
async def xagam52(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/288", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam53 (\\d+)$"))
async def xagam53(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/289", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam54 (\\d+)$"))
async def xagam54(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/290", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam55 (\\d+)$"))
async def xagam55(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/291", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam56 (\\d+)$"))
async def xagam56(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/292", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam57 (\\d+)$"))
async def xagam57(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/293", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam58 (\\d+)$"))
async def xagam58(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/294", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam59 (\\d+)$"))
async def xagam59(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/295", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam60 (\\d+)$"))
async def xagam60(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/296", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam61 (\\d+)$"))
async def xagam61(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/297", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam62 (\\d+)$"))
async def xagam62(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/298", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam63 (\\d+)$"))
async def xagam63(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/299", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam64 (\\d+)$"))
async def xagam64(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/300", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam65 (\\d+)$"))
async def xagam65(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/301", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam66 (\\d+)$"))
async def xagam66(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/302", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam67 (\\d+)$"))
async def xagam67(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/303", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam68 (\\d+)$"))
async def xagam68(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/304", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam69 (\\d+)$"))
async def xagam69(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/305", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam70 (\\d+)$"))
async def xagam70(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/306", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam71 (\\d+)$"))
async def xagam71(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/307", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam72 (\\d+)$"))
async def xagam72(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/308", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam73 (\\d+)$"))
async def xagam73(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/309", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam74 (\\d+)$"))
async def xagam74(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/310", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam75 (\\d+)$"))
async def xagam75(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/311", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam76 (\\d+)$"))
async def xagam76(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/312", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam77 (\\d+)$"))
async def xagam77(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/313", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam78 (\\d+)$"))
async def xagam78(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/314", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam79 (\\d+)$"))
async def xagam79(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/315", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam80 (\\d+)$"))
async def xagam80(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/316", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam81 (\\d+)$"))
async def xagam81(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/317", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam82 (\\d+)$"))
async def xagam82(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/318", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam83 (\\d+)$"))
async def xagam83(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/319", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam84 (\\d+)$"))
async def xagam84(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/320", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam85 (\\d+)$"))
async def xagam85(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/321", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam86 (\\d+)$"))
async def xagam86(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/322", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam87 (\\d+)$"))
async def xagam87(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/323", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam88 (\\d+)$"))
async def xagam88(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/324", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam89 (\\d+)$"))
async def xagam89(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/325", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam90 (\\d+)$"))
async def xagam90(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/326", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam91 (\\d+)$"))
async def xagam91(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/327", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam92 (\\d+)$"))
async def xagam92(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/328", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam93 (\\d+)$"))
async def xagam93(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/329", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam94 (\\d+)$"))
async def xagam94(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/330", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam95 (\\d+)$"))
async def xagam95(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/331", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam96 (\\d+)$"))
async def xagam96(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/332", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam97 (\\d+)$"))
async def xagam97(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/333", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam98 (\\d+)$"))
async def xagam98(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/334", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam99 (\\d+)$"))
async def xagam99(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/335", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam100 (\\d+)$"))
async def xagam100(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/336", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam101 (\\d+)$"))
async def xagam101(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/337", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam102 (\\d+)$"))
async def xagam102(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/338", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam103 (\\d+)$"))
async def xagam103(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/339", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam104 (\\d+)$"))
async def xagam104(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/340", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam105 (\\d+)$"))
async def xagam105(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/341", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam106 (\\d+)$"))
async def xagam106(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/342", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam107 (\\d+)$"))
async def xagam107(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/343", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam108 (\\d+)$"))
async def xagam108(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/344", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam109 (\\d+)$"))
async def xagam109(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/345", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam110 (\\d+)$"))
async def xagam110(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/346", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam111 (\\d+)$"))
async def xagam111(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/347", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam112 (\\d+)$"))
async def xagam112(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/348", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam113 (\\d+)$"))
async def xagam113(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/349", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xagam114 (\\d+)$"))
async def xagam114(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/350", reply_to_message_id=mid)


########################################################################################################################
########################################################################################################################


@Client.on_callback_query(filters.regex("^maher (\\d+)$"))
async def maher(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("الفاتحه 🕋", callback_data="xmah1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البقرة 🕋", callback_data="xmah2 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ال عمران 🕋", callback_data="xmah3 " + str(m.from_user.id))],
        [InlineKeyboardButton("النساء 🕋", callback_data="xmah4 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المائدة 🕋", callback_data="xmah5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الانعام 🕋", callback_data="xmah6 " + str(m.from_user.id))],
        [InlineKeyboardButton("الأعراف 🕋", callback_data="xmah7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الأنفال 🕋", callback_data="xmah8 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التوبة 🕋", callback_data="xmah9 " + str(m.from_user.id))],
        [InlineKeyboardButton("يونس 🕋", callback_data="xmah10 " + str(m.from_user.id))] +
        [InlineKeyboardButton("هود 🕋", callback_data="xmah11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يوسف 🕋", callback_data="xmah12 " + str(m.from_user.id))],
        [InlineKeyboardButton("الرعد 🕋", callback_data="xmah13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("أبراهيم 🕋", callback_data="xmah14 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحجر 🕋", callback_data="xmah15 " + str(m.from_user.id))],
        [InlineKeyboardButton("النحل 🕋", callback_data="xmah16 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاسراء 🕋", callback_data="xmah17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الكهف 🕋", callback_data="xmah18 " + str(m.from_user.id))],
        [InlineKeyboardButton("مريم 🕋", callback_data="xmah19 " + str(m.from_user.id))] +
        [InlineKeyboardButton("طه 🕋", callback_data="xmah20 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الأنبياء 🕋", callback_data="xmah21 " + str(m.from_user.id))],
        [InlineKeyboardButton("الحج 🕋", callback_data="xmah22 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المؤمنون 🕋", callback_data="xmah23 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النور 🕋", callback_data="xmah24 " + str(m.from_user.id))],
        [InlineKeyboardButton("الفرقان 🕋", callback_data="xmah25 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الشعراء 🕋", callback_data="xmah26 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النحل 🕋", callback_data="xmah27 " + str(m.from_user.id))],
        [InlineKeyboardButton("القصص 🕋", callback_data="xmah28 " + str(m.from_user.id))] +
        [InlineKeyboardButton("العنكبوت 🕋", callback_data="xmah29 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الروم 🕋", callback_data="xmah30 " + str(m.from_user.id))],
        [InlineKeyboardButton("لقمان 🕋", callback_data="xmah31 " + str(m.from_user.id))] +
        [InlineKeyboardButton("السجدة 🕋", callback_data="xmah32 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاحزاب 🕋", callback_data="xmah33 " + str(m.from_user.id))],
        [InlineKeyboardButton("سبأ 🕋", callback_data="xmah34 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فاطر 🕋", callback_data="xmah35 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يس 🕋", callback_data="xmah36 " + str(m.from_user.id))],
        [InlineKeyboardButton("الصافات 🕋", callback_data="xmah37 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ص 🕋", callback_data="xmah38 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الزمر 🕋", callback_data="xmah39 " + str(m.from_user.id))],
        [InlineKeyboardButton("غافر 🕋", callback_data="xmah40 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فصلت 🕋", callback_data="xmah41 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الشورئ 🕋", callback_data="xmah42 " + str(m.from_user.id))],
        [InlineKeyboardButton("الزخرف 🕋", callback_data="xmah43 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الدخان 🕋", callback_data="xmah44 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجاثيه 🕋", callback_data="xmah45 " + str(m.from_user.id))],
        [InlineKeyboardButton("الاحقاف 🕋", callback_data="xmah46 " + str(m.from_user.id))] +
        [InlineKeyboardButton("محمد 🕋", callback_data="xmah47 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفتح 🕋", callback_data="xmah48 " + str(m.from_user.id))],
        [InlineKeyboardButton("الحجرات 🕋", callback_data="xmah49 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ق 🕋", callback_data="xmah50 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الذاريات 🕋", callback_data="xmah51 " + str(m.from_user.id))],

        [InlineKeyboardButton("➡️ التالي", callback_data="maher2 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اختر سوره للقارئ ماهر المعيقلي\n√", reply_markup=keyboard, disable_web_page_preview=True)


@Client.on_callback_query(filters.regex("^maher2 (\\d+)$"))
async def maher2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("الطور 🕋", callback_data="xmah52 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النجم 🕋", callback_data="xmah53 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القمر 🕋", callback_data="xmah54 " + str(m.from_user.id))],
        [InlineKeyboardButton("الرحمن 🕋", callback_data="xmah55 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الواقعه 🕋", callback_data="xmah56 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحديد 🕋", callback_data="xmah57 " + str(m.from_user.id))],
        [InlineKeyboardButton("المجادلة 🕋", callback_data="xmah58 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحشر 🕋", callback_data="xmah59 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الممتحنة 🕋", callback_data="xmah60 " + str(m.from_user.id))],
        [InlineKeyboardButton("الصف 🕋", callback_data="xmah61 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجمعة 🕋", callback_data="xmah62 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المنافقون 🕋", callback_data="xmah63 " + str(m.from_user.id))],
        [InlineKeyboardButton("التغابن 🕋", callback_data="xmah64 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الطلاق 🕋", callback_data="xmah65 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التحريم 🕋", callback_data="xmah66 " + str(m.from_user.id))],
        [InlineKeyboardButton("الملك 🕋", callback_data="xmah67 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القلم 🕋", callback_data="xmah68 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحاقة 🕋", callback_data="xmah69 " + str(m.from_user.id))],
        [InlineKeyboardButton("المعارج 🕋", callback_data="xmah70 " + str(m.from_user.id))] +
        [InlineKeyboardButton("نوح 🕋", callback_data="xmah71 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجن 🕋", callback_data="xmah72 " + str(m.from_user.id))],
        [InlineKeyboardButton("المزمل 🕋", callback_data="xmah73 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المدثر 🕋", callback_data="xmah74 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القيامة 🕋", callback_data="xmah75 " + str(m.from_user.id))],
        [InlineKeyboardButton("الانسان 🕋", callback_data="xmah76 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المرسلات 🕋", callback_data="xmah77 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النبأ 🕋", callback_data="xmah78 " + str(m.from_user.id))],
        [InlineKeyboardButton("النازعات 🕋", callback_data="xmah79 " + str(m.from_user.id))] +
        [InlineKeyboardButton("عبس 🕋", callback_data="xmah80 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التكوير 🕋", callback_data="xmah81 " + str(m.from_user.id))],
        [InlineKeyboardButton("الانفطار 🕋", callback_data="xmah82 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المطففين 🕋", callback_data="xmah83 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الانشقاق 🕋", callback_data="xmah84 " + str(m.from_user.id))],
        [InlineKeyboardButton("البروج 🕋", callback_data="xmah85 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الطارق 🕋", callback_data="xmah86 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاعلي 🕋", callback_data="xmah87 " + str(m.from_user.id))],
        [InlineKeyboardButton("الغاشية 🕋", callback_data="xmah88 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفجر 🕋", callback_data="xmah89 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البلد 🕋", callback_data="xmah90 " + str(m.from_user.id))],
        [InlineKeyboardButton("الشمس 🕋", callback_data="xmah91 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الليل 🕋", callback_data="xmah92 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الضحئ 🕋", callback_data="xmah93 " + str(m.from_user.id))],
        [InlineKeyboardButton("الشرح 🕋", callback_data="xmah94 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التين 🕋", callback_data="xmah95 " + str(m.from_user.id))] +
        [InlineKeyboardButton("العلق 🕋", callback_data="xmah96 " + str(m.from_user.id))],
        [InlineKeyboardButton("القدر 🕋", callback_data="xmah97 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البينة 🕋", callback_data="xmah98 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الزلزلة 🕋", callback_data="xmah99 " + str(m.from_user.id))],
        [InlineKeyboardButton("العاديات 🕋", callback_data="xmah100 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القارعة 🕋", callback_data="xmah101 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التكاثر 🕋", callback_data="xmah102 " + str(m.from_user.id))],
        [InlineKeyboardButton("العصر 🕋", callback_data="xmah103 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الهمزة 🕋", callback_data="xmah104 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفيل 🕋", callback_data="xmah105 " + str(m.from_user.id))],
        [InlineKeyboardButton("قريش 🕋", callback_data="xmah106 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الماعون 🕋", callback_data="xmah107 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الكوثر 🕋", callback_data="xmah108 " + str(m.from_user.id))],
        [InlineKeyboardButton("الكافرون 🕋", callback_data="xmah109 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النصر 🕋", callback_data="xmah110 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المسد 🕋", callback_data="xmah111 " + str(m.from_user.id))],
        [InlineKeyboardButton("الاخلاص 🕋", callback_data="xmah112 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفلق 🕋", callback_data="xmah113 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الناس 🕋", callback_data="xmah114 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="maher " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اختر سوره للقارئ ماهر المعيقلي\n√", reply_markup=keyboard, disable_web_page_preview=True)


@Client.on_callback_query(filters.regex("^xmah1 (\\d+)$"))
async def xmah1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2749", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah2 (\\d+)$"))
async def xmah2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2750", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah3 (\\d+)$"))
async def xmah3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2751", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah4 (\\d+)$"))
async def xmah4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2752", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah5 (\\d+)$"))
async def xmah5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2753", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah6 (\\d+)$"))
async def xmah6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2754", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah7 (\\d+)$"))
async def xmah7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2755", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah8 (\\d+)$"))
async def xmah8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2756", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah9 (\\d+)$"))
async def xmah9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2757", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah10 (\\d+)$"))
async def xmah10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2758", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah11 (\\d+)$"))
async def xmah11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2759", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah12 (\\d+)$"))
async def xmah12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2760", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah13 (\\d+)$"))
async def xmah13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2761", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah14 (\\d+)$"))
async def xmah14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2762", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah15 (\\d+)$"))
async def xmah15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2763", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah16 (\\d+)$"))
async def xmah16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2764", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah17 (\\d+)$"))
async def xmah17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2765", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah18 (\\d+)$"))
async def xmah18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2766", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah19 (\\d+)$"))
async def xmah19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2767", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah20 (\\d+)$"))
async def xmah20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2768", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah21 (\\d+)$"))
async def xmah21(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2769", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah22 (\\d+)$"))
async def xmah22(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2770", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah23 (\\d+)$"))
async def xmah23(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2771", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah24 (\\d+)$"))
async def xmah24(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2772", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah25 (\\d+)$"))
async def xmah25(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2773", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah26 (\\d+)$"))
async def xmah26(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2774", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah27 (\\d+)$"))
async def xmah27(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2775", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah28 (\\d+)$"))
async def xmah28(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2776", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah29 (\\d+)$"))
async def xmah29(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2777", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah30 (\\d+)$"))
async def xmah30(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2778", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah31 (\\d+)$"))
async def xmah31(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2779", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah32 (\\d+)$"))
async def xmah32(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2780", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah33 (\\d+)$"))
async def xmah33(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2781", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah34 (\\d+)$"))
async def xmah34(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2782", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah35 (\\d+)$"))
async def xmah35(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2783", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah36 (\\d+)$"))
async def xmah36(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2784", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah37 (\\d+)$"))
async def xmah37(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2785", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah38 (\\d+)$"))
async def xmah38(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2786", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah39 (\\d+)$"))
async def xmah39(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2787", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah40 (\\d+)$"))
async def xmah40(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2788", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah41 (\\d+)$"))
async def xmah41(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2789", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah42 (\\d+)$"))
async def xmah42(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2790", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah43 (\\d+)$"))
async def xmah43(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2791", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah44 (\\d+)$"))
async def xmah44(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2792", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah45 (\\d+)$"))
async def xmah45(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2793", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah46 (\\d+)$"))
async def xmah46(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2794", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah47 (\\d+)$"))
async def xmah47(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2795", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah48 (\\d+)$"))
async def xmah48(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2796", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah49 (\\d+)$"))
async def xmah49(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2797", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah50 (\\d+)$"))
async def xmah50(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2798", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah51 (\\d+)$"))
async def xmah51(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2799", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah52 (\\d+)$"))
async def xmah52(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2800", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah53 (\\d+)$"))
async def xmah53(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2801", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah54 (\\d+)$"))
async def xmah54(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2802", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah55 (\\d+)$"))
async def xmah55(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2803", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah56 (\\d+)$"))
async def xmah56(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2804", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah57 (\\d+)$"))
async def xmah57(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2805", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah58 (\\d+)$"))
async def xmah58(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2806", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah59 (\\d+)$"))
async def xmah59(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2807", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah60 (\\d+)$"))
async def xmah60(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2808", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah61 (\\d+)$"))
async def xmah61(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2809", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah62 (\\d+)$"))
async def xmah62(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2810", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah63 (\\d+)$"))
async def xmah63(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2811", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah64 (\\d+)$"))
async def xmah64(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2812", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah65 (\\d+)$"))
async def xmah65(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2813", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah66 (\\d+)$"))
async def xmah66(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2814", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah67 (\\d+)$"))
async def xmah67(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2815", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah68 (\\d+)$"))
async def xmah68(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2816", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah69 (\\d+)$"))
async def xmah69(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2817", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah70 (\\d+)$"))
async def xmah70(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2818", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah71 (\\d+)$"))
async def xmah71(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2819", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah72 (\\d+)$"))
async def xmah72(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2820", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah73 (\\d+)$"))
async def xmah73(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2821", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah74 (\\d+)$"))
async def xmah74(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2822", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah75 (\\d+)$"))
async def xmah75(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2823", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah76 (\\d+)$"))
async def xmah76(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2824", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah77 (\\d+)$"))
async def xmah77(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2825", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah78 (\\d+)$"))
async def xmah78(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2826", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah79 (\\d+)$"))
async def xmah79(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2827", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah80 (\\d+)$"))
async def xmah80(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2828", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah81 (\\d+)$"))
async def xmah81(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2829", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah82 (\\d+)$"))
async def xmah82(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2830", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah83 (\\d+)$"))
async def xmah83(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2831", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah84 (\\d+)$"))
async def xmah84(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2832", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah85 (\\d+)$"))
async def xmah85(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2833", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah86 (\\d+)$"))
async def xmah86(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2834", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah87 (\\d+)$"))
async def xmah87(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2835", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah88 (\\d+)$"))
async def xmah88(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2836", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah89 (\\d+)$"))
async def xmah89(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2837", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah90 (\\d+)$"))
async def xmah90(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2838", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah91 (\\d+)$"))
async def xmah91(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2839", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah92 (\\d+)$"))
async def xmah92(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2840", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah93 (\\d+)$"))
async def xmah93(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2841", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah94 (\\d+)$"))
async def xmah94(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2842", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah95 (\\d+)$"))
async def xmah95(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2843", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah96 (\\d+)$"))
async def xmah96(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2844", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah97 (\\d+)$"))
async def xmah97(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2845", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah98 (\\d+)$"))
async def xmah98(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2846", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah99 (\\d+)$"))
async def xmah99(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2847", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah100 (\\d+)$"))
async def xmah100(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2848", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah101 (\\d+)$"))
async def xmah101(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2849", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah102 (\\d+)$"))
async def xmah102(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2850", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah103 (\\d+)$"))
async def xmah103(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2851", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah104 (\\d+)$"))
async def xmah104(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2852", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah105 (\\d+)$"))
async def xmah105(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2853", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah106 (\\d+)$"))
async def xmah106(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2854", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah107 (\\d+)$"))
async def xmah107(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2855", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah108 (\\d+)$"))
async def xmah108(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2856", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah109 (\\d+)$"))
async def xmah109(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2857", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah110 (\\d+)$"))
async def xmah110(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2858", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah111 (\\d+)$"))
async def xmah111(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2859", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah112 (\\d+)$"))
async def xmah112(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2860", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah113 (\\d+)$"))
async def xmah113(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2861", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xmah114 (\\d+)$"))
async def xmah114(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/2862", reply_to_message_id=mid)


########################################################################################################################
########################################################################################################################


@Client.on_callback_query(filters.regex("^galel (\\d+)$"))
async def galel(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("الفاتحه 🕋", callback_data="xgal1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البقرة 🕋", callback_data="xgal2 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ال عمران 🕋", callback_data="xgal3 " + str(m.from_user.id))],
        [InlineKeyboardButton("النساء 🕋", callback_data="xgal4 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المائدة 🕋", callback_data="xgal5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الانعام 🕋", callback_data="xgal6 " + str(m.from_user.id))],
        [InlineKeyboardButton("الأعراف 🕋", callback_data="xgal7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الأنفال 🕋", callback_data="xgal8 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التوبة 🕋", callback_data="xgal9 " + str(m.from_user.id))],
        [InlineKeyboardButton("يونس 🕋", callback_data="xgal10 " + str(m.from_user.id))] +
        [InlineKeyboardButton("هود 🕋", callback_data="xgal11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يوسف 🕋", callback_data="xgal12 " + str(m.from_user.id))],
        [InlineKeyboardButton("الرعد 🕋", callback_data="xgal13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("أبراهيم 🕋", callback_data="xgal14 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحجر 🕋", callback_data="xgal15 " + str(m.from_user.id))],
        [InlineKeyboardButton("النحل 🕋", callback_data="xgal16 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاسراء 🕋", callback_data="xgal17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الكهف 🕋", callback_data="xgal18 " + str(m.from_user.id))],
        [InlineKeyboardButton("مريم 🕋", callback_data="xgal19 " + str(m.from_user.id))] +
        [InlineKeyboardButton("طه 🕋", callback_data="xgal20 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الأنبياء 🕋", callback_data="xgal21 " + str(m.from_user.id))],
        [InlineKeyboardButton("الحج 🕋", callback_data="xgal22 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المؤمنون 🕋", callback_data="xgal23 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النور 🕋", callback_data="xgal24 " + str(m.from_user.id))],
        [InlineKeyboardButton("الفرقان 🕋", callback_data="xgal25 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الشعراء 🕋", callback_data="xgal26 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النحل 🕋", callback_data="xgal27 " + str(m.from_user.id))],
        [InlineKeyboardButton("القصص 🕋", callback_data="xgal28 " + str(m.from_user.id))] +
        [InlineKeyboardButton("العنكبوت 🕋", callback_data="xgal29 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الروم 🕋", callback_data="xgal30 " + str(m.from_user.id))],
        [InlineKeyboardButton("لقمان 🕋", callback_data="xgal31 " + str(m.from_user.id))] +
        [InlineKeyboardButton("السجدة 🕋", callback_data="xgal32 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاحزاب 🕋", callback_data="xgal33 " + str(m.from_user.id))],
        [InlineKeyboardButton("سبأ 🕋", callback_data="xgal34 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فاطر 🕋", callback_data="xgal35 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يس 🕋", callback_data="xgal36 " + str(m.from_user.id))],
        [InlineKeyboardButton("الصافات 🕋", callback_data="xgal37 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ص 🕋", callback_data="xgal38 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الزمر 🕋", callback_data="xgal39 " + str(m.from_user.id))],
        [InlineKeyboardButton("غافر 🕋", callback_data="xgal40 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فصلت 🕋", callback_data="xgal41 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الشورئ 🕋", callback_data="xgal42 " + str(m.from_user.id))],
        [InlineKeyboardButton("الزخرف 🕋", callback_data="xgal43 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الدخان 🕋", callback_data="xgal44 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجاثيه 🕋", callback_data="xgal45 " + str(m.from_user.id))],
        [InlineKeyboardButton("الاحقاف 🕋", callback_data="xgal46 " + str(m.from_user.id))] +
        [InlineKeyboardButton("محمد 🕋", callback_data="xgal47 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفتح 🕋", callback_data="xgal48 " + str(m.from_user.id))],
        [InlineKeyboardButton("الحجرات 🕋", callback_data="xgal49 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ق 🕋", callback_data="xgal50 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الذاريات 🕋", callback_data="xgal51 " + str(m.from_user.id))],

        [InlineKeyboardButton("➡️ التالي", callback_data="galel2 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="quran2 " + str(m.from_user.id))]
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اختر سوره للقارئ خالد عبدالجليل\n√", reply_markup=keyboard, disable_web_page_preview=True)


@Client.on_callback_query(filters.regex("^galel2 (\\d+)$"))
async def galel2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("الطور 🕋", callback_data="xgal52 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النجم 🕋", callback_data="xgal53 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القمر 🕋", callback_data="xgal54 " + str(m.from_user.id))],
        [InlineKeyboardButton("الرحمن 🕋", callback_data="xgal55 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الواقعه 🕋", callback_data="xgal56 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحديد 🕋", callback_data="xgal57 " + str(m.from_user.id))],
        [InlineKeyboardButton("المجادلة 🕋", callback_data="xgal58 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحشر 🕋", callback_data="xgal59 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الممتحنة 🕋", callback_data="xgal60 " + str(m.from_user.id))],
        [InlineKeyboardButton("الصف 🕋", callback_data="xgal61 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجمعة 🕋", callback_data="xgal62 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المنافقون 🕋", callback_data="xgal63 " + str(m.from_user.id))],
        [InlineKeyboardButton("التغابن 🕋", callback_data="xgal64 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الطلاق 🕋", callback_data="xgal65 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التحريم 🕋", callback_data="xgal66 " + str(m.from_user.id))],
        [InlineKeyboardButton("الملك 🕋", callback_data="xgal67 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القلم 🕋", callback_data="xgal68 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحاقة 🕋", callback_data="xgal69 " + str(m.from_user.id))],
        [InlineKeyboardButton("المعارج 🕋", callback_data="xgal70 " + str(m.from_user.id))] +
        [InlineKeyboardButton("نوح 🕋", callback_data="xgal71 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجن 🕋", callback_data="xgal72 " + str(m.from_user.id))],
        [InlineKeyboardButton("المزمل 🕋", callback_data="xgal73 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المدثر 🕋", callback_data="xgal74 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القيامة 🕋", callback_data="xgal75 " + str(m.from_user.id))],
        [InlineKeyboardButton("الانسان 🕋", callback_data="xgal76 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المرسلات 🕋", callback_data="xgal77 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النبأ 🕋", callback_data="xgal78 " + str(m.from_user.id))],
        [InlineKeyboardButton("النازعات 🕋", callback_data="xgal79 " + str(m.from_user.id))] +
        [InlineKeyboardButton("عبس 🕋", callback_data="xgal80 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التكوير 🕋", callback_data="xgal81 " + str(m.from_user.id))],
        [InlineKeyboardButton("الانفطار 🕋", callback_data="xgal82 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المطففين 🕋", callback_data="xgal83 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الانشقاق 🕋", callback_data="xgal84 " + str(m.from_user.id))],
        [InlineKeyboardButton("البروج 🕋", callback_data="xgal85 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الطارق 🕋", callback_data="xgal86 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاعلي 🕋", callback_data="xgal87 " + str(m.from_user.id))],
        [InlineKeyboardButton("الغاشية 🕋", callback_data="xgal88 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفجر 🕋", callback_data="xgal89 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البلد 🕋", callback_data="xgal90 " + str(m.from_user.id))],
        [InlineKeyboardButton("الشمس 🕋", callback_data="xgal91 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الليل 🕋", callback_data="xgal92 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الضحئ 🕋", callback_data="xgal93 " + str(m.from_user.id))],
        [InlineKeyboardButton("الشرح 🕋", callback_data="xgal94 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التين 🕋", callback_data="xgal95 " + str(m.from_user.id))] +
        [InlineKeyboardButton("العلق 🕋", callback_data="xgal96 " + str(m.from_user.id))],
        [InlineKeyboardButton("القدر 🕋", callback_data="xgal97 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البينة 🕋", callback_data="xgal98 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الزلزلة 🕋", callback_data="xgal99 " + str(m.from_user.id))],
        [InlineKeyboardButton("العاديات 🕋", callback_data="xgal100 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القارعة 🕋", callback_data="xgal101 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التكاثر 🕋", callback_data="xgal102 " + str(m.from_user.id))],
        [InlineKeyboardButton("العصر 🕋", callback_data="xgal103 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الهمزة 🕋", callback_data="xgal104 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفيل 🕋", callback_data="xgal105 " + str(m.from_user.id))],
        [InlineKeyboardButton("قريش 🕋", callback_data="xgal106 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الماعون 🕋", callback_data="xgal107 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الكوثر 🕋", callback_data="xgal108 " + str(m.from_user.id))],
        [InlineKeyboardButton("الكافرون 🕋", callback_data="xgal109 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النصر 🕋", callback_data="xgal110 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المسد 🕋", callback_data="xgal111 " + str(m.from_user.id))],
        [InlineKeyboardButton("الاخلاص 🕋", callback_data="xgal112 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفلق 🕋", callback_data="xgal113 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الناس 🕋", callback_data="xgal114 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="galel " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اختر سوره للقارئ خالد عبدالجيل\n√", reply_markup=keyboard, disable_web_page_preview=True)


@Client.on_callback_query(filters.regex("^xgal1 (\\d+)$"))
async def xgal1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3697", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal2 (\\d+)$"))
async def xgal2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3698", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal3 (\\d+)$"))
async def xgal3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3699", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal4 (\\d+)$"))
async def xgal4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3700", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal5 (\\d+)$"))
async def xgal5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3701", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal6 (\\d+)$"))
async def xgal6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3702", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal7 (\\d+)$"))
async def xgal7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3703", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal8 (\\d+)$"))
async def xgal8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3704", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal9 (\\d+)$"))
async def xgal9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3705", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal10 (\\d+)$"))
async def xgal10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3706", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal11 (\\d+)$"))
async def xgal11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3707", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal12 (\\d+)$"))
async def xgal12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3708", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal13 (\\d+)$"))
async def xgal13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3709", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal14 (\\d+)$"))
async def xgal14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3710", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal15 (\\d+)$"))
async def xgal15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3711", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal16 (\\d+)$"))
async def xgal16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3712", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal17 (\\d+)$"))
async def xgal17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3713", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal18 (\\d+)$"))
async def xgal18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3714", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal19 (\\d+)$"))
async def xgal19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3715", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal20 (\\d+)$"))
async def xgal20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3716", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal21 (\\d+)$"))
async def xgal21(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3717", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal22 (\\d+)$"))
async def xgal22(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3718", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal23 (\\d+)$"))
async def xgal23(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3719", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal24 (\\d+)$"))
async def xgal24(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3720", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal25 (\\d+)$"))
async def xgal25(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3721", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal26 (\\d+)$"))
async def xgal26(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3722", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal27 (\\d+)$"))
async def xgal27(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3723", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal28 (\\d+)$"))
async def xgal28(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3724", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal29 (\\d+)$"))
async def xgal29(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3725", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal30 (\\d+)$"))
async def xgal30(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3726", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal31 (\\d+)$"))
async def xgal31(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3727", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal32 (\\d+)$"))
async def xgal32(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3728", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal33 (\\d+)$"))
async def xgal33(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3729", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal34 (\\d+)$"))
async def xgal34(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3730", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal35 (\\d+)$"))
async def xgal35(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3731", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal36 (\\d+)$"))
async def xgal36(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3732", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal37 (\\d+)$"))
async def xgal37(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3733", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal38 (\\d+)$"))
async def xgal38(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3734", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal39 (\\d+)$"))
async def xgal39(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3735", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal40 (\\d+)$"))
async def xgal40(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3736", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal41 (\\d+)$"))
async def xgal41(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3737", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal42 (\\d+)$"))
async def xgal42(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3738", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal43 (\\d+)$"))
async def xgal43(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3739", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal44 (\\d+)$"))
async def xgal44(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3740", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal45 (\\d+)$"))
async def xgal45(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3741", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal46 (\\d+)$"))
async def xgal46(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3742", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal47 (\\d+)$"))
async def xgal47(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3743", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal48 (\\d+)$"))
async def xgal48(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3744", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal49 (\\d+)$"))
async def xgal49(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3745", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal50 (\\d+)$"))
async def xgal50(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3746", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal51 (\\d+)$"))
async def xgal51(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3747", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal52 (\\d+)$"))
async def xgal52(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3748", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal53 (\\d+)$"))
async def xgal53(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3749", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal54 (\\d+)$"))
async def xgal54(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3750", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal55 (\\d+)$"))
async def xgal55(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3751", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal56 (\\d+)$"))
async def xgal56(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3752", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal57 (\\d+)$"))
async def xgal57(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3753", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal58 (\\d+)$"))
async def xgal58(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3754", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal59 (\\d+)$"))
async def xgal59(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3755", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal60 (\\d+)$"))
async def xgal60(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3756", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal61 (\\d+)$"))
async def xgal61(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3757", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal62 (\\d+)$"))
async def xgal62(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3758", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal63 (\\d+)$"))
async def xgal63(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3759", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal64 (\\d+)$"))
async def xgal64(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3760", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal65 (\\d+)$"))
async def xgal65(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3761", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal66 (\\d+)$"))
async def xgal66(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3762", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal67 (\\d+)$"))
async def xgal67(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3763", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal68 (\\d+)$"))
async def xgal68(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3764", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal69 (\\d+)$"))
async def xgal69(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3765", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal70 (\\d+)$"))
async def xgal70(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3766", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal71 (\\d+)$"))
async def xgal71(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3767", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal72 (\\d+)$"))
async def xgal72(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3768", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal73 (\\d+)$"))
async def xgal73(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3769", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal74 (\\d+)$"))
async def xgal74(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3770", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal75 (\\d+)$"))
async def xgal75(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3771", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal76 (\\d+)$"))
async def xgal76(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3772", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal77 (\\d+)$"))
async def xgal77(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3773", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal78 (\\d+)$"))
async def xgal78(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3774", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal79 (\\d+)$"))
async def xgal79(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3775", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal80 (\\d+)$"))
async def xgal80(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3776", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal81 (\\d+)$"))
async def xgal81(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3777", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal82 (\\d+)$"))
async def xgal82(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3778", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal83 (\\d+)$"))
async def xgal83(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3779", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal84 (\\d+)$"))
async def xgal84(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3780", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal85 (\\d+)$"))
async def xgal85(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3781", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal86 (\\d+)$"))
async def xgal86(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3782", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal87 (\\d+)$"))
async def xgal87(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3783", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal88 (\\d+)$"))
async def xgal88(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3784", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal89 (\\d+)$"))
async def xgal89(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3785", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal90 (\\d+)$"))
async def xgal90(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3786", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal91 (\\d+)$"))
async def xgal91(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3787", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal92 (\\d+)$"))
async def xgal92(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3788", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal93 (\\d+)$"))
async def xgal93(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3789", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal94 (\\d+)$"))
async def xgal94(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3790", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal95 (\\d+)$"))
async def xgal95(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3791", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal96 (\\d+)$"))
async def xgal96(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3792", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal97 (\\d+)$"))
async def xgal97(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3793", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal98 (\\d+)$"))
async def xgal98(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3794", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal99 (\\d+)$"))
async def xgal99(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3795", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal100 (\\d+)$"))
async def xgal100(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3796", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal101 (\\d+)$"))
async def xgal101(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3797", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal102 (\\d+)$"))
async def xgal102(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3798", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal103 (\\d+)$"))
async def xgal103(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3799", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal104 (\\d+)$"))
async def xgal104(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3800", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal105 (\\d+)$"))
async def xgal105(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3801", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal106 (\\d+)$"))
async def xgal106(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3802", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal107 (\\d+)$"))
async def xgal107(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3803", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal108 (\\d+)$"))
async def xgal108(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3804", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal109 (\\d+)$"))
async def xgal109(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3805", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal110 (\\d+)$"))
async def xgal110(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3806", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal111 (\\d+)$"))
async def xgal111(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3807", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal112 (\\d+)$"))
async def xgal112(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3808", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal113 (\\d+)$"))
async def xgal113(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3809", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xgal114 (\\d+)$"))
async def xgal114(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/MP3_QURAN/3810", reply_to_message_id=mid)

################################
## Dev By: @WWWL5 & @MRv7x  ##
################################

########################################################################################################################
########################################################################################################################
