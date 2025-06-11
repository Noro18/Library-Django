from django.urls import path
from . import views

urlpatterns = [
    path('', views.livru, name='livru'),
    path('add', views.add_livru, name='aumenta_livru'),
    path('edit/<int:pk>', views.edit_livru, name='edit_livru'),
    path('delete/<int:prim>', views.delete_livru, name='delete_livru'),
    # path('dashboard/', views.dashboard_render, name='dashboard')

]