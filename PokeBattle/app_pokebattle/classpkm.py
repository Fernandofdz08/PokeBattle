import os, pandas as pd
import random, requests
from bs4 import BeautifulSoup

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
    
def damage(allies, enemies, caracteristicas_ataque):
    # Detectar si el ataque es de tipo Físico o Especial
    if caracteristicas_ataque["especial_fisico"] == "physical":
        Attack = int(allies.At)
    if caracteristicas_ataque["especial_fisico"] == "special":
        Attack = int(allies.AtEsp)

    # Valor de bonificación, si esta teracristalizado, si tanto su tipo original como su teratipo coinciden con el tipo del ataque
    # la bonificación es de 2, si solo coincide su tipo original, la bonificación es de 1.5, si no coincide ninguno, la bonificación es de 1, si no esta teracristalizado
    # si el ataque es del mismo tipo que el pokemon que lo lanza oma valor 1.5, si el ataque es de un tipo diferente al del pokemon que lo lanza toma un valor de 1. 
    
    if allies.Is_Teratype == True: 
        if allies.type1 == allies.teratype and allies.type2 == allies.teratype:
            Bonif = 2
        elif allies.type1 == allies.teratype or allies.type2 == allies.teratype:
            Bonif = 1.5
        else:
            Bonif = 1
    else: 
        print("El pokemon no es teratipo")
        Bonif = 1
        

    # La efectividad vendrá dada por la tabla de tipos, por el momento, por pruebas se establece en 1
    Efectivity = 1
    # La variación vendrá dada por un número aleatorio entre 85 y 100
    Variation =  random.randint(85,100)
    # Nivel del pokemon, por defecto, todos en 100
    Level = 100

    Power = int(caracteristicas_ataque["potencia"])
    Defense = int(enemies.Def)

    Daño = 0.01 * Bonif * Efectivity * Variation *(((0.2 * Level + 1) * Attack * Power) / (25 * Defense) + 2)
    print(f"{allies.name} ha hecho un total de daño a {enemies.name} de {Daño} PS.")
    enemies.PS -= Daño
    print(f"Los PS del pokemon {enemies.name} son {enemies.PS}")
    if enemies.PS <= 0:
        print(f"El pokemon {enemies.name} ha sido derrotado.")
        # Eliminar el objeto pokemon
        del enemies
        return True


def batalla_pokemon(pkm1, pkm2, ataques):
    print(f"Va a comenzar la batalla pokemon entre  {pkm1.name} y {pkm2.name}")
    print(f"Es el turno de {pkm1.name}")
    while pkm1.PS > 0 and pkm2.PS > 0:
        print(f"El pokemon {pkm1.name} tiene {pkm1.PS} PS y el pokemon {pkm2.name} tiene {pkm2.PS} PS")
        print("Es el turno de {pkm1.name}")
        print("Elige un ataque: ")
        print(f"1. Ataque 1: {pkm1.At1}")
        print(f"2. Ataque 2: {pkm1.At2}")
        print(f"3. Ataque 3: {pkm1.At3}")
        print(f"4. Ataque 4: {pkm1.At4}")

        ataque_elegido = input("Elige un ataque: ")
        
        print(f"El ataque_elegido es {ataque_elegido}")

        dict_caracteristicas_ataque = read_at_type_csv(ataque_elegido, ataques)

        damage(pkm1, pkm2, dict_caracteristicas_ataque)


        print(f"Es el turno de {pkm2.name}")
        print(f"A {pkm2.name} le quedan {pkm2.PS} PS")
        print("Elige un ataque: ")
        print(f"1. Ataque 1: {pkm2.At1}")
        print(f"2. Ataque 2: {pkm2.At2}")
        print(f"3. Ataque 3: {pkm2.At3}")
        print(f"4. Ataque 4: {pkm2.At4}")

        ataque_elegido = input("Elige un ataque: ")
        print(f"El ataque elegido es {ataque_elegido}")

        dict_caracteristicas_ataque = read_at_type_csv(ataque_elegido, ataques)

        damage(pkm2, pkm1, dict_caracteristicas_ataque)

    print("La batalla ha terminado, has sido eliminado")
    pass


#############
#Funciones csv
#############

def read_csv(nombre_pkm1):
    csv_path = os.path.abspath(os.path.join(os.getcwd(), "Pokemon - Físicos.csv"))

    with open(csv_path, "r") as pokemon_csv:
        df = pd.read_csv(pokemon_csv)
        cabecera = df.columns.tolist()
        fila_leida = df.loc[df['name'] == nombre_pkm1].values[0]
        ###Valorar si se lee equipo propio o enemigo
        ###Decidir qué pokemon es mejor si hay duplicidad del mismo
        ###Para decidir, tener en cuenta los ataques y características
        atributos_pkm = dict(zip(cabecera, fila_leida))
        return atributos_pkm
    
def read_at_type_csv(ataque_elegido, ataque):
    fila_ataque = ataque.loc[ataque['nombre_ataques'] == ataque_elegido]
    tipo_ataque = fila_ataque['tipo_ataques'].values[0]
    especial_fisico = fila_ataque['especial_fisico'].values[0]
    precision = fila_ataque['precision_ataques'].values[0]
    potencia = fila_ataque['potencia'].values[0]
    caracteristicas_ataque_elegido = dict(zip(['tipo_ataque', 'especial_fisico', 'precision', 'potencia'], [tipo_ataque, especial_fisico, precision, potencia]))
    """
    Esto devuelve un diccionario con el siguiente estilo: 

    características_ataque_elegido = {
        'tipo_ataque': 'tipo_ataque',
        'especial_fisico': 'especial_fisico',
        'precision': 'precision'
    }
    """

    # Se devuelve el diccionario con las carácterísticas del ataque pokemon elegído. 

    return caracteristicas_ataque_elegido
    #print(f"El ataque elegido es de tipo {tipo_ataque} y es special/physical: {especial_fisico}, con accuracy {precision}")


    
#############
# Funcion para obtener datos
#############
    
###### ATAQUES POKEMON #########

def ataques_pokemon():
    nombre_ataques = []
    tipo_ataques = []
    especial_fisico = []
    precision_ataques = []
    potencia_ataque = []
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
                ataque_spe_phy = celdas[2]['data-sort-value']
                #ataque_spe_phy = soup.find('td', attrs={'data-sort-value': True})
                #valor_tipo_ataque = ataque_spe_phy['data-sort-value']
                especial_fisico.append(ataque_spe_phy)
                potencia = celdas[3].text.strip()
                potencia_ataque.append(potencia)
                precision = celdas[4].text.strip()
                precision_ataques.append(precision)
                
            
    dict_ataque = dict(
        zip(
            ['nombre_ataques', 'tipo_ataques', 'especial_fisico', 'potencia', 'precision_ataques'],  # Claves
            [nombre_ataques, tipo_ataques, especial_fisico, potencia_ataque, precision_ataques]  # Valores
        )
    )

    df = pd.DataFrame(dict_ataque)

    df.to_csv(os.path.join('.','Pokemon - Ataques.csv'), index=False, sep=';')

    return df


def __main__(*args):

    # 1º Fase. Quedarse con los pokemon escogidos. 
    # Realizar la busqueda en el archivo CSV de pokemons escogidos y crear objetos de la clase pokemon con sus atributos. 

    pokemons_escogidos = []
    for variable in args:
        atributos_pkm = read_csv(variable)
        pkm = Pokemon(**atributos_pkm)
        pokemons_escogidos.append(pkm)
    
    pokemons_aliado_1 = pokemons_escogidos[0]
    pokemons_enemigo_1 = pokemons_escogidos[1]

    # 2º Fase. Obtener los distintos ataques pokemons escogidos para a posteriori realizar el cálculo de daño.
    # Se llama a la función para obtener todos los ataques, para a posteriori saber que tipos de ataque pueden utilizar

    ataques = ataques_pokemon()

    # 3º Fase. Implementar la lucha pokemon

    batalla_pokemon(pokemons_aliado_1, pokemons_enemigo_1, ataques)

    #pokemons_aliado_3 = pokemons_aliados[2]
    #r = damage(pokemons_aliado_1, pokemons_enemigo_2)

    
