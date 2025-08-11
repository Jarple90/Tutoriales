import os  # Interactuar con el sistema operativo
print("Ruta de trabajo actual:", os.getcwd())  #Importante siempre para saber donde se está trabajando

import pandas as pd  

df_laptops = pd.read_csv("R:/PROYECTOS/Data Science/Proyecto Data Science/laptop_price.csv", encoding="ISO-8859-1")

print(df_laptops.head(8))

### Unique () ###

# Devolver valores unicos de una serie ( los valores unicos son devueltos en el orde que aparecen)

# Obtener elementos únicos en la columna 'Company'

df_laptops['Company'].unique()
print(df_laptops['Company'].unique())

# Obtener elementos únicos en la columna 'Inches'

df_laptops['Inches'].unique()
print(df_laptops['Inches'].unique())

# Obtener el tamaño de los elementos únicos 

len(df_laptops['Inches'].unique())
print(len(df_laptops['Inches'].unique()))

len(df_laptops['Company'].unique())
print(len(df_laptops['Company'].unique()))