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