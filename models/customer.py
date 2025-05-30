

from lib.base import Base,session
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    phone_number = Column(String(13))
    location = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)

    # one-to-many relationship with Vehicle

    vehicles = relationship("Vehicle", back_populates="customer",cascade="all, delete, delete-orphan")


    @classmethod
    def create_customer(cls,name,phone,location):
        customer=cls(name=name, phone_number=phone, location=location)
        session.add(customer)
        session.commit()
        return customer
    
    def delete_customer(self):
        session.delete(self)
        session.commit()

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).filter_by(id=id).first()
        

    def edit_customer(self):
        print("\n--- Edit Customer ---")
        self.name = input(f"Name [{self.name}]: ") or self.name

        self.phone_number = input(f"Phone [{self.phone_number}]: ") or self.phone_number

        self.location = input(f"Location [{self.location}]: ") or self.location
        session.commit()
        print("Customer updated.")
