"""diary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from home import views

urlpatterns = [
   
   path('', views.home, name='home'),
   path('search', views.homesearch, name='homesearch'),
   path('search-date', views.search_date, name='search-date'),
   path('s', views.s, name='s'),
   path('diary/<str:slug>', views.diaryseperate, name='diaryseperate'),
   path('delete/<str:slug>', views.delete, name='delete'),

   
    path('signup', views.handleauth, name='handleauth'),
    path('login', views.handlelogin, name='handlelogin'),
    path('logout', views.handlelogout, name='handlelogout'),

]
