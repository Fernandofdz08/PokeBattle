from django.shortcuts import render
from django.http import HttpResponse
import os, csv, pandas as pd

# Create your views here.

def prueba(request):
    a = 5 
    b = 3
    c = a + b
    print(c)
    return HttpResponse(f"La suma de {a} + {b} es igual a {c}")

def pokemon_csv(request):
    # Sabemos que estamos en directorio app_pokebattle
    # Nuestro archivo csv está en la carpeta raiz del proyecto
    # Vamos a obtener la ruta del archivo csv
    # Sabemos que esta dos directorios atrás, por lo que
    # la ruta sería ../../nombre_archivo.csv

    # Obtenemos la ruta del archivo csv
    csv_path = os.path.abspath(os.path.join(os.getcwd(), "../Pokemon - Especiales.csv"))

    # Abrimos el archivo csv en modo lectura

    with open(csv_path, "r") as pokemon_csv:
        # Con el modulo pandas, leemos el archivo. 
        #Esto devuelve una lista, que contiene un elemento por cada fila leida
        df = pd.read_csv(pokemon_csv)
        print(df)
        return HttpResponse(df.to_html())
        
