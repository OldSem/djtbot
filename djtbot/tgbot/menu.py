from .buttons import Buttons as btn, Url
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup


class Views(object):
    """View menu for Bot"""
    @classmethod
    def menu(cls):
        markup = ReplyKeyboardMarkup()
        markup.row(btn.btn11)
        markup.row(btn.btn5)
        markup.row(btn.btn6)
        markup.row(btn.btn7)
        markup.row(btn.btn8)
        markup.row(btn.btn9)
        markup.row(btn.btn10, btn.btn12)
        return markup

    @classmethod
    def question_country(cls):
        markup = ReplyKeyboardMarkup()
        markup.row(btn.btn1, btn.btn2)
        markup.resize_keyboard = True
        return markup

    @classmethod
    def question_male(cls):
        markup = ReplyKeyboardMarkup()
        markup.row(btn.btn3, btn.btn4)
        markup.resize_keyboard = True
        return markup

    @classmethod
    def outerwear(cls):
        markup = ReplyKeyboardMarkup()
        markup.row(btn.btn14)
        markup.row(btn.btn15)
        markup.row(btn.btn16)
        markup.row(btn.btn17)
        markup.row(btn.btn18)
        markup.row(btn.btn19)
        markup.row(btn.btn20)
        markup.row(btn.btn13, btn.btn12)
        return markup

    @classmethod
    def underwear(cls):
        markup = ReplyKeyboardMarkup()
        markup.row(btn.btn21)
        markup.row(btn.btn22)
        markup.row(btn.btn23)
        markup.row(btn.btn24)
        markup.row(btn.btn25)
        markup.row(btn.btn13, btn.btn12)
        return markup

    @classmethod
    def costumes(cls):
        markup = ReplyKeyboardMarkup()
        markup.row(btn.btn26)
        markup.row(btn.btn27)
        markup.row(btn.btn13, btn.btn12)
        markup.resize_keyboard = True
        return markup

    @classmethod
    def footwear(cls):
        markup = ReplyKeyboardMarkup()
        markup.row(btn.btn28)
        markup.row(btn.btn29)
        markup.row(btn.btn30)
        markup.row(btn.btn31)
        markup.row(btn.btn13, btn.btn12)
        return markup

    @classmethod
    def accessories(cls):
        markup = ReplyKeyboardMarkup()
        markup.row(btn.btn32)
        markup.row(btn.btn33)
        markup.row(btn.btn34)
        markup.row(btn.btn38)
        markup.row(btn.btn39)
        markup.row(btn.btn13, btn.btn12)
        return markup

    @classmethod
    def basket(cls):
        markup = ReplyKeyboardMarkup()
        markup.row(btn.btn13, btn.btn12)
        markup.resize_keyboard = True
        return markup

    @classmethod
    def price(cls, category):
        markup = InlineKeyboardMarkup()
        btn.btn40.switch_inline_query_current_chat = '#'+(str(category).lower())
        markup.add(btn.btn40)
        return markup

    @classmethod
    def see_basket(cls):
        markup = InlineKeyboardMarkup()
        markup.add(btn.btn48)
        return markup

    @classmethod
    def navigator(cls):
        markup = InlineKeyboardMarkup()
        markup.add(btn.btn43, btn.btn44)
        return markup

    @classmethod
    def to_share(cls):
        markup = InlineKeyboardMarkup()
        markup.add(btn.btn49)
        return markup

    @classmethod
    def reviews(cls):
        markup = InlineKeyboardMarkup()
        markup.add(btn.btn51)
        return markup

    @classmethod
    def product(cls, article_id, category=None, user_id=None):
        markup = InlineKeyboardMarkup()
        btn.btn45.callback_data = f'{article_id}, {user_id}'
        btn.btn46.callback_data = article_id
        btn.btn47.switch_inline_query_current_chat = category if category else 'all_category'
        markup.add(btn.btn45, btn.btn46)
        markup.add(btn.btn47)
        return markup

    @classmethod
    def all_product(cls):
        markup = InlineKeyboardMarkup()
        markup.add(btn.btn45, btn.btn46)
        markup.add(btn.btn47)
        return markup

    @classmethod
    def order(cls):
        markup = InlineKeyboardMarkup()
        markup.add(btn.btn50)
        return markup

    @classmethod
    def get_text(cls, data):
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

    @classmethod
    def chat_id(cls, data):
        try:
            if isinstance(data, dict):
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
        except:
            pass

    @classmethod
    def first_name(cls, data):
        try:
            if isinstance(data, dict):
                try:
                    value = data["message"]["chat"]["first_name"]
                except KeyError:
                    value = None

                if value is None:
                    try:
                        value = data["callback_query"]["message"]["chat"]["first_name"]
                    except KeyError:
                        value = None

                if value is None:
                    try:
                        value = data["inline_query"]["from"]["first_name"]
                    except KeyError:
                        value = None

                return value
        except:
            pass

    @classmethod
    def username(cls, data):
        try:
            if isinstance(data, dict):
                try:
                    value = data["message"]["chat"]["username"]
                except KeyError:
                    value = None

                if value is None:
                    try:
                        value = data["callback_query"]["message"]["chat"]["username"]
                    except KeyError:
                        value = None

                if value is None:
                    try:
                        value = data["inline_query"]["from"]["username"]
                    except KeyError:
                        value = None

                return value
        except:
            pass

    @classmethod
    def is_bot(cls, data):
        try:
            if isinstance(data, dict):
                try:
                    value = data["message"]["from"]["is_bot"]
                except KeyError:
                    value = None

                if value is None:
                    try:
                        value = data["callback_query"]["message"]["from"]["is_bot"]
                    except KeyError:
                        value = None

                if value is None:
                    try:
                        value = data["inline_query"]["from"]["is_bot"]
                    except KeyError:
                        value = None

                return value
        except:
            pass

    @classmethod
    def user_id(cls, data):
        try:
            if isinstance(data, dict):
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
                        value = data["callback_query"]["from"]["id"]
                    except KeyError:
                        value = None

                if value is None:
                    try:
                        value = data["inline_query"]["from"]["id"]
                    except KeyError:
                        value = None

                return value
        except:
            pass

    @classmethod
    def get_caption(cls, data):
        try:
            value = data["callback_query"]["caption"]
        except KeyError:
            value = None

        return value

    @classmethod
    def get_product_id(cls, data):
        try:
            value = data['callback_query']['data']
        except KeyError:
            value = None
        return value

    @classmethod
    def get_photo_id(cls, data):
        try:
            value = data['message']['photo']
        except KeyError:
            value = None
        return value

    @classmethod
    def get_inline_query_id(cls, data):
        try:
            value = data["callback_query"]["id"]
        except KeyError:
            value = None

        return value

    @classmethod
    def error_code(cls, data):
        try:
            value = data["error_code"]
        except KeyError:
            value = None

        return value
