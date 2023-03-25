from django.shortcuts import render
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from.models import*

def todo(request):
    return render(request,'todo/todo.html') 