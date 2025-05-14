from django.shortcuts import render
from .models import Fertilizer

def fertilizer_list(request):
    fertilizers = Fertilizer.objects.all()
    return render(request, 'fertilizer_management/fertilizer_list.html', {'fertilizers': fertilizers})
