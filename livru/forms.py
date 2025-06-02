from django import forms
from .models import Livru

class LivruForm(forms.ModelForm):
    class Meta:
        model = Livru
        fields = ['titulu_livru', 'isbn', 'id_kategoria', 'id_autor', 'id_publisher', 'data_publica']
        labels = {
            'id_autor': 'Naran Autor',
            'id_publisher': 'Publisher',
            'id_kategoria': 'Kategoria',
        }
        widgets = {
            'titulu_livru': forms.TextInput(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'id_kategoria': forms.Select(attrs={'class': 'form-select'}),
            'id_autor': forms.Select(attrs={'class': 'form-select'}),
            'id_publisher': forms.Select(attrs={'class': 'form-select'}),
            'data_publica': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
