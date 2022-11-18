import logging
from keyboards.inline.course import courseCategory
from keyboards.inline.programmingInfo import proInfo
from keyboards.inline.beginnerStart import beginnerStart
from aiogram.types import Message, CallbackQuery
from loader import dp

@dp.callback_query_handler(text="cancel")
async def cancel(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=courseCategory)
    await call.message.answer('')