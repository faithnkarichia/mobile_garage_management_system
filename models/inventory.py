


from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from lib.base import Base,session

class Inventory(Base):
    __tablename__ = "inventories"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    quantity = Column(Integer)
    price = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

    service_request_items = relationship("ServiceRequestInventory", back_populates="inventory",cascade="all, delete, delete-orphan")
    

    
    @classmethod
    def create_inventory(cls, name, quantity, price):
        item = cls(name=name, quantity=quantity, price=price)
        session.add(item)
        session.commit()
        return item

    def delete_inventory(self):
        session.delete(self)
        session.commit()
        return True

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).filter_by(id=id).first()
    
    
    def edit_inventory(self):
        print("\n--- Edit Inventory ---")
        self.name = input(f"Name [{self.name}]: ") or self.name
        price_input = input(f"Price [{self.price}]: ")
        self.price = float(price_input) if price_input else self.price
        quantity_input = input(f"Quantity [{self.quantity}]: ")
        self.quantity = int(quantity_input) if quantity_input else self.quantity
        session.commit()
        print("Inventory updated.")


