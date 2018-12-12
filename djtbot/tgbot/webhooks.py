from telebot import TeleBot, logger
from django.conf import settings
import requests


class Bot(object):
    def __init__(self):
        self._setting = settings
        self._bot = TeleBot(self._setting.TOKEN)
        self._logger = logger
        self._request = requests

    def delete_webhook(self):
        self._bot.delete_webhook()

    def _get_url(self, method):
        return "{}/bot{}/{}".format(self._setting.TELEGRAM_URL, self._setting.TOKEN, method)

    def set_webhook(self):
        self._request.get(self._get_url("setWebhook"),
                         data={"url": f"{self._setting.DOMAIN}/{self._setting.TOKEN}"})
        self._request.get(self._get_url("getWebhookInfo"))