import logging
from aiogram import executor
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode
from Keyboards.inline import asosiy_menyu, ortga1
from Keyboards.default import buyurtma_berish
from aiogram.types import ReplyKeyboardRemove
API_TOKEN = '6044644610:AAGH3mQRdCHeT6CbqY1XvkhjXP21nOe9cAc'

# Logging konfiguratsiyasi
logging.basicConfig(level=logging.INFO)

# Botni yaratish
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands='start')
async def boshlaovchi(message: types.Message):
    await message.answer('Buyurtmani birga joylashtiramizmi? 🤗')
    await message.answer('''
Buyurtma berishni boshlash uchun 🛒 Buyurtma qilish tugmasini bosing
 
Shuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin
''', reply_markup=asosiy_menyu)


@dp.callback_query_handler(text='buyurtma')
async def buyurtmalar(call: types.CallbackQuery):
    await call.answer('Buyurtma Bering❤️')
    await call.message.answer('Buyurtmani birga joylashtiramizmi? 🤗')
    await call.message.answer('Buyurtma turini tanlang', reply_markup=buyurtma_berish)


@dp.callback_query_handler(text='bizhaqqimizda')
async def biz(call: types.CallbackQuery):
    await call.message.answer('''
    
Biz O‘zbekiston bozorida 12 yildan beri faoliyat yuritamiz va bugungi kunda butun mamlakat bo‘ylab 50 dan ortiq filiallarimiz mavjud. Mazali va to‘yimli taomlar, qulay narxlar, tez yetkazib berish xizmatidan mamnun mijozlar yana va yana bizni tanlamoqda.

Qaynoqqina va mazali lavashlarimiz, shaurmayu donerlarimiz, gamburger va pitsalarimizdan albatta tatib ko'rishingizni tavsiya qilamiz va buyurtmangizga tovuq go'shtidan yangiliklarimizni qo'shishni unutmang!

Yetkazib berish xizmati:  +998781500030
Sayt (https://oqtepalavash.uz/) | Facebook (http://fb.me/oqtepalavash.official) | Instagram (https://www.instagram.com/oqtepalavash.official)   

 
''', reply_markup=ortga1)
@dp.callback_query_handler(text='ortga')
async def ortga(call: types.CallbackQuery):
    await call.message.answer('Buyurtmani birga joylashtiramizmi? 🤗')
    await call.message.answer('''
    Buyurtma berishni boshlash uchun 🛒 Buyurtma qilish tugmasini bosing

    Shuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin
    ''', reply_markup=asosiy_menyu)

@dp.message_handler(text = 'Ortga')
async def back(message: types.Message):
    await message.answer('ortga qaytildi',reply_markup=ReplyKeyboardRemove())
    await message.answer('''
    Buyurtma berishni boshlash uchun 🛒 Buyurtma qilish tugmasini bosing

    Shuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin
    ''', reply_markup=asosiy_menyu)





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
