import requests
from bs4 import BeautifulSoup

url = "https://www.sepg.pap.hacienda.gob.es/Presup/PGE2023Prorroga/MaestroDocumentos/PGE-ROM/N_23P_E_R_31_101_1_1.htm"
base_url = "https://www.sepg.pap.hacienda.gob.es"

response = requests.get(url)
response.encoding = 'utf-8'

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    enlaces = soup.find_all('a')

    # Fragmentos de href que identifican cada apartado
    claves_href = {
        "Estado de gastos": "N_23P_E_R_31_101_1_1_1.htm",
        "Resumen orgánico por programas del presupuesto de gastos": "N_23P_E_R_31_101_1_1_2.htm",
        "Resumen económico por programas del presupuesto de gastos": "N_23P_E_R_31_101_1_1_3.htm"
    }

    resultados = {}

    for clave, fragmento in claves_href.items():
        for a in enlaces:
            href = a.get('href')
            if href and fragmento in href:
                resultados[clave] = base_url + "/" + href if not href.startswith("http") else href
                break
        if clave not in resultados:
            resultados[clave] = None

    # Mostrar resultados filtrados
    print("🔗 Enlaces clave encontrados:\n")
    for clave, url_final in resultados.items():
        if url_final:
            print(f"✅ {clave}: {url_final}")
        else:
            print(f"❌ No encontrado: {clave}")
else:
    print(f"❌ Error al acceder a la página (status code: {response.status_code})")


import pandas as pd
import requests

# URL del CSV
url_2 = "https://www.sepg.pap.hacienda.gob.es/Presup/PGE2023Prorroga/MaestroDocumentos/PGE-ROM/doc/CSV/N_23P_E_R_31_101_1_1_1_1911M_2.CSV"

# Paso 1: inspeccionar el contenido
response = requests.get(url_2)
lines = response.text.splitlines()

# Mostrar las primeras 20 líneas para ver dónde empieza la tabla
for i, line in enumerate(lines[:20]):
    print(f"{i}: {line}")

#✅ Carga limpia del CSV 2 (Estado de Gastos)

import pandas as pd

url_2 = "https://www.sepg.pap.hacienda.gob.es/Presup/PGE2023Prorroga/MaestroDocumentos/PGE-ROM/doc/CSV/N_23P_E_R_31_101_1_1_1_1911M_2.CSV"

# Cargar saltando las primeras 9 líneas
df_2 = pd.read_csv(url_2, sep=';', encoding='latin1', skiprows=9)

# Eliminar columnas vacías
df_2 = df_2.dropna(axis=1, how='all')

# Renombrar columnas si es necesario
df_2.columns = [col.strip() for col in df_2.columns]

# Mostrar primeras filas
print("📄 Estado de Gastos limpio:")
print(df_2.head())
#🧠 ¿Qué conseguimos con esto?
#Cargamos solo la parte útil del archivo.

#Eliminamos columnas vacías (como las dobles ;;).

#Dejamos el DataFrame listo para análisis por orgánica, económica, explicación y total.

# Rellenar valores hacia adelante
df_2['Orgánica'] = df_2['Orgánica'].ffill()
df_2['Económica'] = df_2['Económica'].ffill()

# Limpiar y convertir la columna Total
df_2['Total'] = df_2['Total'].str.replace('.', '', regex=False)  # eliminar separador de miles
df_2['Total'] = df_2['Total'].str.replace(',', '.', regex=False)  # convertir coma decimal
df_2['Total'] = pd.to_numeric(df_2['Total'], errors='coerce')

# Filtrar solo filas con importe
df_gastos = df_2[df_2['Total'].notna()]

print(df_gastos.groupby('Económica')['Total'].sum())

rey = df_gastos[df_gastos['Explicación'].str.contains("S.M. el Rey", na=False)]
print(rey)

# Program 911M. Resumen Orgánico económico 

import requests

url_3 = "https://www.sepg.pap.hacienda.gob.es/Presup/PGE2023Prorroga/MaestroDocumentos/PGE-ROM/doc/CSV/N_23P_E_R_31_101_1_1_1_1911M_3.CSV"
response = requests.get(url_3)
lines = response.text.splitlines()

# Mostrar las primeras 20 líneas
for i, line in enumerate(lines[:20]):
    print(f"{i}: {line}")

import pandas as pd

# URL del segundo CSV
url_3 = "https://www.sepg.pap.hacienda.gob.es/Presup/PGE2023Prorroga/MaestroDocumentos/PGE-ROM/doc/CSV/N_23P_E_R_31_101_1_1_1_1911M_3.CSV"

# Cargar el CSV saltando las primeras 10 líneas
df_3 = pd.read_csv(url_3, sep=';', encoding='latin1', skiprows=10)

# Eliminar columnas vacías
df_3 = df_3.dropna(axis=1, how='all')

# Renombrar columnas
df_3.columns = [col.strip() for col in df_3.columns]

# Convertir la columna 'Total' a numérica
df_3['Total'] = df_3['Total'].str.replace('.', '', regex=False)
df_3['Total'] = df_3['Total'].str.replace(',', '.', regex=False)
df_3['Total'] = pd.to_numeric(df_3['Total'], errors='coerce')

# Filtrar filas con datos válidos
df_economico = df_3[df_3['Total'].notna()]

import pandas as pd

# URL del segundo CSV
url_3 = "https://www.sepg.pap.hacienda.gob.es/Presup/PGE2023Prorroga/MaestroDocumentos/PGE-ROM/doc/CSV/N_23P_E_R_31_101_1_1_1_1911M_3.CSV"

# Cargar el CSV saltando las primeras 10 líneas
df_raw = pd.read_csv(url_3, sep=';', encoding='latin1', skiprows=10)

# Eliminar columnas vacías
df_raw = df_raw.dropna(axis=1, how='all')

# Renombrar columnas
df_raw.columns = [col.strip() for col in df_raw.columns]

# Limpiar y convertir la columna 'Total' a euros
df_raw['Total'] = df_raw['Total'].str.replace('.', '', regex=False)
df_raw['Total'] = df_raw['Total'].str.replace(',', '.', regex=False)
df_raw['Total'] = pd.to_numeric(df_raw['Total'], errors='coerce') * 1000  # Convertir a euros

# Filtrar filas válidas (con importe)
df_clean = df_raw[df_raw['Total'].notna()].copy()

# Renombrar columnas para mayor claridad
df_clean = df_clean.rename(columns={
    'Económica': 'Código Económico',
    'Explicación': 'Tipo de Gasto',
    'Total': 'Importe (€)'
})

# Opcional: eliminar fila de total duplicado si existe
df_clean = df_clean[df_clean['Tipo de Gasto'].str.upper() != 'TOTAL']

# Mostrar tabla final
print(df_clean[['Código Económico', 'Tipo de Gasto', 'Importe (€)']])

### Resumen Orgánico por programas del presupuesto de Gastos ###
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import matplotlib.pyplot as plt

# URL del documento HTML
url = "https://www.sepg.pap.hacienda.gob.es/Presup/PGE2023Prorroga/MaestroDocumentos/PGE-ROM/doc/HTM/N_23P_E_R_31_101_1_1_3_1.HTM"

# Descargar el contenido
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Extraer texto plano
texto = soup.get_text(separator="\n")

# Buscar líneas que contengan importes y programas
patron = re.compile(r"(911M|TOTAL CONSOLIDADO|TOTAL)\s+Jefatura del Estado\s+(\d{1,3}\.\d{3},\d{2})\s+(\d{1,3}\.\d{3},\d{2})\s+(\d{1,3}\.\d{3},\d{2})")
resultados = patron.findall(texto)

# Crear lista de diccionarios con conversión a euros reales
datos = []
for programa, cap4, cap1a8, total in resultados:
    datos.append({
        "Programa": programa,
        "Capítulo 4 (€)": float(cap4.replace(".", "").replace(",", ".")) * 1000,
        "Cap. 1 a 8 (€)": float(cap1a8.replace(".", "").replace(",", ".")) * 1000,
        "Total (€)": float(total.replace(".", "").replace(",", ".")) * 1000
    })

# Crear DataFrame
df = pd.DataFrame(datos)

# Mostrar tabla
print("\n📊 DataFrame con importes en euros:")
print(df)

# Visualizar con gráfico de barras
plt.figure(figsize=(8, 5))
plt.bar(df["Programa"], df["Total (€)"], color="royalblue")
plt.title("Presupuesto por programa - Casa del Rey (2023)")
plt.ylabel("Total (€)")
plt.xlabel("Programa")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()








