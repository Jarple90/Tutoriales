from fastapi import APIRouter  ###FastAPI

router = APIRouter(prefix="/products",
                tags=["products"],
                responses = {404:{"message": "No encontrado"}}) ### app = FastAPI

products_list = ["Producto 1", "Producto 2",
                "Producto 3", "Producto 4", "Producto 5"]

@router.get("/")  #app.get hacemos la modificación porque es un script y funcionen en el principal, además de que ("/products/") podemos quitarlo porque hemos puesto un prefix
async def products():
    return products_list

@router.get("/{id}")
async def products(id: int):
    return products_list[id]

# cd R:\PROYECTOS\Backend\FastAPI
# python -m uvicorn products:app --reload

