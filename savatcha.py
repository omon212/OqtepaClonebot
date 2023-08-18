from aiogram.dispatcher import Dispatcher
from aiogram.types import Message

from Keyboards.inline import snakes
from bot import dp
from aiogram import types


from bot import savatchamiz



from bot import son

savatchamiz_user = {
    'user_id': [],
}

@dp.callback_query_handler(text='savat')
async def sous(call: types.CallbackQuery):
    user_id = call.message.from_user.id
    photo = open('pictures/kategoriya.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer("Kategoriyalardan birini tanlang", reply_markup=snakes)


@dp.callback_query_handler(text='savatcha_snek')
async def sous(call: types.CallbackQuery):
    user_id = call.message.chat.id
    user_num = son.get(str(user_id,0))
    savatchamiz_user[user_id] = [f"Xlapeniyo: {user_num}"]
    await call.message.answer('Mahsulot Savatchaga qo`shildi')





