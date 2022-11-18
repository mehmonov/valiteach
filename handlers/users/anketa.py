from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
# from getData import sendData
from keyboards.default.tel2 import tel2
from keyboards.default.kursvaqt import kursvaqt
from keyboards.default.holat import holat
from loader import dp
from keyboards.default.welcomeBtn import menu
from keyboards.default.kurs import kurs
from states.personalData import PersonalData


@dp.message_handler(text='💡 Grand uchun ro\'yhatdan o\'tish')
async def enter(message: types.Message):
    await message.answer("Assalomu alaykum. Grafik dizayn va python telegram bot kurslari uchun grand tashkil qilinmoqda \n Iltimos ism va familiyangizni kiriting")
    await PersonalData.fullname.set()

@dp.message_handler(state=PersonalData.fullname)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname = message.text
    await state.update_data(
        {
            "fullname": fullname
        }
    )
    
    await PersonalData.next()
    await message.answer("Iltimos telefon raqamingizni kiriting kiriting")

@dp.message_handler(state=PersonalData.tel)
async def answer_tel(message: types.Message, state: FSMContext):
    tel = message.text
    await state.update_data(
        {
            "tel1": tel
        }
    
    )
    await message.answer("Yaxshi. Agar bu raqamga telefon qilib bog'lana olmasak, boshqa telefon raqam bormi biz bog'lanishimiz uchun? Bor bo'lsa o'shani kiriting. Agar ikkinchi raqam mavjud bo'lmasa shunchaki pastdagi tugmani bosing ", reply_markup=tel2)
    await PersonalData.next()
    
@dp.message_handler(state=PersonalData.tel2)
async def answer_tel2(message: types.Message, state: FSMContext):
    tel2 = message.text
    await state.update_data(
        {
            "tel2": tel2
        }
    )
    await message.answer("Yoshingizni kiriting")
    await PersonalData.next()
    
@dp.message_handler(state=PersonalData.yosh)
async def answer_yosh(message: types.Message, state: FSMContext):
    yosh = message.text
    await state.update_data(
        {
            "yosh": yosh
        }
    )
    await message.answer("Qaysi kurs uchun elon qilingan grandni yutmoqchisiz? ", reply_markup=kurs)
    await PersonalData.next()
    
    
@dp.message_handler(state=PersonalData.kurs)
async def answer_kurs(message: types.Message, state: FSMContext):
    kurs = message.text
    await state.update_data(
        {
            "kurs": kurs
        }
    )
    await message.answer("Sizga kurs uchun kunning qaysi yarmida bo'lgani yaxshi",reply_markup=kursvaqt)
    await PersonalData.next()
@dp.message_handler(state=PersonalData.vaqt)
async def answer_vaqt(message: types.Message, state: FSMContext):
    vaqt = message.text
    await state.update_data(
        {
            "vaqt": vaqt
        }
    )
    await message.answer("Siz o'qiysizmi yoki ishlaysizmi?",reply_markup=holat)
    await PersonalData.next()
    
    
@dp.message_handler(state=PersonalData.holat)
async def answer_holat(message: types.Message, state: FSMContext):
    holat = message.text
    await state.update_data(
        {
            "holat": holat
        }
    )
    await message.answer("Grand yutishdan maqsadingiz nima? Shu haqida yozing",reply_markup=ReplyKeyboardRemove())
    await PersonalData.next()
    
@dp.message_handler(state=PersonalData.maqsad)
async def answer_maqsad(message: types.Message, state: FSMContext):
    maqsad = message.text
    await state.update_data(
        {
            "maqsad": maqsad
        }
    )
    await message.answer("Vali-Teach o'quv markazi haqida qayerdan eshitdingiz? ")
    await PersonalData.next()
    
    
@dp.message_handler(state=PersonalData.vInfo)
async def answer_vinfo(message: types.Message, state: FSMContext):
    vInfo = message.text
    await state.update_data(
        {
            "vInfo": vInfo
        }
    )
    data = await state.get_data()
    fullname = data.get("fullname")
    tel1 = data.get("tel1")
    tel2 = data.get("tel2")
    yosh = data.get("yosh")
    vaqt = data.get("vaqt")
    holat = data.get("holat")
    maqsad = data.get("maqsad")
    vInfo = data.get("vInfo")
    
    msg  = f"<b>Foydalanuvchi  - {message.from_user.id}</b> \n"
    msg += f"Ism - {fullname} \n"
    msg += f"Tel1 - {tel1} \n"
    msg += f"Tel2 - {tel2} \n"
    msg += f"Yosh - {yosh} \n"
    msg += f"Vaqt - {vaqt} \n"
    msg += f"Holat - {holat} \n"
    msg += f"Maqsad - {maqsad} \n"
    msg += f"qayerdan eshitgan - {vInfo} \n"
    guruh = '-1001600163364'
    
    await dp.bot.send_message(guruh, msg)
    await message.answer("Tashakkur! \n Sizning malumotlaringiz tekshirish uchun yuborildi. Tez orada siz bilan aloqaga chiqamiz",reply_markup=menu)
    await state.finish()    



