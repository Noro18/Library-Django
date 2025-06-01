from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def render_empresta(request):
    return render(request, 'empresta.html')