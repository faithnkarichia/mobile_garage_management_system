import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from base import session
from models import Customer, Mechanic, Vehicle, Inventory, ServiceRequest, ServiceRequestInventory

customers= session.query(Customer).all()
names=[customer.name for customer in customers] 
print(names)

mechanics= session.query(Mechanic).all()
mechs_names=[mechanic.name for mechanic in mechanics]
print(mechs_names)


vehicles = session.query(Vehicle).all()
vehicles_make = [vehicle.make for vehicle in vehicles]
vehicles_model = [vehicle.model for vehicle in vehicles]

# Join the lists into comma-separated strings
make_string = ", ".join(vehicles_make)
model_string = ", ".join(vehicles_model)

print("Makes:", make_string)
print("Models:", model_string)

inventories=session.query(Inventory).all()