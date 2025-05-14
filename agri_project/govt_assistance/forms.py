from django import forms
from .models import AssistanceApplication

class AssistanceForm(forms.ModelForm):
    class Meta:
        model = AssistanceApplication
        fields = '__all__'
