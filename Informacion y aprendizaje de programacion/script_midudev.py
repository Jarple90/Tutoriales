# ============================================
# 📚 Script para descargar y leer libros del repo
# midudev/libros-programacion-gratis
# ============================================

import os
import requests
from bs4 import BeautifulSoup
import PyPDF2

# -----------------------------
# 1. URL base del repositorio
# -----------------------------
BASE_URL = "https://github.com/midudev/libros-programacion-gratis/tree/main/web/public/books"
RAW_BASE = "https://raw.githubusercontent.com/midudev/libros-programacion-gratis/main/web/public/books/"

# -----------------------------
# 2. Crear carpetas locales
# -----------------------------
os.makedirs("libros_descargados", exist_ok=True)
os.makedirs("libros_texto", exist_ok=True)

# -----------------------------
# 3. Obtener lista de archivos
# -----------------------------
def obtener_archivos():
    page = requests.get(BASE_URL)
    soup = BeautifulSoup(page.text, "html.parser")

    archivos = []
    for link in soup.find_all("a"):
        href = link.get("href", "")
        if href.endswith(".pdf") or href.endswith(".epub"):
            nombre = href.split("/")[-1]
            archivos.append(nombre)

    return archivos

# -----------------------------
# 4. Descargar archivos
# -----------------------------
def descargar_archivo(nombre):
    url = RAW_BASE + nombre
    ruta = os.path.join("libros_descargados", nombre)

    print(f"📥 Descargando: {nombre}")
    r = requests.get(url)

    if r.status_code == 200:
        with open(ruta, "wb") as f:
            f.write(r.content)
        print("✔️ Descargado")
    else:
        print("❌ Error al descargar:", nombre)

# -----------------------------
# 5. Leer PDF y extraer texto
# -----------------------------
def leer_pdf(nombre):
    ruta = os.path.join("libros_descargados", nombre)
    salida = os.path.join("libros_texto", nombre.replace(".pdf", ".txt"))

    print(f"📖 Leyendo PDF: {nombre}")

    with open(ruta, "rb") as f:
        lector = PyPDF2.PdfReader(f)
        texto = ""

        for pagina in lector.pages:
            texto += pagina.extract_text() + "\n"

    with open(salida, "w", encoding="utf-8") as f:
        f.write(texto)

    print("✔️ Texto extraído:", salida)

# -----------------------------
# 6. Ejecutar todo
# -----------------------------
def main():
    archivos = obtener_archivos()
    print(f"📚 Archivos encontrados: {len(archivos)}")

    for archivo in archivos:
        descargar_archivo(archivo)

        if archivo.endswith(".pdf"):
            leer_pdf(archivo)
        else:
            print(f"⚠️ EPUB detectado (requiere ebooklib): {archivo}")

if __name__ == "__main__":
    main()
