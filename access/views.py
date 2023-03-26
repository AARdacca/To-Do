from django.shortcuts import render
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from.models import*

def login(request):
    return render(request,'access/login.html')

def logout(request):
    return render(request,'access/logout.html')

def signup(request):
    return render(request,'access/signup.html')