from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Empresta, Empresta_Detail
from .forms import EmprestaForm, EmprestaDetailFormSet

# List all borrowings

def render_empresta(request):
    form = EmprestaForm()
    formset = EmprestaDetailFormSet()
    empresta_list = Empresta.objects.all()
    return render(request, 'empresta.html', {
        'empresta_list': empresta_list,
        'form': form,
        'formset': formset
        

        })

# Add a new borrowing (Empresta + Empresta_Detail)
def add_empresta(request):
    if request.method == 'POST':
        form = EmprestaForm(request.POST)
        formset = EmprestaDetailFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            empresta = form.save()
            details = formset.save(commit=False)
            for detail in details:
                detail.id_empresta = empresta
                detail.save()
            messages.success(request, 'Borrowing record added successfully!')
            return redirect('empresta')  # Change to your list view name
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = EmprestaForm()
        formset = EmprestaDetailFormSet()
    return render(request, 'modal_add_empresta.html', {
        'form': form,
        'formset': formset
    })

# Borrowing detail view
def empresta_detail(request, id_empresta):
    empresta = Empresta.objects.get(pk=id_empresta)
    details = Empresta_Detail.objects.filter(id_empresta=empresta)
    return render(request, 'empresta_detail.html', {
        'empresta': empresta,
        'details': details
    })

def empresta_returned(request, id_empresta):
    return render(request, 'empresta.html')