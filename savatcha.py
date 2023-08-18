from aiogram.dispatcher import Dispatcher
from aiogram.types import Message

from Keyboards.inline import snakes
from bot import dp
from aiogram import types

savatchamiz = {
    'user_id': []
}
from bot import son

@dp.callback_query_handler(text='savat')
async def sous(call: types.CallbackQuery):
    user_id = call.message.from_user.id
    photo = open('pictures/kategoriya.jpg', 'rb')
    await call.message.answer_photo(photo=photo)
    await call.message.answer("Kategoriyalardan birini tanlang", reply_markup=snakes)
