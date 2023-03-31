from django.contrib import admin
from django.urls import path
from Toggle.views import index , toggle_led

urlpatterns = [
    path('',index,name='index'),
    path("toggle_led/",toggle_led,name= "toggle_led")
]