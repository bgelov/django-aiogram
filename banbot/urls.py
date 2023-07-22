from django.urls import path

from banbot.views import telegram_webhook

app_name = 'banbot'
urlpatterns = [
    path('', telegram_webhook, name='telegram_webhook'),
]