import os, pandas as pd



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
    pokemons_aliados = []
    for variable in args:
        atributos_pkm = read_csv(variable)
        pkm = Pokemon(**atributos_pkm)
        pokemons_aliados.append(pkm)
    
    pokemons_aliado_1 = pokemons_aliados[0]
    pokemons_aliado_2 = pokemons_aliados[1]
    pokemons_aliado_3 = pokemons_aliados[2]
    print(pokemons_aliado_1.name)
    print(pokemons_aliado_2.name)
    print(pokemons_aliado_3.name)