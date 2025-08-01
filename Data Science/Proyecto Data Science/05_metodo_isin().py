import os  # Interactuar con el sistema operativo
print("Ruta de trabajo actual:", os.getcwd())  #Importante siempre para saber donde se está trabajando

import pandas as pd  

df_laptops = pd.read_csv("R:/PROYECTOS/Data Science/Proyecto Data Science/laptop_price.csv", encoding="ISO-8859-1")

print(df_laptops.head(5))

### .isin(): Filtrado Simple

# Seleccionar laptops Apple o HP 

df_laptops['Company'].isin(['Apple','HP']) 

print(df_laptops['Company'].isin(['Apple','HP'])) 

# Filtrar dataframes

df_laptops[df_laptops['Company'].isin(['Apple', 'HP'])]

print(df_laptops[df_laptops['Company'].isin(['Apple', 'HP'])])

print(df_laptops[df_laptops['Company'].isin(['Apple', 'HP'])].value_counts('Company')) 

### .isin(): Filtrado Múltiple

# Encontrar Notebooks o Ultrabooks de Apple o HP

filtro1 = df_laptops['TypeName'].isin(['Notebooks', 'Ultrabook'])
filtro2 = df_laptops['Company'].isin(['Apple', 'HP'])

# Filtrar Dataframes

df_laptops[filtro1 & filtro2]

print(df_laptops[filtro1 & filtro2])