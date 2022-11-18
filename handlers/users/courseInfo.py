import logging
from keyboards.inline.course import courseCategory
from keyboards.inline.programmingInfo import proInfo
from keyboards.inline.beginnerStart import beginnerStart

from aiogram.types import Message, CallbackQuery
from loader import dp

@dp.message_handler(text_contains="Kurslar haqida")
async def choose_course(message: Message):
    await message.answer(f"Kurslarni tanlang", reply_markup=courseCategory)

@dp.callback_query_handler(text='programming')
async def info_programming(call: CallbackQuery):
        await call.message.answer("Dasturlash kursi bir nechta bo\'limdan tashkil topgan. Siz o\'zingizga kerakli bo'lgan bo'limni tanlang", reply_markup=proInfo)
        await call.message.delete()
        await call.answer(cache_time=60)

@dp.callback_query_handler(text='javascipt')
async def info_programming(call: CallbackQuery):
        await call.message.answer("Ushbu kursda saytni interaktivroq qilishingiz mumkin", reply_markup=beginnerStart)
        await call.message.delete()
       
        await call.answer(cache_time=60)
@dp.callback_query_handler(text='react')
async def info_programming(call: CallbackQuery):
        await call.message.answer("Ushbu kursda saytni interaktivroq qilishingiz mumkin", reply_markup=beginnerStart)
        await call.message.delete()
        await call.answer(cache_time=60)
@dp.callback_query_handler(text='php')
async def info_programming(call: CallbackQuery):
        await call.message.answer("Ushbu kursda saytni interaktivroq qilishingiz mumkin", reply_markup=beginnerStart)
        await call.message.delete()
        
        await call.answer(cache_time=60)

@dp.callback_query_handler(text='pybeginner')
async def info_programming(call: CallbackQuery):
        await call.message.answer("Ushbu kursda butun dunyo bo'yicha juda mashhur bo'lgan python dasturlas tilini o'rganasiz", reply_markup=beginnerStart)
        await call.message.delete()
        await call.answer(cache_time=60)

@dp.callback_query_handler(text='tgbot')
async def info_programming(call: CallbackQuery):
        await call.message.answer("Ushbu kursda butun dunyo bo'yicha juda mashhur bo'lgan python dasturlas tilini o'rganasiz", reply_markup=beginnerStart)
        await call.message.delete()  
        await call.answer(cache_time=60)

@dp.callback_query_handler(text='beginner')
async def info_beginner(call: CallbackQuery):
    await call.message.answer('Ushbu kurs ikki oy davom etadi. Siz bu kurs davomida dasturlash asoslarini o\'rganasiz. Kursda web saytlarni dizaynni kod ko\'rinishiga o\'tkizishni ham ko\'rib chiqasiz',reply_markup=beginnerStart)
    await call.message.delete()
    
    await call.answer(cache_time=60)
@dp.callback_query_handler(text='design')
async def info_beginner(call: CallbackQuery):
    await call.message.answer('Ushbu kurs ikki oy davom etadi. Siz bu kurs davomida grafik dizayn asoslarini o\'rganasiz. Kursda web saytlarni dizaynni  ko\'rinishiga o\'tkizishni ham ko\'rib chiqasiz',reply_markup=beginnerStart)
    await call.message.delete()
    await call.answer(cache_time=60)
