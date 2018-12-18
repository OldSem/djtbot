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
            bot.send_message(v.chat_id(data), msg.price_jackets(), reply_markup=v.price(), parse_mode='HTML')

        elif v.get_text(data) == b.btn15.text:
            bot.send_message(v.chat_id(data), msg.price_sweatshirts(), reply_markup=v.price(), parse_mode='HTML')

        elif v.get_text(data) == b.btn16.text:
            bot.send_message(v.chat_id(data), msg.price_t_shirts(), reply_markup=v.price(), parse_mode='HTML')

        elif v.get_text(data) == b.btn17.text:
            bot.send_message(v.chat_id(data), msg.price_shirts(), reply_markup=v.price(), parse_mode='HTML')

        elif v.get_text(data) == b.btn18.text:
            bot.send_message(v.chat_id(data), msg.price_shirts_warm(), reply_markup=v.price(), parse_mode='HTML')

        elif v.get_text(data) == b.btn19.text:
            bot.send_message(v.chat_id(data), msg.price_caps(), reply_markup=v.price(), parse_mode='HTML')

        elif v.get_text(data) == b.btn20.text:
            bot.send_message(v.chat_id(data), msg.price_hats(), reply_markup=v.price(), parse_mode='HTML')

        elif v.get_text(data) == b.btn21.text:
            bot.send_message(v.chat_id(data), msg.price_trousers(), reply_markup=v.price(), parse_mode='HTML')

        elif v.get_text(data) == b.btn22.text:
            bot.send_message(v.chat_id(data), msg.price_shorts(), reply_markup=v.price(), parse_mode='HTML')

        elif v.get_text(data) == b.btn23.text:
            bot.send_message(v.chat_id(data), msg.price_belts(), reply_markup=v.price(), parse_mode='HTML')

        elif v.get_text(data) == b.btn24.text:
            bot.send_message(v.chat_id(data), msg.price_underwear(), reply_markup=v.price(), parse_mode='HTML')

        elif v.get_text(data) == b.btn25.text:
            bot.send_message(v.chat_id(data), msg.price_socks(), reply_markup=v.price(), parse_mode='HTML')

        elif v.get_text(data) == b.btn26.text:
            bot.send_message(v.chat_id(data), msg.price_tracksuits(), reply_markup=v.price(), parse_mode='HTML')

        elif v.get_text(data) == b.btn27.text:
            bot.send_message(v.chat_id(data), msg.price_classic_costumes(), reply_markup=v.price(), parse_mode='HTML')

        elif v.get_text(data) == b.btn28.text:
            bot.send_message(v.chat_id(data), msg.price_sneakers(), reply_markup=v.price(), parse_mode='HTML')

        elif v.get_text(data) == b.btn29.text:
            bot.send_message(v.chat_id(data), msg.price_lightweight_sneakers(), reply_markup=v.price(), parse_mode='HTML')

        elif v.get_text(data) == b.btn30.text:
            bot.send_message(v.chat_id(data), msg.price_boots(), reply_markup=v.price(), parse_mode='HTML')

        elif v.get_text(data) == b.btn31.text:
            bot.send_message(v.chat_id(data), msg.price_shoes(), reply_markup=v.price(), parse_mode='HTML')

        elif v.get_text(data) == b.btn32.text:
            bot.send_message(v.chat_id(data), msg.price_backpacks(), reply_markup=v.price(), parse_mode='HTML')

        elif v.get_text(data) == b.btn33.text:
            bot.send_message(v.chat_id(data), msg.price_bags(), reply_markup=v.price(), parse_mode='HTML')

        elif v.get_text(data) == b.btn34.text:
            bot.send_message(v.chat_id(data), msg.price_glasses(), reply_markup=v.price(), parse_mode='HTML')

        elif v.get_text(data) == b.btn35.text:
            bot.send_message(v.chat_id(data), msg.price_clock(), reply_markup=v.price(), parse_mode='HTML')

        elif v.get_text(data) == b.btn36.text:
            bot.send_message(v.chat_id(data), msg.price_wallets(), reply_markup=v.price(), parse_mode='HTML')

        elif v.get_text(data) == b.btn37.text:
            bot.send_message(v.chat_id(data), msg.price_covers(), reply_markup=v.price(), parse_mode='HTML')

        elif v.get_text(data) == b.btn38.text:
            bot.send_message(v.chat_id(data), msg.price_perfume(), reply_markup=v.price(), parse_mode='HTML')

        elif v.get_text(data) == b.btn39.text:
            bot.send_message(v.chat_id(data), msg.price_umbrellas(), reply_markup=v.price(), parse_mode='HTML')

        elif v.get_text(data) == b.btn40.switch_inline_query_current_chat:
            see_product_view(data)

        elif v.get_text(data) == b.btn48.switch_inline_query_current_chat:
            get_all_product_in_basket(data)

        elif v.get_product_id(data) or v.get_product_id(data):
            add_product_to_basket(data)

        return HttpResponse('Ok', status=200)
