from aiogram.types import KeyboardButton, ReplyKeyboardMarkup



menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='English'),
        ],
        
        [
            KeyboardButton(text="O'zbek"),
        ],
        
        [
            KeyboardButton(text='Pусский'),
        ],
            
        [
            KeyboardButton(text='Tоҷикӣ'),
        ],
        
        [
            KeyboardButton(text='عربى'),
        ]
    ],
    resize_keyboard=True
)



# b1 = KeyboardButton('/english')
# b2 = KeyboardButton('/o\'zbek')
# b3 = KeyboardButton('/русский')
# b4 = KeyboardButton('/عربى')
# b5 = KeyboardButton('/тоҷикӣ')
