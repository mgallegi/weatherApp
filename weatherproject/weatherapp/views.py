from msilib.schema import AppId
from django.shortcuts import render
import requests
import datetime
import json
from urllib.request import urlopen


# https://www.youtube.com/watch?v=HCAWDqlfXUc
# Create your views here.


def index(request):

    if 'city' in request.POST:
        city = request.POST['city']

    else:
        url = 'http://ipinfo.io/json'
        response = urlopen(url)
        data = json.load(response)
        city = data['city']

    appId = 'da5354142d071b67865a1398ee317a39'
    appUrl = 'https://api.openweathermap.org/data/2.5/weather'

    appParams = {'q': city, 'appid': appId, 'units': 'metric'}

    r = requests.get(url=appUrl, params=appParams)
    res = r.json()
    print(res)
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temperature = res['main']['temp']
    humedad = res['main']['humidity']
    sensacion = res['main']['feels_like']
    tempMax = res['main']['temp_max']
    tempMin = res['main']['temp_min']

    day = datetime.date.today()

    return render(request, 'weatherapp/index.html', {'description': description, 'icon': icon, 'temperature': temperature, 'day': day, 'city': city, 'humedad': humedad, 'sensacion': sensacion, 'tempMax': tempMax, 'tempMin': tempMin})
