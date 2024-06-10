from django.contrib import admin
from django.urls import path
from . import views

app_name = "artigos"

urlpatterns = [
    path('autores/', views.autor_list_view, name='lista_autores'),
    path('artigos/', views.artigo_list_view, name='lista_artigos'),
    path('autor/<int:autor_id>', views.autor_view, name='detalhes_autor'),
    path('artigo/<int:artigo_id>', views.artigo_view, name='detalhes_artigo'),

    path('autor/novo', views.novo_autor_view, name="novo_autor"),
    path('autor/<int:autor_id>/edita', views.edita_autor_view, name="edita_autor"),
    path('autor/<int:autor_id>/apaga', views.apaga_autor_view,name="apaga_autor"),

    path('artigo/novo', views.novo_artigo_view, name="novo_artigo"),
    path('artigo/<int:artigo_id>/edita', views.edita_artigo_view, name="edita_artigo"),
    path('artigo/<int:artigo_id>/apaga', views.apaga_artigo_view,name="apaga_artigo"),

    path('comentario/novo', views.novo_comentario_view, name="novo_comentario"),
    path('comentario/<int:comentario_id>/edita', views.edita_comentario_view,name="edita_comentario"),
    path('comentario/<int:comentario_id>/apaga', views.apaga_comentario_view,name="apaga_comentario"),

    path('signin/', views.signin_view, name="signin"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]