from django.conf.urls import url, include
from django.contrib import admin
import user
from . import views
urlpatterns = [
    url(r'map/', views.Map.as_view(), name='job location'),            # дорога до роботи
    url(r'all/', views.JobAll.as_view(), name='all jobs'),            # усі роботи
    url(r'$', views.JobSearch.as_view(), name='job search'),        # пошук роботи
]