from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from app.database import Base
import enum
from datetime import datetime

class MovementType(str, enum.Enum):
    IN = "IN"
    OUT = "OUT"

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String, unique=True, index=True)
    ean13 = Column(String, unique=True)
    quantity = Column(Integer)

class Movement(Base):
    __tablename__ = "movements"
    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"))
    type = Column(Enum(MovementType))
    quantity = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)
