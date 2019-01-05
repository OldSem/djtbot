from django.http import HttpResponse
from pprint import pprint
from django.views.decorators.csrf import csrf_exempt
import json

from .exeptions import BotError
from .manager import SystemPhotoManager
from .logger import logger_djtbot
from .bot_view import view, bot_error
from .webhooks import Bot
from .menu import Views as v
from django.conf import settings
from django.http import Http404
from django.shortcuts import render


set_bot = Bot()
set_bot.delete_webhook()
set_bot.set_webhook()


def start(request):
    img = SystemPhotoManager.get_product_img()
    return render(request, "tgbot/index.html", {'photo': f"{settings.DOMAIN}{img.img.url}"})


@csrf_exempt
def bot_view(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        if settings.DEBUG:
            pprint(data)

        view(data)
        return HttpResponse('Ok', status=200)
