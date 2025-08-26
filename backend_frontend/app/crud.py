from sqlalchemy.orm import Session
from app import models

def get_items(db: Session):
    return db.query(models.Item).all()

def update_stock(db: Session, item_id: int, new_quantity: int):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if item:
        item.quantity = new_quantity
        db.commit()
        db.refresh(item)
    return item

def get_movements(db: Session):
    return db.query(models.Movement).order_by(models.Movement.timestamp.desc()).all()
