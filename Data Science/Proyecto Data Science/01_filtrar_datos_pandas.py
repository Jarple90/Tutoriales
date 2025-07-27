#import pandas as pd

#df_laptops = pd.read_csv('laptop_price.csv')

#df_laptops.head(3)

import os
print("Ruta de trabajo actual:", os.getcwd())  #Importante siempre para saber donde se está trabajando

import pandas as pd  # pandas es una librería de Python para el análisis de datos y abrir archivos CSV

df_laptops = pd.read_csv("R:/PROYECTOS/Data Science/Proyecto Data Science/laptop_price.csv", encoding="ISO-8859-1") # Leer el archivo CSV con la codificación adecuada iso-8859-1 
# hace que se interpreten correctamente los caracteres especiales como la ñ y acentos

print(df_laptops.head(3)) # Muestra las primeras 3 filas del DataFrame para verificar que se ha cargado correctamente

# Encontrar filas que tengan "Apple" en la columna "Company"
apple_laptops = df_laptops[df_laptops['Company'] == "Apple"]
print(apple_laptops) # Esto crea una serie booleana donde True indica que la fila tiene "Apple" en la columna "Company"

print(df_laptops[df_laptops['Company'] == "Apple"].value_counts('Company')) # Cuenta cuántas veces aparece "Apple" en la columna "Company"

# Encontrar filas que no tienen "HP" en la columna "Company"
hp_laptops = df_laptops[df_laptops['Company'] != "HP"]
print(hp_laptops) # Esto crea una serie booleana donde True indica que la fila no tiene "HP" en la columna "Company"

# Encontrar laptops con un precio mayor a 1000
expensive_laptops = df_laptops[df_laptops['Price_euros'] > 1000]
print(expensive_laptops) # Esto crea una serie booleana donde True indica que el precio es mayor a 1000 euros

