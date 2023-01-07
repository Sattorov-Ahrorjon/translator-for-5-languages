from aiogram.dispatcher.filters import Text
from loader import dp, db
from aiogram import types
from keyboards.default.til_tanlash import menu
from utils import get_uzbek, get_arab, get_english, get_ruskiy, get_tojik


@dp.message_handler(Text('English'))
async def english(msg: types.Message):
    try:
        await msg.reply(text=await get_english(db.get_text(ind=msg.from_user.id, name=msg.from_user.full_name)[0]))
    except:
        await msg.answer("No such sentence found")


@dp.message_handler(Text("O'zbek"))
async def uzbek(msg: types.Message):
    try:
        await msg.reply(text=await get_uzbek(db.get_text(ind=msg.from_user.id, name=msg.from_user.full_name)[0]))
    except:
        await msg.answer("Bunday jumla topilmadi!")


@dp.message_handler(Text('Pусский'))
async def ruskiy(msg: types.Message):
    try:
        await msg.reply(text=await get_ruskiy(db.get_text(ind=msg.from_user.id, name=msg.from_user.full_name)[0]))
    except:
        await msg.answer("Это предложение не найдено!")


@dp.message_handler(Text('عربى'))
async def arab(msg: types.Message):
    try:
        await msg.reply(text=await get_arab(db.get_text(ind=msg.from_user.id, name=msg.from_user.full_name)[0]))
    except:
        await msg.answer("!لم يتم العثور على هذا العرض.")


@dp.message_handler(Text('Tоҷикӣ'))
async def tojik(msg: types.Message):
    try:
        await msg.reply(text=await get_tojik(db.get_text(ind=msg.from_user.id, name=msg.from_user.full_name)[0]))
    except:
        await msg.answer("Ин пешниҳод ёфт нашуд!")


@dp.message_handler()
async def get_text(message: types.Message):
    await message.reply("🇺🇿 Qaysi tilga tarjima qilasiz ?\n\n"
                        "🇬🇧 What language do you translate into?\n\n"
                        "🇹🇯 Шумо ба кадом забон тарҷума мекунед?\n\n"
                        "🇷🇺 На какой язык вы переводите?\n\n"
                        "🇸🇦 إلى أي لغة تترجم؟", reply_markup=menu)
    text = message.text
    db.add_text(text=text, id=message.from_user.id)

