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

