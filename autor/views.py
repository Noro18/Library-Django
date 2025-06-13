from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor
from django.http import HttpResponse
from .forms import AutorForm
# Create your views here.

def autor(request):
    form = AutorForm() # jadi instance husi from maibe nia prense hotu ona ho valor husi post nian
    autor = Autor.objects.all()
    return render(request, 'autor.html', 
                {
                'autors': autor, 
                'form': form
            })

def aumenta_autor(request):
    if request.method == 'POST': # ida ne'e atu check nia request ne POST ou Get tanba nia form nia url mai ba iha view ida entaun tenki hare nia mehtod se post anta nia save data
        form = AutorForm(request.POST) # jadi instance husi from maibe nia prense hotu ona ho valor husi post nian 
        if form.is_valid():
            form.save()
            return redirect('autor')
    else:
        form = AutorForm() # se quando nai metodo GET ou seidauk iah dados entaun ni kria deit form mamuk ida
    return render(request, 'add_autor.html', {'form': form})

def edit_autor(request, pk):
    autor = Autor.objects.get(pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('autor')
    else:
        form = AutorForm(instance=autor) # iha ne'e nia kria form ida ho inrance ba object ida determina ona
    return render(request, 'edit_Autor.html', {'form': form, 'edit': True, 'autor': autor})


def delete_autor(request, prim):
    autor = get_object_or_404(Autor ,pk=prim)
    if request.method == "POST":
        autor.delete()  # ida ne'e atu delete object ne'e
        return redirect('autor')
        # print("deleeted")
    else:
        return HttpResponse("404, autor not found")