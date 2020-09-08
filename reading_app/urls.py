from django.contrib import admin
from .views import read_view
from django.urls import path,include

urlpatterns = [
    
    path('',read_view,name="reading_img")
]
