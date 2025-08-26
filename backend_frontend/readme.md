# 📦 Inventory API

Una API REST construida con **FastAPI** para gestionar productos en stock y sus movimientos. Este proyecto está diseñado para demostrar el uso de rutas, dependencias, SQLAlchemy y estructura modular en Python.

---

## 🚀 Tecnologías utilizadas

- Python 3.11
- FastAPI
- SQLAlchemy
- Uvicorn
- PostgreSQL (como base de datos)

---

## 📁 Estructura del proyecto

cd "R:\PROYECTOS\backend_frontend"

backend_frontend/
├── app/ │ 
├── routers/ │ 
│ └── stock.py │ 
├── crud.py │ 
├── database.py │ 
├── models.py 
├── main.py 
├── venv/


---

## ⚙️ Instalación

1. Clona el repositorio o copia el proyecto.
2. Crea y activa el entorno virtual:

```bash
cd "R:\PROYECTOS\backend_frontend"
python -m venv venv
.\venv\Scripts\Activate.ps1

pip install -r requirements.txt
Si no tienes requirements.txt, puedes generarlo con: pip freeze > requirements.txt

DATABASE_URL = "postgresql+psycopg2://usuario:contraseña@localhost:5432/nombre_db"

uvicorn main:app --reload

Accede a la documentación interactiva en:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

📌 Endpoints disponibles
GET /stock/items → Lista todos los productos

PUT /stock/items/{item_id}?quantity=... → Actualiza el stock de un producto

GET /stock/movements → Lista los movimientos registrados

🧪 Pruebas
Puedes usar Swagger UI para probar los endpoints directamente desde el navegador.

🧑‍💻 Autor
José — Málaga, España Proyecto realizado como ejercicio de backend con FastAPI.
