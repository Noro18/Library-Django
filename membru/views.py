from django.shortcuts import render, redirect, get_object_or_404
from .models import Membru
from .forms import MembruForm

def membru(request):
    form = MembruForm() # iha ne'e nia kria form ida ho inrance ba object ida determina ona
    lista_membru = Membru.objects.all()
    return render(request, 'membru.html', {
        'membru_list': lista_membru,
        'form': form
    })

def add_membru(request):
    if request.method == 'POST': # ida ne'e atu check nia request ne POST ou Get tanba nia form nia url mai ba iha view ida entaun tenki hare nia mehtod se post anta nia save data
        form = MembruForm(request.POST) # jadi instance husi from maibe nia prense hotu ona ho valor husi post nian 
        if form.is_valid():
            form.save()
            return redirect('membru')
    else:
        form = MembruForm() # se quando nai metodo GET ou seidauk iah dados entaun ni kria deit form mamuk ida
    return render(request, 'membru.html', {'form': form}) # e depois maka nia render form ne'e iha add livru no lori hanesan context iha form


def edit_membru(request, pk):
    membru = Membru.objects.get(pk=pk) # iha ne'e atu fori object sira ho pk ne'ebe define iha tablea
    naran = Membru.objects.get(id_membru = pk)
    if request.method == 'POST':
        form = MembruForm(request.POST, instance=membru) # ida ne'e nia fill hotu ho valor husi submited form 
        if form.is_valid():
            form.save()
            return redirect('membru')
    else:
        form = MembruForm(instance=membru) # iha ne'e nia kria form ida ho inrance ba object ida determina ona
    return render(request, 'edit_membru.html', {'form': form, 'edit': True, 'membru': membru, 'naran': naran})

def delete_membru(request, pk):
    livro = get_object_or_404(Membru, pk = pk) # ida uza method ida ne'e atu handle mos se quando nai object la existe ou 404 
    if request.method == "POST":
        livro.delete()  # ida ne'e atu delete object ne'e
        return redirect('membru')
        # print("deleeted")
    else:
        return render(request, 'membru.html', {'livru_object': livro})