from .menu import Views as v
from .messages import Messages as msg
from .buttons import Buttons as b
from .settings import bot
from .routes import start_view, country_view, male_view, see_product_view, \
    add_product_to_basket, see_product_basket, get_all_product_in_basket, get_product, to_share, order, reviews


def view(data):
    if v.get_text(data) == "/start":
        return start_view(data)

    elif v.get_text(data) == b.btn1.text or v.get_text(data) == b.btn2.text:
        return country_view(data)

    elif v.get_text(data) == b.btn3.text or v.get_text(data) == b.btn4.text:
        return male_view(data)

    elif v.get_text(data) == b.btn5.text:
        return bot.send_message(v.chat_id(data), msg.clothes(), reply_markup=v.outerwear())

    elif v.get_text(data) == b.btn6.text:
        return bot.send_message(v.chat_id(data), msg.clothes(), reply_markup=v.underwear())

    elif v.get_text(data) == b.btn7.text:
        return bot.send_message(v.chat_id(data), msg.clothes(), reply_markup=v.costumes())

    elif v.get_text(data) == b.btn8.text:
        return bot.send_message(v.chat_id(data), msg.clothes(), reply_markup=v.footwear())

    elif v.get_text(data) == b.btn9.text:
        return bot.send_message(v.chat_id(data), msg.clothes(), reply_markup=v.accessories())

    elif v.get_text(data) == b.btn10.text:
        return reviews(data)

    elif v.get_text(data) == b.btn11.text:
        return to_share(data)

    elif v.get_text(data) == b.btn12.text:
        return see_product_basket(data)

    elif v.get_text(data) == b.btn13.text:
        return bot.send_message(v.chat_id(data), msg.user_return(), reply_markup=v.menu())

    elif v.get_text(data) == b.btn14.text:
        return get_product(data, text=b.btn14.text)

    elif v.get_text(data) == b.btn15.text:
        return get_product(data, text=b.btn15.text)

    elif v.get_text(data) == b.btn16.text:
        return get_product(data, text=b.btn16.text)

    elif v.get_text(data) == b.btn17.text:
        return get_product(data, text=b.btn17.text)

    elif v.get_text(data) == b.btn18.text:
        return get_product(data, text=b.btn18.text)

    elif v.get_text(data) == b.btn19.text:
        return get_product(data, text=b.btn19.text)

    elif v.get_text(data) == b.btn20.text:
        return get_product(data, text=b.btn20.text)

    elif v.get_text(data) == b.btn21.text:
        return get_product(data, text=b.btn21.text)

    elif v.get_text(data) == b.btn22.text:
        return get_product(data, text=b.btn22.text)

    elif v.get_text(data) == b.btn23.text:
        return get_product(data, text=b.btn23.text)

    elif v.get_text(data) == b.btn24.text:
        return get_product(data, text=b.btn24.text)

    elif v.get_text(data) == b.btn25.text:
        return get_product(data, text=b.btn25.text)

    elif v.get_text(data) == b.btn26.text:
        return get_product(data, text=b.btn26.text)

    elif v.get_text(data) == b.btn27.text:
        return get_product(data, text=b.btn27.text)

    elif v.get_text(data) == b.btn28.text:
        return get_product(data, text=b.btn28.text)

    elif v.get_text(data) == b.btn29.text:
        return get_product(data, text=b.btn29.text)

    elif v.get_text(data) == b.btn30.text:
        return get_product(data, text=b.btn30.text)

    elif v.get_text(data) == b.btn31.text:
        return get_product(data, text=b.btn31.text)

    elif v.get_text(data) == b.btn32.text:
        return get_product(data, text=b.btn32.text)

    elif v.get_text(data) == b.btn33.text:
        return get_product(data, text=b.btn33.text)

    elif v.get_text(data) == b.btn34.text:
        return get_product(data, text=b.btn34.text)

    elif v.get_text(data) == b.btn35.text:
        return get_product(data, text=b.btn35.text)

    elif v.get_text(data) == b.btn36.text:
        return get_product(data, text=b.btn36.text)

    elif v.get_text(data) == b.btn37.text:
        return get_product(data, text=b.btn37.text)

    elif v.get_text(data) == b.btn38.text:
        return get_product(data, text=b.btn38.text)

    elif v.get_text(data) == b.btn39.text:
        return get_product(data, text=b.btn39.text)

    elif v.get_text(data) == b.btn40.switch_inline_query_current_chat:
        return see_product_view(data)

    elif v.get_product_id(data):
        count = len(v.get_product_id(data).split(','))

        if count > 1:
            return order(data)
        else:
            return add_product_to_basket(data)

    elif v.get_text(data) == b.btn48.switch_inline_query_current_chat:
        return get_all_product_in_basket(data)


def bot_error(data):
    return bot.answer_callback_query(v.user_id(data), msg.no_product(),
                            reply_markup=v.menu(), parse_mode='HTML')
