from django.shortcuts import render, redirect
from .models import Curso, Disciplina, Projeto, Linguagem, Docente
from .forms import CursoForm, DisciplinaForm, ProjetoForm, LinguagemForm, DocenteForm
from django.contrib.auth import models, logout, authenticate, login
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test

def group_required(*all_groups):
    def in_groups(user):
        if user.is_authenticated:
            if bool(user.groups.filter(name__in=all_groups)) | user.is_superuser:
                return True
        raise PermissionDenied
    return user_passes_test(in_groups)

def curso_list_view(request):
    cursos = Curso.objects.all()
    context = {'cursos': cursos}
    return render(request, 'cursos/cursoList.html', context)

def curso_view(request, curso_id):
    curso = Curso.objects.get(id = curso_id)
    disciplinas = Disciplina.objects.filter(curso = curso)
    projects = Projeto.objects.filter(disciplina__in = disciplinas)
    context = {'curso': curso, 'disciplinas': disciplinas, 'projects': projects}
    return render(request, 'cursos/curso.html', context)

def disciplina_view(request, curso_id, disciplina_id):
    curso = Curso.objects.get(id = curso_id)
    disciplina = Disciplina.objects.get(id = disciplina_id, curso = curso)

    try:
        project = Projeto.objects.get(disciplina = disciplina)
        linguagens = Linguagem.objects.filter(project = project)
    except Projeto.DoesNotExist:
        project = None
        linguagens = None

    docentes = Docente.objects.filter(disciplinas = disciplina)
    context = {'curso': curso, 'disciplina': disciplina, 'project': project, 'linguagens': linguagens, 'docentes': docentes}
    return render(request, 'cursos/disciplina.html', context)

def projeto_view(request, curso_id, disciplina_id):
    curso = Curso.objects.get(id = curso_id)
    disciplina = Disciplina.objects.get(id = disciplina_id, curso = curso)
    project = Projeto.objects.get(disciplina = disciplina)
    context = {'curso': curso, 'disciplina': disciplina, 'project': project}
    return render(request, 'cursos/projeto.html', context)

@group_required('Admin', 'Editor de Cursos')
def novo_curso_view(request):
    form = CursoForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('cursos:lista_cursos')

    context = {'form': form}
    return render(request, 'cursos/novo_curso.html', context)

@group_required('Admin', 'Editor de Cursos')
def edita_curso_view(request, curso_id):
    curso = Curso.objects.get(id = curso_id)

    if request.POST:
        form = CursoForm(request.POST or None, request.FILES, instance = curso)
        if form.is_valid():
            form.save()
            return redirect('cursos:detalhes_curso', curso_id)

    else:
        form = CursoForm(instance = curso)

    context = {'form': form,'curso': curso}
    return render(request, 'cursos/edita_curso.html', context)

@group_required('Admin', 'Editor de Cursos')
def apaga_curso_view(request, curso_id):
    curso = Curso.objects.get(id = curso_id)
    curso.delete()
    return redirect('cursos:lista_cursos')

@group_required('Admin', 'Editor de Cursos')
def nova_disciplina_view(request, curso_id):
    curso = Curso.objects.get(id = curso_id)

    if request.method == 'POST':
        form = DisciplinaForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cursos:detalhes_curso', curso_id)

    else:
        form = DisciplinaForm(initial={'curso': curso})

    context = {'form': form, 'curso': curso}
    return render(request, 'cursos/nova_disciplina.html', context)

@group_required('Admin', 'Editor de Cursos')
def edita_disciplina_view(request, curso_id, disciplina_id):
    curso = Curso.objects.get(id = curso_id)
    disciplina = Disciplina.objects.get(id = disciplina_id, curso = curso)

    if request.POST:
        form = DisciplinaForm(request.POST or None, request.FILES, instance = disciplina)
        if form.is_valid():
            form.save()
            return redirect('cursos:detalhes_disciplina', curso_id , disciplina_id)

    else:
        form = DisciplinaForm(instance = disciplina)

    context = {'form': form,'curso': curso,'disciplina': disciplina}
    return render(request, 'cursos/edita_disciplina.html', context)

@group_required('Admin', 'Editor de Cursos')
def apaga_disciplina_view(request, curso_id, disciplina_id):
    curso = Curso.objects.get(id = curso_id)
    disciplina = Disciplina.objects.get(id = disciplina_id, curso = curso)
    disciplina.delete()
    return redirect('cursos:detalhes_curso', curso_id)

@group_required('Admin', 'Editor de Cursos')
def novo_projeto_view(request, curso_id, disciplina_id):
    curso = Curso.objects.get(id = curso_id)
    disciplina = Disciplina.objects.get(id = disciplina_id, curso=curso)

    if request.method == 'POST':
        form = ProjetoForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cursos:detalhes_disciplina', curso_id, disciplina_id)

    else:
        form = ProjetoForm(initial={'curso': curso, 'disciplina':disciplina})

    context = {'form': form,'curso': curso}
    return render(request, 'curso/novo_projeto.html', context)

@group_required('Admin', 'Editor de Cursos')
def edita_projeto_view(request, curso_id, disciplina_id):
    curso = Curso.objects.get(id = curso_id)
    disciplina = Disciplina.objects.get(nome = disciplina_id, curso=curso)
    projeto = Projeto.objects.get(disciplina = disciplina)

    if request.POST:
        form = ProjetoForm(request.POST or None, request.FILES, instance = projeto)
        if form.is_valid():
            form.save()
            return redirect('cursos:detalhes_projeto', curso_id, disciplina_id)

    else:
        form = ProjetoForm(instance = projeto)

    context = {'form': form, 'curso': curso, 'disciplina': disciplina, 'projeto':projeto}
    return render(request, 'cursos/editar_projeto.html', context)

@group_required('Admin', 'Editor de Cursos')
def apaga_projeto_view(request, curso_id, disciplina_id):
    curso = Curso.objects.get(id = curso_id)
    disciplina = Disciplina.objects.get(id = disciplina_id, curso=curso)
    projeto = Projeto.objects.get(disciplina = disciplina)
    projeto.delete()
    return redirect('cursos:detalhes_disciplina', curso_id, disciplina_id)

@group_required('Admin', 'Editor de Cursos')
def nova_linguagem_view(request, curso_id, disciplina_id):
    curso = Curso.objects.get(id = curso_id)
    disciplina = Disciplina.objects.get(id = disciplina_id, curso = curso)
    projetos = Projeto.objects.get(disciplina = disciplina)

    if request.method == 'POST':
        form = LinguagemForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('curso:projeto_detail',curso.nome, disciplina.nome)

    else:
        form = LinguagemForm(initial={'projetos':projetos})

    context = {'form': form, 'curso': curso, 'disciplina':disciplina}
    return render(request, 'cursos/nova_linguagem.html', context)

@group_required('Admin', 'Editor de Cursos')
def edita_linguagem_view(request, curso_id, disciplina_id, linguagem_id):
    curso = Curso.objects.get(id = curso_id)
    disciplina = Disciplina.objects.get(id = disciplina_id, curso = curso)
    projeto = Projeto.objects.get(disciplina = disciplina)
    linguagem = Linguagem.objects.get(id = linguagem_id)

    if request.POST:
        form = LinguagemForm(request.POST or None, request.FILES, instance = linguagem)
        if form.is_valid():
            form.save()
            return redirect('curso:detalhes_projeto', curso_id, disciplina_id)

    else:
        form = LinguagemForm(instance = linguagem)

    context = {'form': form,'curso': curso,'disciplina': disciplina,'projeto':projeto,'linguagem':linguagem}
    return render(request, 'curso/editar_linguagemProgramacao.html', context)

@group_required('Admin', 'Editor de Cursos')
def apaga_linguagem_view(request, curso_id, disciplina_id, linguagem_id):
    curso = Curso.objects.get(id = curso_id)
    disciplina = Disciplina.objects.get(id = disciplina_id, curso = curso)
    linguagem = Linguagem.objects.get(id = linguagem_id)
    linguagem.delete()
    return redirect('curso:detalhes_projeto', curso_id, disciplina_id)

@group_required('Admin', 'Editor de Cursos')
def novo_docente_view(request, curso_id, disciplina_id):
    curso = Curso.objects.get(id = curso_id)
    disciplina = Disciplina.objects.get(id = disciplina_id, curso = curso)

    if request.method == 'POST':
        form = DocenteForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cursos:detalhes_disciplina', curso_id, disciplina_id)

    else:
        form = DocenteForm(initial={'disciplinas':disciplina})

    context = {'form': form, 'curso': curso, 'disciplinas':disciplina}
    return render(request, 'cursos/novo_docente.html', context)

@group_required('Admin', 'Editor de Cursos')
def edita_docente_view(request, curso_id, disciplina_id, docente_id):
    curso = Curso.objects.get(id = curso_id)
    disciplina = Disciplina.objects.get(id = disciplina_id, curso = curso)
    docente = Docente.objects.get(id = docente_id)

    if request.POST:
        form = DocenteForm(request.POST or None, request.FILES, instance=docente)
        if form.is_valid():
            form.save()
            return redirect('curso:detalhes_disciplina', curso_id, disciplina_id)

    else:
        form = DocenteForm(instance = docente)

    context = {'form': form, 'curso': curso, 'disciplina': disciplina, 'docente':docente}
    return render(request, 'cursos/editar_docente.html', context)

@group_required('Admin', 'Editor de Cursos')
def apaga_docente_view(request, curso_id, disciplina_id, docente_id):
    curso = Curso.objects.get(id = curso_id)
    disciplina = Disciplina.objects.get(id = disciplina_id, curso = curso)
    docente = Docente.objects.get(id = docente_id)
    docente.delete()
    return redirect('curso:detalhes_disciplina', curso_id, disciplina_id)



# Login Auth

def signin_view(request):
    if request.method == "POST":
        models.User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['nome'],
            last_name=request.POST['apelido'],
            password=request.POST['password']
        )
        return redirect('cursos:login')

    return render(request, 'cursos/signin.html')

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('cursos:lista_cursos')
        else:
            render(request, 'cursos/login.html', {
                'mensagem':'Credenciais Inválidas'
            })

    return render(request, 'cursos/login.html')

def logout_view(request):
    logout(request)
    return redirect('cursos:lista_cursos')