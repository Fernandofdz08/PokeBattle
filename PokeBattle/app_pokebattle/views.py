from django.shortcuts import render
from django.http import HttpResponse
import os, csv, requests, pandas as pd
from . import classpkm
# Create your views here.

def prueba(request):
    a = 5 
    b = 3
    c = a + b
    print(c)
    return HttpResponse(f"La suma de {a} + {b} es igual a {c}")

def pokemon_csv(request):
    csv_path = os.path.abspath(os.path.join(os.getcwd(), "../Pokemon - Físicos.csv"))

    with open(csv_path, "r") as pokemon_csv:
        df = pd.read_csv(pokemon_csv)
        cabecera = df.columns.tolist()
        fila_leida = df.iloc[0].tolist()
        atributos_pkm = dict(zip(cabecera, fila_leida))
        print(atributos_pkm)
        #print(' '.join(map(str, cabecera)))
        #print(' '.join(map(str, fila_leida.values))) 
    
        return HttpResponse(atributos_pkm)#and ' '.join(map(str, fila_leida.values)))
        
def showdown(request):
    r = requests.get("https://play.pokemonshowdown.com/teambuilder")
    print(r.text)
    return HttpResponse("none")

def clases_pokemon(request):
    pkm1 = input("Qué pokemon quieres?")
    pkm2 = input("Qué pokemon quieres?")
    pkm3 = input("Qué pokemon quieres?")
    #pkm3 = input("Qué pokemon quieres?")
    r = classpkm.__main__(pkm1, pkm2, pkm3) #pkm2, pkm3)
    return HttpResponse(r)

