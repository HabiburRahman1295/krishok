from django import forms
from .models import Krishok

class KrishokForm(forms.ModelForm):
    class Meta:
        model = Krishok
        fields = '__all__'
