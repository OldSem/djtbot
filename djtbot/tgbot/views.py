from django.http import HttpResponse
from pprint import pprint
from django.views.decorators.csrf import csrf_exempt
import json
from .menu import Views as v
from .messages import Messages as msg
from .buttons import Buttons as b
from .settings import bot
from .routes import start_view, country_view, male_view, see_product_view,\
    add_product_to_basket, see_product_basket, get_all_product_in_basket
from .webhooks import Bot


set_bot = Bot()
set_bot.delete_webhook()
set_bot.set_webhook()


@csrf_exempt
def bot_view(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        pprint(data)

        if v.get_text(data) == "/start":
            start_view(data)

        elif v.get_text(data) == b.btn1.text or v.get_text(data) == b.btn2.text:
            country_view(data)

        elif v.get_text(data) == b.btn3.text or v.get_text(data) == b.btn4.text:
            male_view(data)

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
            see_product_basket(data)

        elif v.get_text(data) == b.btn13.text:
            bot.send_message(v.chat_id(data), msg.user_return(), reply_markup=v.menu())

        elif v.get_text(data) == b.btn15.text:
            bot.send_message(v.chat_id(data), msg.price(), reply_markup=v.price(), parse_mode='HTML')

        elif v.get_text(data) == b.btn40.switch_inline_query_current_chat:
            see_product_view(data)

        elif v.get_text(data) == b.btn48.switch_inline_query_current_chat:
            get_all_product_in_basket(data)

        elif v.get_product_id(data) or v.get_product_id(data):
            add_product_to_basket(data)

        return HttpResponse('Ok', status=200)
