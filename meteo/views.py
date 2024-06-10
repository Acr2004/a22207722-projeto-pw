from django.shortcuts import render
from datetime import datetime
import requests

def api_view(request):
    return render(request, 'meteo/api.html')

def meteo_view(request):
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
        'city': 'Lisboa',
        'tempMin': today['tMin'],
        'tempMax': today['tMax'],
        'iconUrl': iconUrl,
        'probabilityPrec': today['precipitaProb'],
        'windDir': today['predWindDir'],
        'windSpeed': today['classWindSpeed'],
        'long': today['longitude'],
        'lat': today['latitude'],
        'day': today['forecastDate'],
    }

    return render(request, 'meteo/index.html', context)

def nextdays_view(request, city_id="1110600"):
    url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{city_id}.json'
    resp = requests.get(url)
    resp.raise_for_status()
    data = resp.json()

    if not isinstance(data, dict) or 'data' not in data:
        raise ValueError("Error")

    nextDays = []

    citiesUrl = 'https://api.ipma.pt/open-data/distrits-islands.json'
    resp = requests.get(citiesUrl)
    resp.raise_for_status()
    citiesData = resp.json()

    city = 'Erro'

    for cityy in citiesData['data']:
        if cityy['globalIdLocal'] == city_id:
            city = cityy['local']

    for day in data['data'][:5]:
        weather = day['idWeatherType']

        time = datetime.now().hour
        if 8 <= time < 18:
            icon = f'w_ic_d_{weather:02}anim.svg'
        else:
            icon = f'w_ic_n_{weather:02}anim.svg'

        iconUrl = f'/static/meteo/icons/{icon}'

        nextDays.append(
            {
                'tempMin': day['tMin'],
                'tempMax': day['tMax'],
                'iconUrl': iconUrl,
                'probabilityPrec': day['precipitaProb'],
                'windDir': day['predWindDir'],
                'windSpeed': day['classWindSpeed'],
                'long': day['longitude'],
                'lat': day['latitude'],
                'day': day['forecastDate'],
            }
        )

    context = {
        'city': city,
        'cities': citiesData['data'],
        'nextDays': nextDays,
    }

    return render(request, 'meteo/nextdays.html', context)