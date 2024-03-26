from django.urls import path
from . import views

urlpatterns = [
    path('prueba/', views.prueba, name='prueba_django'), 
    path('pokemon_csv/', views.pokemon_csv, name='pokemon_csv'),
    path('showdown/', views.showdown, name="showdown"),
    path('clases_pokemon/',views.clases_pokemon, name="clases_pokemon"),
    path('ataques_pokemon/', views.ataques_pokemon, name="ataques_pokemon"),
]