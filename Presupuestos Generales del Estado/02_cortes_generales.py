import pandas as pd
import requests

def cargar_estado_gastos_csv(url_csv):
    # Descargar y cargar el CSV, saltando cabecera
    df = pd.read_csv(url_csv, sep=';', encoding='latin1', skiprows=9)
    df = df.dropna(axis=1, how='all')
    df.columns = [col.strip() for col in df.columns]

    # Rellenar valores faltantes
    df['Orgánica'] = df['Orgánica'].ffill()
    df['Económica'] = df['Económica'].ffill()

    # Limpiar y convertir columna Total
    df['Total'] = df['Total'].str.replace('.', '', regex=False)
    df['Total'] = df['Total'].str.replace(',', '.', regex=False)
    df['Total'] = pd.to_numeric(df['Total'], errors='coerce')

    # Convertir de miles de euros a euros
    df['Total'] = df['Total'] * 1000

    return df[df['Total'].notna()]

# URL del CSV de Cortes Generales
csv_estado_gastos = "https://www.sepg.pap.hacienda.gob.es/Presup/PGE2023Prorroga/MaestroDocumentos/PGE-ROM/doc/CSV/N_23P_E_R_31_102_1_1_1_1911N_2.CSV"

# Cargar datos
df_csv = cargar_estado_gastos_csv(csv_estado_gastos)

# 📊 Mostrar resultados
print("\n📄 Estado de Gastos (CSV):")
print(df_csv.head())

# Diccionario de códigos orgánicos
organismos = {
    '02.01': 'Congreso de los Diputados',
    '02.02': 'Senado',
    '02.03': 'Tribunal de Cuentas',
    '02.04': 'Defensor del Pueblo'
}

# Mostrar ejemplos válidos
for codigo, nombre in organismos.items():
    filtro = df_csv[df_csv['Orgánica'] == codigo]
    print(f"\n🏛️ {nombre} ({codigo})")
    print(filtro.head())  # Primeras filas
    print(f"💰 Total de gasto: {filtro['Total'].sum():,.2f} euros")

    ### Resumen Orgánico económico ###

import pandas as pd

def cargar_presupuesto_entidades(url_csv):
    # Cargar el CSV saltando las filas decorativas
    df = pd.read_csv(url_csv, sep=';', encoding='latin1', skiprows=20)
    df.columns = [col.strip() for col in df.columns]

    # Renombrar columnas si es necesario
    if 'Entidad' not in df.columns:
        df = df.rename(columns={df.columns[0]: 'Entidad', df.columns[1]: 'Explicación'})

    # Detectar columna de totales (última columna con valores numéricos y comas)
    posibles_totales = df.columns[-5:]  # Últimas columnas suelen contener los totales
    col_total = None
    for col in posibles_totales:
        if df[col].astype(str).str.contains(',', regex=False).sum() > 0:
            col_total = col
            break

    if not col_total:
        raise ValueError("❌ No se encontró la columna de totales en el DataFrame.")

    # Detectar columnas numéricas (EU-1 a EU-7 y Total)
    columnas_euros = [col for col in df.columns if col.startswith('EU-')] + [col_total]

    # Convertir valores a euros
    for col in columnas_euros:
        df[col] = df[col].astype(str).str.replace('.', '', regex=False)
        df[col] = df[col].str.replace(',', '.', regex=False)
        df[col] = pd.to_numeric(df[col], errors='coerce') * 1000

    return df, col_total

# URL del CSV
url_entidades = "https://www.sepg.pap.hacienda.gob.es/Presup/PGE2023Prorroga/MaestroDocumentos/PGE-ROM/doc/CSV/N_23P_E_R_31_102_1_1_1_1911N_3.CSV"

# Cargar datos
df_entidades, col_total = cargar_presupuesto_entidades(url_entidades)

# Mostrar primeras filas
print("\n📄 Presupuesto por Entidad:")
print(df_entidades[['Entidad', 'Explicación', col_total]].head())

# Limpiar columna 'Entidad' para evitar errores
df_entidades['Entidad'] = df_entidades['Entidad'].astype(str).str.strip()

# Mostrar total de gasto por entidad
print("\n🧾 Total de gasto por entidad:")
entidades_unicas = df_entidades['Entidad'].dropna().unique()

for entidad in entidades_unicas:
    entidad = str(entidad).strip()
    total_entidad = df_entidades[df_entidades['Entidad'] == entidad][col_total].sum()
    print(f"🏛️ {entidad} → 💰 {total_entidad:,.0f} euros")

# Mostrar el total general del presupuesto
total_general = df_entidades[col_total].sum()
print(f"\n📊 Total general del presupuesto: {total_general:,.0f} euros")


### Resumen Orgánico por programas ###

import pandas as pd
import requests

# Diccionario con nombres para cada CSV
csv_urls = {
    "Capítulo 1": "https://www.sepg.pap.hacienda.gob.es/Presup/PGE2023Prorroga/MaestroDocumentos/PGE-ROM/doc/CSV/N_23P_E_R_31_102_1_1_2_1_1.CSV",
    "Capítulo 2": "https://www.sepg.pap.hacienda.gob.es/Presup/PGE2023Prorroga/MaestroDocumentos/PGE-ROM/doc/CSV/N_23P_E_R_31_102_1_1_2_2_1.CSV",
    "Capítulo 3": "https://www.sepg.pap.hacienda.gob.es/Presup/PGE2023Prorroga/MaestroDocumentos/PGE-ROM/doc/CSV/N_23P_E_R_31_102_1_1_2_3.CSV"
}

# Función para procesar cada CSV
def procesar_csv(nombre, url):
    response = requests.get(url)
    lines = response.text.splitlines()
    data = []

    for line in lines:
        fields = line.split(';')
        if len(fields) >= 3 and fields[0].strip() not in ['', 'Clasif. por programas']:
            data.append(fields[:3])

    # Crear DataFrame
    df = pd.DataFrame(data, columns=['Programa', 'Descripción', 'Importe'])

    # Limpiar y convertir importes
    df['Importe'] = (
        df['Importe']
        .str.replace('.', '', regex=False)
        .str.replace(',', '.', regex=False)
        .str.replace('€', '', regex=False)
        .str.strip()
    )
    df['Importe'] = pd.to_numeric(df['Importe'], errors='coerce')

    # Mostrar resultados
    print(f"\n📁 Datos extraídos de {nombre}:")
    print(df)

# Ejecutar para cada CSV
for nombre, url in csv_urls.items():
    procesar_csv(nombre, url)

### Resumen económico por programas del prespuesto de gastos ###

import pandas as pd
import requests

# URL del CSV
url = "https://www.sepg.pap.hacienda.gob.es/Presup/PGE2023Prorroga/MaestroDocumentos/PGE-ROM/doc/CSV/N_23P_E_R_31_102_1_1_3_1.CSV"

# Descargar contenido
response = requests.get(url)
lines = response.text.splitlines()

# Buscar la fila que contiene el programa 911N
datos = None
for line in lines:
    fields = line.split(';')
    if '911N' in fields[0]:
        datos = fields
        break

# Verificar que se encontró la fila
if datos is None:
    raise ValueError("No se encontró la fila del programa 911N.")

# Crear nombres de columna dinámicos
num_columnas = len(datos)
columnas = [f'Col_{i+1}' for i in range(num_columnas)]

# Crear DataFrame
df = pd.DataFrame([datos], columns=columnas)

# Renombrar columnas con nombres reales (ajustado a 12 columnas)
df.columns = [
    'Programa', 'Descripción', 'Capítulo 1', 'Capítulo 2', 'Capítulo 3',
    'Capítulo 4', 'Capítulo 6', 'Capítulo 8', 'Capítulos 1 a 8',
    'Capítulo 9', 'Total', 'Observaciones'
]

# Función robusta para limpiar valores numéricos
def limpiar_valor(valor):
    if not valor or valor.strip() == '':
        return None
    try:
        return float(
            valor.replace('.', '').replace(',', '.').replace('€', '').strip()
        )
    except ValueError:
        return None

# Aplicar limpieza a columnas numéricas
columnas_numericas = [
    'Capítulo 1', 'Capítulo 2', 'Capítulo 3', 'Capítulo 4',
    'Capítulo 6', 'Capítulo 8', 'Capítulos 1 a 8', 'Capítulo 9', 'Total'
]
for col in columnas_numericas:
    df[col] = df[col].apply(limpiar_valor)

# Mostrar resultado limpio
print(df)













