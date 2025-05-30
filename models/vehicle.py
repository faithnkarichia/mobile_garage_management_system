

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from lib.base import Base,session

class Vehicle(Base):
    __tablename__ = "vehicles"
    id = Column(Integer, primary_key=True)
    make = Column(String(50))
    model = Column(String(50))
    year_of_manufacture = Column(Integer)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

    customer = relationship("Customer", back_populates="vehicles")
    service_requests = relationship("ServiceRequest", back_populates="vehicle",cascade="all, delete, delete-orphan")
    @classmethod
    def create_vehicle(cls, make, model, year, customer_id):
        vehicle = cls(make=make, model=model, year_of_manufacture=year, customer_id=customer_id)
        session.add(vehicle)
        session.commit()
        return vehicle

    def delete_vehicle(self):
        session.delete(self)
        session.commit()

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).filter_by(id=id).first()
    



    def edit_vehicle(self):
        print("\n--- Edit Vehicle ---")
        self.make = input(f"Make [{self.make}]: ") or self.make
        self.model = input(f"Model [{self.model}]: ") or self.model
        year_input = input(f"Year of Manufacture [{self.year_of_manufacture}]: ")
        self.year_of_manufacture = int(year_input) if year_input else self.year_of_manufacture
        self.customer_id = input(f"Customer ID [{self.customer_id}]: ") or self.customer_id
        session.commit()
        print("Vehicle updated.")

