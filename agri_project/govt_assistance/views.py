from django.shortcuts import render, redirect
from .forms import AssistanceForm
from .models import AssistanceApplication

def apply_for_assistance(request):
    if request.method == 'POST':
        form = AssistanceForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'govt_assistance/success.html')
    else:
        form = AssistanceForm()
    return render(request, 'govt_assistance/apply.html', {'form': form})

def view_applications(request):
    applications = AssistanceApplication.objects.all().order_by('-submitted_at')
    return render(request, 'govt_assistance/applications.html', {'applications': applications})
