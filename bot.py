import logging
from aiogram import executor
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode
from Keyboards.inline import asosiy_menyu, ortga1, snakes, qarsildoq_oyoqlar, savat, savat_salatlar
from Keyboards.inline import salats, ichimliklar_1, hot_tea, choylar, yaxna_water, pepsi_water, pepsi_savat, dolina_choy, burgers_savat, burgerlar
from Keyboards.inline import mirinda1, icetea, mountain, souslar, sous1, lavash_button, lavash_savat, setlar, set_savat, pitsa_savat, pitsa, shaurma
from Keyboards.inline import klab_sendvich, sneklar, sneks
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
    await message.answer('Locatsiya qabul qilindi',reply_markup=ReplyKeyboardRemove())
    photo = open('kategoriya.jpg', 'rb')
    await message.answer_photo(photo=photo)
    await message.answer("Kategoriyalrdan birini tanlang",reply_markup=snakes)




@dp.callback_query_handler(text='tovuq')
async def tovuqlar(call: types.CallbackQuery):
    photo = open('qarsildoq.jpg', 'rb')
    await call.message.answer_photo(photo=photo,)
    await call.message.answer("🍗Qarsildoq Jojalar",reply_markup=qarsildoq_oyoqlar)

@dp.callback_query_handler(text='box')
async def box(call: types.CallbackQuery):
    photo = open('JOJABOX.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
    Jo'ja box
Narxi:   26 000 so'm
Tavsif: Strips 3 dona, kartoshka fri o'rta va ketchup
Miqdorini tanlang yoki kiriting
    ''',reply_markup=savat)




@dp.callback_query_handler(text='stips')
async def stips(call: types.CallbackQuery):
    photo = open('stipsdona.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
    Stips 5 dona
Narxi:   26 000 so'm
Tavsif: Qarsildoq panirovkadagi uzun shaklda kesilgan tovuq bo'laklari
Miqdorini tanlang yoki kiriting
    ''',reply_markup=savat)


@dp.callback_query_handler(text='stip')
async def stips(call: types.CallbackQuery):
    photo = open('Stips3don.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
    Stips 3 dona
Narxi:   16 000 so'm
Tavsif: Qarsildoq panirovkadagi uzun shaklda kesilgan tovuq bo'laklari
Miqdorini tanlang yoki kiriting
    ''',reply_markup=savat)


@dp.callback_query_handler(text='bayt')
async def stips(call: types.CallbackQuery):
    photo = open('bayts.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
    Bayts
Narxi:   16 000 so'm
Tavsif: Qarsildoq panirovkadagi tovuq bo'laklari 
Miqdorini tanlang yoki kiriting
    ''',reply_markup=savat)





@dp.callback_query_handler(text='salat')
async def salat(call: types.CallbackQuery):
    photo = open('importtant_salat.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer("🥗 Salatlar",reply_markup=salats)

@dp.callback_query_handler(text='kapriz')
async def kap(call: types.CallbackQuery):
    photo = open('kapriz.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
    Mujskoy kapriz
Narxi:   25 000 so'm
Tavsif: Dudlangan kolbasa, kurka, qazi, pishloq, mayonez
Miqdorini tanlang yoki kiriting
    ''',reply_markup=savat_salatlar)

@dp.callback_query_handler(text='sezat')
async def kap(call: types.CallbackQuery):
    photo = open('sezar.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
    Sezar
Narxi:   23 000 so'm
Tavsif: Tovuq filesi, pomidor, aysberg, pishloq, kruton, sarimsoq sousi.
Miqdorini tanlang yoki kiriting
    ''',reply_markup=savat_salatlar)


@dp.callback_query_handler(text='salat_exit')
async def jojaexit(call: types.CallbackQuery):
    photo = open('importtant_salat.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer("🥗Salatlar",reply_markup=salats)

@dp.callback_query_handler(text='exits')
async def exits(call: types.CallbackQuery):
    photo = open('2023-08-10 14.15.12.jpg', 'rb')
    await call.message.answer_photo(photo=photo,reply_markup=snakes)
@dp.callback_query_handler(text='qarsildoq_exit')
async def qarsildoqexit(call: types.CallbackQuery):
    photo = open('kategoriya.jpg', 'rb')
    await call.message.answer_photo(photo=photo,reply_markup=snakes)


@dp.callback_query_handler(text='joja_exit')
async def jojaexit(call: types.CallbackQuery):
    photo = open('qarsildoq.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer("🍗Qarsildoq Jo'jalar",reply_markup=qarsildoq_oyoqlar)


@dp.callback_query_handler(text='ichimlik_cola')
async def ichimlik(call: types.CallbackQuery):
    photo = open('important.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer("🥤Ichimliklar",reply_markup=ichimliklar_1)

@dp.callback_query_handler(text='qaynoq_ichimlik')
async def qaynoq(call: types.CallbackQuery):
    photo = open('important1.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer("🥤Ichimliklar> Qaynoq ichimliklar", reply_markup=hot_tea)

@dp.callback_query_handler(text='qora')
async def qorachoy(call: types.CallbackQuery):
    photo = open('qora.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
    Qora choy
Narxi:   3 000 so'm
Tavsif: Qora choy
Miqdorini tanlang yoki kiriting''', reply_markup=choylar)

@dp.callback_query_handler(text='kok')
async def kokchoy(call:types.CallbackQuery):
    photo = open('2023-08-10 14.15.12.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
    Ko'k choy
Narxi:   3 000 so'm
Tavsif: Ko'k choy
Miqdorini tanlang yoki kiriting
    ''', reply_markup=choylar)

@dp.callback_query_handler(text='kok2')
async def limonchoy(call: types.CallbackQuery):
    photo = open('limon.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
    Ko'k choy
Narxi:   3 000 so'm
Tavsif: Ko'k choy
Miqdorini tanlang yoki kiriting
    ''',reply_markup=choylar)

@dp.callback_query_handler(text='hot_exit')
async def hotexit(call: types.CallbackQuery):
    photo = open('important1.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer("🥤Ichimliklar > Qaynoq ichimliklar", reply_markup=ichimliklar_1)
@dp.callback_query_handler(text='choylar_exit')
async def ortga(call: types.CallbackQuery):
    photo = open('important.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer( "🥤Ichimliklar > Qaynoq ichimliklar", reply_markup=hot_tea)


@dp.callback_query_handler(text='yaxna_ichimlik')
async def yaxna(call: types.CallbackQuery):
    photo = open('yaxna ichimliklar.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer("🥤Ichimliklar > Yahna ichimliklar", reply_markup=yaxna_water)

@dp.callback_query_handler(text='pepsi')
async def pepsi(call:types.CallbackQuery):
    photo = open('pepsi.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer("🥤Ichimliklar > Yahna ichimliklar > pepsi",reply_markup=pepsi_water)

@dp.callback_query_handler(text='ichimlik_exit')
async def pepsi(call: types.CallbackQuery):
    photo = open('kategoriya.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer("Kategoriyalardan birini tanlang", reply_markup=snakes)


@dp.callback_query_handler(text='pepsi_exit')
async def pepsiexit(call:types.CallbackQuery):
    photo = open('yaxna ichimliklar.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer("🥤Ichimliklar > Yahna ichimliklar", reply_markup=yaxna_water)


@dp.callback_query_handler(text='pepsi1_exit')
async def pepsiexit(call:types.CallbackQuery):
    photo = open('yaxna ichimliklar.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer("🥤Ichimliklar > Yahna ichimliklar", reply_markup=pepsi_water)

@dp.callback_query_handler(text='pepsi1.5')
async def pepsi(call:types.CallbackQuery):
    photo = open('pepsi1.5.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
    Pepsi 1.5
Narxi:   17 000 so'm
Tavsif: Pepsi 1.5
Miqdorini tanlang yoki kiriting
    ''', reply_markup=pepsi_savat)


@dp.callback_query_handler(text='pepsi0.4')
async def pepsi(call:types.CallbackQuery):
    photo = open('pepsi0.4.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
Pepsi 0.4
Narxi:   8 000 so'm
Tavsif: Pepsi 0.4
Miqdorini tanlang yoki kiriting
    ''', reply_markup=pepsi_savat)

@dp.callback_query_handler(text='pepsi0.3')
async def pepsi(call:types.CallbackQuery):
    photo = open('pepsi03.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
Pepsi 0.3 L
Narxi:   6 000 so'm
Tavsif: Pepsi 0.3 L
Miqdorini tanlang yoki kiriting
    ''', reply_markup=pepsi_savat)


@dp.callback_query_handler(text='dolina_exit')
async def dolinaexit(call:types.CallbackQuery):
    photo = open('pepsi.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer("🥤Ichimliklar > Yahna ichimliklar", reply_markup=yaxna_water)

@dp.callback_query_handler(text='pepsi0.5')
async def pepsi(call: types.CallbackQuery):
        photo = open('pepsi05.jpg', 'rb')
        await call.message.answer_photo(photo=photo)
        await call.message.answer('''
Pepsi 0.5
Narxi:   9 000 so'm
Tavsif: Pepsi 0.5
Miqdorini tanlang yoki kiriting
        ''', reply_markup=pepsi_savat)


@dp.callback_query_handler(text='dolina')
async def pepsi(call: types.CallbackQuery):
        photo = open('dolina.jpg', 'rb')
        await call.message.answer_photo(photo=photo)
        await call.message.answer('''
Sochnaya dolina 1L
Narxi:   16 000 so'm
Tavsif: Sochnaya dolina 1L
Miqdorini tanlang yoki kiriting
        ''', reply_markup=dolina_choy)


@dp.callback_query_handler(text='mirinda')
async def mirinda(call:types.CallbackQuery):
    photo = open('mirinda.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
    Mirinda 0.4L
Narxi:   8 000 so'm
Tavsif: Mirinda 0.4L, 
Miqdorini tanlang yoki kiriting
    ''',reply_markup=mirinda1)


@dp.callback_query_handler(text='mirinda1')
async def mirinda(call:types.CallbackQuery):
    photo = open('yaxna ichimliklar.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer("🥤Ichimliklar > Yahna ichimliklar", reply_markup=yaxna_water)


@dp.callback_query_handler(text='mountain')
async def mirinda(call:types.CallbackQuery):
    photo = open('mountindew.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
    Mountain Dew 0.4L
Narxi:   8 000 so'm
Tavsif: Mountain Dew 0.4L, 
Miqdorini tanlang yoki kiriting
    ''', reply_markup=mountain)

@dp.callback_query_handler(text='mountain_exit')
async def mirinda(call: types.CallbackQuery):
    photo = open('yaxna ichimliklar.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer("🥤Ichimliklar > Yahna ichimliklar",reply_markup=yaxna_water)


@dp.callback_query_handler(text='icetea')
async def hello(call: types.CallbackQuery):
    photo = open('icetea.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
    Ice tea 0.5
Narxi:   15 000 so'm
Tavsif: Ice tea 0.5
Miqdorini tanlang yoki kiriting
    ''', reply_markup=icetea)


@dp.callback_query_handler(text='icetea_exit')
async def hello(call: types.CallbackQuery):
    photo = open('yaxna ichimliklar.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('🥤Ichimliklar > Yahna ichimliklar',reply_markup=yaxna_water)


@dp.callback_query_handler(text='yaxna_exit')
async def hello(call: types.CallbackQuery):
    photo = open('important.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('🥤Ichimliklar',reply_markup=ichimliklar_1)

@dp.callback_query_handler(text='sous')
async def hello(call: types.CallbackQuery):
    photo = open('first_sous.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('🍅Souslar',reply_markup=souslar)



@dp.callback_query_handler(text='ketchup')
async def hello(call:types.CallbackQuery):
    photo = open('sous1.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
    <b>Ketchup</b>
Narxi:  <b> 3 000 so'm</b>
Tavsif: Ketchup
Miqdorini tanlang yoki kiriting
    ''', reply_markup=sous1)


@dp.callback_query_handler(text='sous1_exit')
async def sous(call:types.CallbackQuery):
    photo = open('first_sous.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('🍅Souslar', reply_markup=souslar)

@dp.callback_query_handler(text='chili')
async def sous(call:types.CallbackQuery):
    photo = open('chili.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
    <b>Chili sous</b>
Narxi:    <b>3 000 so'm</b>
Tavsif: Chili sous
Miqdorini tanlang yoki kiriting
    ''', reply_markup=sous1)

@dp.callback_query_handler(text='pishloq_sous')
async def sous(call:types.CallbackQuery):
    photo = open('pishloqli.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
<b>Pishloqli  sous</b>
Narxi:    <b>3 000 so'm</b>
Tavsif: Pishloqli  sous
Miqdorini tanlang yoki kiriting
    ''', reply_markup=sous1)


@dp.callback_query_handler(text='oq_sous')
async def sous(call:types.CallbackQuery):
    photo = open('oqsous.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
<b>Oq Sous</b>
Narxi:   <b> 3 000 so'm</b>
Tavsif: Oq Sous
Miqdorini tanlang yoki kiriting
    ''', reply_markup=sous1)


@dp.callback_query_handler(text='savat')
async def sous(call:types.CallbackQuery):
    photo = open('kategoriya.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer("Kategoriyalardan birini tanlang",reply_markup=snakes)

@dp.callback_query_handler(text='lavash')
async def lavash(call:types.CallbackQuery):
    photo = open('lavash.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('🌯Lavashlar', reply_markup=lavash_button)

@dp.callback_query_handler(text='lavash_exit')
async def lavash(call:types.CallbackQuery):
    photo = open('kategoriya.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('Kategoriyalardan birini tanlang', reply_markup=snakes)


@dp.callback_query_handler(text='savat_exit')
async def savat_exit(call: types.CallbackQuery):
    photo = open('lavash.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('🌯Lavashlar', reply_markup=lavash_button)



@dp.callback_query_handler(text='original')
async def original(call:types.CallbackQuery):
    photo = open('original.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
    Original lavash
Narxi:   28 000 so'm
Tavsif: Yupqa lavash non, pomidor, chips, mol ,go'shti\nqizil sous, mayonez.
Miqdorini tanlang yoki kiriting
    ''', reply_markup=lavash_savat)




@dp.callback_query_handler(text='org_kichik')
async def original(call:types.CallbackQuery):
    photo = open('orgkichik.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
Original kichik lavash
Narxi:   23 000 so'm
Tavsif: Yupqa lavash non, pomidor, chips, mol go'shti, qizil\nsous, mayonez, pishloq.
Miqdorini tanlang yoki kiriting
    ''', reply_markup=lavash_savat)

@dp.callback_query_handler(text='pishloq')
async def original(call:types.CallbackQuery):
    photo = open('pishloqli.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
Pishloqli lavash
Narxi:   31 000 so'm
Tavsif: Yupqa lavash non, pomidor, chips, mol go'shti, qizil\nsous, mayonez, pishloq.
Miqdorini tanlang yoki kiriting
    ''', reply_markup=lavash_savat)

@dp.callback_query_handler(text='pish_kichik')
async def original(call:types.CallbackQuery):
    photo = open('pishloqlikich.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''Pishloqli kichik lavash
Narxi:   26 000 so'm
Tavsif: Yupqa lavash non, pomidor, chips, mol go'shti, qizil\nsous, mayonez, pishloq.
Miqdorini tanlang yoki kiriting
    ''', reply_markup=lavash_savat)

@dp.callback_query_handler(text='tandir')
async def original(call: types.CallbackQuery):
        photo = open('TANDIR.jpg', 'rb')
        await call.message.answer_photo(photo=photo)
        await call.message.answer('''
        Tandir lavash
Narxi:   29 000 so'm
Tavsif: Tandir pechida pishirilgan yupqa lavash non, pomidor,\nchips, mol go'shti, qizil sous, mayonez, kunjut.
Miqdorini tanlang yoki kiriting
        ''', reply_markup=lavash_savat)

@dp.callback_query_handler(text='pish_tandir')
async def original(call: types.CallbackQuery):
        photo = open('pishtandir.jpg', 'rb')
        await call.message.answer_photo(photo=photo)
        await call.message.answer('''
Pishloqli tandir lavash
Narxi:   32 000 so'm
Tavsif: Tandirda pishirilgan yupqa lavash non, pomidor, chips,\nmol go'shti, pishloq, qizil sous, mayonez, kunjut.
Miqdorini tanlang yoki kiriting
        ''', reply_markup=lavash_savat)


@dp.callback_query_handler(text='set')
async def set(call:types.CallbackQuery):
    photo = open('setlar.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('🍟🌯🥤Setlar',reply_markup=setlar)

@dp.callback_query_handler(text='setlar_exit')
async def set(call:types.CallbackQuery):
    photo = open('kategoriya.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('Kategoriyalardan birini tanlang',reply_markup=snakes)

@dp.callback_query_handler(text='oqtepa')
async def set(call:types.CallbackQuery):
    photo = open('oqtepa.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
    Oqtepa seti
Narxi:   17 000 so'm
Tavsif: Kartoshka fri o'rta, Pepsi 0.4L, 
Miqdorini tanlang yoki kiriting
    ''',reply_markup=set_savat)

@dp.callback_query_handler(text='juftlik')
async def set(call:types.CallbackQuery):
    photo = open('juftlik.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
"Juftlik" Seti
Narxi:   58 000 so'm
Tavsif: Klab sendvich, strips 3 dona, Pepsi 0.4L\n2 dona, ketchup 2 dona
Miqdorini tanlang yoki kiriting
    ''',reply_markup=set_savat)

@dp.callback_query_handler(text='baraka')
async def set(call:types.CallbackQuery):
    photo = open('baraka.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
"Baraka" Seti
Narxi:   134 000 so'm
Tavsif: Assorti pitsa, kartoshka fri o'rta 3 dona,\nPepsi 0.4L 3 dona, ketchup 3 dona
Miqdorini tanlang yoki kiriting
    ''',reply_markup=set_savat)

@dp.callback_query_handler(text='set_exit')
async def set(call:types.CallbackQuery):
    photo = open('setlar.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('🍟🌯🥤Setlar',reply_markup=setlar)

@dp.callback_query_handler(text='pitsa')
async def set(call: types.CallbackQuery):
        photo = open('pitsalar.jpg', 'rb')
        await call.message.answer_photo(photo=photo)
        await call.message.answer('🍕Pitsalar', reply_markup=pitsa)

@dp.callback_query_handler(text='assorti')
async def set(call: types.CallbackQuery):
        photo = open('assorti.jpg', 'rb')
        await call.message.answer_photo(photo=photo)
        await call.message.answer('''
        Assorti pitsa
Narxi:   89 000 so'm
Tavsif: Oq sous, zaytun, qo'ziqorin, bulg'or\nqalampiri, pomidor, dudlangan kurka,\ndudlangan kolbasa, mol go'shti, sosiska,\nMozzarella va Akbel pishloqlari.
Miqdorini tanlang yoki kiriting
        ''', reply_markup=pitsa_savat)

@dp.callback_query_handler(text='peperonni')
async def set(call: types.CallbackQuery):
        photo = open('peperoni.jpg', 'rb')
        await call.message.answer_photo(photo=photo)
        await call.message.answer('''
        Pepperoni pitsa
Narxi:   75 000 so'm
Tavsif: “OQTEPA” pomidor sousi, dudlangan\nkolbasa,Mozzarella va Akbel pishlog'i 
Miqdorini tanlang yoki kiriting
                ''', reply_markup=pitsa_savat)

@dp.callback_query_handler(text='goshtli')
async def set(call: types.CallbackQuery):
        photo = open('goshtli.jpg', 'rb')
        await call.message.answer_photo(photo=photo)
        await call.message.answer('''
        Go'shtli pitsa
Narxi:   87 000 so'm
Tavsif: Tomato sauce “OQTEPA”, chicken meat,\nbell pepper, beef, tomatoes, Mozzarella and Akbel cheese
Miqdorini tanlang yoki kiriting
                ''', reply_markup=pitsa_savat)

@dp.callback_query_handler(text='qazi')
async def set(call: types.CallbackQuery):
        photo = open('qazi.jpg', 'rb')
        await call.message.answer_photo(photo=photo)
        await call.message.answer('''
        Qazi pizza
Narxi:   90 000 so'm
Tavsif: “OQTEPA” pomidor sousi, "Brunswick"\nshirin piyoz halqalari, qazi, Mozzarella va Akbel pishloqlari
Miqdorini tanlang yoki kiriting
                ''', reply_markup=pitsa_savat)

@dp.callback_query_handler(text='tovuqli_pitsa')
async def set(call: types.CallbackQuery):
        photo = open('tovuqli_pitsa.jpg', 'rb')
        await call.message.answer_photo(photo=photo)
        await call.message.answer('''
        Tovuqli pitsa
Narxi:   75 000 so'm
Tavsif: OQTEPA pomidor sousi, kurka, tovuq,\nqo'ziqorin, zaytun, pishloq, oregano
Miqdorini tanlang yoki kiriting
                ''', reply_markup=pitsa_savat)

@dp.callback_query_handler(text='pitsa_Exit')
async def set(call:types.CallbackQuery):
    photo = open('setlar.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('Kategorilardan birini tanlang',reply_markup=snakes)

@dp.callback_query_handler(text='pitsa_exit')
async def set(call: types.CallbackQuery):
    photo = open('pitsalar.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('🍕Pitsalar', reply_markup=pitsa)


@dp.callback_query_handler(text='burger')
async def set(call: types.CallbackQuery):
    photo = open('burgerlar.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('🍔 Burger va donerlar',reply_markup=burgerlar)

@dp.callback_query_handler(text='gamburger')
async def set(call: types.CallbackQuery):
    photo = open('gamburger.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
    Gamburger
Narxi:   22 000 so'm
Tavsif: Shirin bulochka, maxsus sous, aysberg,\ntuzlangan bodring, mol go'shtidan kotlet,\npomidor, "Brunswick" shirin piyoz halqalari
Miqdorini tanlang yoki kiriting
    ''', reply_markup=burgers_savat)

@dp.callback_query_handler(text='chizburger')
async def set(call: types.CallbackQuery):
    photo = open('chizburger.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
Chizburger
Narxi:   24 000 so'm
Tavsif: Shirin bulochka, maxsus sous, aysberg,\ntuzlangan bodring, mol go'shtidan kotlet,\npomidor, pishloq, "Brunswik" shirin piyoz\nhalqalari
Miqdorini tanlang yoki kiriting
    ''', reply_markup=burgers_savat)

@dp.callback_query_handler(text='big_burger')
async def set(call: types.CallbackQuery):
    photo = open('big_burger.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
Big burger
Narxi:   33 000 so'm
Tavsif: Shirin bulochka, maxsus sous, aysberg,\ntuzlangan bodring, ikkita mol go'shtidan kotlet,\npomidor, "Brunswick" shirin piyoz halqalari
Miqdorini tanlang yoki kiriting
    ''', reply_markup=burgers_savat)

@dp.callback_query_handler(text='bigchizburger')
async def set(call: types.CallbackQuery):
    photo = open('bigchiz.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
Big Chizburger
Narxi:   37 000 so'm
Tavsif: Shirin bulochka, maxsus sous, aysberg,\ntuzlangan bodring, ikkita mol go'shtidan kotlet,\npomidor, pishloq, "Brunswick" shirin piyoz\nhalqalari
Miqdorini tanlang yoki kiriting
    ''', reply_markup=burgers_savat)

@dp.callback_query_handler(text='bigdoner')
async def set(call: types.CallbackQuery):
    photo = open('bigdoner.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
Big doner
Narxi:   26 000 so'm
Tavsif: Ekmek mualliflik noni, oq va qizil souslar,\nchiplar, mol go'shti, bodring, pomidor.
Miqdorini tanlang yoki kiriting
    ''', reply_markup=burgers_savat)

@dp.callback_query_handler(text='shaurma')
async def set(call: types.CallbackQuery):
    photo = open('shaurma.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
Shaurma
Narxi:   22 000 so'm
Tavsif: Tandirli pita noni, mol go'shti, bodring,\npomidor, qizil sous, "Brunswick" shirin piyoz\nhalqalari
Miqdorini tanlang yoki kiriting
    ''', reply_markup=burgers_savat)

@dp.callback_query_handler(text='burgers_exit')
async def set(call: types.CallbackQuery):
    photo = open('kategoriya.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('Kategoriyalardan birini tanlang',reply_markup=snakes)

@dp.callback_query_handler(text='chizburger_exit')
async def set(call: types.CallbackQuery):
    photo = open('burgerlar.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('🍔 Burger va donerlar',reply_markup=burgerlar)

@dp.callback_query_handler(text='hotdog')
async def set(call: types.CallbackQuery):
    photo = open('hotdoglar.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('🌭Hot doglar',reply_markup=burgerlar)


@dp.callback_query_handler(text='haggi')
async def set(call: types.CallbackQuery):
    photo = open('haggi.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
    Xaggi
Narxi:   31 000 so'm
Tavsif: Baget noni, mayonez, mol go'shti, salat\nbargi, bodring, pomidor, pishloq, qizil sous,\n"Brunswick" shirin piyoz halqalari
Miqdorini tanlang yoki kiriting
    ''',reply_markup=shaurma)

@dp.callback_query_handler(text='shaurma_exit')
async def set(call: types.CallbackQuery):
    photo = open('kategoriya.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('Kategoriyalardan birini tanlang', reply_markup=snakes)



@dp.callback_query_handler(text='klab')
async def set(call: types.CallbackQuery):
    photo = open('klabsendvich.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
Klab sendvich
Narxi:   30 000 so'm
Tavsif: Toster non, maxsus sous, bodring,\npomidor, tovuq filesi, salat bargi, pishloq,\nkartoshka fri
Miqdorini tanlang yoki kiriting
    ''',reply_markup=klab_sendvich)

@dp.callback_query_handler(text='klab_exit')
async def set(call: types.CallbackQuery):
    photo = open('kategoriya.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('Kategoriyalardan birini tanlang', reply_markup=snakes)


@dp.callback_query_handler(text='snek')
async def set(call: types.CallbackQuery):
    photo = open('sneklar.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('🍟Sneklar', reply_markup=sneklar)


@dp.callback_query_handler(text='fri')
async def set(call: types.CallbackQuery):
    photo = open('friorta.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
Kartoshka fri o'rta
Narxi:   14 000 so'm
Tavsif: Kartoshka fri o'rta
Miqdorini tanlang yoki kiriting
    ''',reply_markup=sneks)

@dp.callback_query_handler(text='fri_katta')
async def set(call: types.CallbackQuery):
    photo = open('frikatta.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
Kartoshka fri katta
Narxi:   18 000 so'm
Tavsif: Kartoshka fri katta
Miqdorini tanlang yoki kiriting
    ''',reply_markup=sneks)

@dp.callback_query_handler(text='fri_kichik')
async def set(call: types.CallbackQuery):
    photo = open('frikichik.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
Kartoshka fri kichik
Narxi:   8 000 so'm
Tavsif: Kartoshka fri kichik
Miqdorini tanlang yoki kiriting
    ''',reply_markup=sneks)


@dp.callback_query_handler(text='jaydari')
async def set(call: types.CallbackQuery):
    photo = open('jaydari.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
Jaydari kartoshka
Narxi:   15 000 so'm
Tavsif: Jaydari kartoshka
Miqdorini tanlang yoki kiriting
    ''',reply_markup=sneks)



@dp.callback_query_handler(text='non')
async def set(call: types.CallbackQuery):
    photo = open('non.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
Non
Narxi:   3 000 so'm
Tavsif: Non
Miqdorini tanlang yoki kiriting
    ''',reply_markup=sneks)

@dp.callback_query_handler(text='xala')
async def set(call: types.CallbackQuery):
    photo = open('xala.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('''
Xalapenyo
Narxi:   3 000 so'm
Tavsif: Xalapenyo
Miqdorini tanlang yoki kiriting
    ''',reply_markup=sneks)

@dp.callback_query_handler(text='sneks_exit')
async def set(call: types.CallbackQuery):
    photo = open('sneklar.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('🍟Sneklar', reply_markup=sneklar)

@dp.callback_query_handler(text='snek_exit')
async def set(call: types.CallbackQuery):
    photo = open('kategoriya.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer('Kategoriyalardan birini tanlang', reply_markup=snakes)

@dp.callback_query_handler(text='menu')
async def set(call: types.CallbackQuery):
    await call.message.answer('Buyurtmani birga joylashtiramizmi? 🤗', reply_markup=asosiy_menyu)









if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
