import requests
from django.shortcuts import render

def get_weather(request):
    weather_data = None
    error = None

    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = '1b5cbaa3a79bde91ab31f9ef6050f0c0'  
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={23.777176}&lon={90.399452}&appid={'1b5cbaa3a79bde91ab31f9ef6050f0c0'}"

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': city,
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'description': data['weather'][0]['description'],
            }
        else:
            error = "শহরের নাম সঠিক নয় বা API সমস্যা হয়েছে।"

    return render(request, 'weather/weather.html', {'weather': weather_data, 'error': error})

