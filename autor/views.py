from django.shortcuts import render

# Create your views here.

def render_autor(request):
    return render(request, 'autor.html' )