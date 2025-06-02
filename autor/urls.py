from django.urls import path
from . import views
urlpatterns = [
    path("", views.autor, name="autor"),
    path("aumenta", views.aumenta_autor, name="aumenta_autor")
]
