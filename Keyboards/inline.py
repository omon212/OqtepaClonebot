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

snakes = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🍗Qarsildoq Jo'jalar", callback_data='tovuq'),
            InlineKeyboardButton("🥗Salatlar",callback_data='salat')
        ],
        [
            InlineKeyboardButton("🥤Ichimliklar",callback_data='ichimlikar'),
            InlineKeyboardButton("🍅Souslar",callback_data='sous')
        ],
        [
            InlineKeyboardButton("🌯Lavashlar",callback_data='lavash'),
            InlineKeyboardButton("🍟🌯🥤Setlar",callback_data='set')
        ],
        [
            InlineKeyboardButton("🍕Pitsalar", callback_data='pitsa'),
            InlineKeyboardButton("🍔Burger va donerlar", callback_data='burger')
        ],
        [
            InlineKeyboardButton("🌭Hot doglar", callback_data='hotdog'),
            InlineKeyboardButton("🥙Haggi", callback_data='haggi')
        ],
        [
            InlineKeyboardButton("🥪Klab sendvich", callback_data='klab'),
            InlineKeyboardButton("🍟Sneklar", callback_data='snek')
        ],
        [
           InlineKeyboardButton("⬅️Asosiy menu", callback_data='menu')
        ]
    ],
)
qarsildoq_oyoqlar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Jo'ja box" , callback_data='box'),
            InlineKeyboardButton("Stips 5 dona" , callback_data='stips')
        ],
        [
            InlineKeyboardButton("Stips 3 dona",callback_data='stip'),
            InlineKeyboardButton("Bayts",callback_data='bayt')
        ],
        [
            InlineKeyboardButton("⬅️ortga", callback_data='ortga2'),
        ],

    ],
)
savat = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('-',callback_data='minus'),
            InlineKeyboardButton("1",callback_data='son'),
            InlineKeyboardButton('-',callback_data='plus')
        ],
        [
            InlineKeyboardButton("Savatga qo'shish", callback_data='savat'),
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data='ortga3'),
        ],

    ],
)

salats = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Mujskoy kapriz",callback_data='kapriz'),
            InlineKeyboardButton("Sezar",callback_data='sezat')
        ],
        [
            InlineKeyboardButton("⬅️ Ortga",callback_data="ortga4")
        ],
    ],
)


