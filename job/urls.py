from django.conf.urls import url, include
from django.contrib import admin
import user
from . import views
urlpatterns = [
    url(r'', views.JobSearch.as_view(), name='log in'),        # пошук роботи

]