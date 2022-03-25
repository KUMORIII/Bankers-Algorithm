from django.shortcuts import render
from information.models import *

# Create your views here.

def start(request):
    return render(request, 'mainpage/start.html')