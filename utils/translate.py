from googletrans import Translator
translator = Translator()



async def get_english(text_en):
    try:
        txt_en = (translator.translate(text_en, dest='en').text)
    except:
        txt_en = "No such sentence found"
    return txt_en


async def get_uzbek(text_uz):
    try:
        txt_uz = translator.translate(text_uz, dest='uz').text
    except:
        txt_uz = "Bunday jumla topilmadi!"
    return txt_uz


async def get_ruskiy(text_ru):
    try:
        txt_ru = translator.translate(text_ru, dest='ru').text
    except:
        txt_ru = "Это предложение не найдено!"
    return txt_ru


async def get_arab(text_ar):
    try:
        txt_ar = translator.translate(text_ar, dest='ar').text
    except:
        txt_ar = "!لم يتم العثور على هذا العرض."
    return txt_ar


async def get_tojik(text_tj):
    try:
        txt_tj = translator.translate(text_tj, dest='tg').text
    except:
        txt_tj = "Ин пешниҳод ёфт нашуд!"
    return txt_tj
