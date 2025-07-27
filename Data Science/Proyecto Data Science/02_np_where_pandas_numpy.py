import os
print("Ruta de trabajo actual:", os.getcwd())  #Importante siempre para saber donde se está trabajando

import pandas as pd

df_laptops = pd.read_csv("R:/PROYECTOS/Data Science/Proyecto Data Science/laptop_price.csv", encoding="ISO-8859-1")

print(df_laptops.head(3))

# CRAR UNA COLUMNA BASDADA EN 1 CONDICIÓN: np.where()

import numpy as np

# creara un arrya basado en nivel de precio (price_tier)

np.where(df_laptops['Price_euros']> 2000, 'Caro', 'Barato') # Esto crea un array donde si el precio es mayor a 2000, se marca como 'Caro', de lo contrario 'Barato'

df_laptops['Price_euros']> 2000

# Añadir la nueva columna al DataFrame

df_laptops['Price_categoria'] = np.where(df_laptops['Price_euros'] > 2000, 'Caro', 'Barato')

# Mostrar los 5 primeras columnas
print(df_laptops.head(5))

# Contar los valores en columna price_tier

print(df_laptops.value_counts('Price_categoria'))

### Ejercicio adicional ###

# Crear un array basado en el tamaño de la pantalla (screen size >15)

np.where(df_laptops['Inches'] > 15, 'Grande', 'Pequeño')
df_laptops['Inches'] > 15

# Añadir la nueva columna al DataFrame

df_laptops['Screen_Size'] = np.where(df_laptops['Inches'] > 15, 'Grande', 'Pequeño')

# Mostrar los 5 primeras columnas

print(df_laptops.head(5))

# Contar los valores en columna de Screen Size

print(df_laptops.value_counts('Screen_Size'))