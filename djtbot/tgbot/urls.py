from django.urls import path
from .views import bot_view, start
from django.conf import settings
from django.urls import re_path

urlpatterns = [
    re_path(r'^$', start, name='start'),
    # path('{}'.format(settings.TOKEN), bot_view, name='bot_view'),
]