from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

courseCategory = InlineKeyboardMarkup(
    inline_keyboard=[
       [
         InlineKeyboardButton(text="Dasturlash",callback_data="programming"),
         InlineKeyboardButton(text="grafik dizayn",callback_data="design"),
       ]
    ]
)