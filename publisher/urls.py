from django.urls import path
from . import views

urlpatterns = [
    path('', views.publisher, name='publisher'),
    path('aumenta', views.aumenta_publisher, name='aumenta_publisher'),
    path('edit/<int:pk>', views.edit_publisher, name='edit_publisher')

]