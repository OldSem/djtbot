from django.urls import path
from .views import bot_view, RenderStartView, StartView, CSVViews, parse
from django.conf import settings
from django.urls import re_path

urlpatterns = [
    re_path(r'^$', RenderStartView.as_view(), name='start_template'),
    re_path(r'^api/$', StartView.as_view(), name='start_api'),
    re_path(r'^csv/$', CSVViews.as_view(), name='csv_files'),
    re_path(r'^parse/answear/$', parse, name='parse'),
    path('{}'.format(settings.TOKEN), bot_view, name='bot_view'),
]