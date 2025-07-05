from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def home(request):
    return HttpResponse("Users app ishlayapti!")


def my_portfolio(request):
    return render(request, 'index.html')
