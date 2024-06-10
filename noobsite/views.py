from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index_view1(request):
    return HttpResponse("Olá n00b, esta é a página web mais básica do mundo!")

def index_view2(request):
    return HttpResponse("Hello Football!")

def index_view3(request):
    return HttpResponse("Hello Handball!")

def index_view4(request):
    return HttpResponse("Hello Basketball!")