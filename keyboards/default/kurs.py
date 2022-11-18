from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kurs = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Python: telegram bot"),
            KeyboardButton(text="Grafik dizayn"),
           
        ],
    ],
    resize_keyboard=True
)