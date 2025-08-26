import requests
from bs4 import BeautifulSoup

# URL principal de la Serie Roja
url_base = "https://www.sepg.pap.hacienda.gob.es/Presup/PGE2023Prorroga/MaestroDocumentos/PGE-ROM/N_23P_E_R.htm"

# Realizar la solicitud
response = requests.get(url_base)
response.encoding = 'utf-8'  # Asegura que se lean bien los caracteres especiales

# Verificar que la página se ha cargado correctamente
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    print("🔍 Enlaces encontrados en la Serie Roja:\n")

    # Buscar todos los enlaces que llevan a secciones presupuestarias
    for link in soup.find_all('a'):
        href = link.get('href')
        text = link.get_text(strip=True)

        # Filtrar enlaces relevantes (por ejemplo, los que llevan a secciones)
        if href and href.startswith("N_23P_E_R_"):
            full_url = f"https://www.sepg.pap.hacienda.gob.es/Presup/PGE2023Prorroga/MaestroDocumentos/PGE-ROM/{href}"
            print(f"📎 {text} → {full_url}")
else:
    print(f"❌ Error al acceder a la página principal (status code: {response.status_code})")
