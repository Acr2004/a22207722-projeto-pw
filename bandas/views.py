from django.shortcuts import render, redirect
from .models import Banda, Album, Musica
from .forms import BandaForm, AlbumForm, MusicaForm
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

def list_view(request):
    bandas = Banda.objects.all()
    context = { 'bandas': bandas }
    return render(request, "bandas/list.html", context)

def band_view(request, band_id):
    banda = Banda.objects.get(id = band_id)
    albuns = Album.objects.filter(banda = banda)
    context = { 'banda': banda, 'albuns': albuns }
    return render(request, 'bandas/banda.html', context)

def album_view(request, album_id):
    album = Album.objects.get(id = album_id)
    musicas = Musica.objects.filter(album = album)
    context = { 'album': album, 'musicas': musicas }
    return render(request, 'bandas/album.html', context)

def music_view(request, music_id):
    musica = Musica.objects.get(id = music_id)
    context = { 'musica': musica }
    return render(request, 'bandas/musica.html', context)

@group_required('Admin', 'Editor de Bandas')
def nova_banda_view(request):
    form = BandaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('bandas:lista_bandas')

    context = {'form': form}
    return render(request, 'bandas/nova_banda.html', context)

@group_required('Admin', 'Editor de Bandas')
def edita_banda_view(request, banda_id):
    banda = Banda.objects.get(id = banda_id)

    if request.POST:
        form = BandaForm(request.POST or None, request.FILES, instance = banda)
        if form.is_valid():
            form.save()
            return redirect('bandas:detalhes_banda', banda_id)
    else:
        form = BandaForm(instance = banda)

    context = {'form': form, 'banda':banda}
    return render(request, 'bandas/edita_banda.html', context)

@group_required('Admin', 'Editor de Bandas')
def apaga_banda_view(request, banda_id):
    banda = Banda.objects.get(id = banda_id)
    banda.delete()
    return redirect('bandas:lista_bandas')

@group_required('Admin', 'Editor de Bandas')
def novo_album_view(request, banda_id):
    banda = Banda.objects.get(id = banda_id)

    form = AlbumForm(request.POST or None, request.FILES)
    if form.is_valid():
        album = form.save(commit = False)
        album.banda = banda
        album.save()
        return redirect('bandas:detalhes_banda', banda_id)

    context = {'form': form}
    return render(request, 'bandas/novo_album.html', context)

@group_required('Admin', 'Editor de Bandas')
def edita_album_view(request, album_id):
    album = Album.objects.get(id = album_id)

    if request.POST:
        form = AlbumForm(request.POST or None, request.FILES, instance = album)
        if form.is_valid():
            form.save()
            return redirect('bandas:detalhes_album', album_id)
    else:
        form = AlbumForm(instance = album)

    context = {'form': form, 'album':album}
    return render(request, 'bandas/edita_album.html', context)

@group_required('Admin', 'Editor de Bandas')
def apaga_album_view(request, album_id):
    album = Album.objects.get(id = album_id)
    banda = Banda.objects.get(album = album)
    album.delete()
    return redirect('bandas:detalhes_banda', banda.id)

@group_required('Admin', 'Editor de Bandas')
def nova_musica_view(request, album_id):
    album = Album.objects.get(id = album_id)

    form = MusicaForm(request.POST or None, request.FILES)
    if form.is_valid():
        musica = form.save(commit = False)
        musica.album = album
        musica.save()
        return redirect('bandas:detalhes_album', album_id)

    context = {'form': form}
    return render(request, 'bandas/nova_musica.html', context)

@group_required('Admin', 'Editor de Bandas')
def edita_musica_view(request, musica_id):
    musica = Musica.objects.get(id = musica_id)

    if request.POST:
        form = MusicaForm(request.POST or None, request.FILES, instance = musica)
        if form.is_valid():
            form.save()
            return redirect('bandas:detalhes_musica', musica_id)
    else:
        form = MusicaForm(instance = musica)

    context = {'form': form, 'musica':musica}
    return render(request, 'bandas/edita_musica.html', context)

@group_required('Admin', 'Editor de Bandas')
def apaga_musica_view(request, musica_id):
    musica = Musica.objects.get(id = musica_id)
    album = Album.objects.get(musica = musica)
    musica.delete()
    return redirect('bandas:detalhes_album', album.id)



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
        return redirect('bandas:login')

    return render(request, 'bandas/signin.html')

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('bandas:lista_bandas')
        else:
            render(request, 'bandas/login.html', {
                'mensagem':'Credenciais Inválidas'
            })

    return render(request, 'bandas/login.html')

def logout_view(request):
    logout(request)
    return redirect('bandas:lista_bandas')