from telebot.types import KeyboardButton, InlineKeyboardButton


class Url(object):
    def __init__(self):
        self.url_api = 'https://telegram.me/'
        self.callback_user = 'RoboSapiensX'

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
    btn45 = InlineKeyboardButton(text='Заказать')
    btn46 = InlineKeyboardButton(text='Корзина')
    btn47 = InlineKeyboardButton(text='Назад')
    btn48 = InlineKeyboardButton(text="Смотреть!", switch_inline_query_current_chat='#корзина')
    btn49 = InlineKeyboardButton(text="Отправить!", url="https://t.me/share/url?url=https%3A//telegram.me/Robo_Sapiens_Bot&text=%D0%9C%D0%B5%D0%BD%D1%8F%20%D0%B7%D0%BE%D0%B2%D1%83%D1%82%20Rosie.%20%D0%AF%20%D0%B1%D0%BE%D1%82%20%D0%BA%D0%BE%D1%82%D0%BE%D1%80%D1%8B%D0%B9%20%D0%BF%D0%BE%D0%BC%D0%BE%D0%B6%D0%B5%D1%82%20%D0%B2%D0%B0%D0%BC%20%D0%BD%D0%B0%D0%B9%D1%82%D0%B8%20%D0%BD%D1%83%D0%B6%D0%BD%D1%83%D1%8E%20%D0%BE%D0%B4%D0%B5%D0%B6%D0%B4%D1%83%2C%20%D0%BE%D0%B1%D1%83%D0%B2%D1%8C%20%D0%B8%20%D0%B4%D1%80%D1%83%D0%B3%D0%B8%D0%B5%20%D0%B0%D0%BA%D1%81%D0%B5%D1%81%D1%81%D1%83%D0%B0%D1%80%D1%8B%21")
    btn50 = InlineKeyboardButton(text="Оформить заказ!", url=url)
    btn51 = InlineKeyboardButton(text='Смотреть!', url='https://comments.bot/thread/Sky8HflbV')
