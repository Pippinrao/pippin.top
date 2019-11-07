"""pippin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from . import views

app_name = 'note'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('create/', views.Create.as_view(), name='create'),
    path('detail/<int:id>/', views.Detail.as_view(), name='detail'),
    path('edit/<int:id>/', views.Edit.as_view(), name='edit'),
    path('delete/<int:id>/', views.Delete.as_view(), name='delete'),
    path('add-something/<int:id>/', views.Add_something.as_view(), name='add_something'),
    path('rm-something/<int:id>/', views.Rm_something.as_view(), name='rm_something'),
]
