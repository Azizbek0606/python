from abc import ABC, abstractmethod
from datetime import datetime
import uuid

class Vehicle(ABC):
    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_spot_type(self):
        pass

class Car(Vehicle):
    def get_type(self):
        return "Car"
    
    def get_spot_type(self):
        return "compact"

class Truck(Vehicle):
    def get_type(self):
        return "Truck"
    
    def get_spot_type(self):
        return "large"

class Van(Vehicle):
    def get_type(self):
        return "Van"
    
    def get_spot_type(self):
        return "compact"

class Motorcycle(Vehicle):
    def get_type(self):
        return "Motorcycle"
    
    def get_spot_type(self):
        return "motorcycle"

class ParkingLot:
    def __init__(self):
        self.total_capacity = 40000
        self.spots = {
            "handicapped": {"total": 2000, "occupied": 0},
            "compact": {"total": 15000, "occupied": 0},
            "large": {"total": 10000, "occupied": 0},
            "motorcycle": {"total": 13000, "occupied": 0}
        }
        self.tickets = {}
        self.hourly_rate = 2

    def is_full(self):
        total_occupied = sum(spot["occupied"] for spot in self.spots.values())
        return total_occupied >= self.total_capacity

    def display_board(self):
        print("\nAvailable Parking Spots:")
        for spot_type, info in self.spots.items():
            print(f"{spot_type.capitalize()}: {info['total'] - info['occupied']}")
        if self.is_full():
            print("WARNING: Parking Lot is Full!")

    def issue_ticket(self, vehicle):
        if self.is_full():
            print("Error: Parking lot is full!")
            return None
        
        spot_type = vehicle.get_spot_type()
        if self.spots[spot_type]["occupied"] >= self.spots[spot_type]["total"]:
            print(f"Error: No {spot_type} spots available!")
            return None

        ticket_id = str(uuid.uuid4())[:8]
        entry_time = datetime.now()
        self.tickets[ticket_id] = {
            "vehicle": vehicle,
            "spot_type": spot_type,
            "entry_time": entry_time
        }
        self.spots[spot_type]["occupied"] += 1
        print(f"Ticket Issued: {ticket_id} for {vehicle.get_type()}")
        return ticket_id

    def process_payment(self, ticket_id, payment_method):
        if ticket_id not in self.tickets:
            print("Error: Invalid Ticket ID!")
            return False

        ticket = self.tickets[ticket_id]
        exit_time = datetime.now()
        hours = max(1, ((exit_time - ticket["entry_time"]).total_seconds() / 3600))
        amount = hours * self.hourly_rate

        print(f"Payment of ${amount:.2f} for {ticket['vehicle'].get_type()} via {payment_method} successful!")
        self.spots[ticket["spot_type"]]["occupied"] -= 1
        del self.tickets[ticket_id]
        return True

def main():
    parking_lot = ParkingLot()
    
    while True:
        print("\nParking Lot System Menu:")
        print("1. Enter Vehicle")
        print("2. Exit and Pay")
        print("3. Show Available Spots")
        print("4. Exit System")
        choice = input("Enter choice (1-4): ")

        if choice == "1":
            print("\nSelect Vehicle Type:")
            print("1. Car")
            print("2. Truck")
            print("3. Van")
            print("4. Motorcycle")
            vehicle_choice = input("Enter choice (1-4): ")
            
            vehicle = None
            if vehicle_choice == "1":
                vehicle = Car()
            elif vehicle_choice == "2":
                vehicle = Truck()
            elif vehicle_choice == "3":
                vehicle = Van()
            elif vehicle_choice == "4":
                vehicle = Motorcycle()
            else:
                print("Invalid vehicle type!")
                continue

            ticket_id = parking_lot.issue_ticket(vehicle)
            if ticket_id:
                print(f"Please save your Ticket ID: {ticket_id}")

        elif choice == "2":
            ticket_id = input("Enter Ticket ID: ")
            print("\nSelect Payment Method:")
            print("1. Credit/Debit Card")
            print("2. Cash")
            payment_choice = input("Enter choice (1-2): ")
            
            payment_method = "Card" if payment_choice == "1" else "Cash" if payment_choice == "2" else None
            if not payment_method:
                print("Invalid payment method!")
                continue

            parking_lot.process_payment(ticket_id, payment_method)

        elif choice == "3":
            parking_lot.display_board()

        elif choice == "4":
            print("Exiting system. Thank you!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()