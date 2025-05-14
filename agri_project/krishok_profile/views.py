from django.shortcuts import render
from .forms import KrishokForm
from .models import Krishok

def register_krishok(request):
    form = KrishokForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return render(request, 'krishok_profile/success.html', {'name': form.cleaned_data['name']})
    return render(request, 'krishok_profile/register.html', {'form': form})

def search_krishok(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Krishok.objects.filter(phone__icontains=query) | Krishok.objects.filter(nid__icontains=query)
    return render(request, 'krishok_profile/search.html', {'results': results, 'query': query})

