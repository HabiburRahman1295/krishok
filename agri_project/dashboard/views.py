from django.shortcuts import render
from krishok_profile.models import Krishok
from crop_management.models import Crop
from fertilizer_management.models import Fertilizer
from marketing.models import Product
from govt_assistance.models import AssistanceApplication
from advisory_forum.models import Advisory
import requests
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def dashboard_view(request):
    weather = {}
    try:
        city = "Dhaka"
        api_key = 'your_openweathermap_api_key'
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        r = requests.get(url).json()
        weather = {
            'temp': r['main']['temp'],
            'desc': r['weather'][0]['description'].capitalize(),
            'humidity': r['main']['humidity']
        }
    except:
        weather = {'temp': '--', 'desc': 'Unavailable', 'humidity': '--'}

    context = {
        'krishok_count': Krishok.objects.count(),
        'crop_count': Crop.objects.count(),
        'fertilizer_count': Fertilizer.objects.count(),
        'product_count': Product.objects.count(),
        'application_count': AssistanceApplication.objects.count(),
        'advice_count': Advisory.objects.count(),
        'weather': weather,
    }
    return render(request, 'dashboard/dashboard.html', context)
@login_required
def dashboard_view(request):
    username = request.user.username
    return render(request, 'dashboard/dashboard.html', {'username': username})
