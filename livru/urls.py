from django.urls import path
from . import views

urlpatterns = [
    path('', views.empresta_render, name='livru'),
    path('add', views.add_livru, name='add_livru'),
    # path('dashboard/', views.dashboard_render, name='dashboard')

]