from django.urls import path
from . import views

# List of the URLS

urlpatterns = [
    path('', views.index)
]

