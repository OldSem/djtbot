class Messages(object):
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
        return "@Shoppi_bot - <strong>Меня зовут Rossi!</strong>\n"\
                "Я бот который поможет вам найти нужную одежду," \
               " обувь и другие аксессуары. Меня разработали для того," \
               " чтобы предоставить вам сервис до сих пор не виденного уровня."

    @classmethod
    def reviews(cls):
        return "Оставить отзыв"

    @classmethod
    def price_sweatshirts(cls):
        return "<strong>Вы выбрали - Кофты!\n</strong>"\
                "Чтобы просмотреть все имеющиеся товары, нажмите кнопку - <strong>Смотреть все!</strong>"

    @classmethod
    def price_jackets(cls):
        return "<strong>Вы выбрали - Куртки!\n</strong>" \
               "Чтобы просмотреть все имеющиеся товары, нажмите кнопку - <strong>Смотреть все!</strong>"

    @classmethod
    def price_t_shirts(cls):
        return "<strong>Вы выбрали - Майки!\n</strong>" \
               "Чтобы просмотреть все имеющиеся товары, нажмите кнопку - <strong>Смотреть все!</strong>"

    @classmethod
    def price_shirts(cls):
        return "<strong>Вы выбрали - Футболки!\n</strong>" \
               "Чтобы просмотреть все имеющиеся товары, нажмите кнопку - <strong>Смотреть все!</strong>"

    @classmethod
    def price_shirts_warm(cls):
        return "<strong>Вы выбрали - Рубашки!\n</strong>" \
               "Чтобы просмотреть все имеющиеся товары, нажмите кнопку - <strong>Смотреть все!</strong>"

    @classmethod
    def price_caps(cls):
        return "<strong>Вы выбрали - Шапки!\n</strong>" \
               "Чтобы просмотреть все имеющиеся товары, нажмите кнопку - <strong>Смотреть все!</strong>"

    @classmethod
    def price_hats(cls):
        return "<strong>Вы выбрали - Кепки!\n</strong>" \
               "Чтобы просмотреть все имеющиеся товары, нажмите кнопку - <strong>Смотреть все!</strong>"

    @classmethod
    def price_tracksuits(cls):
        return "<strong>Вы выбрали - Спортивные костюмы!\n</strong>" \
               "Чтобы просмотреть все имеющиеся товары, нажмите кнопку - <strong>Смотреть все!</strong>"

    @classmethod
    def price_classic_costumes(cls):
        return "<strong>Вы выбрали - Классические костюмы!\n</strong>" \
               "Чтобы просмотреть все имеющиеся товары, нажмите кнопку - <strong>Смотреть все!</strong>"

    @classmethod
    def price_trousers(cls):
        return "<strong>Вы выбрали - Брюки!\n</strong>" \
               "Чтобы просмотреть все имеющиеся товары, нажмите кнопку - <strong>Смотреть все!</strong>"

    @classmethod
    def price_shorts(cls):
        return "<strong>Вы выбрали - Шорты!\n</strong>" \
               "Чтобы просмотреть все имеющиеся товары, нажмите кнопку - <strong>Смотреть все!</strong>"

    @classmethod
    def price_belts(cls):
        return "<strong>Вы выбрали - Ремни!\n</strong>" \
               "Чтобы просмотреть все имеющиеся товары, нажмите кнопку - <strong>Смотреть все!</strong>"

    @classmethod
    def price_underwear(cls):
        return "<strong>Вы выбрали - Белье!\n</strong>" \
               "Чтобы просмотреть все имеющиеся товары, нажмите кнопку - <strong>Смотреть все!</strong>"

    @classmethod
    def price_socks(cls):
        return "<strong>Вы выбрали - Носки!\n</strong>" \
               "Чтобы просмотреть все имеющиеся товары, нажмите кнопку - <strong>Смотреть все!</strong>"

    @classmethod
    def price_sneakers(cls):
        return "<strong>Вы выбрали - Красовки!\n</strong>" \
               "Чтобы просмотреть все имеющиеся товары, нажмите кнопку - <strong>Смотреть все!</strong>"

    @classmethod
    def price_lightweight_sneakers(cls):
        return "<strong>Вы выбрали - Кеды!\n</strong>" \
               "Чтобы просмотреть все имеющиеся товары, нажмите кнопку - <strong>Смотреть все!</strong>"

    @classmethod
    def price_boots(cls):
        return "<strong>Вы выбрали - Ботинки!\n</strong>" \
               "Чтобы просмотреть все имеющиеся товары, нажмите кнопку - <strong>Смотреть все!</strong>"

    @classmethod
    def price_shoes(cls):
        return "<strong>Вы выбрали - Туфли!\n</strong>" \
               "Чтобы просмотреть все имеющиеся товары, нажмите кнопку - <strong>Смотреть все!</strong>"

    @classmethod
    def price_backpacks(cls):
        return "<strong>Вы выбрали - Рюкзаки!\n</strong>" \
               "Чтобы просмотреть все имеющиеся товары, нажмите кнопку - <strong>Смотреть все!</strong>"

    @classmethod
    def price_bags(cls):
        return "<strong>Вы выбрали - Сумки!\n</strong>" \
               "Чтобы просмотреть все имеющиеся товары, нажмите кнопку - <strong>Смотреть все!</strong>"

    @classmethod
    def price_glasses(cls):
        return "<strong>Вы выбрали - Очки!\n</strong>" \
               "Чтобы просмотреть все имеющиеся товары, нажмите кнопку - <strong>Смотреть все!</strong>"

    @classmethod
    def price_clock(cls):
        return "<strong>Вы выбрали - Часы!\n</strong>" \
               "Чтобы просмотреть все имеющиеся товары, нажмите кнопку - <strong>Смотреть все!</strong>"

    @classmethod
    def price_wallets(cls):
        return "<strong>Вы выбрали - Кошельки!\n</strong>" \
               "Чтобы просмотреть все имеющиеся товары, нажмите кнопку - <strong>Смотреть все!</strong>"

    @classmethod
    def price_covers(cls):
        return "<strong>Вы выбрали - Чехлы!\n</strong>" \
               "Чтобы просмотреть все имеющиеся товары, нажмите кнопку - <strong>Смотреть все!</strong>"

    @classmethod
    def price_perfume(cls):
        return "<strong>Вы выбрали - Духи!\n</strong>" \
               "Чтобы просмотреть все имеющиеся товары, нажмите кнопку - <strong>Смотреть все!</strong>"

    @classmethod
    def price_umbrellas(cls):
        return "<strong>Вы выбрали - Зонты!\n</strong>" \
               "Чтобы просмотреть все имеющиеся товары, нажмите кнопку - <strong>Смотреть все!</strong>"

    @classmethod
    def product(cls, product_description):
        return product_description
