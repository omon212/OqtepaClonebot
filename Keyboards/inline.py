from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

asosiy_menyu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('🛒Buyurtma berish', callback_data='Buyurtma'),
        ],
        [
            InlineKeyboardButton('ℹ️Biz Haqqimizda', callback_data='bizhaqqimizda'),
            InlineKeyboardButton('🛍️Buyurtmalarim', callback_data='buyurtmalar')
        ],
        [
            InlineKeyboardButton('🏘️Filiallar', callback_data='filial')
        ],
        [
            InlineKeyboardButton('✍️Fikr Bildirish', callback_data='fikr'),
            InlineKeyboardButton('⚙️Sozlamalar', callback_data='sozlamalar')
        ]
    ]
)
ortga1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('ortga', callback_data='ortga')
        ],
    ],
)
