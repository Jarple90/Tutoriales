import os
import requests
import markdown2
import pdfkit

# ---------------------------------------
# REPOSITORIO REAL DE INGLÉS
# ---------------------------------------
REPO = "EbookFoundation/free-programming-books"
API_URL = f"https://api.github.com/repos/{REPO}/contents/"

# Carpetas
CARPETA_MD = "ingles_md"
CARPETA_PDF = "ingles_pdf"

os.makedirs(CARPETA_MD, exist_ok=True)
os.makedirs(CARPETA_PDF, exist_ok=True)

# ---------------------------------------
# DESCARGAR ARCHIVOS .MD
# ---------------------------------------
def descargar_md():
    print("📚 Buscando archivos de inglés...")

    r = requests.get(API_URL)

    if r.status_code != 200:
        print("❌ Error al acceder:", r.status_code)
        return

    archivos = r.json()

    for item in archivos:
        nombre = item["name"]

        if nombre.endswith(".md"):
            url = item["download_url"]
            ruta = os.path.join(CARPETA_MD, nombre)

            print(f"📥 Descargando: {nombre}")
            contenido = requests.get(url).text

            with open(ruta, "w", encoding="utf-8") as f:
                f.write(contenido)

            print("✔ Guardado:", ruta)

# ---------------------------------------
# CONVERTIR MD → PDF
# ---------------------------------------
def convertir_md_a_pdf():
    print("\n📄 Convirtiendo archivos a PDF...")

    for archivo in os.listdir(CARPETA_MD):
        if archivo.endswith(".md"):
            ruta_md = os.path.join(CARPETA_MD, archivo)
            ruta_pdf = os.path.join(CARPETA_PDF, archivo.replace(".md", ".pdf"))

            with open(ruta_md, "r", encoding="utf-8") as f:
                texto_md = f.read()

            html = markdown2.markdown(texto_md)
            pdfkit.from_string(html, ruta_pdf)

            print("✔ PDF generado:", ruta_pdf)

# ---------------------------------------
# PROCESO PRINCIPAL
# ---------------------------------------
def main():
    descargar_md()
    convertir_md_a_pdf()
    print("\n🎉 Proceso completado. PDFs en la carpeta 'ingles_pdf'.")

main()
