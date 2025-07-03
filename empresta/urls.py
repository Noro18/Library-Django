from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_empresta, name='empresta'),
    path('add/', views.add_empresta, name='aumenta_empresta'),
    path('<int:id_empresta>/', views.empresta_detail, name='empresta_detail'),
]
