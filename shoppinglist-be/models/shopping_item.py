from sqlalchemy import Column, Integer, String, Boolean
from utils.db import Base


class ShoppingItem(Base):
    __tablename__ = 'shopping_items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    purchased = Column(Boolean, default=False)

    def __repr__(self):
        return f"<ShoppingItem(name={self.name}, quantity={self.quantity}, purchased={self.purchased})>"