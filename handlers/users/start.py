from aiogram import types

from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.welcomeBtn import menu
from keyboards.inline.check import check_button
from utils.misc import obuna
from loader import bot, dp
@dp.message_handler(commands=['start'])
async def show_channels(message: types.Message):
    await message.answer(f"Assalomu alaykum. Quyidagi tugmalardan foydalaning \n \n <b> Grand haqida ma'lumot olish uchun ushbu kommandani bosing - /infoGrand </b>",reply_markup=menu)
    
@dp.message_handler(commands=['infoGrand'])
async def infoGrand(message: types.Message):
    await message.answer("Bilimlining qadri ham qaddi ham egilmaydi!\n \n 🚀Vali-Teach Siz azizlar uchun o'zining Web-dasturlash va Grafik dizayn kurslariga 5 tadan <b>GRAND</b> e'lon qiladi.\n \n🤓Grand yutish uchun nomzodlar quyidagi 3 bosqichli imtihonlardan o'tishlari zarur: \n\n 1-Ingliz tilini bilish darajasi\n 2-IQ darajasi \n3-Suxbat \n\n Ushbu imkoniyat foydalaning va bizning kurslarimizda <b>BEPUL</b> tahsil oling. \n  \n 👨‍🏫Kurs bitiruvchilariga Vali-Teach tomonidan yo'nalish bo'yicha ish topishga ko'maklashiladi.\n<b>☝️Biz uchun boy avlod emas bilimli avlod muhim!</b>\n💡Vali-Teach kelajaging uchun imkoniyat")


    # chennels_format = str()
    # for channel in CHANNELS:
    #     chat = await bot.get_chat(channel)
    #     invite_link = await chat.export_invite_link()
    #     chennels_format +=f"<a href='{invite_link}'>{chat.title}</a>\n"
    
    # await message.answer(f"Botdan foydalanishdan avval kanalga a'zo bo'ling: \n"
    #         f"{chennels_format}",
    #         reply_markup=check_button,
    #         disable_web_page_preview=True
    # )

# @dp.callback_query_handler(text="check")
# async def checker(call: types.CallbackQuery):
#     await call.answer()
#     result = str()
#     for channel in CHANNELS:
#         status = await obuna.check(user_id=call.from_user.id,
#             channel=channel
#             )
#         channel = await bot.get_chat(channel)
#         if status:
#             result +=(f"Bu kanalga obuna bo'ling {channel.title}." f"<a href='{invite_link}'>Obuna bo\'lish</a>\n\n")
#     await call.message.answer(result, disable_web_page_preview=True)
