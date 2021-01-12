from django.contrib import admin
from django.urls import path
from . import views

app_name = 'starts'
urlpatterns = [
    path('index/', views.index),
    path('dinner/', views.dinner),
    path('form/', views.form),
    path('throw/', views.throw, name="throw"),
    path('catch/', views.catch, name="catch"),
]
