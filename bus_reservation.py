# ================= BUS RESERVATION SYSTEM =================
# Features Added:
# 1. View Buses
# 2. Book Ticket
# 3. Cancel Ticket
# 4. Booking Details
# 5. Search Bus
# 6. Admin Panel
# 7. PNR Generation
# 8. Seat Selection
# 9. JSON File Storage
# 10. Exception Handling
# 11. Ticket Printing
# ==========================================================

import json
import random
from datetime import datetime


class Bus:

    bookings = {}
    booking_id = 1

    buses = {
        1001: {
            "route": "HYD-RJY",
            "type": "AC Sleeper",
            "seats": [1, 2, 3, 4, 5],
            "price": 1200
        },

        1002: {
            "route": "HYD-VJA",
            "type": "Super Luxury",
            "seats": [1, 2, 3],
            "price": 900
        },

        1003: {
            "route": "HYD-AMP",
            "type": "Express",
            "seats": [1, 2, 3, 4],
            "price": 700
        }
    }

    # ================= VIEW BUSES =================

    def view_buses(self):

        print("\n================ AVAILABLE BUSES ================")

        print("ServiceNo\tRoute\t\tType\t\tPrice\tAvailable Seats")

        for k, v in Bus.buses.items():

            print(
                f"{k}\t\t{v['route']}\t{v['type']}\t₹{v['price']}\t{len(v['seats'])}"
            )

    # ================= SEARCH BUS =================

    def search_bus(self):

        route = input("Enter Route To Search: ").upper()

        found = False

        for k, v in Bus.buses.items():

            if route in v['route']:

                print("\nBus Found")
                print(
                    f"Service No : {k}\nRoute : {v['route']}\nType : {v['type']}\nPrice : ₹{v['price']}"
                )

                found = True

        if not found:
            print("No Bus Found")

    # ================= BOOK TICKET =================

    def book_ticket(self):

        try:

            service_no = int(input("Enter Service Number: "))

            if service_no not in Bus.buses:
                print("Invalid Service Number")
                return

            bus = Bus.buses[service_no]

            print(f"\nAvailable Seats : {bus['seats']}")

            n = int(input("How Many Tickets: "))

            if n > len(bus['seats']):
                print("Seats Not Available")
                return

            passengers = []
            booked_seats = []

            total_fare = 0

            for i in range(n):

                print(f"\nPassenger {i+1}")

                name = input("Enter Name: ")
                age = int(input("Enter Age: "))

                seat = int(input("Choose Seat Number: "))

                if seat not in bus['seats']:
                    print("Seat Not Available")
                    return

                bus['seats'].remove(seat)

                booked_seats.append(seat)

                passengers.append({
                    "name": name,
                    "age": age,
                    "seat": seat
                })

                fare = bus['price']

                # Senior Citizen Discount
                if age >= 60:
                    fare = fare - (fare * 10 / 100)

                total_fare += fare

            gst = total_fare * 5 / 100
            total_fare += gst

            pnr = random.randint(10000, 99999)

            Bus.bookings[Bus.booking_id] = {
                "PNR": pnr,
                "service_no": service_no,
                "route": bus['route'],
                "tickets": n,
                "passengers": passengers,
                "fare": total_fare,
                "date": str(datetime.now())
            }

            print("\n========= TICKET BOOKED SUCCESSFULLY =========")

            self.print_ticket(Bus.booking_id)

            self.save_data()

            Bus.booking_id += 1

        except ValueError:
            print("Invalid Input")

    # ================= PRINT TICKET =================

    def print_ticket(self, bid):

        data = Bus.bookings[bid]

        print("\n============== BUS TICKET ==============")

        print(f"Booking ID : {bid}")
        print(f"PNR Number : {data['PNR']}")
        print(f"Route      : {data['route']}")
        print(f"Tickets    : {data['tickets']}")
        print(f"Total Fare : ₹{data['fare']}")
        print(f"Date       : {data['date']}")

        print("\nPassengers:")

        for p in data['passengers']:

            print(
                f"Name : {p['name']} | Age : {p['age']} | Seat : {p['seat']}"
            )

        print("========================================")

    # ================= BOOKING DETAILS =================

    def booking_details(self):

        if not Bus.bookings:
            print("No Bookings Available")
            return

        for bid in Bus.bookings:

            self.print_ticket(bid)

    # ================= CANCEL TICKET =================

    def cancel_ticket(self):

        try:

            bid = int(input("Enter Booking ID: "))

            if bid not in Bus.bookings:
                print("Booking ID Not Found")
                return

            booking = Bus.bookings[bid]

            print("\nPassengers:")

            for i, p in enumerate(booking['passengers'], start=1):

                print(
                    f"{i}. {p['name']} | Seat : {p['seat']}"
                )

            cancel_seat = int(input("Enter Seat Number To Cancel: "))

            found = False

            for p in booking['passengers']:

                if p['seat'] == cancel_seat:

                    Bus.buses[booking['service_no']]['seats'].append(cancel_seat)

                    refund = Bus.buses[booking['service_no']]['price']
                    refund = refund - (refund * 10 / 100)

                    booking['fare'] -= refund

                    booking['passengers'].remove(p)

                    booking['tickets'] -= 1

                    found = True

                    print(f"Refund Amount : ₹{refund}")

                    break

            if booking['tickets'] == 0:
                del Bus.bookings[bid]

            if found:
                print("Ticket Cancelled Successfully")
            else:
                print("Seat Not Found")

            self.save_data()

        except ValueError:
            print("Invalid Input")

    # ================= SAVE DATA =================

    def save_data(self):

        with open("bookings.json", "w") as f:

            json.dump(Bus.bookings, f, indent=4)

    # ================= LOAD DATA =================

    def load_data(self):

        try:

            with open("bookings.json", "r") as f:

                Bus.bookings = json.load(f)

        except:
            pass

    # ================= ADMIN PANEL =================

    def admin_panel(self):

        password = input("Enter Admin Password: ")

        if password != "admin123":

            print("Wrong Password")
            return

        while True:

            print("\n=========== ADMIN PANEL ===========")
            print("1. Add Bus")
            print("2. Delete Bus")
            print("3. View Total Revenue")
            print("4. Back")

            choice = input("Enter Choice: ")

            # ===== ADD BUS =====

            if choice == "1":

                try:

                    service_no = int(input("Enter Service Number: "))
                    route = input("Enter Route: ")
                    bus_type = input("Enter Bus Type: ")
                    seats = int(input("Enter Number Of Seats: "))
                    price = int(input("Enter Ticket Price: "))

                    Bus.buses[service_no] = {
                        "route": route,
                        "type": bus_type,
                        "seats": list(range(1, seats + 1)),
                        "price": price
                    }

                    print("Bus Added Successfully")

                except:
                    print("Invalid Input")

            # ===== DELETE BUS =====

            elif choice == "2":

                service_no = int(input("Enter Service Number: "))

                if service_no in Bus.buses:

                    del Bus.buses[service_no]

                    print("Bus Deleted Successfully")

                else:
                    print("Bus Not Found")

            # ===== REVENUE =====

            elif choice == "3":

                revenue = 0

                for v in Bus.bookings.values():

                    revenue += v['fare']

                print(f"Total Revenue : ₹{revenue}")

            elif choice == "4":
                break

            else:
                print("Invalid Choice")


# ================= MAIN FUNCTION =================

def main():

    obj = Bus()

    obj.load_data()

    while True:

        print("\n=========== BUS RESERVATION SYSTEM ===========")

        print("1. View Buses")
        print("2. Search Bus")
        print("3. Book Ticket")
        print("4. Booking Details")
        print("5. Cancel Ticket")
        print("6. Admin Panel")
        print("7. Exit")

        try:

            choice = int(input("Enter Your Choice: "))

            if choice == 1:
                obj.view_buses()

            elif choice == 2:
                obj.search_bus()

            elif choice == 3:
                obj.book_ticket()

            elif choice == 4:
                obj.booking_details()

            elif choice == 5:
                obj.cancel_ticket()

            elif choice == 6:
                obj.admin_panel()

            elif choice == 7:

                print("Thank You")
                break

            else:
                print("Invalid Choice")

        except ValueError:
            print("Enter Numbers Only")


if __name__ == "__main__":
    main()
