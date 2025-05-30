

from lib.base import Base,session
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class ServiceRequest(Base):
    __tablename__ = "service_requests"
    id = Column(Integer, primary_key=True)
    issue = Column(String)
    status = Column(String)
    location = Column(String)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    mech_id = Column(Integer, ForeignKey("mechanics.id"))
    requested_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    # customer_id = Column(Integer, ForeignKey("customers.id")) 

    mechanic = relationship("Mechanic", back_populates="service_requests") 
    vehicle = relationship("Vehicle", back_populates="service_requests")
    service_request_items = relationship("ServiceRequestInventory", back_populates="service_request",cascade="all, delete, delete-orphan")

    @classmethod
    def create_service_request(cls, issue, status, location, vehicle_id, mech_id,requested_at,completed_at=None):
        sr = cls(issue=issue, status=status, location=location, vehicle_id=vehicle_id, mech_id=mech_id,requested_at=requested_at,completed_at=completed_at)
        session.add(sr)
        session.commit()
        session.refresh(sr)
        return sr

    def delete_service_request(self):
        session.delete(self)
        session.commit()

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).filter_by(id=id).first()
    

    def edit_service_request(self):
        print("\n--- Edit Service Request ---")
        self.issue = input(f"Issue [{self.issue}]: ") or self.issue
        self.status = input(f"Status [{self.status}]: ") or self.status
        self.location = input(f"Location [{self.location}]: ") or self.location
        self.vehicle_id = input(f"Vehicle ID [{self.vehicle_id}]: ") or self.vehicle_id
        self.mech_id = input(f"Mechanic ID [{self.mech_id}]: ") or self.mech_id
        session.commit()
        print("Service request updated.")

