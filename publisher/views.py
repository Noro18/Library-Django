from django.shortcuts import render, redirect, get_list_or_404
from .models import Publisher
from .forms import PublisherForm

def publisher(request):
    form = PublisherForm() # iha ne'e nia kria form ida ho inrance ba object ida determina ona
    lista_publisher = Publisher.objects.all()
    return render(request, 'publisher.html', 
    {
        'publisher_list': lista_publisher,
        'form': form
    }              
    )
