from django.shortcuts import render, redirect, get_object_or_404
from .models import Livru
from .forms import LivruForm
# Create your views here.

def empresta_render(request):
    lista_livru = Livru.objects.all()
    return render(request, 'livru.html', {
        'livru_list': lista_livru,
    })

def add_livru(request):
    if request.method == 'POST': # ida ne'e atu check nia request ne POST ou Get tanba nia form nia url mai ba iha view ida entaun tenki hare nia mehtod se post anta nia save data
        form = LivruForm(request.POST) # jadi instance husi from maibe nia prense hotu ona ho valor husi post nian 
        if form.is_valid():
            form.save()
            return redirect('livru')
    else:
        form = LivruForm() # se quando nai metodo GET ou seidauk iah dados entaun ni kria deit form mamuk ida
    return render(request, 'add_livru.html', {'form': form}) # e depois maka nia render form ne'e iha add livru no lori hanesan context iha form

def edit_livru(request, pk):
    livru = Livru.objects.get(pk=pk) # iha ne'e atu fori object sira ho pk ne'ebe define iha tablea
    if request.method == 'POST':
        form = LivruForm(request.POST, instance=livru) # ida ne'e nia fill hotu ho valor husi submited form 
        if form.is_valid():
            form.save()
            return redirect('livru')
    else:
        form = LivruForm(instance=livru) # iha ne'e nia kria form ida ho inrance ba object ida determina ona
    return render(request, 'add_livru.html', {'form': form, 'edit': True, 'livru': livru})

def delete_livru(request, prim):
    # livru = Livru.objects.get(pk=prim) ida bele uza ida ne'e mais diak liu uza get_object_or_404

    livro = get_object_or_404(Livru, pk = prim) # ida uza method ida ne'e atu handle mos se quando nai object la existe ou 404 
    if request.method == "POST":
        livro.delete()  # ida ne'e atu delete object ne'e
        return redirect('livru')
        # print("deleeted")
    else:
        return render(request, 'delete.html', {'livru_object': livro})
    