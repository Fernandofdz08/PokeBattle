import os, pandas as pd
import random

class Pokemon:

    """def __init__(self, name : str, type1 : str, type2 : str, Ps : int, At : int, Def : int, AtSp : int, DefSp : int, Vel : int, Hability : str, Object : str, At1 : str, TypeAt1 : str, At2 : str, TypeAt2 : str, At3 : str, TypeAt3 : str, At4 : str, TypeAt4 : str, Teratype : str, Is_Teratype : bool):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.Ps = Ps
        self.At = At
        self.Def = Def
        self.AtSp = AtSp
        self.DefSp = DefSp
        self.Vel = Vel
        self.Hability = Hability
        self.Object = Object
        self.At1 = At1
        self.TypeAt1 = TypeAt1
        self.At2 = At2
        self.TypeAt2 = TypeAt2
        self.At3 = At3
        self.TypeAt3 = TypeAt3
        self.At4 = At4
        self.TypeAt4 = TypeAt4
        self.Is_Teratype = Is_Teratype"""
    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    
def damage(allies, enemies):
    # Valor de bonificación, si esta teracristalizado, si tanto su tipo original como su teratipo coinciden con el tipo del ataque
    # la bonificación es de 2, si solo coincide su tipo original, la bonificación es de 1.5, si no coincide ninguno, la bonificación es de 1, si no esta teracristalizado
    # si el ataque es del mismo tipo que el pokemon que lo lanza oma valor 1.5, si el ataque es de un tipo diferente al del pokemon que lo lanza toma un valor de 1. 
    # 

    if allies.isTeraType == True: 
        if allies.type1 == allies.teratype and allies.type2 == allies.teratype:
            bonif = 2
        elif allies.type1 == allies.teratype or allies.type2 == allies.teratype:
            bonif = 1.5
        else:
            bonif = 1

    # La efectividad vendrá dada por la tabla de tipos, por el momento, por pruebas se establece en 1
    Efectivity = 1
    # La variación vendrá dada por un número aleatorio entre 85 y 100
    Variation =  random.randint(85,100)
    # Nivel del pokemon, por defecto, todos en 100
    Level = 100
    

    #Daño = 0.01 * Bonif * Efectivity * Variation ( between 85 and 100) *(((0.2 * Level + 1) * Attack * Power) / (25 * Defense) + 2)


    


#############
#Funciones csv
#############

def read_csv(nombre_pkm1):
    csv_path = os.path.abspath(os.path.join(os.getcwd(), "../Pokemon - Físicos.csv"))

    with open(csv_path, "r") as pokemon_csv:
        df = pd.read_csv(pokemon_csv)
        cabecera = df.columns.tolist()
        fila_leida = df.loc[df['name'] == nombre_pkm1].values[0]
        ###Valorar si se lee equipo propio o enemigo
        ###Decidir qué pokemon es mejor si hay duplicidad del mismo
        ###Para decidir, tener en cuenta los ataques y características
        print(fila_leida)
        atributos_pkm = dict(zip(cabecera, fila_leida))
        return atributos_pkm

def __main__(*args):
    pokemons_escogidos = []
    for variable in args:
        atributos_pkm = read_csv(variable)
        pkm = Pokemon(**atributos_pkm)
        pokemons_escogidos.append(pkm)
    
    pokemons_aliado_1 = pokemons_escogidos[0]
    pokemons_enemigo_2 = pokemons_escogidos[1]
    #pokemons_aliado_3 = pokemons_aliados[2]
    r = damage(pokemons_aliado_1, pokemons_enemigo_2)

    
