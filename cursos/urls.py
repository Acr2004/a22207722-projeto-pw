from django.contrib import admin
from django.urls import path
from . import views

app_name = "cursos"

urlpatterns = [
    path('cursos/', views.curso_list_view, name='lista_cursos'),
    path('curso/<int:curso_id>', views.curso_view, name='detalhes_curso'),
    path('curso/<int:curso_id>/<int:disciplina_id>', views.disciplina_view, name='detalhes_disciplina'),
    path('curso/<int:curso_id>/<int:disciplina_id>/<int:projeto_id>', views.projeto_view, name='detalhes_projeto'),

    path('curso/novo', views.novo_curso_view, name="novo_curso"),
    path('curso/<int:curso_id>/edita', views.edita_curso_view, name="edita_curso"),
    path('curso/<int:curso_id>/apaga', views.apaga_curso_view, name="apaga_curso"),

    path('disciplina/<int:curso_id>/nova_disciplina', views.nova_disciplina_view, name="nova_disciplina"),
    path('disciplina/<int:disciplina_id>/edita', views.edita_disciplina_view, name="edita_disciplina"),
    path('disciplina/<int:disciplina_id>/apaga', views.apaga_disciplina_view,name="apaga_disciplina"),

    path('projeto/<int:disciplina_id>/novo_projeto', views.novo_projeto_view, name="novo_projeto"),
    path('projeto/<int:projeto_id>/edita', views.edita_projeto_view, name="edita_projeto"),
    path('projeto/<int:projeto_id>/apaga', views.apaga_projeto_view,name="apaga_projeto"),

    path('linguagem/<int:disciplina_id>/nova_linguagem', views.nova_linguagem_view, name="nova_linguagem"),
    path('linguagem/<int:linguagem_id>/edita', views.edita_linguagem_view, name="edita_linguagem"),
    path('linguagem/<int:linguagem_id>/apaga', views.apaga_linguagem_view,name="apaga_linguagem"),

    path('docente/<int:disciplina_id>/novo_docente', views.novo_docente_view, name="novo_docente"),
    path('docente/<int:docente_id>/edita', views.edita_docente_view, name="edita_docente"),
    path('docente/<int:docente_id>/apaga', views.apaga_docente_view,name="apaga_docente"),

    path('signin/', views.signin_view, name="signin"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]