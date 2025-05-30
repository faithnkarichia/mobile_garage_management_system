# cli.py

from models import Customer, Mechanic, Vehicle, Inventory, ServiceRequest, ServiceRequestInventory
import datetime
from lib.base import session


def main_menu():
    while True:
        print("Welcome to the mobile garage management system!")
        print("1. Customers")
        print("2. Mechanics")
        print("3. Vehicles")
        print("4. Inventory")
        print("5. Service Requests")
        print("6. Service Request Inventory")
        print("7. Edit Records")
        print("8. Exit")

        choice = input("Please select an option (1-8): ")
        if choice == '1':
            print("You selected Customers.")
            customer_menu()
        elif choice == '2':
            print("You selected Mechanics.")
            mechanic_menu()
        elif choice == '3':
            print("You selected Vehicles.")
            vehicle_menu()
        elif choice == '4':
            print("You selected Inventory.")
            inventory_menu()
        elif choice == '5':
            print("You selected Service Requests.")
            service_request_menu()
        elif choice == '6':
            print("You selected Service Request Inventory.")
            link_menu()

        elif choice == '7':
            print("You selected Service Request Inventory.")
            edit_menu()
        elif choice == '8':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


def customer_menu():
    while True:
        print("\n--- Customer Menu ---")
        print("1. Create Customer")
        print("2. Delete Customer")
        print("3. View All Customers")
        print("4. Find Customer by ID")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")
# create customer
        if choice == "1":
            name = input("Enter name: ")
            print("Now asking for phone number...")
            phone = input("Enter phone number: ")
            print("Phone entered:", phone)
            location = input("Enter location: ")
            
            print("Location entered:", location)
            customer = Customer.create_customer(name, phone, location)
            print(
                f"Created customer: {customer.id}, {customer.name}, {customer.location}")
# delete customer
        elif choice == "2":
            id = input("Enter customer ID to delete: ")
            customer = Customer.find_by_id(id)
            if customer:
                customer.delete_customer()
                print("Customer deleted.")
            else:
                print("Customer not found.")

        elif choice == "3":
            customers = Customer.get_all()
            for c in customers:
                print(f"{c.id}: {c.name} - {c.phone_number}")
# find customer by id
        elif choice == "4":
            id = input("Enter customer ID: ")
            customer = Customer.find_by_id(id)
            if customer:
                print(
                    f"{customer.id}: {customer.name}, Phone: {customer.phone_number}")
            else:
                print("Customer not found.")

        elif choice == "0":
            break
        else:
            print("Invalid input.")


def mechanic_menu():
    while True:
        print("\n--- Mechanic Menu ---")
        print("1. Create Mechanic")
        print("2. Delete Mechanic")
        print("3. View All Mechanics")
        print("4. Find Mechanic by ID")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter mechanic name: ")
            speciality = input("Enter mechanic speciality: ")
            location = input("Enter mechanic location: ")
            # phone = input("Enter phone number: ")
            mechanic = Mechanic.create_mechanic(name, speciality, location)
            print(
                f"Created mechanic: {mechanic.id}, {mechanic.name} speciality: {mechanic.speciality}, location: {mechanic.location}")

        elif choice == "2":
            id = input("Enter mechanic ID to delete: ")
            mechanic = Mechanic.find_by_id(id)
            if mechanic:
                mechanic.delete_mechanic()
                print("Mechanic deleted.")
            else:
                print("Mechanic not found.")

        elif choice == "3":
            mechanics = Mechanic.get_all()
            for m in mechanics:
                print(f"{m.id}: {m.name} - {m.speciality}, Location: {m.location}")

        elif choice == "4":
            id = input("Enter mechanic ID: ")
            mechanic = Mechanic.find_by_id(id)
            if mechanic:
                print(
                    f"{mechanic.id}: {mechanic.name}, Speciality: {mechanic.speciality}, Location: {mechanic.location}")
            else:
                print("Mechanic not found.")

        elif choice == "0":
            break
        else:
            print("Invalid input.")


def vehicle_menu():
    while True:
        print("\n--- Vehicle Menu ---")
        print("1. Create Vehicle")
        print("2. Delete Vehicle")
        print("3. View All Vehicles")
        print("4. Find Vehicle by ID")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            make = input("Enter vehicle make: ")
            model = input("Enter vehicle model: ")
            year_of_manufacture = input("Enter vehicle year of manufacture: ")
            customer_id = input("Enter owner (Customer) ID: ")
            vehicle = Vehicle.create_vehicle(
                make, model, year_of_manufacture, customer_id)
            print(
                f"Created vehicle: {vehicle.id}, {vehicle.make},{vehicle.model}, Year: {vehicle.year_of_manufacture}, Owner ID: {vehicle.customer_id}")

        elif choice == "2":
            id = input("Enter vehicle ID to delete: ")
            vehicle = Vehicle.find_by_id(id)
            if vehicle:
                vehicle.delete_vehicle()
                print("Vehicle deleted.")
            else:
                print("Vehicle not found.")

        elif choice == "3":
            vehicles = Vehicle.get_all()
            for v in vehicles:
                print(
                    f"{v.id}: {v.make} {v.model}, Year: {v.year_of_manufacture}, Owner ID: {v.customer_id}")

        elif choice == "4":
            id = input("Enter vehicle ID: ")
            vehicle = Vehicle.find_by_id(id)
            if vehicle:
                print(
                    f"{vehicle.id}: {vehicle.model}, Make: {vehicle.make}, Year: {vehicle.year_of_manufacture}, Owner: {vehicle.customer.name}")
            else:
                print("Vehicle not found.")

        elif choice == "0":
            break
        else:
            print("Invalid input.")


def inventory_menu():
    while True:
        print("\n--- Inventory Menu ---")
        print("1. Add Inventory Item")
        print("2. Delete Inventory Item")
        print("3. View All Inventory")
        print("4. Find Inventory by ID")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter item name: ")
            quantity = input("Enter quantity: ")
            price = input("Enter price: ")
            inventory = Inventory.create_inventory(name, quantity, price)
            print(f"Added inventory: {inventory.id}, {inventory.name}")

        elif choice == "2":
            id = input("Enter inventory ID to delete: ")
            item = Inventory.find_by_id(id)
            if item:

                if item.delete_inventory():
                    print("Inventory item deleted.")
                else:
                    print(
                        "Failed to delete inventory item (possible database error or item already gone).")
            else:
                print("Inventory item not found.")

        elif choice == "3":
            items = Inventory.get_all()
            for i in items:
                print(f"{i.id}: {i.name}, Quantity: {i.quantity}, Price: {i.price}")

        elif choice == "4":
            id = input("Enter inventory ID: ")
            item = Inventory.find_by_id(id)
            if item:
                print(
                    f"{item.id}: {item.name}, Quantity: {item.quantity}, Price: {item.price}")
            else:
                print("Item not found.")

        elif choice == "0":
            break
        else:
            print("Invalid input.")


def service_request_menu():
    while True:
        print("\n--- Service Request Menu ---")
        print("1. Create Service Request")
        print("2. Delete Service Request")
        print("3. View All Service Requests")
        print("4. Find Request by ID")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            issue = input("Enter service issue: ")
            status = input("Enter service status: ")
            location = input("Enter service location: ")

            mech_id = input("Enter mechanic ID: ")

            mechanic = session.query(Mechanic).filter_by(id=mech_id).first()
            if not mechanic:
                print(
                    f"No mechanic found with ID {mech_id}. Please try again.")
                return
            vehicle_id = input("Enter vehicle ID: ")
            requested_at_dt = None
            while requested_at_dt is None:
                requested_at_str = input(
                    "Enter requested date (YYYY-MM-DD HH:MM:SS): ")
                if not requested_at_str:
                    requested_at_dt = datetime.datetime.now()
                    print(
                        f"Requested date set to current time: {requested_at_dt.strftime('%Y-%m-%d %H:%M:%S')}")
                else:
                    try:
                        requested_at_dt = datetime.datetime.strptime(
                            requested_at_str, '%Y-%m-%d %H:%M:%S')
                    except ValueError:
                        print(
                            "Invalid date/time format. Please use `YYYY-MM-DD HH:MM:SS`.")

            completed_at_dt = None
            while True:
                completed_at_str = input(
                    "Enter completed date and time (YYYY-MM-DD HH:MM:SS, leave blank if not completed yet): ")
                if not completed_at_str:
                    completed_at_dt = None
                    print("Service not yet completed.")
                    break
                else:
                    try:
                        completed_at_dt = datetime.datetime.strptime(
                            completed_at_str, '%Y-%m-%d %H:%M:%S')

                        if requested_at_dt and completed_at_dt < requested_at_dt:
                            print(
                                "Completed date cannot be before requested date. Please try again.")
                            completed_at_dt = None
                        else:
                            break
                    except ValueError:
                        print(
                            "Invalid date/time format. Please use `YYYY-MM-DD HH:MM:SS`.")

            request = ServiceRequest.create_service_request(
                issue, status, location, vehicle_id, mech_id, requested_at_dt, completed_at_dt)
            print(
                f"Created service request: {request.id} issue: {request.issue}, Status: {request.status}, Location: {request.location}, Vehicle ID: {request.vehicle_id}, Mechanic name: {request.mechanic.name}")

        elif choice == "2":
            id = input("Enter request ID to delete: ")
            request = ServiceRequest.find_by_id(id)
            if request:
                request.delete_service_request()
                print("Service request deleted.")
            else:
                print("Request not found.")

        elif choice == "3":
            requests = ServiceRequest.get_all()
            for r in requests:
                print(
                    f"{r.id}: {r.issue}, Status: {r.status}, Location: {r.location}, Vehicle ID: {r.vehicle_id}, Mechanic ID: {r.mech_id}")

        elif choice == "4":
            id = input("Enter request ID: ")
            request = ServiceRequest.find_by_id(id)
            if request:
                
                mechanic_name = request.mechanic.name if request.mechanic else "Unassigned"
                vehicle_info = f"{request.vehicle.make} {request.vehicle.model}" if request.vehicle else "Unknown Vehicle"

                print(
                    f"{request.id}: {request.status}, Mechanic: {mechanic_name}, Vehicle: {vehicle_info}, Status: {request.status}")
            else:
                print("Request not found.")

        elif choice == "0":
            print("Returning to main menu...")
            break

        else:
            print("Invalid input.")


# def link_menu():
#     while True:
#         print("\n--- View Spare Parts for a Service Request ---")
#         print("1. Show Spare Parts, Owner & Total Price by Service Request ID")
#         print("0. Back to Main Menu")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             service_request_id = input("Enter service request ID: ")
#             request = ServiceRequest.find_by_id(service_request_id)

#             if request:
#                 print(f"\nService Request ID: {request}")
#                 print(f"\nService Request ID----: {request.vehicle}")

#                 owner = request.vehicle.owner
#                 car = request.vehicle
#                 spare_parts = request.spare_parts  # Assuming this is a list of Inventory/Parts objects

#                 print(f"\nOwner: {owner.name}")
#                 print(f"Car: {car.make} {car.model}")

#                 if spare_parts:
#                     total_price = sum(part.price for part in spare_parts)
#                     print("Spare Parts:")
#                     for part in spare_parts:
#                         print(f"- {part.name}: ${part.price}")
#                     print(f"Total Price of Spare Parts: ${total_price}")
#                 else:
#                     print("No spare parts associated with this service request.")
#             else:
#                 print("Service request not found.")

#         elif choice == "0":
#             break
#         else:
#             print("Invalid input.")
def link_menu():
    while True:
        print("\n--- Spare Parts & Service Request Menu ---")
        print("1. Link Spare Part to Service Request")
        print("2. Show Spare Parts, Owner & Total Price by Service Request ID")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            service_request_id = input("Enter service request ID: ")
            inventory_id = input("Enter inventory ID to link: ")

            request = ServiceRequest.find_by_id(service_request_id)
            inventory = Inventory.find_by_id(inventory_id)

            if not request:
                print(f"❌ Service Request with ID {service_request_id} does not exist.")
            elif not inventory:
                print(f"❌ Inventory item with ID {inventory_id} does not exist.")
            else:
                try:
                    link = ServiceRequestInventory.create_link(service_request_id, inventory_id)
                    print(f"✅ Linked Inventory {inventory_id} to Service Request {service_request_id}")
                except Exception as e:
                    print(f"❌ Failed to create link: {e}")

        elif choice == "2":
            service_request_id = input("Enter service request ID: ")
            request = ServiceRequest.find_by_id(service_request_id)

            if request:
                print(f"\nService Request ID: {request.id}")
                print(f"Issue: {request.issue}")
                print(f"Status: {request.status}")

                if request.vehicle and request.vehicle.customer:
                    owner = request.vehicle.customer
                    car = request.vehicle
                    print(f"\nOwner: {owner.name}")
                    print(f"Car: {car.make} {car.model} ({car.year_of_manufacture})")
                else:
                    print("\nOwner or vehicle information not available")

                spare_parts = []
                total_price = 0.0
                for item in request.service_request_items:
                    if item.inventory:
                        spare_parts.append(item.inventory)
                        total_price += item.inventory.price

                if spare_parts:
                    print("\nSpare Parts:")
                    for part in spare_parts:
                        print(f"- {part.name}: ${part.price}")
                    print(f"Total Price of Spare Parts: ${total_price}")
                else:
                    print("\nNo spare parts associated with this service request.")
            else:
                print("Service request not found.")

        elif choice == "0":
            break
        else:
            print("Invalid input.")



def edit_menu():
    while True:
        print("\n--- Edit Records ---")
        print("1. Edit Service Request")
        print("2. Edit Mechanic")
        print("3. Edit Vehicle")
        print("4. Edit Inventory")
        print("5. Edit Customer")
        print("6. Edit Service Request Inventory")
        print("0. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            sr_id = input("Enter service request ID: ")
            sr = ServiceRequest.find_by_id(sr_id)
            if sr:
                sr.edit_service_request()
            else:
                print("Service request not found.")

        elif choice == "2":
            mech_id = input("Enter mechanic ID: ")
            mech = Mechanic.find_by_id(mech_id)
            if mech:
                mech.edit_mechanic()
            else:
                print("Mechanic not found.")

        elif choice == "3":
            vehicle_id = input("Enter vehicle ID: ")
            vehicle = Vehicle.find_by_id(vehicle_id)
            if vehicle:
                vehicle.edit_vehicle()
            else:
                print("Vehicle not found.")

        elif choice == "4":
            inventory_id = input("Enter inventory ID: ")
            inventory = Inventory.find_by_id(inventory_id)
            if inventory:
                inventory.edit_inventory()
            else:
                print("Inventory not found.")

        elif choice == "5":
            customer_id = input("Enter customer ID: ")
            customer = Customer.find_by_id(customer_id)
            if customer:
                customer.edit_customer()
            else:
                print("Customer not found.")

        elif choice == "6":
            link_id = input("Enter ServiceRequestInventory ID: ")
            link = ServiceRequestInventory.find_by_id(link_id)
            if link:
                link.edit_service_request_inventory()
            else:
                print("Service Request Inventory link not found.")

        elif choice == "0":
            break
        else:
            print("Invalid input.")

