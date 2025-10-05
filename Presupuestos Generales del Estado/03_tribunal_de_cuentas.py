### Control externo del Sector Público y Resumen Orgán
import pandas as pd
import requests

# URLs de los dos CSV
urls = {
    "CSV 1": "https://www.sepg.pap.hacienda.gob.es/Presup/PGE2023Prorroga/MaestroDocumentos/PGE-ROM/doc/CSV/N_23P_E_R_31_103_1_1_1_1911O_2.CSV",
    "CSV 2": "https://www.sepg.pap.hacienda.gob.es/Presup/PGE2023Prorroga/MaestroDocumentos/PGE-ROM/doc/CSV/N_23P_E_R_31_103_1_1_1_1911O_3.CSV"
}

# Función para limpiar importes
def limpiar_importe(valor):
    if not valor or valor.strip() == '':
        return None
    try:
        return float(valor.replace('.', '').replace(',', '.').replace('€', '').strip())
    except ValueError:
        return None

# Procesar cada CSV
for nombre, url in urls.items():
    response = requests.get(url)
    lines = response.text.splitlines()

    # Filtrar líneas útiles
    data = []
    for line in lines:
        fields = line.split(';')
        if len(fields) >= 3 and fields[0].strip() not in ['', 'Clasif. por programas']:
            data.append(fields[:3])  # Tomar solo las primeras 3 columnas

    # Crear DataFrame
    df = pd.DataFrame(data[1:], columns=data[0])  # Usar primera fila como encabezado

    # Renombrar columnas si es necesario
    df.columns = ['Económica', 'Descripción', 'Importe']

    # Limpiar columna de importes
    df['Importe'] = df['Importe'].apply(limpiar_importe)

    # Mostrar resultado
    print(f"\n📁 Datos extraídos de {nombre}:")
    print(df)
