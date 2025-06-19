
# Archivo: routers/products.py

from fastapi import APIRouter  # Importamos APIRouter para modularizar

# Definimos el router con prefijo y etiqueta para Swagger
router = APIRouter(
    prefix="/products",
    tags=["products"],
    responses={404: {"message": "No encontrado"}}
)

# Lista simulando una base de datos de productos
products_list = ["Producto 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5"]

# GET /products → Devuelve todos los productos
@router.get("/")
async def list_products():
    return products_list

# GET /products/{id} → Devuelve un producto específico
@router.get("/{id}")
async def get_product(id: int):
    try:
        return {"producto": products_list[id]}
    except IndexError:
        return {"error": f"No existe producto con ID {id}"}

# Comentario CLI
# cd R:\PROYECTOS\Backend\FastAPI
# python -m uvicorn main:app --reload  # Ejecutamos la app principal




