from telebot.types import KeyboardButton, InlineKeyboardButton


class Url(object):
    def __init__(self):
        self.url_api = 'https://telegram.me/'
        self.callback_user = 'My_Order'

    def set(self):
        return f'{self.url_api}{self.callback_user}'


class Buttons(object):
    url = Url().set()

    """Buttons for use in Bot"""
    btn1 = KeyboardButton(text="Украина")
    btn2 = KeyboardButton(text="Россия")
    btn3 = KeyboardButton(text="Мужской")
    btn4 = KeyboardButton(text="Женский")
    btn5 = KeyboardButton(text="Верхняя одежда")
    btn6 = KeyboardButton(text="Нижняя одежда")
    btn7 = KeyboardButton(text="Костюмы")
    btn8 = KeyboardButton(text="Обувь")
    btn9 = KeyboardButton(text="Аксессуары")
    btn10 = KeyboardButton(text="💭 Отзывы")
    btn11 = KeyboardButton(text="📬 Рассказать друзьям")
    btn12 = KeyboardButton(text="🛍 Корзина")
    btn13 = KeyboardButton(text="◀️ Назад")
    btn14 = KeyboardButton(text="Куртки")
    btn15 = KeyboardButton(text="Кофты")
    btn16 = KeyboardButton(text="Майки")
    btn17 = KeyboardButton(text="Футболки")
    btn18 = KeyboardButton(text="Рубашки")
    btn19 = KeyboardButton(text="Шапки")
    btn20 = KeyboardButton(text="Кепки")
    btn21 = KeyboardButton(text="Брюки")
    btn22 = KeyboardButton(text="Шорты")
    btn23 = KeyboardButton(text="Ремни")
    btn24 = KeyboardButton(text="Бельё")
    btn25 = KeyboardButton(text="Носки")
    btn26 = KeyboardButton(text="Спортивные костюмы")
    btn27 = KeyboardButton(text="Классические костюмы")
    btn28 = KeyboardButton(text="Крассовки")
    btn29 = KeyboardButton(text="Кеды")
    btn30 = KeyboardButton(text="Ботинки")
    btn31 = KeyboardButton(text="Туфли")
    btn32 = KeyboardButton(text="Рюкзаки")
    btn33 = KeyboardButton(text="Сумки")
    btn34 = KeyboardButton(text="Очки")
    btn35 = KeyboardButton(text="Часы")
    btn36 = KeyboardButton(text="Кошельки")
    btn37 = KeyboardButton(text="Чехлы")
    btn38 = KeyboardButton(text="Духи")
    btn39 = KeyboardButton(text="Зонты")
    btn40 = InlineKeyboardButton(text="Смотреть все!")
    btn41 = InlineKeyboardButton(text="до 500 (грн)", callback_data='<500')
    btn42 = InlineKeyboardButton(text="от 500 (грн)", callback_data='>500')
    btn43 = InlineKeyboardButton(text="<", callback_data='<')
    btn44 = InlineKeyboardButton(text=">", callback_data='>')
    btn45 = InlineKeyboardButton(text='Заказать', url=url)
    btn46 = InlineKeyboardButton(text='Корзина')
    btn47 = InlineKeyboardButton(text='Назад')
    btn48 = InlineKeyboardButton(text="Смотреть", switch_inline_query_current_chat='#корзина')