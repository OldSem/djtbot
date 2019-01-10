class Messages(object):
    @classmethod
    def start(cls):
        return "Чтобы искать одежду которая интересует, используйте меню. Оно находится внизу в виде кнопок."

    @classmethod
    def clothes(cls):
        return "Отлично, теперь выбирай одежду которая интересует!"

    @classmethod
    def user_return(cls):
        return "Хорошо, что дальше?"

    @classmethod
    def country(cls):
        return "Выберите пожалуйста свою страну проживания." \
               " Это нужно для того, чтобы предоставлять вам актуальную информацию о товарах."

    @classmethod
    def male(cls):
        return "Прекрасно! А теперь выберите свой пол, чтобы я понимал, что для вас искать."

    @classmethod
    def basket_not_items(cls):
        return "<strong>В корзине пока нет товаров!</strong>\n"\
               "Чтобы добавить товар в корзину, при просмотре описания\n" \
               "товара нажмите кнопку - <strong>Корзина!</strong>\n"\
                "<a href='https://robosapiens.icu/media/bot_media/photo_2019-01-03_00-39-41.jpg'>&#160;</a>"

    @classmethod
    def basket(cls):
        return "<strong>Вы выбрали - Корзину!\n</strong>"\
                "Чтобы просмотреть все имеющиеся товары которые" \
               " вы добавили в корзину, нажмите кнопку - <strong>Смотреть!</strong>\n" \
               "<a href='https://robosapiens.icu/media/bot_media/photo_2019-01-03_00-39-27.jpg'>&#160;</a>"

    @classmethod
    def basket_remove_product(cls, product_id):
        return f"Удалили: {product_id}\n"\
                "Если вы хотите добавить товар в корзину, нажмите еще раз кнопку - Корзина."

    @classmethod
    def basket_add_product(cls, product_id):
        return f"Добавили: {product_id}\n"\
                "Если вы хотите удалить товар из корзины, нажмите еще раз кнопку - Корзина."

    @classmethod
    def to_share(cls):
        return "@Robo_Sapiens_Bot - <strong>Меня зовут Robo Sapiens.</strong> " \
               "Я бот который поможет вам найти нужную одежду, обувь и другие аксессуары!\n\n"\
                "Моя цель - положить начало эры удобных покупок через мессенджеры." \
               " С каждым вашим выбором, я становлюсь умнее.\n"\
               "<a href='https://robosapiens.icu/media/bot_media/photo_2019-01-03_00-39-50.jpg'>&#160;</a> "

    @classmethod
    def reviews(cls):
        return '<strong>Вы хотели бы знать, что люди думают о вас?</strong>\n' \
               'Мы очень хотим 😌\n\n' \
               'Предлагаю всем пользователям, которые хотят оставить свой отзыв - сделать это.\n' \
               'Назовем это нашей "книгой жалоб и предложений"\n' \
               'Это будет полезно для новых пользователей,' \
               ' которые хотят видеть реальное мнение о Боте.' \
               '<a href = "https://robosapiens.icu/media/bot_media/photo_2019-01-03_00-39-37.jpg">&#160;</a>'

    @classmethod
    def price(cls, category):
        return f"<strong>Вы выбрали - {category}!\n</strong>"\
                "Чтобы просмотреть все имеющиеся товары, нажмите кнопку - <strong>Смотреть все!</strong>\n"\
                "<a href ='https://robosapiens.icu/media/bot_media/photo_2019-01-03_00-39-17.jpg'>&#160;</a>"

    @classmethod
    def product(cls, product_description):
        return product_description

    @classmethod
    def no_product(cls):
        return "<strong>Товара нет в наличии!\n</strong>"

    @classmethod
    def order(cls):
        return "Оформляем заказ"

    @classmethod
    def to_manager(cls):
        return "<strong>Отличный выбор!</strong>\n" \
               "Чтобы закончить оформление заказа, перейдите пожалуйста в чат с нашим менеджером.\n\n" \
               "© Robo Sapiens\n"\
                "<a href ='https://robosapiens.icu/media/bot_media/photo_2019-01-03_00-39-46.jpg'>&#160;</a>"
