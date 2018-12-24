class Messages(object):
    @classmethod
    def start(cls):
        return "Здравствуйте.\n\n<strong>Меня зовут Rosie!</strong>\nЯ бот который поможет вам найти нужную одежду," \
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
        return "<strong>В корзине пока нет товаров!</strong>\n"\
               "Чтобы добавить товар в корзину, при просмотре описания\n" \
               "товара нажмите кнопку - <strong>Корзина!</strong>"

    @classmethod
    def basket(cls):
        return "<strong>Вы выбрали - Корзину!\n</strong>"\
                "Чтобы просмотреть все имеющиеся товары которые" \
               " вы добавили в корзину, нажмите кнопку - <strong>Смотреть!</strong>"

    @classmethod
    def basket_remove_product(cls, product_id):
        return f"<strong>Удалили:</strong> {product_id}\n"\
                "Если вы хотите добавить товар в корзину, нажмите еще раз кнопку - Корзина."

    @classmethod
    def basket_add_product(cls, product_id):
        return f"<strong>Добавили:</strong> {product_id}\n"\
                "Если вы хотите удалить товар из корзины, нажмите еще раз кнопку - Корзина."

    @classmethod
    def to_share(cls):
        return "@Shoppi_bot - <strong>Меня зовут Rosie.</strong> " \
               "Я бот который поможет вам найти нужную одежду, обувь и другие аксессуары!"

    @classmethod
    def reviews(cls):
        return "Оставить отзыв https://comments.bot/thread/HJO5kQInz"

    @classmethod
    def price(cls, category):
        return f"<strong>Вы выбрали - {category}!\n</strong>"\
                "Чтобы просмотреть все имеющиеся товары, нажмите кнопку - <strong>Смотреть все!</strong>"

    @classmethod
    def product(cls, product_description):
        return product_description

    @classmethod
    def no_product(cls):
        return "<strong>Товара нет в наличии!\n</strong>"
