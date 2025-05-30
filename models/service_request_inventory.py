from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from lib.base import Base, session

class ServiceRequestInventory(Base):
    __tablename__ = "service_request_inventories"

    id = Column(Integer, primary_key=True)
    service_request_id = Column(Integer, ForeignKey("service_requests.id"))
    inventory_id = Column(Integer, ForeignKey("inventories.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

    # Corrected relationships
    service_request = relationship("ServiceRequest", back_populates="service_request_items")
    inventory = relationship("Inventory", back_populates="service_request_items")

    @classmethod
    def create_link(cls, service_request_id, inventory_id):
        link = cls(service_request_id=service_request_id, inventory_id=inventory_id)
        session.add(link)
        session.commit()
        return link

    def delete_link(self):
        session.delete(self)
        session.commit()

    @classmethod
    def get_all(cls):
        return session.query(cls).all()
    



    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).filter_by(id=id).first()
    



    def edit_service_request_inventory(self):
        print("\n--- Edit Service Request Inventory ---")
        self.service_request_id = input(f"Service Request ID [{self.service_request_id}]: ") or self.service_request_id
        self.inventory_id = input(f"Inventory ID [{self.inventory_id}]: ") or self.inventory_id
        session.commit()
        print("ServiceRequestInventory link updated.")

