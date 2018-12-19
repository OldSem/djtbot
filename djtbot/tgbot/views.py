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

        elif v.get_text(data) == b.btn14.text:
            bot.send_message(v.chat_id(data), msg.price(b.btn14.text),
                             reply_markup=v.price(b.btn14.text), parse_mode='HTML')

        elif v.get_text(data) == b.btn15.text:
            bot.send_message(v.chat_id(data), msg.price(b.btn15.text),
                             reply_markup=v.price(b.btn15.text), parse_mode='HTML')

        elif v.get_text(data) == b.btn16.text:
            bot.send_message(v.chat_id(data), msg.price(b.btn16.text),
                             reply_markup=v.price(b.btn16.text), parse_mode='HTML')

        elif v.get_text(data) == b.btn17.text:
            bot.send_message(v.chat_id(data), msg.price(b.btn17.text),
                             reply_markup=v.price(b.btn17.text), parse_mode='HTML')

        elif v.get_text(data) == b.btn18.text:
            bot.send_message(v.chat_id(data), msg.price(b.btn18.text),
                             reply_markup=v.price(b.btn18.text), parse_mode='HTML')

        elif v.get_text(data) == b.btn19.text:
            bot.send_message(v.chat_id(data), msg.price(b.btn19.text),
                             reply_markup=v.price(b.btn19.text), parse_mode='HTML')

        elif v.get_text(data) == b.btn20.text:
            bot.send_message(v.chat_id(data), msg.price(b.btn20.text),
                             reply_markup=v.price(b.btn20.text), parse_mode='HTML')

        elif v.get_text(data) == b.btn21.text:
            bot.send_message(v.chat_id(data), msg.price(b.btn21.text),
                             reply_markup=v.price(b.btn21.text), parse_mode='HTML')

        elif v.get_text(data) == b.btn22.text:
            bot.send_message(v.chat_id(data), msg.price(b.btn22.text),
                             reply_markup=v.price(b.btn22.text), parse_mode='HTML')

        elif v.get_text(data) == b.btn23.text:
            bot.send_message(v.chat_id(data), msg.price(b.btn23.text),
                             reply_markup=v.price(b.btn23.text), parse_mode='HTML')

        elif v.get_text(data) == b.btn24.text:
            bot.send_message(v.chat_id(data), msg.price(b.btn24.text),
                             reply_markup=v.price(b.btn24.text), parse_mode='HTML')

        elif v.get_text(data) == b.btn25.text:
            bot.send_message(v.chat_id(data), msg.price(b.btn25.text),
                             reply_markup=v.price(b.btn25.text), parse_mode='HTML')

        elif v.get_text(data) == b.btn26.text:
            bot.send_message(v.chat_id(data), msg.price(b.btn26.text),
                             reply_markup=v.price(b.btn26.text), parse_mode='HTML')

        elif v.get_text(data) == b.btn27.text:
            bot.send_message(v.chat_id(data), msg.price(b.btn27.text),
                             reply_markup=v.price(b.btn27.text), parse_mode='HTML')

        elif v.get_text(data) == b.btn28.text:
            bot.send_message(v.chat_id(data), msg.price(b.btn28.text),
                             reply_markup=v.price(b.btn28.text), parse_mode='HTML')

        elif v.get_text(data) == b.btn29.text:
            bot.send_message(v.chat_id(data), msg.price(b.btn29.text),
                             reply_markup=v.price(b.btn29.text), parse_mode='HTML')

        elif v.get_text(data) == b.btn30.text:
            bot.send_message(v.chat_id(data), msg.price(b.btn30.text),
                             reply_markup=v.price(b.btn30.text), parse_mode='HTML')

        elif v.get_text(data) == b.btn31.text:
            bot.send_message(v.chat_id(data), msg.price(b.btn31.text),
                             reply_markup=v.price(b.btn31.text), parse_mode='HTML')

        elif v.get_text(data) == b.btn32.text:
            bot.send_message(v.chat_id(data), msg.price(b.btn32.text),
                             reply_markup=v.price(b.btn32.text), parse_mode='HTML')

        elif v.get_text(data) == b.btn33.text:
            bot.send_message(v.chat_id(data), msg.price(b.btn33.text),
                             reply_markup=v.price(b.btn33.text), parse_mode='HTML')

        elif v.get_text(data) == b.btn34.text:
            bot.send_message(v.chat_id(data), msg.price(b.btn34.text),
                             reply_markup=v.price(b.btn34.text), parse_mode='HTML')

        elif v.get_text(data) == b.btn35.text:
            bot.send_message(v.chat_id(data), msg.price(b.btn35.text),
                             reply_markup=v.price(b.btn35.text), parse_mode='HTML')

        elif v.get_text(data) == b.btn36.text:
            bot.send_message(v.chat_id(data), msg.price(b.btn36.text),
                             reply_markup=v.price(b.btn36.text), parse_mode='HTML')

        elif v.get_text(data) == b.btn37.text:
            bot.send_message(v.chat_id(data), msg.price(b.btn37.text),
                             reply_markup=v.price(b.btn37.text), parse_mode='HTML')

        elif v.get_text(data) == b.btn38.text:
            bot.send_message(v.chat_id(data), msg.price(b.btn38.text),
                             reply_markup=v.price(b.btn38.text), parse_mode='HTML')

        elif v.get_text(data) == b.btn39.text:
            bot.send_message(v.chat_id(data), msg.price(b.btn39.text),
                             reply_markup=v.price(b.btn39.text), parse_mode='HTML')

        elif v.get_text(data) == b.btn40.switch_inline_query_current_chat:
            see_product_view(data)

        elif v.get_text(data) == b.btn48.switch_inline_query_current_chat:
            get_all_product_in_basket(data)

        elif v.get_product_id(data) or v.get_product_id(data):
            add_product_to_basket(data)

        return HttpResponse('Ok', status=200)
