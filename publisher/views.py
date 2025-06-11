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

def aumenta_publisher(request):
    if request.method == 'POST': # ida ne'e atu check nia request ne POST ou Get tanba nia form nia url mai ba iha view ida entaun tenki hare nia mehtod se post anta nia save data
        form = PublisherForm(request.POST) # jadi instance husi from maibe nia prense hotu ona ho valor husi post nian 
        if form.is_valid():
            form.save()
            return redirect('publisher')
    else:
        form = PublisherForm() # se quando nai metodo GET ou seidauk iah dados entaun ni kria deit form mamuk ida
    return render(request, 'add_autor.html', {'form': form}) # e 
