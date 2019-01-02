from django.http import HttpResponse
from pprint import pprint
from django.views.decorators.csrf import csrf_exempt
import json
from .bot_view import view
from .webhooks import Bot


set_bot = Bot()
set_bot.delete_webhook()
set_bot.set_webhook()


@csrf_exempt
def bot_view(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        pprint(data)
        # try:
        #     view(data)
        # except BotError as e:
        #     print(str(e))
        #     bot_error(data)
        # finally:
        #     return HttpResponse('Ok', status=200)
        if data:
            view(data)
            return HttpResponse('Ok', status=200)
