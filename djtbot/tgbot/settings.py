from telebot import TeleBot, logger
from django.conf import settings
import logging


bot = TeleBot(settings.TOKEN)
bot.set_webhook(settings.DOMAIN)

logger.setLevel(logging.DEBUG)