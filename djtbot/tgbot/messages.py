class Messages(object):
    def __init__(self):
        self.article_id1 = 'A CX12451'
        self.article_id2 = 'A CX12452'
        self.article_id3 = 'A CX12453'
        self.article_id4 = 'A CX12454'
        self.article_id5 = 'A CX12455'
        self.article_id6 = 'A CX12456'
        self.article_id7 = 'A CX12457'

    @classmethod
    def start(cls):
        return "Здравствуйте.\n\n<strong>Меня зовут Rossi!</strong>\nЯ бот который поможет вам найти нужную одежду," \
               " обувь и другие аксессуары. Меня разработали для того," \
               " чтобы предоставить вам сервис до сих пор не виденного уровня.\n\n" \
               "Скоро я стану ещё лучше, и смогу подбирать вам одежду под ваш вкус!"

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
        return "В корзине пока нет товаров!\n"\
               "Если вы хотите просмотреть и добавить товар в корзину," \
               "используйте кнопку - Корзина, при просмотре детального описания товара."

    @classmethod
    def basket(cls):
        return "<strong>Вы выбрали - Корзину!\n</strong>"\
                "Чтобы просмотреть все имеющиеся товары которые" \
               " вы добавили в корзину, нажмите кнопку - <strong>Смотреть!</strong>"

    def basket_remove_product(self):
        return f"Удалили: {self.article_id1}\n"\
                "Если вы хотите добавить товар в корзины, нажмите еще раз кнопку - Корзина."

    def basket_add_product(self):
        return f"<strong>Добавили:</strong> {self.article_id1}\n"\
                "Если вы хотите удалить товар из корзины, нажмите еще раз кнопку - Корзина."

    @classmethod
    def to_share(cls):
        return "@Shoppi_bot - <strong>Меня зовут Rossi!</strong>\n"\
                "Я бот который поможет вам найти нужную одежду," \
               " обувь и другие аксессуары. Меня разработали для того," \
               " чтобы предоставить вам сервис до сих пор не виденного уровня."

    @classmethod
    def reviews(cls):
        return "Оставить отзыв"

    @classmethod
    def price(cls):
        return "<strong>Вы выбрали - Кофты!\n</strong>"\
                "Чтобы просмотреть все имеющиеся товары, нажмите кнопку - <strong>Смотреть все!</strong>"

    def product1(self):
        return "<strong>〰 Road to the Dream</strong>\nСпортивный Лонгслив - Серый\n💰 1800.00 RUB\n\n<b>" \
               "Размер:</b> XS,S,M,L,XL\n<b>Состав:</b> Полиэстер 95%, Эластан 5%\n<b>Производитель:</b> Россия\n" \
               "Артикул - {}".format(self.article_id1)

    def product2(self):
        return "<strong>〰 Road to the Dream</strong>\nСпортивный Лонгслив - Серый\n💰 1800.00 RUB\n\n<b>" \
               "Размер:</b> XS,S,M,L,XL\n<b>Состав:</b> Полиэстер 95%, Эластан 5%\n<b>Производитель:</b> Россия\n" \
               "Артикул - {}".format(self.article_id2)

    def product3(self):
        return "<strong>〰 Road to the Dream</strong>\nСпортивный Лонгслив - Серый\n💰 1800.00 RUB\n\n<b>" \
               "Размер:</b> XS,S,M,L,XL\n<b>Состав:</b> Полиэстер 95%, Эластан 5%\n<b>Производитель:</b> Россия\n" \
               "Артикул - {}".format(self.article_id3)

    def product4(self):
        return "<strong>〰 Road to the Dream</strong>\nСпортивный Лонгслив - Серый\n💰 1800.00 RUB\n\n<b>" \
               "Размер:</b> XS,S,M,L,XL\n<b>Состав:</b> Полиэстер 95%, Эластан 5%\n<b>Производитель:</b> Россия\n" \
               "Артикул - {}".format(self.article_id4)

    def product5(self):
        return "<strong>〰 Road to the Dream</strong>\nСпортивный Лонгслив - Серый\n💰 1800.00 RUB\n\n<b>" \
               "Размер:</b> XS,S,M,L,XL\n<b>Состав:</b> Полиэстер 95%, Эластан 5%\n<b>Производитель:</b> Россия\n" \
               "Артикул - {}".format(self.article_id5)

    def product6(self):
        return "<strong>〰 Road to the Dream</strong>\nСпортивный Лонгслив - Серый\n💰 1800.00 RUB\n\n<b>" \
               "Размер:</b> XS,S,M,L,XL\n<b>Состав:</b> Полиэстер 95%, Эластан 5%\n<b>Производитель:</b> Россия\n" \
               "Артикул - {}".format(self.article_id6)

    def product7(self):
        return "<strong>〰 Road to the Dream</strong>\nСпортивный Лонгслив - Серый\n💰 1800.00 RUB\n\n<b>" \
               "Размер:</b> XS,S,M,L,XL\n<b>Состав:</b> Полиэстер 95%, Эластан 5%\n<b>Производитель:</b> Россия\n" \
               "Артикул - {}".format(self.article_id7)