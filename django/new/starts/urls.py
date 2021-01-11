from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('dinner/', views.dinner),
    path('throw/', views.throw, name="throw"),
    path('catch/', views.catch, name="catch"),
]
