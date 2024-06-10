from django.shortcuts import render, redirect
from django.contrib.auth import models, authenticate, login, logout
import requests
from datetime import datetime

def index_view(request):
    url = 'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json'
    resp = requests.get(url)
    resp.raise_for_status()
    data = resp.json()

    if not isinstance(data, dict) or 'data' not in data:
        raise ValueError("Error")

    today = data['data'][0]
    weather = today['idWeatherType']

    time = datetime.now().hour
    if 8 <= time < 18:
        icon = f'w_ic_d_{weather:02}anim.svg'
    else:
        icon = f'w_ic_n_{weather:02}anim.svg'

    iconUrl = f'/static/meteo/icons/{icon}'

    context = {
        'iconUrl': iconUrl,
    }

    return render(request, "portfolio/index.html", context)


def about_me_view(request):
    return render(request, "portfolio/about_me.html")

def tech_tools_view(request):
    return render(request, "portfolio/tech_tools.html")

def signup_view(request):
    if request.method == "POST":
        models.User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['nome'],
            last_name=request.POST['apelido'],
            password=request.POST['password']
        )
        return redirect('portfolio:login')

    return render(request, 'portfolio/signup.html')


def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('portfolio:index')
        else:
            render(request, 'portfolio/login.html', {
                'mensagem':'Credenciais Inválidas'
            })

    return render(request, 'portfolio/login.html')

def logout_view(request):
    logout(request)
    return redirect('portfolio:login')