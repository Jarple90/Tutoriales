import os
print("Ruta de trabajo actual:", os.getcwd())  #Importante siempre para saber donde se está trabajando

import pandas as pd

df_laptops = pd.read_csv("R:/PROYECTOS/Data Science/Proyecto Data Science/laptop_price.csv", encoding="ISO-8859-1")

print(df_laptops.head(5))

### Crear una columna condicional con 2 o mas opciones : np.select() ###

import numpy as np 

# Crear un array basado en multiples niveles de precios (+ 2 opciones)


# Crear "Condiciones" (Conditions) y "Valores" (Values)

condiciones = [
    df_laptops['Price_euros'] > 2500,
    (df_laptops['Price_euros'] > 2000) & (df_laptops['Price_euros'] <= 2500),
    (df_laptops['Price_euros'] > 800) & (df_laptops['Price_euros'] <= 2000),
    df_laptops['Price_euros'] <= 800
]

valores = ['Muy Caro', 'Caro', 'Barato', 'Muy Barato'] # > 2500, > 2000, > 800, <= 800

# Añadir una nueva columna

df_laptops['Niveles_Precio'] = np.select(condiciones, valores, default ='Sin categoria')

print(df_laptops)

# Contar los valores en la columna price_tier

print(df_laptops.value_counts('Niveles_Precio'))

# Ejercicio 

# Crear un array basado en múltiples tamaños de pantallas ("Screen Size")
# Muy grande > 16, Grande > 14, Pequeño > 12, Muy Pequeño < 12

# Crear "Condiciones" (Conditions) y  (Valores) "Valores"

condiciones = [
    df_laptops['Inches'] > 16,
    (df_laptops['Inches']> 14) & (df_laptops['Inches'] <= 16),
    (df_laptops['Inches']> 12) & (df_laptops['Inches'] <= 14),
    df_laptops['Inches'] <= 12
]

valores = ['Muy grande', 'Grande', 'Pequeño', 'Muy Pequeño']

# Añadir una nueva columna

df_laptops['Tamaño_Pantalla'] = np.select(condiciones, valores, default = 'Sin categoria')

# Mostrar Dataframe

print(df_laptops)
print(df_laptops['Tamaño_Pantalla'])

# Contar los valores en columna Screen_Size

print(df_laptops.value_counts(['Tamaño_Pantalla']))
