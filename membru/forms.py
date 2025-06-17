from django import forms
from .models import Membru

class MembruForm(forms.ModelForm):
    class Meta:
        model = Membru
        fields = '__all__'
        labels = {
            'naran_membru': 'Naran Membru',
            'hela_fatin': 'Hela Fatin',
            'sexu': 'Sexu',
            'data_moris': 'Data Moris',
        }
        widgets = {
            'naran_membru': forms.TextInput(attrs={'class': 'form-control'}),
            'hela_fatin': forms.TextInput(attrs={'class': 'form-control'}),
            'sexu': forms.Select(attrs={'class': 'form-select'}),
            'data_moris': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }