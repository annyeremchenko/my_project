from django.conf.urls import url, include
from django.contrib import admin
import user
from . import views

urlpatterns = [
    url(r'login/', views.Login.as_view(), name='log in'),        # вхід
    url(r'logout/', views.Logout.as_view(), name='sign out'),     # вихід
    url(r'signup/', views.Signup.as_view(), name='sign up'),        # реєстрація
    url(r'home/', views.Home.as_view(), name='home'),               # домашня сторінка
    url(r'(\d+)/', views.UserInformation.as_view(), name='another user home'),  # домашня сторінка іншого користувача
    url(r'$', views.Index.as_view(), name='index')  # початкова сторінка
]
