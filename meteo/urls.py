from django.contrib import admin
from django.urls import path
from . import views

app_name = "meteo"

urlpatterns = [
    path('meteo/', views.meteo_view, name='meteo'),
    path('meteo/nextdays/', views.nextdays_view, name='nextdays'),
    path('meteo/api/', views.api_view, name='api'),
]