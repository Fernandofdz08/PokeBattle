from django.shortcuts import render
from django.http import HttpResponse
import os, csv, requests, pandas as pd
from bs4 import BeautifulSoup
from . import classpkm
# Create your views here.

def prueba(request):
    a = 5 
    b = 3
    c = a + b
    print(c)
    return HttpResponse(f"La suma de {a} + {b} es igual a {c}")

def pokemon_csv(request):
    csv_path = os.path.abspath(os.path.join(os.getcwd(), "Pokemon - Físicos.csv"))

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
    #pkm2 = input("Qué pokemon quieres?")
    #pkm3 = input("Qué pokemon quieres?")
    r = classpkm.__main__(pkm1) #, pkm2, pkm3)
    return HttpResponse(r)

def ataques_pokemon(request):
    nombre_ataques = [], tipo_ataques = [], especial_fisico = [], precision_ataques = []
    dict_ataque = {}
    r = requests.get("https://pokemondb.net/move/all")
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        tabla = soup.find('table')
        for fila in tabla.find_all('tr'):
            celdas = fila.find_all('td')
            # Hay 8 columnas, Name, Type, Category, Power, Accuracy, PP, Effect, Prob

            if len(celdas) == 8:
                nombre_ataque = celdas[0].text.strip()
                nombre_ataques.append(nombre_ataque)
                tipo_ataque = celdas[1].text.strip()
                tipo_ataques.append(tipo_ataque)
                ataque_spe_phy = soup.find('td', attrs={'data-sort-value': True})
                valor_tipo_ataque = ataque_spe_phy['data-sort-value']
                especial_fisico.append(valor_tipo_ataque)
                precision = celdas[4].text.strip()
                precision_ataques.append(precision)
    
    dict_ataque = dict(zip(nombre_ataques, tipo_ataques, especial_fisico, precision_ataques))
    print(dict_ataque)
                
    return HttpResponse(r.text)