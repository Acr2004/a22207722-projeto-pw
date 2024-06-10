from django.shortcuts import render
from .models import Localizacao, Banda, Festival
from datetime import datetime

def festival_list_view(request):
    festivais = Festival.objects.all()
    localizacoes = Localizacao.objects.all()
    context = {'festivais': festivais, 'localizacoes': localizacoes}
    return render(request, 'festivais/festivalList.html', context)

def festival_view(request, festival_id):
    festival = Festival.objects.get(id = festival_id)
    localizacao = Localizacao.objects.get(festival = festival)
    bandas = Banda.objects.filter(festival = festival)
    context = {'festival': festival, 'localizacao': localizacao, 'bandas': bandas,}
    return render(request, 'festivais/festival.html', context)