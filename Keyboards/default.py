from aiogram.types import KeyboardButton, ReplyKeyboardMarkup,ReplyKeyboardRemove

buyurtma_berish = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Eltib berish'),
            KeyboardButton('Olib ketish')
        ],
        [
          KeyboardButton('Ortga')
        ],
    ],
    resize_keyboard=True
)
