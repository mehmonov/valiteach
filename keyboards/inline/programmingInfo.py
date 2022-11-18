from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

proInfo = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="dasturlash asoslari",callback_data="beginner"),
        InlineKeyboardButton(text="javascipt",callback_data="javascipt"),
    ],
    [
        InlineKeyboardButton(text="React js",callback_data="react"),
        InlineKeyboardButton(text="Php",callback_data="php"),
    ],
    [
        InlineKeyboardButton(text="Python asoslari",callback_data="pybeginner"),
        InlineKeyboardButton(text="Telegram bot",callback_data="tgbot"),
    ],
    [
        InlineKeyboardButton(text="Ortga qaytish",callback_data='cancel')
    ]
    ]
)