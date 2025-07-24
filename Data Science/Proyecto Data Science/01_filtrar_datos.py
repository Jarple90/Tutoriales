#import pandas as pd

#df_laptops = pd.read_csv('laptop_price.csv')

#df_laptops.head(3)

import os
print("Ruta de trabajo actual:", os.getcwd())  #Importante siempre para saber donde se está trabajando

import pandas as pd  # pandas es una librería de Python para el análisis de datos y abrir archivos CSV


df_laptops = pd.read_csv("R:/PROYECTOS/Data Science/Proyecto Data Science/laptop_price.csv", encoding="ISO-8859-1") # Leer el archivo CSV con la codificación adecuada iso-8859-1 
# hace que se interpreten correctamente los caracteres especiales como la ñ y acentos

print(df_laptops.head(3)) # Muestra las primeras 3 filas del DataFrame para verificar que se ha cargado correctamente
