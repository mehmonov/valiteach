from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

beginnerStart = InlineKeyboardMarkup(
    inline_keyboard=[
       [
         InlineKeyboardButton(text="Ro'yhattan o'tish",url='https://docs.google.com/forms/d/e/1FAIpQLSdRVPH3xxXYNBkn9xHt-uoWfsxBzm0lNyM3FMUg1cl90M342Q/viewform?usp=sf_link'),
       ],
       [
            InlineKeyboardButton(text="Ortga qaytish",callback_data='cancel')
       ]

    ]
)