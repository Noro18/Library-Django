from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
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
    return render(request, 'add_autor.html', {'form': form})

def edit_publisher(request, pk):
    publisher = Publisher.objects.get(pk=pk) # iha ne'e atu fori object sira ho pk ne'ebe define iha tablea
    naran = Publisher.objects.get(id_publisher = pk)
    if request.method == 'POST':
        form = PublisherForm(request.POST, instance=publisher) # ida ne'e nia fill hotu ho valor husi submited form 
        if form.is_valid():
            form.save()
            return redirect('publisher')
    else:
        form = PublisherForm(instance=publisher) # iha ne'e nia kria form ida ho inrance ba object ida determina ona
    return render(request, 'edit_publisher.html', {'form': form, 'edit': True, 'publisher': publisher, 'naran': naran})

def delete_publisher(request, pk):
    publisher = get_object_or_404(Publisher, pk = pk)
    if request.method == 'POST':
        publisher.delete()
        return redirect('publisher')
    else:
        return HttpResponse("Publisher la existe")
