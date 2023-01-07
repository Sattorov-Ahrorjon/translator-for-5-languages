from aiogram import types
from loader import dp, db, bot
from aiogram.dispatcher.filters import Text
from data.config import ADMINS
import time



@dp.message_handler(commands='admin')
async def bot_help(message: types.Message):
    text = (f"Bot yaratuvchisi {5}")
    await message.answer(text)


@dp.message_handler(commands='people', chat_id=ADMINS[0])
async def get_people(msg: types.Message):
    for i in db.select_all_users():
        await bot.send_message(chat_id=ADMINS[0], text=i)
        time.sleep(1)


@dp.message_handler(commands='count', chat_id=ADMINS[0])
async def get_count(msg: types.Message):
    await bot.send_message(chat_id=ADMINS[0], text=db.count_users()[0])


@dp.message_handler(Text(startswith='write'))
async def get_write(msg: types.Message):
    await bot.send_message(chat_id=int(msg.text[5:15]), text=msg.text[15:])


@dp.message_handler(commands='onn_off', chat_id=ADMINS[0])
async def get_reklama(msg: types.Message):
    cll = db.get_id()
    coll=0
    soll=0
    for i in cll:
        try:
            await bot.send_message(chat_id=i[0], text="Assalomu alaykum\nBu bot bilan ba'zi muammolar o'z yechimini topgan bo'lsa hursandmiz !")
            coll+=1
        except Exception as err:
            soll+=1
            pass
    await msg.reply(f"Online - {coll}, Block - {soll}")