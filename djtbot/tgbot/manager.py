from .models import *


class UserManager(object):
    @classmethod
    def is_user(cls, user_id):
        try:
            user = User.objects.get(id_user_in_telegram=user_id)
        except User.DoesNotExist:
            user = None

        return user

    @classmethod
    def add_user(cls, id_user_in_telegram, first_name, username, is_bot):
        user = User.objects.create(
            id_user_in_telegram=id_user_in_telegram,
            first_name=first_name,
            username=username,
            is_bot=is_bot
        )
        user.save()


class ManagerUserCity(object):
    @classmethod
    def get_user(cls, user_id):
        try:
            country = Country.objects.get(user_id=user_id)
        except Country.DoesNotExist:
            country = None

        return country

    @classmethod
    def create(cls, country, user_id):
        user = Country.objects.create(
            name='Украина' if country == 1 else 'Россия',
            user_id=user_id
        )
        user.save()

    @classmethod
    def update(cls, user_id, country):
        user = Country.objects.filter(user_id=user_id).update(name='Украина' if country == 1 else 'Россия')


class ManagerUserTypes(object):
    @classmethod
    def get_user(cls, user_id):
        try:
            male = Male.objects.get(user_id=user_id)
        except Male.DoesNotExist:
            male = None

        return male

    @classmethod
    def create(cls, male, user_id):
        user = Male.objects.create(name='Мужской' if male == 1 else 'Женский', user_id=user_id)
        user.save()

    @classmethod
    def update(cls, user_id, male):
        user = Male.objects.filter(user_id=user_id).update(name='Мужской' if male == 1 else 'Женский')


class ClothesManager(object):
    @classmethod
    def get_clothes_all(cls):
        clothes = Clothes.objects.all()

        return clothes if clothes else None


class BasketManager(object):
    @classmethod
    def add(cls, user_id, product_id):
        basket = Basket.objects.create(user_id=user_id, product_id=product_id)
        basket.save()

    @classmethod
    def get(cls, product_id):
        product = Basket.objects.filter(product_id=product_id)

        return product if product else None

    @classmethod
    def del_product(cls, product_id):
        try:
            product = Basket.objects.filter(product_id=product_id)
            product.delete()
        except Basket.DoesNotExist:
            product = None

        return product
