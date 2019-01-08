from pprint import pprint
import json
from .manager import SystemPhotoManager
from .bot_view import view
from .webhooks import Bot
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.generic import TemplateView


set_bot = Bot()
set_bot.delete_webhook()
set_bot.set_webhook()


class RenderStartView(TemplateView):
    template_name = 'tgbot/index.html'


class StartView(APIView):
    def get(self, request):
        img = SystemPhotoManager.get_product_img()
        return Response({'photo': f"{settings.DOMAIN}{img.img_url}"}, status.HTTP_200_OK)


class BotView(APIView):
    def post(self, request):
        if request.method == 'POST':
            data = json.loads(request.body.decode('utf-8'))

            if settings.DEBUG:
                pprint(data)

            view(data)
            return Response('Ok', status=status.HTTP_200_OK)
