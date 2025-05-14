from django.shortcuts import render
from .models import Crop

def crop_list(request):
    crops = Crop.objects.all()
    return render(request, 'crop_management/crop_list.html', {'crops': crops})
