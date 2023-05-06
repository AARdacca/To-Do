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
from access import views
from access.views import *

app_name = "access"

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('register/', views.register_view, name="register"),
    path('login/', views.login_view, name="login"),
    path('home/', views.home_view, name="home"),
    path('complete_archive_all/', views.complete_archive_all, name="complete_archive_all"),
    path('logout/', views.logout_view, name="logout"),
    path('create_team/', views.create_team, name="create_team"),
    path('team/<int:team_id>/', views.team_detail, name="team_detail"),
    path('team/add_member/', views.add_team_member, name="add_team_member"),
    path('friends/<int:friends_id>/', views.friends_detail, name="friends_detail"),
    path('friends/add_member/', views.add_friends_member, name="add_friends_member"),
]
