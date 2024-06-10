from django.contrib import admin
from django.urls import path
from . import views

app_name = "festivais"

urlpatterns = [
    path('', views.festival_list_view, name='lista_festivais'),
    path('festival/<int:festival_id>', views.festival_view, name='detalhes_festival'),
]