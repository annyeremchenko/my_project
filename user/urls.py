from django.conf.urls import url, include
from django.contrib import admin
import user
from . import views
urlpatterns = [
    url(r'login/', views.Login.as_view(), name='log in'),        # вхід
    url(r'logout/', views.Logout.as_view(), name='sign out'),     # вихід
    url(r'signup/', views.Signup.as_view(), name='sign up'),        # реєстрація
    url(r'home/', views.Home.as_view(), name='home'),               # домашня сторінка
]