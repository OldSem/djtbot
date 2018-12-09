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
            user = Country.objects.get(user=user_id)
        except User.DoesNotExist:
            user = None

        return user

    @classmethod
    def create(cls, country, user_id):
        user = Country.objects.create(name=country(country), user=user_id)
        user.save()

    @classmethod
    def update(cls, user_id, country):
        user = Country.objects.filter(user=user_id).update(name=country(country))
        user.save()

    @staticmethod
    def country(country):
        if country == 1:
            country = 'Украина'
        else:
            country = 'Россия'

        return country
