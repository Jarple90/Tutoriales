import os  # Interactuar con el sistema operativo
print("Ruta de trabajo actual:", os.getcwd())  #Importante siempre para saber donde se está trabajando

import pandas as pd  

df_laptops = pd.read_csv("R:/PROYECTOS/Data Science/Proyecto Data Science/laptop_price.csv", encoding="ISO-8859-1")

print(df_laptops.head(6))

### Duplicated() ###

# Encontrar duplicados en una columna/serie

df_laptops.duplicated('laptop_ID')

# Mostrar los elementos en dataframe con duplicados en la columna 'laptop_ID'

print(df_laptops[df_laptops.duplicated('laptop_ID')])
print(df_laptops[df_laptops.duplicated('laptop_ID')].value_counts())

# Duplicados en dos o más columnas

duplicated = df_laptops.duplicated(['Product', 'TypeName', 'Inches'])

print(df_laptops.duplicated(['Product', 'TypeName', 'Inches']))  # también se puede poner print(duplicated)

# Muestra todos los valores duplicados (exepto por el primero -keep = 'first')

print(df_laptops[duplicated].sort_values(['Product','TypeName']))

### Ejemplo ###

# Encontrar las laptops que sean más baratas y caras de cada compañia usando el método sort_values() y duplicated () (argumentos: keep "first". "last" and False)

# Ordenar dataframe de manera ascendente por "Company" y "Price"
# Más barato primero y más caro último

df_sorted = df_laptops.sort_values(['Company', 'Price_euros'])
print(df_sorted)

# Revisar todas las categorias en la columna "Company"

df_laptops.value_counts('Company')
print(df_laptops.value_counts('Company'))

# Valores duplicados en la columna "Company" (por defecto --> Keep = 'first')

duplicated_first = df_sorted.duplicated('Company', keep = 'first')
print(duplicated_first)

# Mostrar dataframe con valores duplicados en la columna "Company"

df_sorted[duplicated_first]
print(df_sorted[duplicated_first])

# Keep = 'first' (laptops más baratas por compañia)
# Mostrar dataframe con valores no duplicados en la columan "Company"

df_sorted[~duplicated_first]
print(df_sorted[~duplicated_first][['Company','Price_euros']])

# Revisar todas las categorias

df_sorted[~duplicated_first].value_counts('Company')
print(df_sorted[~duplicated_first].value_counts('Company'))

# keep = 'last'

duplicated_last = df_sorted.duplicated('Company', keep = 'last')
print(duplicated_last)
# keep = False

# keep = 'last' (laptops más caras por compañia)
# Mostrar dataframe con valores no duplicados en columna "Company"

df_sorted[~duplicated_last]
print(df_sorted[~duplicated_last])
print(df_sorted[~duplicated_last][['Company','Price_euros']])

# Revisar todas las categorias

df_sorted[~duplicated_last].value_counts('Company')
print(df_sorted[~duplicated_last].value_counts('Company'))

# Duplicados en la columna "Company" (todos los duplicados, incluyendo el primero)
duplicated_all = df_sorted.duplicated('Company', keep=False)

# Mostrar solo las filas que están duplicadas (todas las apariciones)
df_all_duplicates = df_sorted[duplicated_all]
print("Todas las laptops duplicadas por compañía (incluyendo la primera):")
print(df_all_duplicates[['Company', 'Product', 'Price_euros']])

# Contar cuántas veces aparece cada compañía en los duplicados
print("Frecuencia de compañías con laptops duplicadas:")
print(df_all_duplicates['Company'].value_counts())

# Mostrar solo las compañías que tienen una única laptop (no duplicadas)
df_unique_companies = df_sorted[~duplicated_all]
print("Laptops únicas por compañía (sin duplicados):")
print(df_unique_companies[['Company', 'Product', 'Price_euros']])

# Contar cuántas compañías tienen una sola laptop registrada
print("Frecuencia de compañías con laptops únicas:")
print(df_unique_companies['Company'].value_counts())

