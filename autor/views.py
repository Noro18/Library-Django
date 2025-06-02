from django.shortcuts import render, redirect
from .models import Autor
from .forms import AutorForm
# Create your views here.

def autor(request):
    autor = Autor.objects.all()
    return render(request, 'autor.html', {'autors': autor} )

def aumenta_autor(request):
    if request.method == 'POST': # ida ne'e atu check nia request ne POST ou Get tanba nia form nia url mai ba iha view ida entaun tenki hare nia mehtod se post anta nia save data
        form = AutorForm(request.POST) # jadi instance husi from maibe nia prense hotu ona ho valor husi post nian 
        if form.is_valid():
            form.save()
            return redirect('autor')
    else:
        form = AutorForm() # se quando nai metodo GET ou seidauk iah dados entaun ni kria deit form mamuk ida
    return render(request, 'add_autor.html', {'form': form}) # e 