import os
print("Ruta de trabajo actual:", os.getcwd())  #Importante siempre para saber donde se está trabajando

import pandas as pd

df_laptops = pd.read_csv("R:/PROYECTOS/Data Science/Proyecto Data Science/laptop_price.csv", encoding="ISO-8859-1")

print(df_laptops.head(3))

### Filtrar dataframe basado en una condición ###

df_laptops['Company'] == 'Apple'  # Encontrar Laptops  Apple

print(df_laptops['Company'] == 'Apple') # Cadena de texto indicando verdadero y falso en función si son Apple

df_laptops['Price_euros'] > 1500  # Encontrar Laptops  que cuestan más de 1500 euros

print(df_laptops['Price_euros'] > 1500)

### Filtrar dataframe basado en múltiples condiciones ###

# Encontrar Laptops Apple que cuesten más de 1500 euros

(df_laptops['Company'] == 'Apple') & (df_laptops['Price_euros'] > 1500) # En pandas & es And y | es or 

df_laptops[(df_laptops['Company'] == 'Apple') & (df_laptops['Price_euros'] > 1500)] # Filtar dataframe basado en multiples condiciones

print(df_laptops[(df_laptops['Company'] == 'Apple') & (df_laptops['Price_euros'] > 1500)]) 

# Encontrar Laptops Apple o Dell

df_laptops['Company'] == 'Apple'
df_laptops['Company'] == 'Dell'

(df_laptops['Company'] == 'Apple') | (df_laptops['Company'] == 'Dell')

print ((df_laptops['Company'] == 'Apple') | (df_laptops['Company'] == 'Dell'))

# Filtar dataframe basado en multiples condiciones

df_laptops[(df_laptops['Company'] == 'Apple') | (df_laptops['Company'] == 'Dell')]

print(df_laptops[(df_laptops['Company'] == 'Apple') | (df_laptops['Company'] == 'Dell')])

print(df_laptops[(df_laptops['Company'] == 'Apple') | (df_laptops['Company'] == 'Dell')].value_counts('Company'))

# Encontrar Laptops Apple o Dell que cuesten más de 1500 euros
df_laptops['Company'] == 'Apple'
df_laptops['Company'] == 'Dell'
df_laptops['Price_euros'] > 1500

((df_laptops['Company'] == 'Apple') | (df_laptops['Company'] == 'Dell')) & (df_laptops['Price_euros'] > 1500)

# Filtrar dataframe basado en multiples condiciones

df_laptops[((df_laptops['Company'] == 'Apple') | (df_laptops['Company'] == 'Dell')) & (df_laptops['Price_euros'] > 1500)]

print(df_laptops[((df_laptops['Company'] == 'Apple') | (df_laptops['Company'] == 'Dell')) & (df_laptops['Price_euros'] > 1500)])
