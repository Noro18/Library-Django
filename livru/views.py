from django.shortcuts import render
from .models import Livru
# Create your views here.

def empresta_render(request):
    lista_livru = Livru.objects.all()
    return render(request, 'livru.html', {
        'livru_list': lista_livru,
    } )
