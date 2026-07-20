import os
import requests
from bs4 import BeautifulSoup

BASE_CATEGORIAS = "https://openlibro.com/categorias/"
CARPETA_PDF = "libros_pdf"

os.makedirs(CARPETA_PDF, exist_ok=True)

HEADERS = {"User-Agent": "Mozilla/5.0"}

def descargar_pdf(url):
    nombre = url.split("/")[-1]
    ruta = os.path.join(CARPETA_PDF, nombre)

    print(f"📥 Descargando PDF: {url}")

    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        if r.status_code == 200 and "pdf" in r.headers.get("Content-Type", ""):
            with open(ruta, "wb") as f:
                f.write(r.content)
            print("✔️ Guardado:", ruta)
        else:
            print("❌ No es un PDF válido:", url)
    except Exception as e:
        print("❌ Error:", e)

def obtener_categorias():
    print("🔍 Buscando categorías…")

    r = requests.get(BASE_CATEGORIAS, headers=HEADERS)
    soup = BeautifulSoup(r.text, "html.parser")

    categorias = []

    for a in soup.find_all("a"):
        href = a.get("href")
        if href and "/categoria/" in href:
            categorias.append(href)

    print(f"📂 Categorías encontradas: {len(categorias)}")
    return categorias

def obtener_libros(categoria_url):
    print(f"📚 Buscando libros en: {categoria_url}")

    r = requests.get(categoria_url, headers=HEADERS)
    soup = BeautifulSoup(r.text, "html.parser")

    libros = []

    for a in soup.find_all("a"):
        href = a.get("href")
        if href and "/libro/" in href:
            libros.append(href)

    print(f"📘 Libros encontrados: {len(libros)}")
    return libros

def buscar_pdf_en_libro(libro_url):
    print(f"🔎 Analizando libro: {libro_url}")

    try:
        r = requests.get(libro_url, headers=HEADERS)
        soup = BeautifulSoup(r.text, "html.parser")

        for a in soup.find_all("a"):
            href = a.get("href")
            if href and href.endswith(".pdf"):
                descargar_pdf(href)

    except Exception as e:
        print("❌ Error:", e)

def main():
    categorias = obtener_categorias()

    for categoria in categorias:
        libros = obtener_libros(categoria)

        for libro in libros:
            buscar_pdf_en_libro(libro)

    print("\n🎉 Proceso completado.")
    print("📁 PDFs descargados en:", CARPETA_PDF)

if __name__ == "__main__":
    main()
