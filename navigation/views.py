from django.shortcuts import render, redirect 

# Create your views here.

def index(request):
    return redirect('navigation:home')

def about(request):
    return render(request,'about/about.html', {})

def home(request):
    return render(request,'home/home.html', {})
