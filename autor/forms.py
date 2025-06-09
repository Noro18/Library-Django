from django import forms
from .models import Autor

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['naran_autor', 'data_moris', 'nasionalidade']
        widgets = {
            'naran_autor': forms.TextInput(attrs={'class': 'form-control'}),
            'data_moris': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'nasionalidade': forms.TextInput(attrs={'class': 'form-control'}),
            
        }
