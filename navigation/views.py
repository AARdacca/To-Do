import random
from django.shortcuts import render

# Create your views here.

def home(request):
    user_list=["User","UserTemp"]
    user = random.choice(user_list)
    dict = {'user': user}
    return render(request,'home/home.html', context=dict)

def about(request):
    return render(request,'about/about.html')
