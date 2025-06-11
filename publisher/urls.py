from django.urls import path
from . import views

urlpatterns = [
    path('', views.publisher, name='publisher'),
    path('aumenta', views.aumenta_publisher, name='aumenta_publisher')

]