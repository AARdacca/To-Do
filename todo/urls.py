"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo import views


from todo.views import *

app_name = "tasks"

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('create/', views.create_task, name='create'),
    path('<int:task_id>/', views.detail, name='detail'),
    path('edit/', views.edit, name='edit'),
    path('delete/<int:task_id>/', views.delete, name='delete'),
    path('complete_archive/<int:task_id>/', views.complete_archive, name='complete_archive'),
    path('not_complete_archive/<int:task_id>/', views.not_complete_archive, name='not_complete_archive'),
    path('comment/<int:task_id>', views.post_comment, name='comment'),
]
