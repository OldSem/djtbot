from pprint import pprint
import json

from telebot.types import InlineQueryResultPhoto

from .buttons import Buttons
from .menu import Views
from .routes import get_category_id_in_query, get_all_product_in_basket, see_product_view, order, add_product_to_basket
from .manager import SystemPhotoManager
from .bot_view import view
from .webhooks import Bot
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from .manager import UserManager, ManagerUserCity, ManagerUserTypes, ClothesCategoryManager, \
    ClothesManager, BasketManager, OrderManager
from .settings import bot
from .messages import Messages

set_bot = Bot()
set_bot.delete_webhook()
set_bot.set_webhook()


class RenderStartView(TemplateView):
    template_name = 'tgbot/index.html'


class StartView(APIView):
    def get(self, request):
        img = SystemPhotoManager.get_product_img()
        return Response({'photo': f"{settings.DOMAIN}{img.img_url}"}, status.HTTP_200_OK)


class BotView(APIView):
    @csrf_exempt
    def post(self, request):
        if request.method == 'POST':
            data = json.loads(request.body.decode('utf-8'))
            print(data)
            update_id = data['update_id']
            if 'inline_query' in data:
                query = data['inline_query']['query']
                if query is '':
                    clothe = ClothesManager.get_clothes_all()
                    results = []
                    for product in clothe:
                        results.append(InlineQueryResultPhoto(
                            id=product.id,
                            photo_url=f"{settings.DOMAIN}{product.img_center.url}",
                            thumb_url=f"{settings.DOMAIN}{product.img_inline.url}",
                            photo_width=30,
                            photo_height=30,
                            caption=product.description,
                            parse_mode='HTML',
                            description='Photo',
                            reply_markup=Views.product(article_id=product.article_id)))
                    bot.answer_inline_query(data['inline_query']['id'],
                                            results=results,
                                            next_offset='',
                                            switch_pm_parameter='products',
                                            switch_pm_text=f'Все товары в наличии [{len(clothe)}]')
                    return Response('Ok', status=status.HTTP_200_OK)
                elif len(query) > 0:
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
                    bot.answer_inline_query(data['inline_query']['id'],
                                            results=results,
                                            next_offset='',
                                            switch_pm_parameter='products',
                                            switch_pm_text=f'{category_name} [{len(clothe)}]')
                    return Response('Ok', status=status.HTTP_200_OK)
                else:
                    bot.send_message(Views.user_id(data), Messages.no_product(), reply_markup=Views.menu(),
                                     parse_mode='HTML')
                    return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == '/start':
                if UserManager.is_user(data["message"]["chat"]["id"]) is None:
                    UserManager.add_user(data["message"]["chat"]["id"], data["message"]["chat"]["first_name"],
                                         data["message"]["chat"]["username"], data["message"]["from"]["is_bot"])
                    bot.send_message(data["message"]["chat"]["id"], Messages.country(),
                                     reply_markup=Views.question_country())
                    return Response('Ok', status=status.HTTP_200_OK)
                else:
                    bot.send_message(data["message"]["chat"]["id"], Messages.start(), reply_markup=Views.menu(),
                                     parse_mode='HTML')
                    return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == 'Украина':
                user = UserManager.is_user(data["message"]["chat"]["id"])
                if user:
                    status_city = ManagerUserCity.get_user(user.id)
                    if status_city is None:
                        ManagerUserCity.create(user_id=user.id, country=1)
                        bot.send_message(data["message"]["chat"]["id"], Messages.male(),
                                         reply_markup=Views.question_male())
                        return Response('Ok', status=status.HTTP_200_OK)
                    else:
                        ManagerUserCity.update(user_id=user.id, country=1)
                        return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == 'Россия':
                user = UserManager.is_user(data["message"]["chat"]["id"])
                if user:
                    status_city = ManagerUserCity.get_user(user.id)
                    if status_city is None:
                        ManagerUserCity.create(user_id=user.id, country=2)
                        bot.send_message(data["message"]["chat"]["id"], Messages.male(),
                                         reply_markup=Views.question_male())
                        return Response('Ok', status=status.HTTP_200_OK)
                    else:
                        ManagerUserCity.update(user_id=user.id, country=2)
                        return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == 'Мужской':
                user = UserManager.is_user(data["message"]["chat"]["id"])
                if user:
                    status_male = ManagerUserTypes.get_user(user.id)
                    if status_male is None:
                        ManagerUserTypes.create(1, user.id)
                        bot.send_message(data["message"]["chat"]["id"], Messages.start(), reply_markup=Views.menu(),
                                         parse_mode='HTML')
                        return Response('Ok', status=status.HTTP_200_OK)
                    else:
                        ManagerUserTypes.update(user.id, 1)
                        bot.send_message(data["message"]["chat"]["id"], Messages.start(), reply_markup=Views.menu(),
                                         parse_mode='HTML')
                        return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == 'Женский':
                user = UserManager.is_user(data["message"]["chat"]["id"])
                if user:
                    status_male = ManagerUserTypes.get_user(user.id)
                    if status_male is None:
                        ManagerUserTypes.create(2, user.id)
                        bot.send_message(data["message"]["chat"]["id"], Messages.start(), reply_markup=Views.menu(),
                                         parse_mode='HTML')
                        return Response('Ok', status=status.HTTP_200_OK)
                    else:
                        ManagerUserTypes.update(user.id, 2)
                        bot.send_message(data["message"]["chat"]["id"], Messages.start(), reply_markup=Views.menu(),
                                         parse_mode='HTML')
                        return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == 'Верхняя одежда':
                bot.send_message(data["message"]["chat"]["id"], Messages.clothes(), reply_markup=Views.outerwear())
                return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == 'Нижняя одежда':
                bot.send_message(data["message"]["chat"]["id"], Messages.clothes(), reply_markup=Views.underwear())
                return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == 'Костюмы':
                bot.send_message(data["message"]["chat"]["id"], Messages.clothes(), reply_markup=Views.costumes())
                return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == 'Обувь':
                bot.send_message(data["message"]["chat"]["id"], Messages.clothes(), reply_markup=Views.footwear())
                return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == 'Аксессуары':
                bot.send_message(data["message"]["chat"]["id"], Messages.clothes(), reply_markup=Views.accessories())
                return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == '💭 Отзывы':
                bot.send_message(data["message"]["chat"]["id"], Messages.reviews(), reply_markup=Views.reviews(),
                                 parse_mode='HTML')
                return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == '📬 Рассказать друзьям':
                bot.send_message(data["message"]["chat"]["id"], Messages.to_share(), reply_markup=Views.to_share(),
                                 parse_mode='HTML')
                return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == '🛍 Корзина':
                products = BasketManager.get_product_in_basket(data["message"]["chat"]["id"])
                product_list = []
                if products:
                    for product in products:
                        product_list.append(product.product_id)
                if len(product_list) > 0:
                    bot.send_message(data["message"]["chat"]["id"], Messages.basket(), reply_markup=Views.see_basket(),
                                     parse_mode='HTML')
                    return Response('Ok', status=status.HTTP_200_OK)
                else:
                    bot.send_message(data["message"]["chat"]["id"], Messages.basket_not_items(),
                                     reply_markup=Views.basket(),
                                     parse_mode='HTML')
                    return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == '◀️ Назад':
                bot.send_message(data["message"]["chat"]["id"], Messages.user_return(), reply_markup=Views.menu())
                return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == 'Куртки':
                bot.send_message(data["message"]["chat"]["id"], Messages.price(data["message"]["text"]),
                                 reply_markup=Views.price(data["message"]["text"]), parse_mode='HTML')
                return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == 'Кофты':
                bot.send_message(data["message"]["chat"]["id"], Messages.price(data["message"]["text"]),
                                 reply_markup=Views.price(data["message"]["text"]), parse_mode='HTML')
                return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == 'Майки':
                bot.send_message(data["message"]["chat"]["id"], Messages.price(data["message"]["text"]),
                                 reply_markup=Views.price(data["message"]["text"]), parse_mode='HTML')
                return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == 'Футболки':
                bot.send_message(data["message"]["chat"]["id"], Messages.price(data["message"]["text"]),
                                 reply_markup=Views.price(data["message"]["text"]), parse_mode='HTML')
                return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == 'Рубашки':
                bot.send_message(data["message"]["chat"]["id"], Messages.price(data["message"]["text"]),
                                 reply_markup=Views.price(data["message"]["text"]), parse_mode='HTML')
                return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == 'Шапки':
                bot.send_message(data["message"]["chat"]["id"], Messages.price(data["message"]["text"]),
                                 reply_markup=Views.price(data["message"]["text"]), parse_mode='HTML')
                return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == 'Кепки':
                bot.send_message(data["message"]["chat"]["id"], Messages.price(data["message"]["text"]),
                                 reply_markup=Views.price(data["message"]["text"]), parse_mode='HTML')
                return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == 'Брюки':
                bot.send_message(data["message"]["chat"]["id"], Messages.price(data["message"]["text"]),
                                 reply_markup=Views.price(data["message"]["text"]), parse_mode='HTML')
                return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == 'Шорты':
                bot.send_message(data["message"]["chat"]["id"], Messages.price(data["message"]["text"]),
                                 reply_markup=Views.price(data["message"]["text"]), parse_mode='HTML')
                return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == 'Ремни':
                bot.send_message(data["message"]["chat"]["id"], Messages.price(data["message"]["text"]),
                                 reply_markup=Views.price(data["message"]["text"]), parse_mode='HTML')
                return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == 'Бельё':
                bot.send_message(data["message"]["chat"]["id"], Messages.price(data["message"]["text"]),
                                 reply_markup=Views.price(data["message"]["text"]), parse_mode='HTML')
                return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == 'Спортивные костюмы':
                bot.send_message(data["message"]["chat"]["id"], Messages.price(data["message"]["text"]),
                                 reply_markup=Views.price(data["message"]["text"]), parse_mode='HTML')
                return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == 'Классические костюмы':
                bot.send_message(data["message"]["chat"]["id"], Messages.price(data["message"]["text"]),
                                 reply_markup=Views.price(data["message"]["text"]), parse_mode='HTML')
                return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == 'Крассовки':
                bot.send_message(data["message"]["chat"]["id"], Messages.price(data["message"]["text"]),
                                 reply_markup=Views.price(data["message"]["text"]), parse_mode='HTML')
                return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == 'Кеды':
                bot.send_message(data["message"]["chat"]["id"], Messages.price(data["message"]["text"]),
                                 reply_markup=Views.price(data["message"]["text"]), parse_mode='HTML')
                return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == 'Ботинки':
                bot.send_message(data["message"]["chat"]["id"], Messages.price(data["message"]["text"]),
                                 reply_markup=Views.price(data["message"]["text"]), parse_mode='HTML')
                return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == 'Туфли':
                bot.send_message(data["message"]["chat"]["id"], Messages.price(data["message"]["text"]),
                                 reply_markup=Views.price(data["message"]["text"]), parse_mode='HTML')
                return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == 'Рюкзаки':
                bot.send_message(data["message"]["chat"]["id"], Messages.price(data["message"]["text"]),
                                 reply_markup=Views.price(data["message"]["text"]), parse_mode='HTML')
                return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == 'Сумки':
                bot.send_message(data["message"]["chat"]["id"], Messages.price(data["message"]["text"]),
                                 reply_markup=Views.price(data["message"]["text"]), parse_mode='HTML')
                return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == 'Очки':
                bot.send_message(data["message"]["chat"]["id"], Messages.price(data["message"]["text"]),
                                 reply_markup=Views.price(data["message"]["text"]), parse_mode='HTML')
                return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == 'Часы':
                bot.send_message(data["message"]["chat"]["id"], Messages.price(data["message"]["text"]),
                                 reply_markup=Views.price(data["message"]["text"]), parse_mode='HTML')
                return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == 'Кошельки':
                bot.send_message(data["message"]["chat"]["id"], Messages.price(data["message"]["text"]),
                                 reply_markup=Views.price(data["message"]["text"]), parse_mode='HTML')
                return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == 'Чехлы':
                bot.send_message(data["message"]["chat"]["id"], Messages.price(data["message"]["text"]),
                                 reply_markup=Views.price(data["message"]["text"]), parse_mode='HTML')
                return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == 'Духи':
                bot.send_message(data["message"]["chat"]["id"], Messages.price(data["message"]["text"]),
                                 reply_markup=Views.price(data["message"]["text"]), parse_mode='HTML')
                return Response('Ok', status=status.HTTP_200_OK)
            elif data["message"]["text"] == 'Зонты':
                bot.send_message(data["message"]["chat"]["id"], Messages.price(data["message"]["text"]),
                                 reply_markup=Views.price(data["message"]["text"]), parse_mode='HTML')
                return Response('Ok', status=status.HTTP_200_OK)
