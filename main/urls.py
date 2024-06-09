from django.contrib import admin
from django.urls import path
from  main.views import *
urlpatterns = [
    path('', home),
    path('home', home),
    path('places',show_places , name="show_places")
]
