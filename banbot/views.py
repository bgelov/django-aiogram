from django.shortcuts import render
from asgiref.sync import async_to_sync
from .webhook import proceed_update
from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def telegram_webhook(request: HttpRequest):
    try:
        async_to_sync(proceed_update)(request)
    except Exception as e:
        print(e)
    return HttpResponse()