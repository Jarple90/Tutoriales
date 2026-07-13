import os
import requests
import pdfplumber
from deep_translator import GoogleTranslator

# ---------------------------------------
# CONFIGURACIÓN DEL REPO (FUNCIONA)
# ---------------------------------------
OWNER = "dformoso"
REPO = "machine-learning-mindmap"
PATH = ""  # raíz del repositorio

API_URL = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{PATH}?ref=master"
RAW_BASE = f"https://raw.githubusercontent.com/{OWNER}/{REPO}/master/"

# ---------------------------------------
# CREAR CARPETAS
# ---------------------------------------
os.makedirs("ds_libros_pdf", exist_ok=True)
os.makedirs("ds_libros_texto_en", exist_ok=True)
os.makedirs("ds_libros_texto_es", exist_ok=True)

# ---------------------------------------
# 1. Obtener PDFs desde la API de GitHub
# ---------------------------------------
def obtener_archivos():
    print("🔍 Consultando API de GitHub...")
    r = requests.get(API_URL)

    if r.status_code != 200:
        print("❌ Error al acceder a la API:", r.status_code)
        return []

    archivos = [item["name"] for item in r.json() if item["name"].endswith(".pdf")]
    return archivos

# ---------------------------------------
# 2. Descargar PDFs
# ---------------------------------------
def descargar_pdf(nombre):
    url = RAW_BASE + nombre
    ruta = os.path.join("ds_libros_pdf", nombre)

    print(f"📥 Descargando: {nombre}")
    r = requests.get(url)

    if r.status_code == 200:
        with open(ruta, "wb") as f:
            f.write(r.content)
        print("✔️ Descargado")
    else:
        print("❌ Error al descargar:", nombre)

# ---------------------------------------
# 3. Extraer texto + traducir
# ---------------------------------------
def procesar_pdf(nombre):
    ruta_pdf = os.path.join("ds_libros_pdf", nombre)
    ruta_en = os.path.join("ds_libros_texto_en", nombre.replace(".pdf", ".txt"))
    ruta_es = os.path.join("ds_libros_texto_es", nombre.replace(".pdf", ".txt"))

    print(f"📖 Leyendo PDF: {nombre}")

    texto = ""

    with pdfplumber.open(ruta_pdf) as pdf:
        for pagina in pdf.pages:
            contenido = pagina.extract_text()
            if contenido:
                texto += contenido + "\n"

    # Guardar versión original (EN)
    with open(ruta_en, "w", encoding="utf-8") as f:
        f.write(texto)

    print("✔️ Texto original guardado:", ruta_en)

    # Traducir al español
    print("🌐 Traduciendo al español...")
    traduccion = GoogleTranslator(source="auto", target="es").translate(texto)

    with open(ruta_es, "w", encoding="utf-8") as f:
        f.write(traduccion)

    print("✔️ Traducción guardada:", ruta_es)

# ---------------------------------------
# 4. Ejecutar todo
# ---------------------------------------
def main():
    archivos = obtener_archivos()
    print(f"📚 Archivos encontrados: {len(archivos)}")

    for archivo in archivos:
        descargar_pdf(archivo)
        procesar_pdf(archivo)

if __name__ == "__main__":
    main()
