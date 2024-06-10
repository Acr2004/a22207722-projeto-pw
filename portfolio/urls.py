from django.contrib import admin
from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.index_view, name='index'),
    path('about_me', views.about_me_view, name='about_me'),
    path('tech_tools', views.tech_tools_view, name='tech_tools'),

    path('signup', views.signup_view, name='signup'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
]