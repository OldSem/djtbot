import json

from django.http import HttpResponse
from telebot.types import InlineQueryResultPhoto

from .logger import logger_djtbot as log
from .routes import get_category_id_in_query
from .menu import Views
from .manager import SystemPhotoManager
from .webhooks import Bot
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.generic import TemplateView
from .manager import UserManager, ManagerUserCity, ManagerUserTypes, ClothesCategoryManager, \
    ClothesManager, BasketManager, OrderManager, HistoryUpdateManager
from .settings import bot
from .messages import Messages
from django.views.decorators.csrf import csrf_exempt


set_bot = Bot()
set_bot.delete_webhook()
set_bot.set_webhook()


class RenderStartView(TemplateView):
    template_name = 'tgbot/index.html'


class StartView(APIView):
    def get(self, request):
        img = SystemPhotoManager.get_product_img()
        return Response({'photo': f"{settings.DOMAIN}{img.img_url}"}, status.HTTP_200_OK)


@csrf_exempt
def bot_view(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        if 'message' in data:
            try:
                if get_text(data) == '#куртки':
                    print('#куртки')
                result_message(data)
                return HttpResponse("ok")
            except ValueError as error:
                print(str(error))
                return HttpResponse("ok")
        elif 'inline_query' in data:
            print(data)
            inline_query(data)
            return HttpResponse("ok")


def get_text(data):
    try:
        value = data["message"]["text"]
    except KeyError:
        value = None

    if value is None:
        try:
            value = data['callback_query']['data']
        except KeyError:
            value = None

    if value is None:
        try:
            value = data['inline_query']['query']
        except KeyError:
            value = None

    return value


def get_id_for_chat(data):
    try:
        value = data["message"]["chat"]["id"]
    except KeyError:
        value = None

    if value is None:
        try:
            value = data["callback_query"]["message"]["chat"]["id"]
        except KeyError:
            value = None

    if value is None:
        try:
            value = data["inline_query"]["id"]
        except KeyError:
            value = None

    if value is None:
        try:
            value = data["callback_query"]["from"]["id"]
        except KeyError:
            value = None

    return value


def result_message(data):
    chat_id = get_id_for_chat(data)
    user = UserManager.is_user(chat_id)
    if get_text(data) == '/start':
        if user:
            bot.send_message(chat_id, Messages.start(), reply_markup=Views.menu(), parse_mode='HTML')
        else:
            first_name = data["message"]["chat"]["first_name"]
            username = data["message"]["chat"]["username"]
            is_bot = data["message"]["from"]["is_bot"]
            UserManager.add_user(chat_id, first_name, username, is_bot)
            bot.send_message(chat_id, Messages.country(), reply_markup=Views.question_country())
    elif get_text(data) == 'Украина':
        status_city = ManagerUserCity.get_user(user.id)
        if not status_city:
            ManagerUserCity.create(user_id=user.id, country=1)
            bot.send_message(chat_id, Messages.male(), reply_markup=Views.question_male())
        else:
            ManagerUserCity.update(user_id=user.id, country=1)
    elif get_text(data) == 'Россия':
        if user:
            status_city = ManagerUserCity.get_user(user.id)
            if status_city is None:
                ManagerUserCity.create(user_id=user.id, country=2)
                bot.send_message(chat_id, Messages.male(), reply_markup=Views.question_male())
            else:
                ManagerUserCity.update(user_id=user.id, country=2)
    elif get_text(data) == 'Мужской':
        if user:
            status_male = ManagerUserTypes.get_user(user.id)
            if status_male is None:
                ManagerUserTypes.create(1, user.id)
                bot.send_message(chat_id, Messages.start(), reply_markup=Views.menu(),
                                 parse_mode='HTML')
            else:
                ManagerUserTypes.update(user.id, 1)
                bot.send_message(chat_id, Messages.start(), reply_markup=Views.menu(),
                                 parse_mode='HTML')
    elif get_text(data) == 'Женский':
        if user:
            status_male = ManagerUserTypes.get_user(user.id)
            if status_male is None:
                ManagerUserTypes.create(2, user.id)
                bot.send_message(chat_id, Messages.start(), reply_markup=Views.menu(),
                                 parse_mode='HTML')
            else:
                ManagerUserTypes.update(user.id, 2)
                bot.send_message(chat_id, Messages.start(), reply_markup=Views.menu(),
                                 parse_mode='HTML')
    elif get_text(data) == 'Верхняя одежда':
        bot.send_message(chat_id, Messages.clothes(), reply_markup=Views.outerwear())
        return Response('Ok', status=status.HTTP_200_OK)

    elif get_text(data) == 'Нижняя одежда':
        bot.send_message(chat_id, Messages.clothes(), reply_markup=Views.underwear())
    elif get_text(data) == 'Костюмы':
        bot.send_message(chat_id, Messages.clothes(), reply_markup=Views.costumes())
    elif get_text(data) == 'Обувь':
        bot.send_message(chat_id, Messages.clothes(), reply_markup=Views.footwear())
    elif get_text(data) == 'Аксессуары':
        bot.send_message(chat_id, Messages.clothes(), reply_markup=Views.accessories())
    elif get_text(data) == '💭 Отзывы':
        bot.send_message(chat_id, Messages.reviews(), reply_markup=Views.reviews(), parse_mode='HTML')
    elif get_text(data) == '📬 Рассказать друзьям':
        bot.send_message(chat_id, Messages.to_share(), reply_markup=Views.to_share(), parse_mode='HTML')
    elif get_text(data) == '🛍 Корзина':
        products = BasketManager.get_product_in_basket(chat_id)
        product_list = []
        if products:
            for product in products:
                product_list.append(product.product_id)
        if len(product_list) > 0:
            bot.send_message(chat_id, Messages.basket(), reply_markup=Views.see_basket(),
                             parse_mode='HTML')
        else:
            bot.send_message(chat_id, Messages.basket_not_items(),
                             reply_markup=Views.basket(),
                             parse_mode='HTML')
    elif get_text(data) == '◀️ Назад':
        bot.send_message(chat_id, Messages.user_return(), reply_markup=Views.menu())
    elif get_text(data) == 'Куртки':
        bot.send_message(chat_id, Messages.price(get_text(data)),
                         reply_markup=Views.price(get_text(data)), parse_mode='HTML')
    elif get_text(data) == 'Кофты':
        bot.send_message(chat_id, Messages.price(get_text(data)),
                         reply_markup=Views.price(get_text(data)), parse_mode='HTML')
    elif get_text(data) == 'Майки':
        bot.send_message(chat_id, Messages.price(get_text(data)),
                         reply_markup=Views.price(get_text(data)), parse_mode='HTML')
    elif get_text(data) == 'Футболки':
        bot.send_message(chat_id, Messages.price(get_text(data)),
                         reply_markup=Views.price(get_text(data)), parse_mode='HTML')
    elif get_text(data) == 'Рубашки':
        bot.send_message(chat_id, Messages.price(get_text(data)),
                         reply_markup=Views.price(get_text(data)), parse_mode='HTML')
    elif get_text(data) == 'Шапки':
        bot.send_message(chat_id, Messages.price(get_text(data)),
                         reply_markup=Views.price(get_text(data)), parse_mode='HTML')
    elif get_text(data) == 'Кепки':
        bot.send_message(chat_id, Messages.price(get_text(data)),
                         reply_markup=Views.price(get_text(data)), parse_mode='HTML')
    elif get_text(data) == 'Брюки':
        bot.send_message(chat_id, Messages.price(get_text(data)),
                         reply_markup=Views.price(get_text(data)), parse_mode='HTML')
    elif get_text(data) == 'Шорты':
        bot.send_message(chat_id, Messages.price(get_text(data)),
                         reply_markup=Views.price(get_text(data)), parse_mode='HTML')
    elif get_text(data) == 'Ремни':
        bot.send_message(chat_id, Messages.price(get_text(data)),
                         reply_markup=Views.price(get_text(data)), parse_mode='HTML')
    elif get_text(data) == 'Бельё':
        bot.send_message(chat_id, Messages.price(get_text(data)),
                         reply_markup=Views.price(get_text(data)), parse_mode='HTML')
    elif get_text(data) == 'Спортивные костюмы':
        bot.send_message(chat_id, Messages.price(get_text(data)),
                         reply_markup=Views.price(get_text(data)), parse_mode='HTML')
    elif get_text(data) == 'Классические костюмы':
        bot.send_message(chat_id, Messages.price(get_text(data)),
                         reply_markup=Views.price(get_text(data)), parse_mode='HTML')
    elif get_text(data) == 'Крассовки':
        bot.send_message(chat_id, Messages.price(get_text(data)),
                         reply_markup=Views.price(get_text(data)), parse_mode='HTML')
    elif get_text(data) == 'Кеды':
        bot.send_message(chat_id, Messages.price(get_text(data)),
                         reply_markup=Views.price(get_text(data)), parse_mode='HTML')
    elif get_text(data) == 'Ботинки':
        bot.send_message(chat_id, Messages.price(get_text(data)),
                         reply_markup=Views.price(get_text(data)), parse_mode='HTML')
    elif get_text(data) == 'Туфли':
        bot.send_message(chat_id, Messages.price(get_text(data)),
                         reply_markup=Views.price(get_text(data)), parse_mode='HTML')
    elif get_text(data) == 'Рюкзаки':
        bot.send_message(chat_id, Messages.price(get_text(data)),
                         reply_markup=Views.price(get_text(data)), parse_mode='HTML')
    elif get_text(data) == 'Сумки':
        bot.send_message(chat_id, Messages.price(get_text(data)),
                         reply_markup=Views.price(get_text(data)), parse_mode='HTML')
    elif get_text(data) == 'Очки':
        bot.send_message(chat_id, Messages.price(get_text(data)),
                         reply_markup=Views.price(get_text(data)), parse_mode='HTML')
    elif get_text(data) == 'Часы':
        bot.send_message(chat_id, Messages.price(get_text(data)),
                         reply_markup=Views.price(get_text(data)), parse_mode='HTML')
    elif get_text(data) == 'Кошельки':
        bot.send_message(chat_id, Messages.price(get_text(data)),
                         reply_markup=Views.price(get_text(data)), parse_mode='HTML')
    elif get_text(data) == 'Чехлы':
        bot.send_message(chat_id, Messages.price(get_text(data)),
                         reply_markup=Views.price(get_text(data)), parse_mode='HTML')
        return Response('Ok', status=status.HTTP_200_OK)
    elif get_text(data) == 'Духи':
        bot.send_message(chat_id, Messages.price(get_text(data)),
                         reply_markup=Views.price(get_text(data)), parse_mode='HTML')
    elif get_text(data) == 'Зонты':
        bot.send_message(chat_id, Messages.price(get_text(data)),
                         reply_markup=Views.price(get_text(data)), parse_mode='HTML')
    # else:
    #     bot.send_message(chat_id, f'Непонятно: {data}')
    #     return Response('Ok', status=status.HTTP_200_OK)


def inline_query(data):
    inline_id = data['inline_query']['id']
    log.info('Inline Mode')
    query = data['inline_query']['query']
    log.info('Inline Mode: {0}'.format(query))

    if query is '':
        log.info('Inline Mode: query is " null "')
        clothe = ClothesManager.get_clothes_all()
        log.info('Inline Mode: return clothe all: {0}'.format(clothe))
        results = []

        for product in clothe:
            log.info('Inline Mode: add clothe to array inline')
            results.append(InlineQueryResultPhoto(
                id=product.id,
                photo_url=f"{settings.DOMAIN}{product.img_center.url}",
                thumb_url=f"{settings.DOMAIN}{product.img_inline.url}",
                photo_width=30,
                photo_height=30,
                caption=product.description,
                parse_mode='HTML',
                description='Photo',
                reply_markup=Views.product(article_id=product.article_id, category='all_products')))
        log.info('Inline Mode: result {0}'.format(results))
        bot.answer_inline_query(inline_id,
                                results=results,
                                next_offset='',
                                switch_pm_parameter='products',
                                switch_pm_text=f'Все товары в наличии [{len(clothe)}]')
        log.info('Inline Mode: send photo inline OK, return response 200')
    elif 'all_products' == query:
        print('all_products')
    else:
        query = data['inline_query']['query']
        category_name = get_category_id_in_query(query)
        user_instance = Views.user_id(data)
        user = UserManager.is_user(user_instance)
        country = ManagerUserCity.get_user(user.id).name
        male = ManagerUserTypes.get_user(user.id).name
        category = ClothesCategoryManager.get_category_id(category=category_name)
        clothe = ClothesManager.filter_clothes_for_category(
            category_id=category.id,
            male=1 if male == 'Мужской' else 2,
            country=1 if country == 'Украина' else 2)
        results = []
        for product in clothe:
            results.append(InlineQueryResultPhoto(
                id=product.id,
                photo_url=f"{settings.DOMAIN}{product.img_center.url}",
                thumb_url=f"{settings.DOMAIN}{product.img_inline.url}",
                photo_width=30,
                photo_height=30,
                caption=product.description,
                description='Photo',
                parse_mode='HTML',
                reply_markup=Views.product(article_id=product.article_id, category=query)))
        bot.answer_inline_query(inline_id,
                                results=results,
                                next_offset='',
                                switch_pm_parameter='products',
                                switch_pm_text=f'{category_name} [{len(clothe)}]')
