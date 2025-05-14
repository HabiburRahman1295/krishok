from django.shortcuts import render, redirect
from .forms import AdvisoryForm
from .models import Advisory

def ask_question(request):
    if request.method == 'POST':
        form = AdvisoryForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'advisory_forum/success.html')
    else:
        form = AdvisoryForm()
    return render(request, 'advisory_forum/ask.html', {'form': form})

def view_forum(request):
    questions = Advisory.objects.all().order_by('-submitted_at')
    return render(request, 'advisory_forum/forum.html', {'questions': questions})
