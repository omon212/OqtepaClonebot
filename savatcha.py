from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext
from bot import dp, son,bot
from bot import savatchamiz_user
from bot import Shogirdcha
from Keyboards.inline import check_oshpaz
from Keyboards.default import buy
from aiogram.types import ReplyKeyboardRemove


@dp.callback_query_handler(text='savatcha_snek')
async def sous(call: CallbackQuery):
    user_id = call.message.chat.id
    print(user_id)
    user_num = son[user_id]
    savatchamiz_user[user_id] = [f"Xlapeniyo: {user_num}"]
    await call.message.answer('Mahsulot Savatchaga qo`shildi',reply_markup=buy)
    await Shogirdcha.buyurtmachi.set()




@dp.callback_query_handler(text='oshpaz_true')
async def oshaptrue(call: CallbackQuery):
    await bot.send_message(6498877955
,"Buyurtmangiz yarim saot ichida yetkazib beriladi")

@dp.message_handler(text='oshpaz_false')
async def oshapfalse(call: CallbackQuery):
    await bot.send_message(6498877955
,"Buyurtmangiz bekor qilindi")
