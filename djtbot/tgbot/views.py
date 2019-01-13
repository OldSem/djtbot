from pprint import pprint
import json

from telebot.types import InlineQueryResultPhoto

from .buttons import Buttons
from .menu import Views
from .routes import get_category_id_in_query
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
    ClothesManager
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

            if settings.DEBUG:
                pprint(data)
            query = data.get('inline_query', None)
            if query:
                if Views.get_text(data) == Buttons.btn40.switch_inline_query_current_chat:
                    query = Views.get_text(data)
                    print(1)
                    category_name = get_category_id_in_query(query)
                    print(2)
                    user_instance = Views.user_id(data)
                    print(3)
                    user = UserManager.is_user(user_instance)
                    print(4)
                    country = ManagerUserCity.get_user(user.id).name
                    print(5)
                    male = ManagerUserTypes.get_user(user.id).name
                    print(6)
                    category = ClothesCategoryManager.get_category_id(category=category_name)
                    print(7)
                    clothe = ClothesManager.filter_clothes_for_category(
                        category_id=category.id,
                        male=1 if male == 'Мужской' else 2,
                        country=1 if country == 'Украина' else 2)
                    print(8)
                    if clothe:
                        results = []
                        print(9)
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
                        print(10)
                        bot.answer_inline_query(data['inline_query']['id'],
                                                   results=results,
                                                   next_offset='',
                                                   switch_pm_parameter='products',
                                                   switch_pm_text=f'{category_name} [{len(clothe)}]')
                        return Response('Ok', status=status.HTTP_200_OK)
                    else:
                        print(11)
                        bot.send_message(Views.user_id(data), Messages.no_product(), reply_markup=Views.menu(),
                                            parse_mode='HTML')
                        return Response('Ok', status=status.HTTP_200_OK)

                else:
                    print(1)
                    clothe = ClothesManager.get_clothes_all()
                    if clothe:
                        results = []
                        print(9)
                        for product in clothe:
                            results.append(InlineQueryResultPhoto(
                                id=product.id,
                                photo_url=f"{settings.DOMAIN}{product.img_center.url}",
                                thumb_url=f"{settings.DOMAIN}{product.img_inline.url}",
                                photo_width=30,
                                photo_height=30,
                                caption=product.description,
                                description='Photo'))
                        print(10)
                        bot.answer_inline_query(data['inline_query']['id'],
                                                   results=results,
                                                   next_offset='',
                                                   switch_pm_parameter='products',
                                                   switch_pm_text=f'Все товары в наличии [{len(clothe)}]')
                        return Response('Ok', status=status.HTTP_200_OK)
                    else:
                        print(11)
                        bot.send_message(Views.user_id(data), Messages.no_product(), reply_markup=Views.menu(),
                                            parse_mode='HTML')
                        return Response('Ok', status=status.HTTP_200_OK)
            else:
                view(data)
            return Response('Ok', status=status.HTTP_200_OK)
