from django.urls import path
from . import views

urlpatterns = [
    path('prueba/', views.prueba, name='prueba_django'), 
    path('pokemon_csv', views.pokemon_csv, name='pokemon_csv'),
]