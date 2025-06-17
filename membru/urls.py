from django.urls import path
from . import views

urlpatterns = [
    path('', views.membru, name='membru'),
    path('add', views.add_membru, name='aumenta_membru'),
    path('edit/<int:pk>', views.edit_membru, name='edit_membru'),
]
