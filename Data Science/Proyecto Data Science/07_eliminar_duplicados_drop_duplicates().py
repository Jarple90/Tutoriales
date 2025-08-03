import os  # Interactuar con el sistema operativo
print("Ruta de trabajo actual:", os.getcwd())  #Importante siempre para saber donde se está trabajando

import pandas as pd  

df_laptops = pd.read_csv("R:/PROYECTOS/Data Science/Proyecto Data Science/laptop_price.csv", encoding="ISO-8859-1")

print(df_laptops.head(6))

# Eliminar duplicados en 2 o más columnas 
df_laptops.drop_duplicates(['Company'])
print(df_laptops.drop_duplicates(['Company']))

df_laptops.drop_duplicates(['Company'])['Company'].value_counts()
print(df_laptops.drop_duplicates(['Company'])['Company'].value_counts())


# Ordenar dataframe ascendiente por compañia (company) y precio (price)
# Más barato primero y más caro último 

df_sorted= df_laptops.sort_values(['Company', 'Price_euros'])
print(df_sorted)

# Más barato : keep = 'first'

cheapest_by_company = df_sorted.drop_duplicates(['Company'], keep = 'first')[['Company', 'Price_euros']]
print(cheapest_by_company)

# Más caro: keep = 'last'

most_expensive_by_company = df_sorted.drop_duplicates(['Company'], keep = 'last', ignore_index= True)
print(most_expensive_by_company)

# Argumentos

# Inplace : Elimina duplicados en el Dataframe o devuelve copia
# Ignore_index = True : El index es ignorado y de resultado tendría como 0, 1, ...

cheapest_by_company = df_sorted.drop_duplicates('Company', keep='first')[['Company', 'Price_euros']].reset_index(drop=True)
print("Más barato por compañía:")
print(cheapest_by_company)

most_expensive_by_company = df_sorted.drop_duplicates('Company', keep='last')[['Company', 'Price_euros']].reset_index(drop=True)
print("Más caro por compañía:")
print(most_expensive_by_company)

### Ejercicio ###

# Encontrar las pantallas más grandes y pequeñas en laptop por cada compañia usando el método sort_values() y duplicated () (keep 'first', 'last' y False)

df_laptops = pd.read_csv("R:/PROYECTOS/Data Science/Proyecto Data Science/laptop_price.csv", encoding="ISO-8859-1")

# Ordenar Dataframe ascendiente por compañia (company) y pulgadas (Inches)
df_sorted_inches = df_laptops.sort_values(['Company', 'Inches'])

# Pantalla más pequeña por compañía
smallest_screen_by_company = df_sorted_inches.drop_duplicates('Company', keep='first')[['Company', 'Inches']].reset_index(drop=True)
print("Pantalla más pequeña por compañía:")
print(smallest_screen_by_company)

# Pantalla más grande por compañía
largest_screen_by_company = df_sorted_inches.drop_duplicates('Company', keep='last')[['Company', 'Inches']].reset_index(drop=True)
print("Pantalla más grande por compañía:")
print(largest_screen_by_company)
