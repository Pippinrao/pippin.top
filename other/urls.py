from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'note'

urlpatterns = [
    path('', views.Gift.as_view(), name='love_gift'),
]
