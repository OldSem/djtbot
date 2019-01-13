from .menu import Views as v
from .messages import Messages as msg
from .buttons import Buttons as b
from .settings import bot
from .routes import start_view, country_view, male_view, see_product_view, \
    add_product_to_basket, see_product_basket, get_all_product_in_basket, get_product, to_share, order, reviews


def view(data):

    if v.get_text(data) == b.btn40.switch_inline_query_current_chat:
        see_product_view(data)

    elif v.get_product_id(data):
        product_count_array = len(v.get_product_id(data).split(','))

        if product_count_array > 1:
            order(data)
        else:
            add_product_to_basket(data)

    elif v.get_text(data) == b.btn48.switch_inline_query_current_chat:
        get_all_product_in_basket(data)
