from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

buyurtma_berish = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Eltib berish🛵'),
            KeyboardButton('Olib ketish🚶🏼')
        ],
        [
            KeyboardButton('⬅️Ortga')
        ],
    ],
    resize_keyboard=True
)

locations = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('📍 Locatsiya jo`natish', request_location=True),
        ],
        [
            KeyboardButton('⬅️ Ortga')
        ]
    ],
    resize_keyboard=True
)

parol = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Parol ozgartirish'),
            KeyboardButton('Adminlar royxati')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

buy = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Buyurtmani tasdiqlash')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)