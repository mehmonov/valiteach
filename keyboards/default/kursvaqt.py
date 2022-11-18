from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kursvaqt = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Abetdan oldin"),
            KeyboardButton(text="Abetdan keyin"),
            KeyboardButton(text="Farqi yo'q"),
        ],
    ],
    resize_keyboard=True
)