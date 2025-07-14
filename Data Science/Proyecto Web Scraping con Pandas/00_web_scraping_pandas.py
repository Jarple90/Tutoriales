### Importaciones ###
#!pip install pandas en python
#pip install pandas en bash

import pandas as pd

# Leer .csv de un URL con Pandas la url es https://www.football-data.co.uk/englandm.php el tutorial está hecha con la temporada 2021/2022, en nuestro caso lo actualizamos a 2024/2025

# Leer un archivo CSV de una website

df_pm24 = pd.read_csv('https://www.football-data.co.uk/mmz4281/2425/E0.csv')  # Se hace esto para no tener que descargar el archivo manualmente

print(df_pm24.head()) # Muestra las primeras filas del dataframe para verificar que se ha cargado correctamente


df_pm24.rename(columns={'Date': 'fecha',
                        'HomeTeam': 'equipo_local',
                        'AwayTeam': 'equipo_visitante',
                        'FTHG': 'goles_local',
                        'FTAG': 'goles_visitante',
                        'FTR': 'resultado',}, inplace=True) # Renombrar las columnas para que sean más descriptivas y en español

print(df_pm24.head()) # Muestra las primeras filas del dataframe para verificar que se ha renombrado correctamente

### Leer .csv de Multiples URLs con Pandas ###

# https://www.football-data.co.uk/mmz4281/2425/E0.csv
# https://www.football-data.co.uk/mmz4281/2425/E1.csv
# https://www.football-data.co.uk/mmz4281/2425/E2.csv
# https://www.football-data.co.uk/mmz4281/2425/E3.csv
# https://www.football-data.co.uk/mmz4281/2425/EC.csv

"https://www.football-data.co.uk/mmz4281" + "2425" + "E0" + ".csv" # Estructura de un link

root = "https://www.football-data.co.uk/mmz4281/" # crear una variable raiz o root

leagues = ["E0", "E1", "E2", "E3", "EC"] # Creamos una lista de ligas

frames = [] # Creamos una lista vacía para almacenar los dataframes

for league in leagues:
    df = pd.read_csv( root + '2425' + '/' + league +'.csv')
    frames.append(df) # Añadimos el dataframe a la lista de dataframes

print(len(frames)) # Muestra el número de dataframes que se han cargado

print(frames[0]) # Muestra el primer dataframe para verificar que se ha cargado correctamente

### Multiples Temporadas ###

for season in range(15,25): # Iteramos sobre las temporadas desde 2015 hasta 2025
    print(season) # Muestra la temporada actual

leagues = ["E0", "E1", "E2", "E3", "EC"] # Creamos una lista de ligas

frames = [] # Creamos una lista vacía para almacenar los dataframes


for league in leagues:
    for season in range(15,25):
        df = pd.read_csv( root + str(season)+str(season+1) + '/' + league +'.csv',  encoding='ISO-8859-1')
        df.insert(1, 'season', season) # Insertamos una nueva columna 'season' en la posición 1 del dataframe
        frames.append(df) # Añadimos el dataframe a la lista de dataframes

print(len(frames)) # Muestra el número de dataframes que se han cargado

print(frames[0]) # Muestra el primer dataframe para verificar que se ha cargado correctamente hay 50 dataframes, 10 temporadas y 5 ligas

### Organizar Datos en un Diccionario ###

# Crer un dicionario con nombre original de la liga como llave
dict_countries = {
        'Spanish la liga': 'SP1', 'Spanish Segunda Division': 'SP2',
        'German Bundesliga': 'D1',
        'English Premier League': 'E0', 'English League Championship': 'E2','English League 2': 'E3',
}

# obtener un elemento del diccionario

dict_countries['Spanish la liga'] # Devuelve 'SP1'

# crear lista de ligas

leagues = ['E0', 'E2', 'E3']
frames = [] # Creamos una lista vacía para almacenar los dataframes

# obtener un elemento del diccionario

print(dict_countries['Spanish la liga']) # Imprime 'SP1'

for league in dict_countries:
    print(dict_countries[league]) # Imprime el nombre de la liga en español

dict_historical_data = {}

# hacer loop sobre llaves de diccionario

# leagues = ['E0', 'E2', 'E3']

for league in dict_countries:
    frames = [] # Reiniciamos la lista de dataframes para cada liga
    for season in range(15,25):
        df = pd.read_csv( root + str(season)+str(season+1) + '/' + dict_countries[league] +'.csv',  encoding='ISO-8859-1')
        df.insert(1, 'season', season) # Insertamos una nueva columna 'season' en la posición 1 del dataframe
        df.insert(2, 'league', league) # Insertamos una nueva columna 'league' en la posición 2 del dataframe
        frames.append(df) # Añadimos el dataframe a la lista de dataframes
    df_concat = pd.concat(frames)
    dict_historical_data[league] = df_concat # Añadimos el dataframe concatenado al diccionario con la llave del nombre de la liga

    # Mostrar dataframe dentro de dict_hitorical_data
    
print(dict_historical_data.keys())  # Incluir en las llaves el nombre de la liga para obtener los datos

print(list(dict_historical_data.keys()))

print(dict_historical_data['Spanish la liga'].head()) # Muestra las primeras filas del dataframe de la liga española

