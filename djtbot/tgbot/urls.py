from django.urls import path
from .views import BotView, RenderStartView, StartView
from django.conf import settings
from django.urls import re_path

urlpatterns = [
    re_path(r'^$', RenderStartView.as_view(), name='start_template'),
    re_path(r'^api/$', StartView.as_view(), name='start_api'),
    path('{}'.format(settings.TOKEN), BotView.as_view(), name='bot_view'),
]