from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insertar-datos/', views.insertar_datos, name='insertar_datos'),
    path('buscar/', views.buscar, name='buscar'),
]
