from .manager import UserManager as user_manager, ManagerUserCity as city,\
    ManagerUserTypes as types, ClothesManager as clothes, BasketManager as basket
from .menu import Views as view
from .settings import bot
from .messages import Messages as message
from .buttons import Buttons as button
from django.conf import settings
from telebot.types import InlineQueryResultPhoto


def start_view(data):
    if user_manager.is_user(view.chat_id(data)) is None:
        user_manager.add_user(view.user_id(data), view.first_name(data),
                              view.username(data), view.is_bot(data))

        return bot.send_message(view.chat_id(data), message.country(), reply_markup=view.question_country())

    else:
        return bot.send_message(view.chat_id(data), message.start(), reply_markup=view.menu(), parse_mode='HTML')


def country_view(data):
    user_id = view.user_id(data)
    user = user_manager.is_user(user_id)

    if user:
        status_city = city.get_user(user.id)

        if status_city is None:
            if view.get_text(data) == button.btn1.text:
                city.create(user_id=user.id, country=1)

                return bot.send_message(view.chat_id(data), message.male(),
                                        reply_markup=view.question_male())

            elif view.get_text(data) == button.btn2.text:
                city.create(user_id=user.id, country=2)

                return bot.send_message(view.chat_id(data), message.male(),
                                        reply_markup=view.question_male())

        else:
            if view.get_text(data) == button.btn1.text:
                city.update(user_id=user.id, country=1)

                return bot.send_message(view.chat_id(data), message.male(),
                                        reply_markup=view.question_male())

            elif view.get_text(data) == button.btn2.text:
                city.update(user_id=user.id, country=2)

                return bot.send_message(view.chat_id(data), message.male(),
                                        reply_markup=view.question_male())


def male_view(data):
    user_id = view.user_id(data)
    user = user_manager.is_user(user_id)

    if user:
        status_male = types.get_user(user.id)

        if status_male is None:
            if view.get_text(data) == button.btn3.text:
                types.create(1, user.id)

                return bot.send_message(view.chat_id(data), message.start(),
                                        reply_markup=view.menu(), parse_mode='HTML')

            elif view.get_text(data) == button.btn4.text:
                types.create(2, user.id)

                return bot.send_message(view.chat_id(data), message.start(),
                                        reply_markup=view.menu(), parse_mode='HTML')

        else:
            if view.get_text(data) == button.btn3.text:
                types.update(user.id, 1)

                return bot.send_message(view.chat_id(data), message.start(),
                                        reply_markup=view.menu(), parse_mode='HTML')

            elif view.get_text(data) == button.btn4.text:
                types.update(user.id, 2)

                return bot.send_message(view.chat_id(data), message.start(),
                                        reply_markup=view.menu(), parse_mode='HTML')


def see_product_all_view(data):
    results = []
    clothe = clothes.get_clothes_all().values()
    b = []

    if clothe:
        for i in clothe:
            results.append(InlineQueryResultPhoto(
                id=i['article_id'], photo_url=f"{settings.DOMAIN}{settings.MEDIA_URL}{i['img_top']}",
                thumb_url=f"{settings.DOMAIN}{settings.MEDIA_URL}{i['img_left']}", photo_width=30,
                photo_height=30, caption=i['description'], parse_mode='HTML', reply_markup=view.product())
            )
            button.btn46.callback_data = i['article_id']
            b.append(button.btn46)
    print(b)

    return bot.answer_inline_query(view.chat_id(data), results=results, cache_time=0, next_offset='')


def basket_view(data):
    user_id = view.user_id(data)
    product_id = view.get_product_id(data)

    if basket.get(product_id=product_id):
        basket.del_product(product_id=product_id)

        return bot.send_message(view.chat_id(data), message.basket_remove_product(product_id),
                                reply_markup=view.basket(), parse_mode='HTML')
    else:
        basket.add(user_id=user_id, product_id=product_id)

        return bot.send_message(view.chat_id(data), message.basket_add_product(product_id),
                                reply_markup=view.basket(), parse_mode='HTML')
