from fastapi import FastAPI
from app.routers import stock

app = FastAPI(title="Inventory API")
app.include_router(stock.router)
