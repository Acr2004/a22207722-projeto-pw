from django.contrib import admin
from django.urls import path
from . import views

app_name = "bandas"

urlpatterns = [
    path('lista/', views.list_view, name='lista_bandas'),
    path('banda/<int:band_id>', views.band_view, name='detalhes_banda'),
    path('album/<int:album_id>', views.album_view, name='detalhes_album'),
    path('musica/<int:music_id>', views.music_view, name='detalhes_musica'),

    path('banda/nova', views.nova_banda_view, name="nova_banda"),
    path('banda/<int:banda_id>/edita', views.edita_banda_view, name="edita_banda"),
    path('banda/<int:banda_id>/apaga', views.apaga_banda_view,name="apaga_banda"),

    path('banda/<int:banda_id>/novo_album', views.novo_album_view, name="novo_album"),
    path('album/<int:album_id>/edita', views.edita_album_view, name="edita_album"),
    path('album/<int:album_id>/apaga', views.apaga_album_view,name="apaga_album"),

    path('album/<int:album_id>/nova_musica', views.nova_musica_view, name="nova_musica"),
    path('musica/<int:musica_id>/edita', views.edita_musica_view, name="edita_musica"),
    path('musica/<int:musica_id>/apaga', views.apaga_musica_view,name="apaga_musica"),

    path('signin/', views.signin_view, name="signin"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]