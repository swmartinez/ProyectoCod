from django.urls import path
from AppUno import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('smartphone/', views.smartphone, name='smartphone'),
    path('tablet/', views.tablet, name='tablet'),
    path('tv/', views.tv, name='tv'),
    path('notebook/', views.notebook, name='notebook'),
    path('contact/', views.contact, name='contact'),
    path('busqueda-producto/', views.buscar_producto, name='busqueda-producto'),
    path('buscar/', views.buscar, name='buscar'),
]