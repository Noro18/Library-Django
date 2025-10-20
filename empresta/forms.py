from django import forms
from .models import Empresta, Empresta_Detail
from django.forms import inlineformset_factory

class EmprestaForm(forms.ModelForm):
    class Meta:
        model = Empresta
        fields = ['id_membru', 'data_empresta', 'data_hatama']
        widgets = {
            'data_empresta': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'data_hatama': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.__class__.__name__ == 'Select':
                field.widget.attrs['class'] = 'form-select'
            elif field.widget.__class__.__name__ == 'DateInput':
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-control'

class EmprestaDetailForm(forms.ModelForm):
    class Meta:
        model = Empresta_Detail
        fields = ['id_kopia', 'data_hatama_actual']
        widgets = {
            'data_hatama_actual': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Only show available copies
        self.fields['id_kopia'].queryset = self.fields['id_kopia'].queryset.filter(status='available')
        for field_name, field in self.fields.items():
            if field.widget.__class__.__name__ == 'Select':
                field.widget.attrs['class'] = 'form-select'
            elif field.widget.__class__.__name__ == 'DateInput':
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-control'

# Inline formset to add multiple book copies to a borrowing record
EmprestaDetailFormSet = inlineformset_factory(
    Empresta,
    Empresta_Detail,
    form=EmprestaDetailForm,
    extra=2,  # Show two forms by default for borrowing multiple books
    can_delete=True
)
