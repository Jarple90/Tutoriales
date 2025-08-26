from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud

router = APIRouter(prefix="/stock", tags=["Stock"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/items")
def list_items(db: Session = Depends(get_db)):
    return crud.get_items(db)

@router.put("/items/{item_id}")
def update_item(item_id: int, quantity: int, db: Session = Depends(get_db)):
    return crud.update_stock(db, item_id, quantity)

@router.get("/movements")
def list_movements(db: Session = Depends(get_db)):
    return crud.get_movements(db)
