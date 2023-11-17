from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext
from bot import dp, son,bot
from bot import savatchamiz_user
from bot import Shogirdcha
from Keyboards.inline import oshpaz
from Keyboards.default import buy


@dp.callback_query_handler(text='savatcha_snek')
async def sous(call: CallbackQuery):
    user_id = call.message.chat.id
    print(user_id)
    user_num = son[user_id]
    savatchamiz_user[user_id] = [f"Xlapeniyo: {user_num}"]
    await call.message.answer('Mahsulot Savatchaga qo`shildi',reply_markup=buy)
    await Shogirdcha.buyurtmachi.set()


@dp.message_handler(text='Buyurtmani tasdiqlash', state=Shogirdcha.buyurtmachi)
async def apply(message: Message, state=FSMContext):
    await message.answer('Sizning Buyurtmangiz Qabul qilindi!\n\nYaqin orada javobini olasiz.')
    await message.answer('⏳')
    print(savatchamiz_user)
    txt = ''
    for i in range(len(savatchamiz_user[message.from_user.id])):
        txt += f'{i + 1}.' + ' 🍟mahsulot ' + savatchamiz_user[message.from_user.id][i] + '\n'
    await bot.send_message(6580480307,txt,reply_markup=oshpaz)
    await state.finish()
