from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('start/init/', views.init),
    path('start/mainpage/', views.back),
    path('start/mainpage/calculate/', views.calculate),
]
