from django.urls import path
from .views import bot_view
from django.conf import settings


urlpatterns = [
    path('{}'.format(settings.TOKEN), bot_view, name='bot_view'),
]