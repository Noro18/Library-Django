from django.shortcuts import render, redirect

def publisher(request):
    return render(request, 'publisher.html')
