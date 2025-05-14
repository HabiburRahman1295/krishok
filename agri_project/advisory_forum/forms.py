from django import forms
from .models import Advisory

class AdvisoryForm(forms.ModelForm):
    class Meta:
        model = Advisory
        fields = ['farmer_name', 'phone', 'question']
