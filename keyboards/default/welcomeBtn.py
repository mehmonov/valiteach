from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📚 Kurslar haqida'),
            KeyboardButton(text='💡 Grand uchun ro\'yhatdan o\'tish')
        ],
    ],
    resize_keyboard=True
)