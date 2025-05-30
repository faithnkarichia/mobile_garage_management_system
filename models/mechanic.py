

from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from lib.base import Base,session

class Mechanic(Base):
    __tablename__ = "mechanics"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    speciality = Column(String(20))
    location = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)

    service_requests = relationship("ServiceRequest", back_populates="mechanic",cascade="all, delete, delete-orphan")

    @classmethod
    def create_mechanic(cls, name, speciality, location):
        mechanic = cls(name=name, speciality=speciality, location=location)
        session.add(mechanic)
        session.commit()
        return mechanic

    def delete_mechanic(self):
        session.delete(self)
        session.commit()

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).filter_by(id=id).first()
    

    def edit_mechanic(self):
        print("\n--- Edit Mechanic ---")
        self.name = input(f"Name [{self.name}]: ") or self.name
        self.specialty = input(f"Specialty [{self.speciality}]: ") or self.speciality
        self.location = input(f"Location [{self.location}]: ") or self.location
        session.commit()
        print("Mechanic updated.")

