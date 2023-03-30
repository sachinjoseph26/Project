from django.shortcuts import render
from .models import Rolemaster


# Create your views here.

def index(request):
    return render(request, 'index.html')
