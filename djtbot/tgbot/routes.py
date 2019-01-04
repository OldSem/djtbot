from .manager import UserManager as user_manager, ManagerUserCity as city,\
    ManagerUserTypes as types, ClothesManager as clothes, BasketManager as basket,\
    ClothesCategoryManager, SystemPhotoManager, OrderManager
from .menu import Views as view
from .settings import bot
from .messages import Messages as message
from .buttons import Buttons as button
from django.conf import settings
from telebot.types import InlineQueryResultPhoto
from .logger import logger_djtbot


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


def get_category_id_in_query(query):

    if query:
        value = query[1:].capitalize()

        return value

    return None


def format_image_url(img):
    return "{0}{1}{2}".format(settings.DOMAIN, settings.MEDIA_URL, img)


def see_product_view(data):
    query = view.get_text(data)
    category_name = get_category_id_in_query(query)

    if category_name:
        logger_djtbot.info('Category name {}'.format(category_name))
        category = ClothesCategoryManager.get_category_id(category=category_name)

        if category:
            logger_djtbot.info('category yes in db')
            clothe = clothes.filter_clothes_for_category(category_id=category.id)

            if clothe:
                logger_djtbot.info('clothes yes in db')
                results = []

                for product in clothe.values():
                    logger_djtbot.info('add product to arrays')
                    results.append(InlineQueryResultPhoto(
                        id=product['id'],
                        photo_url=format_image_url(product['img_center']),
                        thumb_url=format_image_url(product['img_inline']),
                        photo_width=30,
                        photo_height=30,
                        caption=product['description'],
                        parse_mode='HTML',
                        reply_markup=view.product(article_id=product['article_id'],
                                                  category=query),
                        title='Title')
                    )
                logger_djtbot.info('return query inline mode')

                if len(results) > 0:
                    return bot.answer_inline_query(view.chat_id(data),
                                               results=results,
                                               cache_time=0,
                                               next_offset='',
                                               switch_pm_parameter='products',
                                               switch_pm_text=f'{category_name} [{len(clothe)}]')
                else:
                    return bot.send_message(view.user_id(data), message.no_product(), reply_markup=view.menu(),
                                            parse_mode='HTML')

            else:
                logger_djtbot.info('clothes not in db')
                return bot.send_message(view.user_id(data), message.no_product(), reply_markup=view.menu(),
                                        parse_mode='HTML')

        else:
            logger_djtbot.info('category not in db')
            return bot.send_message(view.user_id(data), message.no_product(), reply_markup=view.menu(), parse_mode='HTML')

    else:
        logger_djtbot.info('not product')
        return bot.send_message(view.user_id(data), message.no_product(), reply_markup=view.menu(), parse_mode='HTML')


def add_product_to_basket(data):
    user_id = view.user_id(data)
    product_id = view.get_product_id(data)

    if basket.get(id_user_in_telegram=user_id, product_id=product_id):
        logger_djtbot.info('Product in basket')
        basket.del_product(id_user_in_telegram=user_id, product_id=product_id)
        logger_djtbot.info('Delete product in basket')
        return bot.answer_callback_query(callback_query_id=view.get_inline_query_id(data),
                                         show_alert=True,
                                         text=message.basket_remove_product(product_id))
    else:
        logger_djtbot.info('Not this product in basket')
        basket.add(user_id=user_id, product_id=product_id)
        logger_djtbot.info('Add product in basket')
        return bot.answer_callback_query(callback_query_id=view.get_inline_query_id(data),
                                         show_alert=True,
                                         text=message.basket_add_product(product_id))


def see_product_basket(data):
    user_id = view.user_id(data)
    products = basket.get_product_in_basket(user_id)
    product_list = []

    if products:
        for product in products.values():
            product_list.append(product['product_id'])

    if len(product_list) > 0:
        try:
            img = SystemPhotoManager.get_basket_photo()

            if getattr(img, 'img'):
                return bot.send_photo(view.chat_id(data),
                                      photo=f"{settings.DOMAIN}{img.img.url}",
                                      caption=message.basket(),
                                      reply_markup=view.see_basket(),
                                      parse_mode='HTML')
        except AttributeError:
            print('System Photo Product None')
            return bot.send_message(view.chat_id(data), text=message.basket(),
                                    reply_markup=view.see_basket(), parse_mode='HTML')
    else:
        return bot.send_message(view.chat_id(data), message.basket_not_items(),
                                reply_markup=view.basket(), parse_mode='HTML')


def get_all_product_in_basket(data):
    user_id = view.user_id(data)
    products = basket.get_product_in_basket(user_id)
    query = view.get_text(data)

    if products:
        results = []

        for i in products.values():
            prod = clothes.get_clothes(i['product_id'])

            if prod:
                for product in prod.values():

                    results.append(InlineQueryResultPhoto(
                        id=product['id'],
                        photo_url=format_image_url(product['img_center']),
                        thumb_url=format_image_url(product['img_inline']),
                        photo_width=30,
                        photo_height=30,
                        caption=product['description'],
                        parse_mode='HTML',
                        reply_markup=view.product(article_id=product['article_id'], category=query))
                    )

        return bot.answer_inline_query(view.chat_id(data),
                                       results=results,
                                       cache_time=0,
                                       next_offset='',
                                       switch_pm_parameter='basket',
                                       switch_pm_text=f'Товары [{len(products)}]')


def get_product(data, text):
    img = SystemPhotoManager.get_product_img()

    if img:
        logger_djtbot.info('Product image yes')
        result = bot.send_photo(view.chat_id(data),
                                  photo=open(img.img.path, 'rb'),
                                  caption=message.price(text),
                                  reply_markup=view.price(text),
                                  parse_mode='HTML')
        logger_djtbot.info('Send image to product')
        return result
    else:
        logger_djtbot.info('Product image not fount')
        return bot.send_message(view.chat_id(data), message.price(text),
                                reply_markup=view.price(text), parse_mode='HTML')


def to_share(data):
    return bot.send_message(chat_id=view.chat_id(data), text=message.to_share(),
                            reply_markup=view.to_share(), parse_mode='HTML')


def order(data):
    user_id = view.user_id(data)
    user = user_manager.is_user(user_id=user_id)
    product_id = view.get_product_id(data).split(',')[0]
    product = clothes.get(article_id=product_id)
    OrderManager.add(user_id=user,
                     first_name=user.first_name,
                     article_id=product,
                     price=product.price,
                     markup=product.markup)

    bot.answer_callback_query(callback_query_id=view.get_inline_query_id(data),
                              show_alert=True,
                              text=message.order())

    return bot.send_message(view.chat_id(data), text=message.to_manager(),
                            reply_markup=view.order(), parse_mode='HTML')


def reviews(data):
    return bot.send_message(chat_id=view.chat_id(data), text=message.reviews(),
                            reply_markup=view.reviews(), parse_mode='HTML')
