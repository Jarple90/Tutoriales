import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote

URL = "https://www.oyejuanjo.com/2021/11/libros-pdf-ingles-a1-a2-b1-b2-c1-c1.html"
CARPETA = "libros_ingles_pdf"
FALLOS = "fallos.txt"

os.makedirs(CARPETA, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def obtener_links_pdf():
    print("🔍 Extrayendo enlaces PDF de la página...")
    r = requests.get(URL, headers=HEADERS)

    if r.status_code != 200:
        print("❌ Error al acceder a la página:", r.status_code)
        return []

    soup = BeautifulSoup(r.text, "html.parser")
    links = []

    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.lower().endswith(".pdf"):
            links.append(href)

    print(f"📚 Encontrados {len(links)} PDFs")
    return list(set(links))  # evitar duplicados

def descargar_pdf(url):
    nombre = unquote(url.split("/")[-1])
    ruta = os.path.join(CARPETA, nombre)

    for intento in range(3):
        try:
            print(f"📥 Descargando ({intento+1}/3): {nombre}")
            r = requests.get(url, headers=HEADERS, timeout=10, verify=False)

            if r.status_code == 200:
                with open(ruta, "wb") as f:
                    f.write(r.content)
                print(f"✔ Guardado en: {ruta}")
                return True
            else:
                print(f"❌ Error ({r.status_code}) al descargar: {url}")

        except Exception as e:
            print(f"⚠ Error: {e}")

    # Si llega aquí, falló
    with open(FALLOS, "a", encoding="utf-8") as f:
        f.write(url + "\n")

    print(f"❌ No se pudo descargar: {url}")
    return False

def main():
    pdfs = obtener_links_pdf()

    if not pdfs:
        print("❌ No se encontraron PDFs.")
        return

    print("\n⬇ Iniciando descargas...\n")
    for pdf in pdfs:
        descargar_pdf(pdf)

    print("\n🎉 Proceso completado.")
    print(f"📄 Revisa la carpeta '{CARPETA}' y el archivo '{FALLOS}' para ver los fallos.")

main()
