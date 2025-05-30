from models import Customer, Mechanic, Vehicle, Inventory, ServiceRequest, ServiceRequestInventory
from lib.base import session

if session.query(Customer).first():
    print("✅ Database already seeded. Skipping...")
else:
    try:
        # --- Create Customers ---
        customer1 = Customer(name="Jane Doe", phone_number="0712345678", location="Nairobi")
        customer2 = Customer(name="John Smith", phone_number="0798765432", location="Mombasa")

        # --- Create Mechanics ---
        mech1 = Mechanic(name="Moses Kimani", speciality="Engine", location="Nairobi")
        mech2 = Mechanic(name="Grace Wanjiru", speciality="Suspension", location="Nakuru")

        # --- Create Vehicles ---
        vehicle1 = Vehicle(make="Toyota", model="Corolla", year_of_manufacture=2015, customer=customer1)
        vehicle2 = Vehicle(make="Honda", model="Fit", year_of_manufacture=2012, customer=customer2)

        # --- Create Inventories ---
        plug = Inventory(name="Spark Plug", quantity=4, price=450.0)
        oil = Inventory(name="Engine Oil", quantity=1, price=1500.0)

        # --- Create Service Requests ---
        request1 = ServiceRequest(
            issue="Engine knocking", 
            status="pending", 
            location="Nairobi", 
            mechanic=mech1, 
            vehicle=vehicle1
        )
        request2 = ServiceRequest(
            issue="Suspension noise", 
            status="completed", 
            location="Nakuru", 
            mechanic=mech2, 
            vehicle=vehicle2
        )

        # --- Link Inventory to Service Requests ---
        # These will automatically create the association table records
        req_inv1 = ServiceRequestInventory(service_request=request1, inventory=plug)
        req_inv2 = ServiceRequestInventory(service_request=request2, inventory=oil)

        # Add all objects to session
        session.add_all([
            customer1, customer2, 
            mech1, mech2, 
            vehicle1, vehicle2, 
            plug, oil, 
            request1, request2, 
            req_inv1, req_inv2
        ])
        
        session.commit()
        print("🌱 Database seeded successfully!")

    except Exception as e:
        session.rollback()
        print(f"❌ Error seeding database: {e}")
        raise