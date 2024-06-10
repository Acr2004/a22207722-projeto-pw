from django.shortcuts import render, redirect
from .models import Autor, Artigo, Comentario
from .forms import AutorForm, ArtigoForm, ComentarioForm
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

def autor_list_view(request):
    autores = Autor.objects.all()
    context = { 'autores': autores }
    return render(request, "artigos/autorList.html", context)

def artigo_list_view(request):
    artigos = Artigo.objects.all()
    context = { 'artigos': artigos }
    return render(request, 'artigos/artigoList.html', context)

def autor_view(request, autor_id):
    autor = Autor.objects.get(id = autor_id)
    artigos = Artigo.objects.filter(autor = autor)
    context = { 'autor': autor, 'artigos': artigos }
    return render(request, 'artigos/autor.html', context)

def artigo_view(request, artigo_id):
    artigo = Artigo.objects.get(id = artigo_id)
    comentarios = Comentario.objects.filter(artigo = artigo)
    context = { 'artigo': artigo, 'comentarios': comentarios }
    return render(request, 'artigos/artigo.html', context)

@group_required('Admin', 'Editor de Artigos')
def novo_autor_view(request):
    form = AutorForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('artigos:lista_autores')

    context = {'form': form}
    return render(request, 'artigos/novo_autor.html', context)

@group_required('Admin', 'Editor de Artigos')
def edita_autor_view(request, autor_id):
    autor = Autor.objects.get(id = autor_id)

    if request.POST:
        form = AutorForm(request.POST or None, request.FILES, instance = autor)
        if form.is_valid():
            form.save()
            return redirect('artigos:detalhes_autor', autor_id)
    else:
        form = AutorForm(instance = autor)

    context = {'form': form, 'autor':autor}
    return render(request, 'artigos/edita_autor.html', context)

@group_required('Admin', 'Editor de Artigos')
def apaga_autor_view(request, autor_id):
    autor = Autor.objects.get(id = autor_id)
    autor.delete()
    return redirect('artigos:lista_autores')

@group_required('Admin', 'Editor de Artigos')
def novo_artigo_view(request):
    form = ArtigoForm(request.POST or None, request.FILES)
    if form.is_valid():
        artigo = form.save(commit = False)
        artigo.save()
        return redirect('artigos:detalhes_artigo', artigo.id)

    context = {'form': form}
    return render(request, 'artigos/novo_artigo.html', context)

@group_required('Admin', 'Editor de Artigos')
def edita_artigo_view(request, artigo_id):
    artigo = Artigo.objects.get(id = artigo_id)

    if request.POST:
        form = ArtigoForm(request.POST or None, request.FILES, instance = artigo)
        if form.is_valid():
            form.save()
            return redirect('artigos:detalhes_artigo', artigo_id)
    else:
        form = ArtigoForm(instance = artigo)

    context = {'form': form, 'artigo':artigo}
    return render(request, 'artigos/edita_artigo.html', context)

@group_required('Admin', 'Editor de Artigos')
def apaga_artigo_view(request, artigo_id):
    artigo = Artigo.objects.get(id = artigo_id)
    artigo.delete()
    return redirect('artigos:lista_artigos')

@group_required('Admin', 'Editor de Artigos')
def novo_comentario_view(request):
    form = ComentarioForm(request.POST or None, request.FILES)
    if form.is_valid():
        comentario = form.save(commit = False)
        comentario.save()
        artigo = Artigo.objects.get(comentario = comentario)
        return redirect('artigos:detalhes_artigo', artigo.id)

    context = {'form': form}
    return render(request, 'artigos/novo_comentario.html', context)

@group_required('Admin', 'Editor de Artigos')
def edita_comentario_view(request, comentario_id):
    comentario = Comentario.objects.get(id = comentario_id)
    artigo = Artigo.objects.get(comentario = comentario)

    if request.POST:
        form = ComentarioForm(request.POST or None, request.FILES, instance = comentario)
        if form.is_valid():
            form.save()
            return redirect('artigos:detalhes_artigo', artigo.id)
    else:
        form = ComentarioForm(instance = comentario)

    context = {'form': form, 'comentario':comentario}
    return render(request, 'artigos/edita_comentario.html', context)

@group_required('Admin', 'Editor de Artigos')
def apaga_comentario_view(request, comentario_id):
    comentario = Comentario.objects.get(id = comentario_id)
    artigo = Artigo.objects.get(comentario = comentario)
    comentario.delete()
    return redirect('artigos:detalhes_artigo', artigo.id)



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
        return redirect('artigos:login')

    return render(request, 'artigos/signin.html')

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('artigos:lista_artigos')
        else:
            render(request, 'artigos/login.html', {
                'mensagem':'Credenciais Inválidas'
            })

    return render(request, 'artigos/login.html')

def logout_view(request):
    logout(request)
    return redirect('artigos:lista_artigos')