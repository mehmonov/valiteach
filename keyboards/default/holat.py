from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

holat = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ishlayman"),
            KeyboardButton(text="O'qiyman"),
            KeyboardButton(text="Boshqa"),
        ],
    ],
    resize_keyboard=True
)