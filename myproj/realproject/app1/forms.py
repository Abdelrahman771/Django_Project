from django import forms
from .models import Car
class Carform(forms.ModelForm):
    class Meta :
        model = Car
        fields ='__all__'