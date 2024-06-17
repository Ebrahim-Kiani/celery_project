from django.http import HttpResponse
from django.shortcuts import render
from .tasks import *
# Create your views here.

def handl_user_data(request):
    task = send_sms_to_user.apply_async()

    return HttpResponse("sync view")

def handl_user_data2(request):
    task = send_sms_to_user.apply_async()
    return HttpResponse("async view")