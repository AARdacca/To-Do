from django.urls import path
from .views import *
from . import views

app_name = "depiction"

urlpatterns = [
    path('<int:pk>/edit_profile_page/',EditProfilePageView.as_view(),name='edit_profile_page'),
    path('<int:pk>/profile/',ShowProfilePageView.as_view(),name='show_profile_page'),
    path('password/',PasswordsChangeView.as_view(template_name='depiction/change-password.html'), name='password'),
    path('password_success/', views.password_success, name="password_success"),
]