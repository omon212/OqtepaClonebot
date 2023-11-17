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
            InlineKeyboardButton("🥤Ichimliklar",callback_data="ichimlik_cola"),
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
            InlineKeyboardButton("⬅Ortga", callback_data='qarsildoq_exit'),
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
            InlineKeyboardButton("⬅Ortga", callback_data='joja_exit'),
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
            InlineKeyboardButton("⬅0rtga",callback_data="exits")
        ],
    ],
)

savat_salatlar = InlineKeyboardMarkup(
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
            InlineKeyboardButton("⬅Ortga", callback_data='salat_exit'),
        ],
    ],
)


ichimliklar_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Qaynoq ichimliklar', callback_data="qaynoq_ichimlik"),
            InlineKeyboardButton('Yaxna ichimlikar', callback_data="yaxna_ichimlik")
        ],
        [
            InlineKeyboardButton("⬅Ortga", callback_data="ichimlik_exit")
        ],
    ],
)

hot_tea = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("☕️Qora choy", callback_data="qora"),
            InlineKeyboardButton("☕️Ko'k choy", callback_data="kok")
        ],
        [
            InlineKeyboardButton("🍋Ko'k choy", callback_data="kok2")
        ],
        [
            InlineKeyboardButton("⬅Ortga", callback_data="hot_exit")
        ],
    ],
)

choylar = InlineKeyboardMarkup(
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
            InlineKeyboardButton("⬅Ortga", callback_data='choylar_exit'),
        ],
    ],
)

yaxna_water = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Pepsi', callback_data='pepsi'),
            InlineKeyboardButton('Sochnaya dolina',callback_data='dolina')
        ],
        [
            InlineKeyboardButton("Mirinda 0.4l", callback_data='mirinda'),
            InlineKeyboardButton('Mountain Dew 0.4l', callback_data='mountain')
        ],
        [
            InlineKeyboardButton('Ice tea0.5l',callback_data='icetea'),
            InlineKeyboardButton('Mohito 0.5l',callback_data='mohito')
        ],
        [
            InlineKeyboardButton('⬅Ortga',callback_data='yaxna_exit')
        ],
    ],
)

pepsi_water = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Pepsi 1.5', callback_data="pepsi1.5"),
            InlineKeyboardButton('Pepsi 0.4', callback_data="pepsi0.4")
        ],
        [
            InlineKeyboardButton('Pepsi 0.3l', callback_data='pepsi0.3'),
            InlineKeyboardButton('Pepsi 0.5l', callback_data="pepsi0.5")
        ],
        [
            InlineKeyboardButton('⬅Ortga', callback_data="pepsi_exit")
        ]

    ]
)

pepsi_savat = InlineKeyboardMarkup(
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
            InlineKeyboardButton("⬅Ortga", callback_data='pepsi1_exit'),
        ],
    ],
)

dolina_choy = InlineKeyboardMarkup(
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
            InlineKeyboardButton("⬅Ortga", callback_data='dolina_exit'),
        ],
    ],
)

mirinda1 = InlineKeyboardMarkup(
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
            InlineKeyboardButton("⬅Ortga", callback_data='mirinda1'),
        ],
    ],
)

mountain = InlineKeyboardMarkup(
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
            InlineKeyboardButton("⬅Ortga", callback_data='mountain_exit'),
        ],
    ],
)


icetea = InlineKeyboardMarkup(
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
            InlineKeyboardButton("⬅Ortga", callback_data='icetea_exit'),
        ],
    ],
)


souslar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Ketchup',callback_data='ketchup'),
            InlineKeyboardButton('Chili sous',callback_data='chili')
        ],
        [
            InlineKeyboardButton('Pishloqli sous',callback_data='pishloq_sous'),
            InlineKeyboardButton('Oq sous',callback_data='oq_sous')
        ],
        [
            InlineKeyboardButton('⬅Ortga',callback_data='savat')
        ]
    ]
)


sous1 = InlineKeyboardMarkup(
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
            InlineKeyboardButton("⬅Ortga", callback_data='sous1_exit'),
        ],
    ],
)

lavash_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Original lavash', callback_data='original'),
            InlineKeyboardButton('Original kichik lavash', callback_data='org_kichik')
        ],
        [
            InlineKeyboardButton('Pishloqli lavash', callback_data='pishloq'),
            InlineKeyboardButton('Pishloqli kichik lavash', callback_data='pish_kichik')
        ],
        [
            InlineKeyboardButton('Tandir lavash', callback_data='tandir'),
            InlineKeyboardButton('Pishloqli tandir lavash', callback_data='pish_tandir')
        ],
        [
            InlineKeyboardButton('⬅Ortga',callback_data='lavash_exit')
        ],
    ],
)

lavash_savat = InlineKeyboardMarkup(
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
            InlineKeyboardButton("⬅Ortga", callback_data='savat_exit'),
        ],
    ],
)

setlar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Oqtepa Seti', callback_data='oqtepa'),
            InlineKeyboardButton('"Juftlik" Seti', callback_data="juftlik")
        ],
        [
            InlineKeyboardButton('"Baraka" Seti', callback_data='baraka')
        ],
        [
            InlineKeyboardButton("⬅Ortga", callback_data='setlar_exit'),
        ],

    ],
)

set_savat = InlineKeyboardMarkup(
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
            InlineKeyboardButton("⬅Ortga", callback_data='set_exit'),
        ],
    ],
)

pitsa = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Assorti pitsa', callback_data='assorti'),
            InlineKeyboardButton('Pepperoni pitsa', callback_data='peperonni')
        ],
        [
            InlineKeyboardButton("Go'shtli pitsa", callback_data='goshtli'),
            InlineKeyboardButton('Qazi pitsa', callback_data='qazi')
        ],
        [
            InlineKeyboardButton('Tovuqli pitsa', callback_data='tovuqli_pitsa')
        ],
        [
            InlineKeyboardButton("⬅Ortga", callback_data='pitsa_Exit')
        ],
    ],
)

pitsa_savat = InlineKeyboardMarkup(
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
            InlineKeyboardButton("⬅Ortga", callback_data='pitsa_exit'),
        ],
    ],
)

burgerlar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Gamburger', callback_data='gamburger'),
            InlineKeyboardButton('Chizburger', callback_data='chizburger')
        ],
        [
            InlineKeyboardButton('Big burger', callback_data='big_burger'),
            InlineKeyboardButton('Big chizburger', callback_data='bigchizburger')
        ],
        [
            InlineKeyboardButton('Big doner', callback_data='bigdoner'),
            InlineKeyboardButton('Shaurma',callback_data='shaurma')
        ],
        [
            InlineKeyboardButton("⬅Ortga", callback_data='burgers_exit'),
        ],

    ],
)
burgers_savat = InlineKeyboardMarkup(
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
            InlineKeyboardButton("⬅Ortga", callback_data='chizburger_exit'),
        ],
    ],
)

hotdog = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Hot-dog",callback_data='hotdog'),
            InlineKeyboardButton("Pishloqli hot-dog",callback_data='pishloqli_hotdog')
        ],
        [
            InlineKeyboardButton("Shoxona Hot_dog",callback_data="shoxona")
        ],
        [
            InlineKeyboardButton("",callback_data="shoxona")
        ],
    ],
)

shaurma = InlineKeyboardMarkup(
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
            InlineKeyboardButton("⬅Ortga", callback_data='shaurma_exit'),
        ],
    ],
)

klab_sendvich = InlineKeyboardMarkup(
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
            InlineKeyboardButton("⬅Ortga", callback_data='klab_exit'),
        ],
    ],
)

sneklar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Katroshka fri', callback_data='fri'),
            InlineKeyboardButton('Katroshka fri katta', callback_data='fri_katta')
        ],
        [
            InlineKeyboardButton('Kartoshka fri kichik', callback_data='fri_kichik'),
            InlineKeyboardButton('Jaydari kartoshka', callback_data='jaydari')
        ],
        [
            InlineKeyboardButton('Non', callback_data='non'),
            InlineKeyboardButton('Xalapenyo',callback_data='xala')
        ],
        [
            InlineKeyboardButton("⬅Ortga", callback_data='snek_exit'),
        ],

    ],
)

sneks = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='minus_xlapeniyo'),
                InlineKeyboardButton("1", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='plus_xlapeniyo')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='savatcha_snek'),
            ],
            [
                InlineKeyboardButton("⬅Ortga", callback_data='sneks_exit'),
            ],
        ],
    )

check_oshpaz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('✅', callback_data='oshpaz_true'),
            InlineKeyboardButton('❌️️️️️️️',callback_data='oshpaz_false')
        ]
    ]
)


kuryer_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('✅', callback_data='kuryer_true'),
            InlineKeyboardButton('❌️️️️️️️',callback_data='kuryer_false')
        ]
    ]
)
