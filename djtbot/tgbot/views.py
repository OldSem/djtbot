from django.http import HttpResponse
from pprint import pprint
from django.views.decorators.csrf import csrf_exempt
import json

from .logger import logger_djtbot
from .bot_view import view, bot_error
from .webhooks import Bot
from .menu import Views as v
from django.conf import settings


set_bot = Bot()
set_bot.delete_webhook()
set_bot.set_webhook()


def start(request):
    return HttpResponse('I am Robot!')


@csrf_exempt
def bot_view(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        if settings.DEBUG:
            pprint(data)

        code = v.error_code(data)

        if code and code != 200:
            logger_djtbot.error('Telegram server return false: {0}'.format(code))
            bot_error(data)
            return HttpResponse('Error', status=400)
        else:
            view(data)
            return HttpResponse('Ok', status=200)
