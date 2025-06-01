from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_render(request):
    return render(request, 'home.html' )

def dashboard_render(request):
    return render(request, 'content.html' )
    