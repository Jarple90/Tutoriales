import os
import requests
import re

# ---------------------------------------
# CONFIGURACIÓN
# ---------------------------------------
GITHUB_USER = "UC3M-Student"  # Cambia esto por el usuario que quieras analizar

API_REPOS_URL = f"https://api.github.com/users/{GITHUB_USER}/repos"

# Palabras clave para clasificar carreras
CARRERAS = {
    "Economia": ["economia", "economics", "micro", "macro", "econometria", "econometrics"],
    "ADE": ["management", "empresa", "business", "administracion"],
    "Finanzas": ["finanzas", "finance", "financial"],
    "Estadistica": ["estadistica", "statistics", "probabilidad"],
    "Ingenieria": ["engineering", "ingenieria", "computacion", "informatica"],
    "Matematicas": ["matematicas", "math", "algebra", "calculo"],
}

# ---------------------------------------
# CREAR CARPETAS BASE
# ---------------------------------------
os.makedirs("universidad", exist_ok=True)

# ---------------------------------------
# CLASIFICAR REPOSITORIO POR CARRERA
# ---------------------------------------
def clasificar_repo(nombre_repo):
    nombre = nombre_repo.lower()
    for carrera, palabras in CARRERAS.items():
        if any(p in nombre for p in palabras):
            return carrera
    return "Otros"

# ---------------------------------------
# OBTENER REPOSITORIOS DEL USUARIO
# ---------------------------------------
def obtener_repos():
    print(f"🔍 Buscando repositorios de {GITHUB_USER}...")
    r = requests.get(API_REPOS_URL)

    if r.status_code != 200:
        print("❌ Error al acceder a la API:", r.status_code)
        return []

    return r.json()

# ---------------------------------------
# BUSCAR PDFs EN UN REPO
# ---------------------------------------
def obtener_pdfs(owner, repo):
    api_url = f"https://api.github.com/repos/{owner}/{repo}/contents/?ref=master"
    r = requests.get(api_url)

    if r.status_code != 200:
        return []

    archivos = r.json()
    pdfs = []

    for item in archivos:
        if item["name"].endswith(".pdf"):
            pdfs.append(item["download_url"])

    return pdfs

# ---------------------------------------
# DESCARGAR PDF
# ---------------------------------------
def descargar_pdf(url, carpeta_destino):
    nombre = url.split("/")[-1]
    ruta = os.path.join(carpeta_destino, nombre)

    print(f"📥 Descargando: {nombre}")
    r = requests.get(url)

    if r.status_code == 200:
        with open(ruta, "wb") as f:
            f.write(r.content)
        print("✔️ Guardado en:", ruta)
    else:
        print("❌ Error al descargar:", nombre)

# ---------------------------------------
# PROCESO PRINCIPAL
# ---------------------------------------
def main():
    repos = obtener_repos()

    for repo in repos:
        nombre_repo = repo["name"]
        carrera = clasificar_repo(nombre_repo)

        carpeta_carrera = os.path.join("universidad", carrera)
        os.makedirs(carpeta_carrera, exist_ok=True)

        print(f"\n📚 Analizando repo: {nombre_repo} → Carrera: {carrera}")

        pdfs = obtener_pdfs(GITHUB_USER, nombre_repo)

        if not pdfs:
            print("   ⚠️ No hay PDFs en este repositorio.")
            continue

        for pdf_url in pdfs:
            descargar_pdf(pdf_url, carpeta_carrera)

    print("\n🎉 Proceso completado. PDFs organizados por carrera.")

if __name__ == "__main__":
    main()
