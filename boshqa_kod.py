from bot import logging
from aiogram import executor
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from Keyboards.inline import asosiy_menyu, ortga1, snakes, qarsildoq_oyoqlar, savat, savat_salatlar
from Keyboards.inline import salats, ichimliklar_1, hot_tea, choylar, yaxna_water, pepsi_water, pepsi_savat, \
    dolina_choy, burgers_savat, burgerlar
from Keyboards.inline import mirinda1, icetea, mountain, souslar, sous1, lavash_button, lavash_savat, setlar, set_savat, \
    pitsa_savat, pitsa, shaurma
from Keyboards.inline import klab_sendvich, sneklar, sneks
from Keyboards.default import buyurtma_berish, locations, parol
from aiogram.types import ReplyKeyboardRemove

@dp.message_handler(state=ADMIN.check)
async def check_password_for_change(message: types.Message, state=FSMContext):
    if message.text == password:
        await message.answer('Yangi parol kiriting🆕️️ !')
        await state.finish()
        await ADMIN.chnage.set()
    else:
        await message.reply('Parol Xato')


    