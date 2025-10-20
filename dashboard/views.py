from django.shortcuts import render
from livru.models import Livru
from membru.models import Membru
from empresta.models import Empresta
# Create your views here.

def dashboard(request):
    livru = Livru.objects.count()
    membru = Membru.objects.count()
    # livru_emprestada = 
    empresta = Empresta.objects.filter(status='borrowing').count()
    overdue =  Empresta.objects.filter(status='overdue').count()
    return render(request, 'dashboard.html', {
        'total_livru': livru,
        'total_membru': membru,
        'livru_emprestada': empresta,
        'livru_overdue': overdue
    
    })