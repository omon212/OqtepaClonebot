import logging
from aiogram import executor
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode
from Keyboards.inline import asosiy_menyu, ortga1, snakes, qarsildoq_oyoqlar, savat
from Keyboards.inline import salats
from Keyboards.default import buyurtma_berish, locations
from aiogram.types import ReplyKeyboardRemove
API_TOKEN = '6044644610:AAGH3mQRdCHeT6CbqY1XvkhjXP21nOe9cAc'


logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN,parse_mode='HTML')
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands='start')
async def boshlaovchi(message: types.Message):
    await message.answer('Buyurtmani birga joylashtiramizmi? 🤗', reply_markup=ReplyKeyboardRemove())
    await message.answer('''
Buyurtma berishni boshlash uchun 🛒 Buyurtma qilish tugmasini bosing
 
Shuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin
''', reply_markup=asosiy_menyu)


@dp.callback_query_handler(text='Buyurtma')
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
@dp.message_handler(text='⬅️Ortga')
async def exit(message: types.Message):
    await message.answer('Buyurtmani birga joylashtiramizmi? 🤗')
    await message.answer('''
        Buyurtma berishni boshlash uchun 🛒 Buyurtma qilish tugmasini bosing

        Shuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin
        ''', reply_markup=asosiy_menyu,)

@dp.message_handler(text = 'Eltib berish🛵')
async def loc_user(message: types.Message):
    await message.answer("<b>Eltib berish</b> uchun <b>geo-joylashuvni</b> jo'nating yoki manzilni tanlang",reply_markup=locations)

@dp.message_handler(text = '⬅️ Ortga')
async def exit2(message: types.Message):
    await message.answer('Orqaga qaytildi',reply_markup=buyurtma_berish)

@dp.message_handler(content_types=types.ContentType.LOCATION)
async def location_saver(message: types.Message):
    await message.answer('Locatsiya qabul qilindi')
    await message.answer_photo(photo=url,reply_markup=snakes)




url = 'https://www.google.com/imgres?imgurl=https%3A%2F%2Flookaside.fbsbx.com%2Flookaside%2Fcrawler%2Fmedia%2F%3Fmedia_id%3D3671245452904393&tbnid=aKgnDuWBwiZpAM&vet=12ahUKEwi_ktHHl9CAAxXGGRAIHQ89CPIQMygDegUIARDEAQ..i&imgrefurl=https%3A%2F%2Fwww.facebook.com%2Foqtepalavash.official%2Fposts%2F%25D0%25BB%25D1%2583%25D1%2587%25D1%2588%25D0%25B8%25D0%25B5-%25D0%25B2%25D1%258B%25D1%2585%25D0%25BE%25D0%25B4%25D0%25BD%25D1%258B%25D0%25B5-%25D1%258D%25D1%2582%25D0%25BE-%25D0%25B2%25D0%25BA%25D1%2583%25D1%2581%25D0%25BD%25D1%258B%25D0%25B5-%25D0%25B2%25D1%258B%25D1%2585%25D0%25BE%25D0%25B4%25D0%25BD%25D1%258B%25D0%25B5%25D0%25B5%25D1%2589%25D0%25B5-%25D0%25B8-%25D1%2581-%25D0%25BA%25D1%2580%25D1%2583%25D1%2582%25D0%25BE%25D0%25B9-%25D0%25B0%25D0%25BA%25D1%2586%25D0%25B8%25D0%25B5%25D0%25B9-%25D1%258D%25D1%2582%25D0%25BE-%25D0%25BF%25D1%2580%25D0%25BE%25D1%2581%25D1%2582%25D0%25BE-%25D0%25BC%25D0%25BC%25D0%25BC%25D0%25BC%25D0%25BF%25D1%2580%25D0%25B8-%25D0%25B7%25D0%25B0%25D0%25BA%2F3671245579571047%2F&docid=ZWcv7cV_GJ2WaM&w=2048&h=1600&q=oq%20tepa%20lavash%20image%20buyurtma%20bering&ved=2ahUKEwi_ktHHl9CAAxXGGRAIHQ89CPIQMygDegUIARDEAQ'

@dp.callback_query_handler(text='tovuq')
async def tovuqlar(call: types.CallbackQuery):
    await call.message.answer_photo(photo=url)
    await call.message.answer("🍗Qarsildoq Jojalar",reply_markup=qarsildoq_oyoqlar)

@dp.callback_query_handler(text='box')
async def box(call: types.CallbackQuery):
    await call.message.answer_photo(photo=url)
    await call.message.answer('''
    Jo'ja box
Narxi:   26 000 so'm
Tavsif: Strips 3 dona, kartoshka fri o'rta va ketchup
Miqdorini tanlang yoki kiriting
    ''',reply_markup=jojacha)

xech_nima = ''
@dp.callback_query_handler(text='ortga3')
async def ortga(call: types.CallbackQuery):
    await call.message.answer_photo(photo=url)
    await call.message.answer("🍗Qarsildoq Jojalar",reply_markup=qarsildoq_oyoqlar)

@dp.callback_query_handler(text='stips')
async def stips(call: types.CallbackQuery):
    await call.message.answer_photo(url)
    await call.message.answer('''
    Stips 5 dona
Narxi:   26 000 so'm
Tavsif: Qarsildoq panirovkadagi uzun shaklda kesilgan tovuq bo'laklari
Miqdorini tanlang yoki kiriting
    ''',reply_markup=jojacha)


@dp.callback_query_handler(text='stip')
async def stips(call: types.CallbackQuery):
    await call.message.answer_photo(url)
    await call.message.answer('''
    Stips 3 dona
Narxi:   16 000 so'm
Tavsif: Qarsildoq panirovkadagi uzun shaklda kesilgan tovuq bo'laklari
Miqdorini tanlang yoki kiriting
    ''',reply_markup=jojacha)


@dp.callback_query_handler(text='bayt')
async def stips(call: types.CallbackQuery):
    await call.message.answer_photo(url)
    await call.message.answer('''
    Stips 3 dona
Narxi:   16 000 so'm
Tavsif: Qarsildoq panirovkadagi uzun shaklda kesilgan tovuq bo'laklari
Miqdorini tanlang yoki kiriting
    ''',reply_markup=jojacha)

@dp.callback_query_handler(text='ortga2')
async def ortga2(call: types.CallbackQuery):
    await call.message.answer_photo(photo=url,reply_markup=snakes,)



@dp.callback_query_handler(text='salat')
async def salat(call: types.CallbackQuery):
    await call.message.answer_photo(photo=url)
    await call.message.answer("🥗 Salatlar",reply_markup=salats)

@dp.callback_query_handler(text='kapriz')
async def kap(call: types.CallbackQuery):
    await call.message.answer_photo(url)
    await call.message.answer('''
    Mujskoy kapriz
Narxi:   25 000 so'm
Tavsif: Dudlangan kolbasa, kurka, qazi, pishloq, mayonez
Miqdorini tanlang yoki kiriting
    ''',reply_markup=savat)

@dp.callback_query_handler(text='sezat')
async def kap(call: types.CallbackQuery):
    await call.message.answer_photo(photo=url)
    await call.message.answer('''
    Sezar
Narxi:   23 000 so'm
Tavsif: Tovuq filesi, pomidor, aysberg, pishloq, kruton, sarimsoq sousi.
Miqdorini tanlang yoki kiriting
    ''')

@dp.callback_query_handler(text='ortga4')
async def ort(call: types.CallbackQuery):
    await call.message.answer_photo(photo=url)
    await call.message.answer('', reply_markup=snakes)






if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
