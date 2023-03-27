from django.shortcuts import render
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from.models import*

project_sample_list = [
    # For short_description String Slicing is needed
    # b = "Hello, World!"
    # print(b[0:9])
    {
        'id': '1',
        'title': 'Bazar Today',
        'short_description': 'Needed groceries...',
        'description': 'Needed groceries from foodstore online'
    },
    {   
        'id': '2',
        'title': 'Project update',
        'short_description': 'fix some CSS...',
        'description': 'fix some CSS issues according to some documentation',
    },
    {   
        'id': '3',
        'title': 'Setting up PC',
        'short_description': 'install VS Code...',
        'description': 'install VS Code and Python',
    },
    {   
        'id': '4',
        'title': 'Setting up TV',
        'short_description': 'Manual Search and...',
        'description': 'Manual Search and Auto Search needs to be conducted',
    },
]

def todo(request):
    dict = {'todo': project_sample_list}
    return render(request,'todo/todo.html', context=dict)

def todo_view(request, pk):
    todo_obj = None
    for i in project_sample_list:
        if i['id'] == pk:
            todo_obj=i
    # Object found
    dict = {'todo': todo_obj}
    return render(request,'todo/todo_view.html', context=dict)

# def todo_search(request, search_key):
#     todo_obj = []
#     for i in project_sample_list:
#         if i['id'] == search_key:
#             todo_obj.append(i)
#     # Object found
#     dict = {'todo': todo_obj}
#     return render(request,'todo/todo_view.html', context=dict)