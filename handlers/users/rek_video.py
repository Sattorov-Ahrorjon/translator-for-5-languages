from aiogram import types
from loader import dp, db, bot
from data.config import ADMINS
from aiogram.utils.markdown import hlink
from states.file_data import Video_Data
from aiogram.dispatcher import FSMContext



@dp.message_handler(chat_id=ADMINS[0], commands='reklama_video', state=None)
async def get_photo(message:types.Message):
    await message.reply("Video yuboring")
    await Video_Data.video_id.set()


@dp.message_handler(state=Video_Data.video_id, content_types=types.ContentTypes.VIDEO)
async def get_file_id(msg: types.Message, state : FSMContext):
    f_id = msg.video.file_id
    await state.update_data(
        {'id':f_id}
    )
    await msg.answer("Video osti matnini yuboring")
    await Video_Data.video_text.set()


@dp.message_handler(state=Video_Data.video_text)
async def get_file_text(msg:types.Message, state:FSMContext):
    msg_text = msg.text
    await state.update_data(
        {'text':msg_text}
    )
    await msg.answer(" Kanal yoki Guruh nomini kiriting")
    await Video_Data.video_channel_name.set()


@dp.message_handler(state=Video_Data.video_channel_name)
async def get_file_name(msg:types.Message, state:FSMContext):
    nomi = msg.text
    await state.update_data(
        {'name':nomi}
    )
    await msg.answer("Kanal yoki Guruh linkini kiriting")
    await Video_Data.video_channel_link.set()


@dp.message_handler(state=Video_Data.video_channel_link)
async def get_file_link(msg:types.Message, state:FSMContext):
    link = msg.text
    await state.update_data(
        {'link':link}
    )
    await msg.answer("Xabar to'liq yuklandi")
    data = await state.get_data()
    f_id = data.get('id')
    text = data.get('text')
    name = data.get('name')
    link = data.get('link')
    
    text += '\n\n' + hlink(name, link)
    
    a=0
    b=0 
    cl = db.get_id()
    for i in cl:
        try:
            await bot.send_video(chat_id=i[0], video=f_id, caption=text)
            a+=1
        except Exception as err:
            b+=1
    await bot.send_message(chat_id=ADMINS[0], text=f"Yuborildi {a} ta Yuborilmadi {b} ta")
    await state.finish()
