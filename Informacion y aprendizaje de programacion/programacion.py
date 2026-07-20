import os
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://freeprogrammingbooks.com/"
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

def obtener_paginas_de_libros():
    print("🔍 Buscando páginas de libros…")

    r = requests.get(BASE_URL, headers=HEADERS)
    soup = BeautifulSoup(r.text, "html.parser")

    paginas = []

    for a in soup.find_all("a"):
        href = a.get("href")
        if href and "/book/" in href:
            paginas.append(href)

    print(f"📄 Páginas de libros encontradas: {len(paginas)}")
    return paginas

def buscar_pdfs_en_pagina(url):
    print(f"🔎 Analizando página del libro: {url}")

    try:
        r = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(r.text, "html.parser")

        for a in soup.find_all("a"):
            href = a.get("href")
            if href and href.endswith(".pdf"):
                descargar_pdf(href)

    except Exception as e:
        print("❌ Error:", e)

def main():
    paginas_libros = obtener_paginas_de_libros()

    for pagina in paginas_libros:
        buscar_pdfs_en_pagina(pagina)

    print("\n🎉 Proceso completado.")
    print("📁 PDFs descargados en:", CARPETA_PDF)

if __name__ == "__main__":
    main()
