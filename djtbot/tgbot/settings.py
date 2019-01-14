from telebot import TeleBot, logger
from django.conf import settings
import logging
from .logger import logger_djtbot


bot = TeleBot(settings.TOKEN)
bot.set_webhook(url=settings.DOMAIN)

logger.setLevel(logging.DEBUG)
logger_djtbot.setLevel(logging.DEBUG)