from django import forms
from .models import Publisher

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['naran_publisher', 'enderesu', 'email', 'nu_telf']
        labels = {
            'naran_publisher' : 'Naran Publisher',
            'enderesu' : 'Enderesu',
            'email' : 'Email',
            'nu_telf' : 'Nu Telf',
        }

        widgets = {
            'naran_publisher': forms.TextInput(attrs={'class': 'form-control'}),
            'enderesu': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'nu_telf': forms.TextInput(attrs={'class': 'form-control'}),
        }