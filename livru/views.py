from django.shortcuts import render, redirect
from .models import Livru
from .forms import LivruForm
# Create your views here.

def empresta_render(request):
    lista_livru = Livru.objects.all()
    return render(request, 'livru.html', {
        'livru_list': lista_livru,
    })

def add_livru(request):
    if request.method == 'POST':
        form = LivruForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livru')
    else:
        form = LivruForm()
    return render(request, 'add_livru.html', {'form': form})
