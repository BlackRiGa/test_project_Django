from django.http import HttpResponseNotFound
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def page_not_found(request, exception):
    return render(request, 'main/404.html')


def server_not_found(request, exception):
    return render(request, 'main/505.html')