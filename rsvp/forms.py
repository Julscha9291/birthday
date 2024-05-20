
from django import forms
from .models import Guest, Drink

class RSVPForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['name', 'guests', 'attendance', 'drinks']
        widgets = {
            'drinks': forms.CheckboxSelectMultiple(),
        }
        
