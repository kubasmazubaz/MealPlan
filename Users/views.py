from django.shortcuts import render
from django.http import HttpResponse
from .models import Login

# Create your views here.

def index(request):
    logins = Login.objects
    return render(request, 'Users/index.html',{'logins':logins})

def log_sign(request):
    return render(request, 'Users/log_sign.html')