from django.urls import path
from . import views
urlpatterns = [
    path("", views.autor, name="autor"),
    path("aumenta", views.aumenta_autor, name="aumenta_autor"),
    path('edit/<int:pk>', views.edit_autor, name='edit_autor'),
]
