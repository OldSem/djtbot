from django.http import HttpResponse
from telebot import TeleBot, logger, types
from django.conf import settings
from pprint import pprint
import requests
from django.views.decorators.csrf import csrf_exempt
import json
from .menu import Views as v
from .messages import Messages as msg
from .buttons import Buttons as b
import logging
from .manager import UserManager as u, ManagerUserCity as city, ManagerUserTypes as t, ClothesManager as c


bot = TeleBot(settings.TOKEN)
bot.set_webhook(settings.DOMAIN)

logger.setLevel(logging.DEBUG)
basket = []


def delete_webhook():
    r = bot.delete_webhook()
    pprint(r)


def get_url(method):
    return "{}/bot{}/{}".format(settings.TELEGRAM_URL, settings.TOKEN, method)


def set_webhook():
    r = requests.get(get_url("setWebhook"), data={"url": f"{settings.DOMAIN}/{settings.TOKEN}"})
    r = requests.get(get_url("getWebhookInfo"))

    pprint(r.status_code)
    pprint(r.json())


delete_webhook()
set_webhook()


@csrf_exempt
def bot_view(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        pprint(data)

        if v.get_text(data) == "/start":
            if u.is_user(v.chat_id(data)) is None:
                u.add_user(v.user_id(data), v.first_name(data), v.username(data), v.is_bot(data))
                bot.send_message(v.chat_id(data), msg.country(), reply_markup=v.question_country())

            else:
                bot.send_message(v.chat_id(data), msg.start(), reply_markup=v.menu(), parse_mode='HTML')

        elif v.get_text(data) == b.btn1.text or v.get_text(data) == b.btn2.text:
            user_id = v.user_id(data)
            user = u.is_user(user_id)

            if user:
                status_city = city.get_user(user.id)

                if status_city is None:
                    if v.get_text(data) == b.btn1.text:
                        city.create(user_id=user.id, country=1)
                        bot.send_message(v.chat_id(data), msg.male(), reply_markup=v.question_male())

                    elif v.get_text(data) == b.btn2.text:
                        city.create(user_id=user.id, country=2)
                        bot.send_message(v.chat_id(data), msg.male(), reply_markup=v.question_male())

                else:
                    if v.get_text(data) == b.btn1.text:
                        city.update(user_id=user.id, country=1)
                        bot.send_message(v.chat_id(data), msg.male(), reply_markup=v.question_male())

                    elif v.get_text(data) == b.btn2.text:
                        city.update(user_id=user.id, country=2)
                        bot.send_message(v.chat_id(data), msg.male(), reply_markup=v.question_male())

        elif v.get_text(data) == b.btn3.text or v.get_text(data) == b.btn4.text:
            user_id = v.user_id(data)
            user = u.is_user(user_id)

            if user:
                status_male = t.get_user(user.id)

                if status_male is None:
                    if v.get_text(data) == b.btn3.text:
                        t.create(1, user.id)
                        bot.send_message(v.chat_id(data), msg.start(), reply_markup=v.menu(), parse_mode='HTML')

                    elif v.get_text(data) == b.btn4.text:
                        t.create(2, user.id)
                        bot.send_message(v.chat_id(data), msg.start(), reply_markup=v.menu(), parse_mode='HTML')

                else:
                    if v.get_text(data) == b.btn3.text:
                        t.update(user.id, 1)
                        bot.send_message(v.chat_id(data), msg.start(), reply_markup=v.menu(), parse_mode='HTML')

                    elif v.get_text(data) == b.btn4.text:
                        t.update(user.id, 2)
                        bot.send_message(v.chat_id(data), msg.start(), reply_markup=v.menu(), parse_mode='HTML')

        elif v.get_text(data) == b.btn5.text:
            bot.send_message(v.chat_id(data), msg.clothes(), reply_markup=v.outerwear())

        elif v.get_text(data) == b.btn6.text:
            bot.send_message(v.chat_id(data), msg.clothes(), reply_markup=v.underwear())

        elif v.get_text(data) == b.btn7.text:
            bot.send_message(v.chat_id(data), msg.clothes(), reply_markup=v.costumes())

        elif v.get_text(data) == b.btn8.text:
            bot.send_message(v.chat_id(data), msg.clothes(), reply_markup=v.footwear())

        elif v.get_text(data) == b.btn9.text:
            bot.send_message(v.chat_id(data), msg.clothes(), reply_markup=v.accessories())

        elif v.get_text(data) == b.btn10.text:
            bot.send_message(v.chat_id(data), msg.reviews(), reply_markup=v.reviews())

        elif v.get_text(data) == b.btn11.text:
            bot.send_message(v.chat_id(data), msg.to_share(), reply_markup=v.to_share(), parse_mode='HTML')

        elif v.get_text(data) == b.btn12.text:
            if len(basket) > 0:
                bot.send_message(v.chat_id(data), text=msg.basket(), reply_markup=v.see_basket(), parse_mode='HTML')

            else:
                bot.send_message(v.chat_id(data), msg.basket_not_items(), reply_markup=v.basket())

        elif v.get_text(data) == b.btn13.text:
            bot.send_message(v.chat_id(data), msg.user_return(), reply_markup=v.menu())

        elif v.get_text(data) == b.btn15.text:
            bot.send_message(v.chat_id(data), msg.price(), reply_markup=v.price(), parse_mode='HTML')

        elif v.get_text(data) == b.btn40.switch_inline_query_current_chat:
            results = []
            clothes = c.get_clothes_all().values()

            if clothes:
                for i in clothes:
                    results.append(types.InlineQueryResultPhoto(
                        id=i['article_id'], photo_url=f"{settings.DOMAIN}{settings.MEDIA_URL}{i['img_top']}",
                        thumb_url=f"{settings.DOMAIN}{settings.MEDIA_URL}{i['img_left']}", photo_width=30,
                        photo_height=30, caption=i['description'], parse_mode='HTML',
                        reply_markup=v.product())
                    )

            bot.answer_inline_query(v.chat_id(data), results=results, cache_time=0, next_offset='')

        elif v.get_text(data) == b.btn48.switch_inline_query_current_chat and len(basket) > 0:
            bot.answer_inline_query(v.chat_id(data), results=basket, cache_time=0, next_offset='')

        # elif v.get_text(data) and b.product.article_id1 in v.get_text(data):
        #     product_id = v.get_product_id(data)
        #
        #     if product_id:
        #         if product_id in basket:
        #             basket.remove(product_id)
        #             bot.send_message(v.chat_id(data), text=msg().basket_remove_product(), parse_mode='HTML')

                #else:
                    #basket.append(types.InlineQueryResultPhoto(id=product_id,
                                                                   # photo_url=img1,
                                                                   # thumb_url=img1,
                                                                   # photo_width=30,
                                                                   # photo_height=30))
                   #bot.send_message(v.chat_id(data), text=msg().basket_add_product(), parse_mode='HTML')

        #elif v.get_text(data) == b.btn47.switch_inline_query_current_chat:
            #results = [r1, r2, r3, r4, r5, r6, r7]
            #bot.answer_inline_query(v.chat_id(data), results=results, cache_time=0, next_offset='')
        return HttpResponse('Ok', status=200)
